import sys
import yaml
from pathlib import Path

from orchestrator.runner import Runner


def load_config():
    config_path = Path("config/config.yaml")
    if not config_path.exists():
        raise FileNotFoundError("config/config.yaml not found.")
    with config_path.open("r") as f:
        return yaml.safe_load(f)


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/run.py \"Analyze ROAS drop in last 7 days\"")
        sys.exit(1)

    query = sys.argv[1]
    config = load_config()

    runner = Runner(config)
    insights, creatives, report_path = runner.run(query)

    print("\n=== RUN COMPLETED ===")
    print(f"- Insights saved to: {insights}")
    print(f"- Creatives saved to: {creatives}")
    print(f"- Report saved to: {report_path}")


if __name__ == "__main__":
    main()
