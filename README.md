# 📊 Kasparro Agentic Facebook Ads Analyst — v1.0

An end-to-end **self-directed agentic analytics system** that:
- Diagnoses **why ROAS changed over time**
- Identifies **drivers behind performance shifts** (platform, audience, creative fatigue)
- Detects **low-CTR creatives**
- **Auto-generates new creative recommendations**
- Produces **fully observable & reproducible outputs**

🔗 **Public Repository:**  
https://github.com/Sharanya-Vemula/kasparro-agentic-fb-analyst-sharanya-vemula.git

---

# 1. QUICK START (EXACT CLI COMMAND)

```bash
git clone https://github.com/Sharanya-Vemula/kasparro-agentic-fb-analyst-sharanya-vemula.git
cd kasparro-agentic-fb-analyst-sharanya-vemula

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python src/run.py "Analyze ROAS drop in last 7 days"
```
# 2. DATA INSTRUCTIONS
📁 Sample Dataset (Reproducible & Mandatory)
```
data/sample_fb_ads.csv
```
Used for evaluation

Small, fast, deterministic

Created using seeded random sampling

Run with:
```
python src/run.py "Analyze ROAS drop in last 7 days"
```

# 3. CONFIG FILE (REPRODUCIBILITY GUARANTEED)

```
config.yaml
```
```
mode: sample      # sample | full
seed: 42          # guarantees identical outputs every run

date_windows:
  latest_days: 7
  previous_days: 7

ctr_threshold: 0.01
min_impressions: 1000
```
# 4. PROJECT STRUCTURE
```
 kasparro-agentic-fb-analyst-sharanya-vemula/
│
├── data/
│   ├── sample_fb_ads.csv                   # Small reproducible dataset (for evaluation)
│   └── synthetic_fb_ads_undergarments.csv  # Full dataset (optional production run)
│
├── config/
│   └── config.yaml                         # Seed, thresholds, mode (sample/full)
│
├── src/
│   ├── run.py                              # Main CLI entry point
│   │
│   ├── orchestrator/
│   │   └── runner.py                      # Controls full agent pipeline
│   │
│   ├── agents/
│   │   ├── planner.py                     # Task decomposition agent
│   │   ├── data_agent.py                  # Data loading + KPI aggregation
│   │   ├── insight_agent.py               # ROAS & CTR hypothesis generator
│   │   ├── evaluator.py                   # Quantitative hypothesis validation
│   │   └── creative_generator.py          # Creative recommendation generator
│   │
│   └── utils/
│       ├── data_loader.py                 # CSV loader + column validation
│       ├── metrics.py                     # ROAS, CTR, and segment metrics
│       └── logging_utils.py               # JSON execution logger
│
├── prompts/
│   ├── planner_prompt.md                  # Planner reasoning prompt
│   ├── insight_prompt.md                  # Insight generation prompt
│   ├── evaluator_prompt.md                # Validation logic prompt
│   └── creative_prompt.md                 # Creative generation prompt
│
├── reports/
│   ├── insights.json                      # Hypotheses + confidence + evidence
│   ├── creatives.json                     # New creative recommendations
│   └── report.md                          # Final marketer-facing summary report
│
├── logs/
│   └── events.jsonl                       # Full agent execution trace
│
├── tests/
│   └── test_evaluator.py                  # Unit test for hypothesis validation
│
├── make_sample.py                         # One-time script to generate sample dataset
├── requirements.txt                       # Pinned Python dependencies
├── LICENSE                                # MIT License (academic & evaluation use)
├── README.md                              # Project documentation
└── venv/                                  # Local virtual environment

```
# 5. EXACT COMMAND USED TO PRODUCE SUBMITTED OUTPUTS
```
python src/run.py "Analyze ROAS drop in last 7 days"
```
This command generated:
```
reports/insights.json
reports/creatives.json
reports/report.md
logs/events.jsonl
```
# 6. EXAMPLE OUTPUT (REAL SNAPSHOT)
```
ROAS Change: -12.84%
CTR Change: +18.35%

Top Drivers:
- Broad audience underperforming
- Lookalike segment highest ROAS
- Instagram weaker than Facebook

Low-CTR Creatives Detected: 173
```
# 7. VALIDATION & HYPOTHESIS ENGINE
Each hypothesis is statistically validated and confidence-scored:
| Hypothesis                | Rule                          | Confidence |
| ------------------------- | ----------------------------- | ---------- |
| ROAS Drop                 | Latest ROAS < Previous ROAS   | 0.70       |
| Platform Driver           | Largest ROAS spread           | 0.50       |
| Audience Underperformance | ROAS < 80% of median          | 0.80       |
| Audience Fatigue          | CTR & ROAS both trending down | 0.40       |
| Creative Underperformance | CTR < 1% & Impressions ≥ 1000 | 0.85       |

 Stored in reports/insights.json
 Explained in reports/report.md

 # 8. EVIDENCE & OBSERVABILITY
 | File                     | Purpose                          |
| ------------------------ | -------------------------------- |
| `reports/insights.json`  | Hypotheses, confidence, segments |
| `reports/creatives.json` | Low-CTR creative clusters        |
| `reports/report.md`      | Final marketer-facing report     |
| `logs/events.jsonl`      | Full agent execution trace       |

All committed for evaluation.

# 9. SYSTEM DIAGRAM (PIPELINE FLOW)
```
CSV Data
   ↓
Metric Aggregator
   ↓
ROAS/CTR Validator
   ↓
Hypothesis Engine
   ↓
Creative Underperformance Detector
   ↓
Creative Recommendation Generator
   ↓
Markdown & JSON Report Builder
   ↓
Evidence Logs
```
# 10. VERSION PINNING 
```
pandas==2.2.1
numpy==1.26.4
pyyaml==6.0.1
```

# 11. GIT HYGIENE
This repository includes:

 At least 3 commits
 Release tag: v1.0
 Pull Request titled: self-review
 PR describes:

-> Design choices

-> Architecture decisions

-> Validation logic

-> Known limitations

# 12. AUTHOR

Sharanya Vemula
Data Analytics • Marketing Intelligence • Agentic AI Systems

# 13. LICENSE
```
This project is licensed under the **MIT License** for the purposes of:

-  Academic evaluation  
-  Technical assessment  
-  Learning & reproducibility  
-  Portfolio demonstration  

You are permitted to:
- Use
- Modify
- Distribute

with proper attribution to the original author.

> This license ensures compliance with the assignment’s requirements for **reproducibility, evaluation, and public submission**.

© 2025 Sharanya Vemula. All rights reserved.
```



