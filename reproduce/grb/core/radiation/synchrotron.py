"""Synchrotron helper functions for GRB afterglow toy models.

Theory page:
  wiki_textbook/grb-afterglow/05-synchrotron余辉谱.md

References:
  Sari, Piran & Narayan 1998
  Granot & Sari 2002

This module intentionally starts with simple spectral-segment utilities. Full
normalizations and smooth breaks should be added only after the textbook page
and validation notes specify the adopted convention.
"""

from __future__ import annotations


def electron_index_from_beta(beta: float, *, segment: str) -> float:
    """Infer electron index p from spectral index beta for slow cooling."""
    if segment == "nu_m_to_nu_c":
        return 2.0 * beta + 1.0
    if segment == "above_nu_c":
        return 2.0 * beta
    raise ValueError("segment must be 'nu_m_to_nu_c' or 'above_nu_c'")


def slow_cooling_beta(p: float, *, segment: str) -> float:
    """Return beta for standard slow-cooling synchrotron segments."""
    if p <= 1.0:
        raise ValueError("p should be > 1 for these toy afterglow segments")
    if segment == "nu_m_to_nu_c":
        return (p - 1.0) / 2.0
    if segment == "above_nu_c":
        return p / 2.0
    raise ValueError("segment must be 'nu_m_to_nu_c' or 'above_nu_c'")


def broken_power_law_spectrum(
    frequency: float,
    *,
    f_peak: float,
    nu_m: float,
    nu_c: float,
    p: float,
) -> float:
    """A sharp-break slow-cooling synchrotron spectrum toy model.

    This is for qualitative checks only. It assumes nu_m < nu_c and ignores
    self-absorption and smooth break shapes.
    """
    if not (frequency > 0 and f_peak > 0 and nu_m > 0 and nu_c > 0):
        raise ValueError("frequency, f_peak, nu_m, and nu_c must be positive")
    if nu_m >= nu_c:
        raise ValueError("this toy model assumes slow cooling: nu_m < nu_c")
    if p <= 1.0:
        raise ValueError("p should be > 1")
    if frequency < nu_m:
        return f_peak * (frequency / nu_m) ** (1.0 / 3.0)
    if frequency < nu_c:
        return f_peak * (frequency / nu_m) ** (-(p - 1.0) / 2.0)
    f_nuc = f_peak * (nu_c / nu_m) ** (-(p - 1.0) / 2.0)
    return f_nuc * (frequency / nu_c) ** (-p / 2.0)