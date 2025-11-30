from typing import Dict, List


class InsightAgent:
    """
    Generates hypotheses about:
      - ROAS change over time
      - Platform / audience drivers
      - Audience fatigue
      - Creative underperformance
    """

    def __init__(self, logger):
        self.logger = logger

    def generate_hypotheses(self, plan: Dict, summary: Dict) -> List[Dict]:
        self.logger.log_event("insight_agent_generate_started", {})

        roas_change = summary.get("roas_change_pct")
        ctr_change = summary.get("ctr_change_pct")
        fatigue_signals = summary.get("fatigue_signals", [])

        hypotheses = []

        # 1) ROAS over time
        if roas_change is not None and roas_change < 0:
            hypotheses.append({
                "statement": "ROAS decreased in the latest period compared to the previous window.",
                "type": "roas_drop_over_time",
                "initial_confidence": 0.7,
                "segments": [],
                "evidence_summary": f"ROAS changed by {roas_change}%.",
            })

        # 2) CTR change
        if ctr_change is not None and ctr_change < 0:
            hypotheses.append({
                "statement": "CTR decreased, suggesting creative fatigue or weaker audience-message fit.",
                "type": "ctr_drop_over_time",
                "initial_confidence": 0.65,
                "segments": [],
                "evidence_summary": f"CTR changed by {ctr_change}%.",
            })

        # 3) Platform-level drivers
        hypotheses.append({
            "statement": "Specific platforms (e.g., Facebook vs Instagram) are driving the ROAS change.",
            "type": "platform_roas_shift",
            "initial_confidence": 0.6,
            "segments": [],
            "evidence_summary": "To be validated by ROAS and spend share by platform.",
        })

        # 4) Audience-type drivers
        hypotheses.append({
            "statement": "Certain audience segments have disproportionately lower ROAS.",
            "type": "audience_roas_shift",
            "initial_confidence": 0.6,
            "segments": [],
            "evidence_summary": "To be validated by ROAS across audience_type.",
        })

        # 5) Audience fatigue (if signals exist)
        if fatigue_signals:
            hypotheses.append({
                "statement": "Some creatives show audience fatigue (ROAS and CTR trend down while impressions stay high).",
                "type": "audience_fatigue",
                "initial_confidence": 0.7,
                "segments": fatigue_signals,
                "evidence_summary": f"{len(fatigue_signals)} campaign-creative pairs flagged for fatigue.",
            })
        else:
            hypotheses.append({
                "statement": "No strong audience fatigue patterns are visible in the current horizon.",
                "type": "audience_fatigue",
                "initial_confidence": 0.4,
                "segments": [],
                "evidence_summary": "Fatigue check returned no strong downward CTR/ROAS trends.",
            })

        # 6) Creative underperformance
        hypotheses.append({
            "statement": "Low-CTR creatives with high impressions are pulling down overall account performance.",
            "type": "creative_underperformance",
            "initial_confidence": 0.6,
            "segments": [],
            "evidence_summary": "To be validated by creative_message-level CTR and impressions.",
        })

        self.logger.log_event("insight_agent_generate_completed", {"hypotheses": hypotheses})
        return hypotheses
