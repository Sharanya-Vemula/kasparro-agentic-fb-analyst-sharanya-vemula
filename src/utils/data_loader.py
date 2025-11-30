from pathlib import Path
import pandas as pd


def load_data(config: dict) -> "pd.DataFrame":
    use_sample = config.get("use_sample_data", True)
    data_cfg = config["data"]

    csv_path = Path(data_cfg["sample_csv_path"] if use_sample else data_cfg["full_csv_path"])
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at {csv_path}. Place the file correctly or update config.")

    df = pd.read_csv(csv_path)

    required_cols = [
        "campaign_name", "adset_name", "date", "spend", "impressions", "clicks",
        "ctr", "purchases", "revenue", "roas", "creative_type", "creative_message",
        "audience_type", "platform", "country",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df
