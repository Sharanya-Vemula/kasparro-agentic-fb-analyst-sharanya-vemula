from pathlib import Path
import json
from datetime import datetime

from agents.planner import PlannerAgent
from agents.data_agent import DataAgent
from agents.insight_agent import InsightAgent
from agents.evaluator import EvaluatorAgent
from agents.creative_generator import CreativeGenerator
from utils.logging_utils import Logger


class Runner:
    def __init__(self, config: dict):
        self.config = config
        self.logger = Logger(config["logs"]["output_dir"])

        self.planner = PlannerAgent(self.logger)
        self.data_agent = DataAgent(config, self.logger)
        self.insight_agent = InsightAgent(self.logger)
        self.evaluator = EvaluatorAgent(config, self.logger)
        self.creative_agent = CreativeGenerator(config, self.logger)

        reports_dir = Path(config["reports"]["output_dir"])
        reports_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir = reports_dir

    def run(self, query: str):
        self.logger.log_event("run_started", {"query": query})

        # 1) Planner: interpret marketer query
        plan = self.planner.plan(query)

        # 2) Data Agent: load + ROAS-over-time summary
        df, summary = self.data_agent.load_and_summarize(plan)

        # 3) Insight Agent: generate hypotheses
        hypotheses = self.insight_agent.generate_hypotheses(plan, summary)

        # 4) Evaluator Agent: validate quantitatively
        evaluated_hypotheses = self.evaluator.evaluate(hypotheses, df)

        # 5) Creative Agent: propose new creatives for low-CTR segments
        creative_recos = self.creative_agent.generate(df, evaluated_hypotheses)

        # 6) Persist outputs
        insights_path = self._save_json("insights.json", evaluated_hypotheses)
        creatives_path = self._save_json("creatives.json", creative_recos)
        report_path = self._save_report_md(query, summary, evaluated_hypotheses, creative_recos)

        self.logger.log_event("run_completed", {
            "insights_path": str(insights_path),
            "creatives_path": str(creatives_path),
            "report_path": str(report_path),
        })

        return insights_path, creatives_path, report_path

    def _save_json(self, filename: str, payload):
        path = self.reports_dir / filename
        with path.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, default=str)
        return path

    def _save_report_md(self, query, summary, hypotheses, creatives):
        path = self.reports_dir / "report.md"
        now = datetime.utcnow().isoformat()

        with path.open("w", encoding="utf-8") as f:
            f.write(f"# Facebook Performance Analysis Report\n\n")
            f.write(f"**Generated at (UTC):** {now}\n\n")
            f.write(f"**User query:** {query}\n\n")

            # 1. Overview of ROAS over time
            f.write("## 1. ROAS & CTR Over Time\n")
            f.write(f"- Latest window: {summary['latest_window']['start']} to {summary['latest_window']['end']}\n")
            f.write(f"- Previous window: {summary['previous_window']['start']} to {summary['previous_window']['end']}\n\n")
            f.write(f"- ROAS change (%): {summary.get('roas_change_pct')}\n")
            f.write(f"- CTR change (%): {summary.get('ctr_change_pct')}\n\n")

            f.write("### Window Metrics\n")
            for k, v in summary.get("window_metrics", {}).items():
                f.write(f"- **{k}**: {v}\n")
            f.write("\n")

            # 2. Drivers behind change
            f.write("## 2. Drivers Behind ROAS Change\n")
            f.write("### By Platform\n")
            for plat, vals in summary.get("platform_metrics", {}).items():
                f.write(f"- **{plat}** → ROAS: {vals['roas']}, CTR: {vals['ctr']}, Spend: {vals['spend']}\n")
            f.write("\n")

            f.write("### By Audience Type\n")
            for aud, vals in summary.get("audience_metrics", {}).items():
                f.write(f"- **{aud}** → ROAS: {vals['roas']}, CTR: {vals['ctr']}, Spend: {vals['spend']}\n")
            f.write("\n")

            f.write("### Audience Fatigue Signals\n")
            fat = summary.get("fatigue_signals", [])
            if not fat:
                f.write("- No strong audience fatigue signals detected.\n\n")
            else:
                for row in fat:
                    f.write(
                        f"- Campaign: {row['campaign_name']} | Creative: {row['creative_message']} "
                        f"| CTR trend: {row['ctr_trend']} | ROAS trend: {row['roas_trend']}\n"
                    )
                f.write("\n")

            # 3. Hypotheses
            f.write("## 3. Validated Hypotheses\n")
            for h in hypotheses:
                f.write(f"- **Hypothesis:** {h['statement']}\n")
                f.write(f"  - Type: {h['type']}\n")
                f.write(f"  - Confidence: {h.get('confidence', h.get('initial_confidence', 0)):.2f}\n")
                f.write(f"  - Evidence: {h.get('evidence_summary', 'N/A')}\n")
                if h.get("segments"):
                    f.write(f"  - Segments: {h['segments']}\n")
                f.write("\n")

            # 4. Creative recommendations
            f.write("## 4. Creative Recommendations for Low-CTR Campaigns\n")
            if not creatives:
                f.write("- No low-CTR segments with sufficient impressions found.\n\n")
            else:
                for c in creatives:
                    f.write(f"- **Campaign:** {c['campaign_name']}\n")
                    f.write(f"  - Audience Type: {c['audience_type']}\n")
                    f.write(f"  - Platform: {c['platform']}\n")
                    f.write(f"  - Old message: {c['source_message']}\n")
                    f.write(f"  - New headline: {c['new_headline']}\n")
                    f.write(f"  - New primary text: {c['new_primary_text']}\n")
                    f.write(f"  - CTA suggestion: {c['cta']}\n\n")

            # 5. Next steps
            f.write("## 5. Suggested Next Actions\n")
            f.write("- Test 2–3 new creatives per fatigued audience/creative cluster.\n")
            f.write("- Shift spend towards high-ROAS platforms and audiences.\n")
            f.write("- Monitor ROAS, CTR and frequency over the next 7–14 days post-changes.\n")

        return path
