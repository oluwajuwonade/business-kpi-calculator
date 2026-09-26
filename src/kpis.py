from __future__ import annotations

def growth_rate(current: float, prior: float) -> float | None:
    if prior == 0:
        return None
    return (current - prior) / prior

def gross_margin(revenue: float, cogs: float) -> float | None:
    if revenue == 0:
        return None
    return (revenue - cogs) / revenue

def contribution_margin(revenue: float, variable_cost: float) -> float | None:
    if revenue == 0:
        return None
    return (revenue - variable_cost) / revenue
