"""Toy hadronic radiation helpers for GRB radiation experiments.

Theory page: TODO.

These functions are placeholders for order-of-magnitude interfaces only. They
do not claim paper-level accuracy, omit detailed particle spectra and cascade
physics, and should be replaced or calibrated after the theory page defines the
adopted conventions.
"""

from __future__ import annotations


def pion_decay_gamma_energy_gev(proton_energy_gev: float, *, pion_fraction: float = 0.2) -> float:
    """Estimate characteristic gamma energy from neutral-pion decay."""
    if proton_energy_gev <= 0:
        raise ValueError("proton_energy_gev must be positive")
    if not 0.0 < pion_fraction <= 1.0:
        raise ValueError("pion_fraction must be in (0, 1]")
    return 0.5 * pion_fraction * proton_energy_gev


def pp_interaction_efficiency(
    target_density_cm3: float,
    path_length_cm: float,
    cross_section_cm2: float = 3.0e-26,
) -> float:
    """Return a thin-target pp interaction efficiency capped at unity."""
    if target_density_cm3 < 0:
        raise ValueError("target_density_cm3 must be non-negative")
    if path_length_cm < 0:
        raise ValueError("path_length_cm must be non-negative")
    if cross_section_cm2 < 0:
        raise ValueError("cross_section_cm2 must be non-negative")
    return min(target_density_cm3 * cross_section_cm2 * path_length_cm, 1.0)
