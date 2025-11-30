from typing import List, Dict
import numpy as np
import pandas as pd


class EvaluatorAgent:
    """
    Quantitatively validates hypotheses and assigns confidence.
    Focus:
      - Segment ROAS shifts (platform, audience, campaign)
      - Creative underperformance
      - Uses config thresholds
    """

    def __init__(self, config: dict, logger):
        self.config = config
        self.logger = logger
        self.conf_min = config.get("confidence_min", 0.6)
        self.low_ctr_threshold = config["analysis"]["low_ctr_threshold"]
        self.min_impr = config["analysis"]["min_impressions_for_eval"]

    def evaluate(self, hypotheses: List[Dict], df: "pd.DataFrame") -> List[Dict]:
        self.logger.log_event("evaluator_evaluate_started", {})

        results = []
        for h in hypotheses:
            h_type = h["type"]

            if h_type == "platform_roas_shift":
                results.append(self._evaluate_platform_roas_shift(h, df))
            elif h_type == "audience_roas_shift":
                results.append(self._evaluate_audience_roas_shift(h, df))
            elif h_type == "creative_underperformance":
                results.append(self._evaluate_creative_underperformance(h, df))
            elif h_type == "audience_fatigue":
                # already came from DataAgent; just set confidence based on count
                count = len(h.get("segments", []))
                h["confidence"] = 0.8 if count > 0 else 0.4
                results.append(h)
            else:
                # generic ROAS/CTR time hypotheses keep initial confidence
                h["confidence"] = h.get("initial_confidence", 0.5)
                results.append(h)

        self.logger.log_event("evaluator_evaluate_completed", {"evaluated_hypotheses": results})
        return results

    def _evaluate_platform_roas_shift(self, h: Dict, df: "pd.DataFrame") -> Dict:
        grouped = df.groupby("platform").agg(
            spend=("spend", "sum"),
            revenue=("revenue", "sum")
        )
        grouped["roas"] = grouped["revenue"] / grouped["spend"].replace(0, np.nan)
        grouped = grouped.dropna(subset=["roas"])

        if grouped.empty or len(grouped) == 1:
            h["confidence"] = 0.4
            h["evidence_summary"] = "Insufficient platform variation to attribute ROAS change."
            return h

        max_roas = grouped["roas"].max()
        min_roas = grouped["roas"].min()
        delta = max_roas - min_roas

        if delta / max_roas > 0.2:  # >20% spread
            underperformers = grouped[grouped["roas"] < max_roas * 0.8]
            h["confidence"] = 0.8
            h["segments"] = [
                {"platform": idx, "roas": float(row["roas"]), "spend": float(row["spend"])}
                for idx, row in underperformers.iterrows()
            ]
            h["evidence_summary"] = (
                f"Platform ROAS ranges from {min_roas:.2f} to {max_roas:.2f}. "
                "Some platforms are significantly below the best performer."
            )
        else:
            h["confidence"] = 0.5
            h["evidence_summary"] = "Platform ROAS spread is small; no strong platform driver detected."

        return h

    def _evaluate_audience_roas_shift(self, h: Dict, df: "pd.DataFrame") -> Dict:
        grouped = df.groupby("audience_type").agg(
            spend=("spend", "sum"),
            revenue=("revenue", "sum")
        )
        grouped["roas"] = grouped["revenue"] / grouped["spend"].replace(0, np.nan)
        grouped = grouped.dropna(subset=["roas"])

        if grouped.empty or len(grouped) == 1:
            h["confidence"] = 0.4
            h["evidence_summary"] = "Insufficient audience_type variation to attribute ROAS change."
            return h

        median_roas = grouped["roas"].median()
        low_aud = grouped[grouped["roas"] < median_roas * 0.8]

        if not low_aud.empty:
            h["confidence"] = 0.8
            h["segments"] = [
                {"audience_type": idx, "roas": float(row["roas"]), "spend": float(row["spend"])}
                for idx, row in low_aud.iterrows()
            ]
            h["evidence_summary"] = (
                f"{len(low_aud)} audience types have ROAS < 80% of median ({median_roas:.2f})."
            )
        else:
            h["confidence"] = 0.5
            h["evidence_summary"] = "No audience_type with ROAS clearly below median."
        return h

    def _evaluate_creative_underperformance(self, h: Dict, df: "pd.DataFrame") -> Dict:
        # Aggregate by creative_message + audience_type + platform (to ground creatives)
        grouped = df.groupby(["creative_message", "audience_type", "platform"]).agg(
            impressions=("impressions", "sum"),
            clicks=("clicks", "sum"),
            revenue=("revenue", "sum"),
            spend=("spend", "sum"),
            campaign_name=("campaign_name", lambda x: list(set(x))),
        )
        grouped["ctr"] = grouped["clicks"] / grouped["impressions"].replace(0, np.nan)
        grouped["roas"] = grouped["revenue"] / grouped["spend"].replace(0, np.nan)

        mask = (grouped["impressions"] >= self.min_impr) & (grouped["ctr"] < self.low_ctr_threshold)
        low_ctr_creatives = grouped[mask].dropna(subset=["ctr"])

        segments = []
        for idx, row in low_ctr_creatives.iterrows():
            msg, aud, plat = idx
            segments.append({
                "creative_message": msg,
                "audience_type": aud,
                "platform": plat,
                "ctr": float(row["ctr"]),
                "impressions": int(row["impressions"]),
                "campaigns": row["campaign_name"],
            })

        if len(segments) == 0:
            h["confidence"] = 0.45
            h["evidence_summary"] = "No creatives with both low CTR and high impressions found."
        else:
            h["confidence"] = 0.85
            h["segments"] = segments
            h["evidence_summary"] = (
                f"Found {len(segments)} creative-audience-platform combinations with "
                f"CTR < {self.low_ctr_threshold} and impressions >= {self.min_impr}."
            )

        return h
