import pandas as pd
from pathlib import Path
import tempfile

from src.agents.evaluator import EvaluatorAgent
from src.utils.logging_utils import Logger


def _dummy_logger():
    tmpdir = tempfile.mkdtemp()
    return Logger(Path(tmpdir))


def _dummy_config():
    return {
        "confidence_min": 0.6,
        "analysis": {
            "low_ctr_threshold": 0.02,
            "min_impressions_for_eval": 1000,
        },
    }


def test_creative_underperformance_detection():
    data = {
        "campaign_name": ["A", "A", "B", "B"],
        "creative_message": ["msg1", "msg1", "msg2", "msg2"],
        "audience_type": ["cold", "cold", "warm", "warm"],
        "platform": ["facebook", "facebook", "instagram", "instagram"],
        "impressions": [2000, 1000, 300, 200],
        "clicks": [10, 5, 10, 5],  # msg1: ctr ~0.005, msg2: higher ctr
        "revenue": [100, 50, 80, 40],
        "spend": [50, 25, 20, 10],
    }
    df = pd.DataFrame(data)

    hypotheses = [{
        "statement": "Low-CTR creatives drag performance.",
        "type": "creative_underperformance",
        "initial_confidence": 0.6,
    }]

    evaluator = EvaluatorAgent(_dummy_config(), _dummy_logger())
    evaluated = evaluator.evaluate(hypotheses, df)

    h = evaluated[0]
    assert "segments" in h
    assert len(h["segments"]) == 1
    assert h["segments"][0]["creative_message"] == "msg1"
    assert h["confidence"] > 0.6