"""Toy gamma-gamma pair-production helpers for GRB radiation experiments.

Theory page: TODO.

These functions are placeholders for order-of-magnitude interfaces only. They
do not claim paper-level accuracy, use simplified threshold and opacity
estimates, and should be replaced or calibrated after the theory page defines
the adopted conventions.
"""

from __future__ import annotations


ELECTRON_REST_ENERGY_KEV = 510.99895


def pair_threshold_target_energy_kev(
    gamma_energy_kev: float,
    *,
    collision_angle_cosine: float = -1.0,
) -> float:
    """Return target photon energy at the gamma-gamma pair threshold."""
    if gamma_energy_kev <= 0:
        raise ValueError("gamma_energy_kev must be positive")
    if not -1.0 <= collision_angle_cosine < 1.0:
        raise ValueError("collision_angle_cosine must be in [-1, 1)")
    angle_factor = 1.0 - collision_angle_cosine
    return 2.0 * ELECTRON_REST_ENERGY_KEV**2 / (gamma_energy_kev * angle_factor)


def compactness_opacity_scale(
    photon_density_cm3: float,
    path_length_cm: float,
    cross_section_cm2: float,
) -> float:
    """Return a simple optical-depth scale tau = n sigma l."""
    if photon_density_cm3 < 0:
        raise ValueError("photon_density_cm3 must be non-negative")
    if path_length_cm < 0:
        raise ValueError("path_length_cm must be non-negative")
    if cross_section_cm2 < 0:
        raise ValueError("cross_section_cm2 must be non-negative")
    return photon_density_cm3 * cross_section_cm2 * path_length_cm
