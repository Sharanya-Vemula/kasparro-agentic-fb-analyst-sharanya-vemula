from typing import Dict
from pathlib import Path


class PlannerAgent:
    """
    Planner: convert marketer's natural language query into objectives and steps
    aligned with the assignment’s 3 core goals:
      1) Diagnose why ROAS changed over time.
      2) Identify drivers (audience fatigue, creative underperformance, platform shifts).
      3) Propose new creative ideas grounded in existing messaging.
    """

    def __init__(self, logger):
        self.logger = logger
        self.prompt_path = Path("prompts/planner_prompt.md")

    def plan(self, query: str) -> Dict:
        self.logger.log_event("planner_plan_started", {"query": query})

        plan = {
            "original_query": query,
            "objectives": [
                "Measure ROAS and CTR change over time windows.",
                "Attribute ROAS change to campaigns, platforms, and audience types.",
                "Detect audience fatigue using CTR and ROAS trends over time.",
                "Find underperforming creatives (low CTR, high impressions).",
                "Generate improved headlines, body copy, and CTAs grounded in existing messages.",
            ],
            "steps": [
                "Load Facebook ads dataset and validate columns.",
                "Build time windows (latest vs previous) and compute KPIs.",
                "Compute ROAS and CTR by platform, audience_type, and campaign.",
                "Analyze trends over multiple weeks for fatigue signals.",
                "Generate hypotheses for ROAS and CTR changes.",
                "Quantitatively validate hypotheses with thresholds.",
                "Identify low-CTR creatives with enough impressions.",
                "Generate creative recommendations rooted in existing messages.",
            ],
        }

        self.logger.log_event("planner_plan_completed", {"plan": plan})
        return plan
