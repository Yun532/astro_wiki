"""Blast-wave helper functions for GRB afterglow toy models.

Theory page:
  wiki_textbook/grb-afterglow/04-external-shock动力学.md

References:
  Blandford & McKee 1976
  Sari, Piran & Narayan 1998

The functions here are convention-explicit toy helpers. Full numerical dynamics
and radiative corrections should be added only with validation records.
"""

from __future__ import annotations

from reproduce.grb.core.constants import C_LIGHT


def observer_time_from_radius(radius_cm: float, gamma: float, *, redshift: float = 0.0, factor: float = 4.0) -> float:
    """Approximate observer time for emission from radius R.

    Uses t_obs = (1 + z) R / (factor c Gamma^2). The factor is convention and
    model dependent; common afterglow estimates use values of order 2-4.
    """
    if radius_cm <= 0 or gamma <= 0 or factor <= 0:
        raise ValueError("radius_cm, gamma, and factor must be positive")
    if redshift < 0:
        raise ValueError("redshift must be non-negative")
    return (1.0 + redshift) * radius_cm / (factor * C_LIGHT * gamma * gamma)


def radius_from_observer_time(time_s: float, gamma: float, *, redshift: float = 0.0, factor: float = 4.0) -> float:
    """Invert observer_time_from_radius for a fixed Lorentz factor."""
    if time_s <= 0 or gamma <= 0 or factor <= 0:
        raise ValueError("time_s, gamma, and factor must be positive")
    if redshift < 0:
        raise ValueError("redshift must be non-negative")
    return time_s * factor * C_LIGHT * gamma * gamma / (1.0 + redshift)