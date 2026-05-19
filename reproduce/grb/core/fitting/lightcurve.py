"""Phenomenological light-curve functions for first-pass GRB fits.

Theory page:
  wiki_textbook/grb-afterglow/17-afterglow-fitting-workflow与参数简并.md

These helpers are intentionally model-agnostic. They are useful before a
physical afterglow model is selected, for example to quantify decay slopes and
break times in GRB 221009A.
"""

from __future__ import annotations


def power_law_flux(time: float, *, norm: float, t_ref: float, alpha: float) -> float:
    """Return F(t) = norm * (t / t_ref)^(-alpha)."""
    if time <= 0 or t_ref <= 0:
        raise ValueError("time and t_ref must be positive")
    return norm * (time / t_ref) ** (-alpha)


def smoothly_broken_power_law(
    time: float,
    *,
    norm: float,
    t_break: float,
    alpha_1: float,
    alpha_2: float,
    smoothness: float = 5.0,
) -> float:
    """Return a continuous smoothly broken power-law light curve.

    The normalization is the approximate flux at t_break. Larger smoothness
    gives a sharper transition.
    """
    if time <= 0 or t_break <= 0 or norm <= 0 or smoothness <= 0:
        raise ValueError("time, t_break, norm, and smoothness must be positive")
    x = time / t_break
    return norm * (x ** (alpha_1 * smoothness) + x ** (alpha_2 * smoothness)) ** (-1.0 / smoothness)