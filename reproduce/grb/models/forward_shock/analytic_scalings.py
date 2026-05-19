"""Analytic forward-shock closure and scaling helpers.

Theory pages:
  wiki_textbook/grb-afterglow/04-external-shock动力学.md
  wiki_textbook/grb-afterglow/05-synchrotron余辉谱.md
  wiki_textbook/grb-afterglow/06-light-curve-closure-relations.md
  wiki_textbook/grb-afterglow/17-afterglow-fitting-workflow与参数简并.md

This file starts with closure-relation utilities. Physical normalizations for
nu_m, nu_c, and F_nu,max should be added only with explicit convention notes and
validation records.
"""

from __future__ import annotations


def closure_alpha(p: float, *, medium: str, segment: str, sideways_jet: bool = False) -> float:
    """Return standard adiabatic forward-shock temporal slope alpha.

    Uses F_nu proportional to t^-alpha in the slow-cooling regime.
    """
    if p <= 1.0:
        raise ValueError("p should be > 1")
    if sideways_jet:
        return p
    if segment == "above_nu_c":
        return (3.0 * p - 2.0) / 4.0
    if segment != "nu_m_to_nu_c":
        raise ValueError("segment must be 'nu_m_to_nu_c' or 'above_nu_c'")
    if medium == "ism":
        return 3.0 * (p - 1.0) / 4.0
    if medium == "wind":
        return (3.0 * p - 1.0) / 4.0
    raise ValueError("medium must be 'ism' or 'wind'")


def closure_beta(p: float, *, segment: str) -> float:
    """Return standard slow-cooling spectral slope beta."""
    if p <= 1.0:
        raise ValueError("p should be > 1")
    if segment == "nu_m_to_nu_c":
        return (p - 1.0) / 2.0
    if segment == "above_nu_c":
        return p / 2.0
    raise ValueError("segment must be 'nu_m_to_nu_c' or 'above_nu_c'")


def infer_p_from_alpha(alpha: float, *, medium: str, segment: str) -> float:
    """Infer p from alpha for common pre-jet-break closure relations."""
    if segment == "above_nu_c":
        return (4.0 * alpha + 2.0) / 3.0
    if segment != "nu_m_to_nu_c":
        raise ValueError("segment must be 'nu_m_to_nu_c' or 'above_nu_c'")
    if medium == "ism":
        return 4.0 * alpha / 3.0 + 1.0
    if medium == "wind":
        return (4.0 * alpha + 1.0) / 3.0
    raise ValueError("medium must be 'ism' or 'wind'")