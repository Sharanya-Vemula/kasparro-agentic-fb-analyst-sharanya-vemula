from typing import Tuple, Dict, List
from datetime import timedelta

from utils.data_loader import load_data
from utils.metrics import compute_window_metrics, compute_segment_metrics


class DataAgent:
    """
    Loads data, computes:
      - ROAS/CTR change over time
      - By-platform and by-audience metrics
      - Simple audience fatigue signals (CTR + ROAS trend over multiple weeks)
    """

    def __init__(self, config: dict, logger):
        self.config = config
        self.logger = logger

    def load_and_summarize(self, plan: Dict) -> Tuple["pd.DataFrame", Dict]:
        self.logger.log_event("data_agent_load_started", {})

        df = load_data(self.config)
        if df.empty:
            raise ValueError("Dataframe is empty. Check CSV paths and config.")

        df["date"] = df["date"].astype("datetime64[ns]")

        lookback_days = self.config["analysis"]["lookback_days"]
        prev_window_days = self.config["analysis"]["prev_window_days"]
        fatigue_lookback = self.config["analysis"]["fatigue_lookback_days"]

        max_date = df["date"].max()
        latest_start = max_date - timedelta(days=lookback_days - 1)
        prev_end = latest_start - timedelta(days=1)
        prev_start = prev_end - timedelta(days=prev_window_days - 1)

        latest_mask = (df["date"] >= latest_start) & (df["date"] <= max_date)
        prev_mask = (df["date"] >= prev_start) & (df["date"] <= prev_end)

        latest_df = df[latest_mask].copy()
        prev_df = df[prev_mask].copy()

        latest_metrics = compute_window_metrics(latest_df)
        prev_metrics = compute_window_metrics(prev_df)

        def pct_change(new, old):
            if old == 0 or old is None:
                return None
            return round(100 * (new - old) / old, 2)

        # segment metrics
        platform_metrics = compute_segment_metrics(latest_df, "platform")
        audience_metrics = compute_segment_metrics(latest_df, "audience_type")

        # fatigue signals over longer horizon
        fatigue_signals = self._compute_fatigue_signals(df, fatigue_lookback)

        summary = {
            "latest_window": {"start": str(latest_start.date()), "end": str(max_date.date())},
            "previous_window": {"start": str(prev_start.date()), "end": str(prev_end.date())},
            "window_metrics": {
                "latest_roas": latest_metrics["roas"],
                "previous_roas": prev_metrics["roas"],
                "latest_ctr": latest_metrics["ctr"],
                "previous_ctr": prev_metrics["ctr"],
                "latest_spend": latest_metrics["spend"],
                "previous_spend": prev_metrics["spend"],
            },
            "roas_change_pct": pct_change(latest_metrics["roas"], prev_metrics["roas"]),
            "ctr_change_pct": pct_change(latest_metrics["ctr"], prev_metrics["ctr"]),
            "platform_metrics": platform_metrics,
            "audience_metrics": audience_metrics,
            "fatigue_signals": fatigue_signals,
        }

        self.logger.log_event("data_agent_load_completed", {"summary": summary})
        return df, summary

    def _compute_fatigue_signals(self, df, fatigue_lookback_days: int) -> List[Dict]:
        """
        Simple audience fatigue detection:
        For recent N days, check creative_message x campaign trends:
          - impressions stable or up
          - CTR trending down
          - ROAS trending down
        """
        import numpy as np
        from collections import defaultdict

        max_date = df["date"].max()
        min_date = max_date - timedelta(days=fatigue_lookback_days - 1)

        window_df = df[(df["date"] >= min_date) & (df["date"] <= max_date)].copy()
        if window_df.empty:
            return []

        # bucket into weekly periods for rough trend
        window_df["week"] = window_df["date"].dt.to_period("W").apply(lambda r: r.start_time)

        grouped = window_df.groupby(["campaign_name", "creative_message", "week"]).agg(
            impressions=("impressions", "sum"),
            clicks=("clicks", "sum"),
            revenue=("revenue", "sum"),
            spend=("spend", "sum"),
        )
        grouped["ctr"] = grouped["clicks"] / grouped["impressions"].replace(0, np.nan)
        grouped["roas"] = grouped["revenue"] / grouped["spend"].replace(0, np.nan)
        grouped = grouped.reset_index()

        signals = []
        for (camp, msg), sub in grouped.groupby(["campaign_name", "creative_message"]):
            sub_sorted = sub.sort_values("week")
            if len(sub_sorted) < 3:
                continue

            ctr_vals = sub_sorted["ctr"].values
            roas_vals = sub_sorted["roas"].values
            impr_vals = sub_sorted["impressions"].values

            # check rough trends: last vs first
            ctr_trend = "down" if ctr_vals[-1] < ctr_vals[0] else "flat_or_up"
            roas_trend = "down" if roas_vals[-1] < roas_vals[0] else "flat_or_up"
            impr_trend = "up" if impr_vals[-1] >= impr_vals[0] else "down"

            if ctr_trend == "down" and roas_trend == "down" and impr_trend == "up":
                signals.append({
                    "campaign_name": camp,
                    "creative_message": msg,
                    "ctr_trend": ctr_trend,
                    "roas_trend": roas_trend,
                    "impressions_trend": impr_trend,
                })

        return signals
