from typing import List, Dict
import textwrap
import random


class CreativeGenerator:
    """
    Generates new creative ideas (headline, primary text, CTA) for low-CTR campaigns.
    Grounding:
      - Uses existing creative_message as base
      - Keeps product + benefit vocabulary
      - Tweaks angle / promise / urgency
    """

    CTA_LIBRARY = [
        "Shop Now",
        "Explore Collection",
        "Grab the Offer",
        "Upgrade Your Comfort",
        "Try It Today",
    ]

    def __init__(self, config: dict, logger):
        self.config = config
        self.logger = logger

    def generate(self, df, evaluated_hypotheses: List[Dict]) -> List[Dict]:
        self.logger.log_event("creative_generate_started", {})
        low_ctr_segments = self._extract_low_ctr_segments(evaluated_hypotheses)

        recommendations = []
        for seg in low_ctr_segments:
            msg = seg["creative_message"]
            campaigns = seg.get("campaigns", [])
            audience_type = seg.get("audience_type", "Unknown")
            platform = seg.get("platform", "Unknown")

            headline = self._generate_headline(msg, audience_type)
            body = self._generate_body(msg, audience_type)
            cta = random.choice(self.CTA_LIBRARY)

            recommendations.append({
                "campaign_name": campaigns[0] if campaigns else "Unknown",
                "audience_type": audience_type,
                "platform": platform,
                "source_message": msg,
                "new_headline": headline,
                "new_primary_text": body,
                "cta": cta,
            })

        self.logger.log_event("creative_generate_completed", {"count": len(recommendations)})
        return recommendations

    def _extract_low_ctr_segments(self, hypotheses: List[Dict]) -> List[Dict]:
        segments = []
        for h in hypotheses:
            if h["type"] == "creative_underperformance" and "segments" in h:
                segments.extend(h["segments"])
        return segments

    def _generate_headline(self, base: str, audience_type: str) -> str:
        b = base.lower()

        if "comfort" in b or "soft" in b:
            return "All-Day Soft Comfort for Everyday Confidence"
        if "seamless" in b:
            return "Seamless Support You’ll Never Feel—but Always Notice"
        if "offer" in b or "discount" in b or "sale" in b:
            return "Premium Comfort, Now at an Irresistible Price"
        if "sport" in b or "workout" in b:
            return "Stay Supported Through Every Move"
        if "plus size" in b or "curve" in b:
            return "Perfect Fit, Designed for Every Curve"

        # fallback
        return "Innerwear That Feels as Good as It Looks"

    def _generate_body(self, base: str, audience_type: str) -> str:
        b = base.strip()
        if len(b) < 20:
            b = "Comfortable, breathable innerwear made to move with you."

        # keep some words from original message to stay grounded
        snippet = b[:120]

        generic = (
            f"{snippet} Upgrade to soft, breathable fabric that "
            f"stays invisible under clothes and comfortable all day long. "
            f"Designed for {audience_type.lower() if audience_type != 'Unknown' else 'your daily routine'}, "
            f"without pinching, digging or constant readjusting."
        )

        return textwrap.shorten(generic, width=220, placeholder="...")
