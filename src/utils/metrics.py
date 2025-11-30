from typing import Dict
import numpy as np


def compute_window_metrics(df) -> Dict:
    if df.empty:
        return {"roas": 0.0, "ctr": 0.0, "spend": 0.0}

    spend = float(df["spend"].sum())
    revenue = float(df["revenue"].sum())
    impressions = float(df["impressions"].sum())
    clicks = float(df["clicks"].sum())

    roas = revenue / spend if spend > 0 else 0.0
    ctr = clicks / impressions if impressions > 0 else 0.0

    return {
        "roas": round(roas, 4),
        "ctr": round(ctr, 4),
        "spend": round(spend, 2),
    }


def compute_segment_metrics(df, segment_col: str) -> Dict:
    """
    Compute ROAS/CTR/spend per segment (e.g., platform, audience_type).
    """
    if df.empty or segment_col not in df.columns:
        return {}

    grouped = df.groupby(segment_col).agg(
        spend=("spend", "sum"),
        revenue=("revenue", "sum"),
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
    )
    grouped["roas"] = grouped["revenue"] / grouped["spend"].replace(0, np.nan)
    grouped["ctr"] = grouped["clicks"] / grouped["impressions"].replace(0, np.nan)

    metrics = {}
    for idx, row in grouped.iterrows():
        metrics[str(idx)] = {
            "spend": round(float(row["spend"]), 2),
            "roas": round(float(row["roas"]) if not np.isnan(row["roas"]) else 0.0, 4),
            "ctr": round(float(row["ctr"]) if not np.isnan(row["ctr"]) else 0.0, 4),
        }
    return metrics
