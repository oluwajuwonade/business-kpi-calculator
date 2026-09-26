# Business KPI Calculator

> Reusable KPI engine for revenue, growth, margins, conversion, retention, productivity, and unit economics.

## Business Problem

Teams frequently calculate similar metrics inconsistently. This project standardizes KPI definitions, inputs, edge cases, and interpretation so reported metrics are comparable and auditable.

## Analytical Questions

- What is the exact KPI definition?\n- Which inputs and denominators are required?\n- How should zero, null, or missing periods be handled?\n- Which KPI movements require investigation?

## Deliverables

- KPI calculation library\n- Metric-definition catalogue\n- Input validation\n- Example business dataset\n- KPI trend report\n- Interpretation guide

## Suggested Repository Structure

```text
business-kpi-calculator/
├── data/
├── notebooks/
├── src/
├── tests/
├── outputs/
├── README.md
└── requirements.txt
```

## Stack

Python, pandas, SQL, Plotly, pytest

## Method

1. Define the decision context and metric definitions.
2. Profile and validate the data.
3. Build reproducible transformations and calculations.
4. Quantify the main drivers, scenarios, or failure modes.
5. Validate outputs and document limitations.
6. Produce an executive-ready decision narrative.

## Portfolio Standard

Use synthetic or public data with documented provenance. Clearly distinguish measured results from assumptions and illustrative scenarios.
