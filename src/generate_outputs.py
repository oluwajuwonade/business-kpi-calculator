from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from kpis import growth_rate, gross_margin, contribution_margin

ROOT = Path(__file__).resolve().parents[1]
DATA, OUTPUTS = ROOT / "data", ROOT / "outputs"
DATA.mkdir(exist_ok=True); OUTPUTS.mkdir(exist_ok=True)


def main() -> None:
    months = pd.date_range("2026-01-01", periods=12, freq="MS")
    revenue = np.array([82000, 84500, 87000, 91000, 93500, 97000, 101000, 104500, 108000, 112000, 116500, 121000], dtype=float)
    cogs = revenue * np.array([.42, .42, .415, .41, .41, .405, .405, .40, .40, .395, .395, .39])
    visitors = np.array([41000, 42500, 43800, 45200, 46800, 49000, 51200, 53000, 54800, 56500, 58600, 61000])
    orders = np.array([820, 850, 900, 950, 1000, 1060, 1125, 1180, 1240, 1300, 1380, 1460])
    customers_open = np.array([5600, 5700, 5800, 5920, 6030, 6150, 6280, 6410, 6550, 6700, 6860, 7020])
    customers_retained = np.array([4380, 4460, 4540, 4660, 4750, 4860, 4980, 5100, 5230, 5370, 5520, 5680])
    df = pd.DataFrame({"month": months, "revenue": revenue, "cogs": cogs, "website_visitors": visitors, "orders": orders, "customers_open": customers_open, "customers_retained": customers_retained})
    df["revenue_growth"] = [np.nan] + [growth_rate(df.revenue.iloc[i], df.revenue.iloc[i-1]) for i in range(1, len(df))]
    df["gross_margin"] = [gross_margin(r, c) for r, c in zip(df.revenue, df.cogs)]
    df["conversion_rate"] = df.orders / df.website_visitors
    df["retention_rate"] = df.customers_retained / df.customers_open
    df["average_order_value"] = df.revenue / df.orders
    df["contribution_margin"] = [contribution_margin(r, c) for r, c in zip(df.revenue, df.cogs)]
    df.to_csv(DATA / "illustrative_monthly_kpis.csv", index=False, date_format="%Y-%m-%d")
    df.to_csv(OUTPUTS / "kpi_trend_report.csv", index=False, date_format="%Y-%m-%d")

    latest = df.iloc[-1]
    summary = pd.DataFrame({"kpi": ["Revenue", "Revenue growth", "Gross margin", "Conversion rate", "Retention rate", "Average order value"], "latest_value": [latest.revenue, latest.revenue_growth, latest.gross_margin, latest.conversion_rate, latest.retention_rate, latest.average_order_value], "format": ["currency", "percent", "percent", "percent", "percent", "currency"]})
    summary.to_csv(OUTPUTS / "kpi_summary.csv", index=False)
    (OUTPUTS / "executive_summary.md").write_text(f"""# Executive Summary — Illustrative KPI Trend Report\n\n**Scope:** Twelve-month synthetic ecommerce KPI series designed to demonstrate reusable metric definitions and trend diagnostics.\n\n## Latest month\n\n- Revenue: **${latest.revenue:,.0f}**\n- Month-on-month revenue growth: **{latest.revenue_growth:.1%}**\n- Gross margin: **{latest.gross_margin:.1%}**\n- Conversion rate: **{latest.conversion_rate:.2%}**\n- Retention rate: **{latest.retention_rate:.1%}**\n- Average order value: **${latest.average_order_value:,.2f}**\n\n## Decision readout\n\nThe illustrative series shows revenue growth alongside improving gross margin and conversion. A production analysis should decompose the movement into traffic, conversion, order value, pricing, mix, and retention effects before recommending action.\n\n## Controls and limitations\n\nZero denominators return `None` in the KPI library. This is a synthetic portfolio artifact; it does not represent a real company, customer cohort, or market benchmark.\n""")

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax1 = plt.subplots(figsize=(9, 5.2))
    ax1.plot(df.month, df.revenue / 1000, marker="o", linewidth=2.5, color="#2563EB", label="Revenue ($000)")
    ax1.set_ylabel("Revenue ($000)", color="#2563EB"); ax1.tick_params(axis="y", labelcolor="#2563EB")
    ax2 = ax1.twinx(); ax2.plot(df.month, df.gross_margin * 100, marker="s", linewidth=2.5, color="#15803D", label="Gross margin")
    ax2.set_ylabel("Gross margin (%)", color="#15803D"); ax2.tick_params(axis="y", labelcolor="#15803D")
    ax1.set_title("Illustrative KPI Trend: Revenue and Gross Margin", loc="left", weight="bold")
    fig.tight_layout(); fig.savefig(OUTPUTS / "revenue_margin_trend.png", dpi=180); plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.plot(df.month, df.conversion_rate * 100, marker="o", linewidth=2.5, label="Conversion rate", color="#7C3AED")
    ax.plot(df.month, df.retention_rate * 100, marker="o", linewidth=2.5, label="Retention rate", color="#EA580C")
    ax.set_title("Illustrative Funnel KPIs", loc="left", weight="bold")
    ax.set_ylabel("Rate (%)"); ax.legend(frameon=False); fig.autofmt_xdate(); fig.tight_layout(); fig.savefig(OUTPUTS / "funnel_kpi_trend.png", dpi=180); plt.close(fig)


if __name__ == "__main__":
    main()
