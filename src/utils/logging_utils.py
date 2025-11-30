from pathlib import Path
import json
from datetime import datetime
from typing import Any, Dict


class Logger:
    def __init__(self, logs_dir: str):
        logs_path = Path(logs_dir)
        logs_path.mkdir(parents=True, exist_ok=True)
        self.logfile = logs_path / "events.jsonl"

    def log_event(self, event_type: str, payload: Dict[str, Any]):
        record = {
            "timestamp_utc": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "payload": payload,
        }
        with self.logfile.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, default=str) + "\n")
