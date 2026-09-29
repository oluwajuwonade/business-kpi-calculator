# Business Metrics & KPI Engine

> **Measurement problem:** Are business metrics defined consistently enough to support reliable decisions?

A reusable KPI engine for revenue, growth, margins, conversion, retention, productivity, and unit economics.

## Purpose

Teams often calculate the same metric differently. This project standardizes KPI definitions, required inputs, denominators, edge cases, and interpretation.

## Workflow

`Metric definition → Input validation → Calculation → Trend analysis → Diagnostic trigger → Interpretation`

## Covered KPI families

- Revenue
- Growth
- Gross margin
- Conversion
- Retention
- Productivity
- Unit economics

## Analytical questions

1. What is the exact metric definition?
2. Which inputs and denominators are required?
3. How should zero, null, and missing periods be handled?
4. Which KPI movements should trigger investigation?

## Deliverables

- KPI calculation library
- Metric-definition catalogue
- Input validation
- Example business dataset
- KPI trend report
- Interpretation guide
- Tests for key calculations

## Reproduce

```bash
python src/generate_outputs.py
```

The generated outputs include a twelve-month illustrative KPI trend report and summary files.

## Data disclosure

The example dataset is synthetic and exists to demonstrate consistent metric definitions and interpretation.

## Important limitations

- Example data is synthetic and used to demonstrate metric definitions and handling rules.
- KPI calculations are only as reliable as the source data, business definitions, and denominators supplied.
- The repository does not claim that one KPI definition is appropriate for every organisation or industry.
- Production use should include stakeholder-agreed definitions, ownership, and reconciliation to source systems.

## Portfolio role

**Tier 2 — BI / Analytics Infrastructure**

This repository is intentionally positioned as a reusable analytical component rather than a standalone business case study.

## Related projects

- [Data Quality & Analytics Assurance](https://github.com/oluwajuwonade/data-quality-audit-toolkit)
- [AI-Powered Retail Sales Diagnostic](https://github.com/oluwajuwonade/AI-Powered-Retail-Sales-Diagnostic)
- [Pricing & ROI Decision Engine](https://github.com/oluwajuwonade/pricing-roi-analytics-engine)

## Author

**Oluwajuwon Adediji**  
Data & Quantitative Analyst | BI & Decision Analytics
