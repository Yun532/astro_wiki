"""Toy bremsstrahlung helpers for GRB radiation experiments.

Theory page: TODO.

These functions are placeholders for order-of-magnitude interfaces only. They
do not claim paper-level accuracy, omit geometry and detailed Gaunt factors,
and should be replaced or calibrated after the theory page defines the adopted
conventions.
"""

from __future__ import annotations

import math


def thermal_cutoff_factor(photon_energy_kev: float, temperature_kev: float) -> float:
    """Return the exponential thermal cutoff exp(-E/kT)."""
    if photon_energy_kev < 0:
        raise ValueError("photon_energy_kev must be non-negative")
    if temperature_kev <= 0:
        raise ValueError("temperature_kev must be positive")
    return math.exp(-photon_energy_kev / temperature_kev)


def optically_thin_emissivity_scale(
    electron_density_cm3: float,
    ion_density_cm3: float,
    temperature_kev: float,
) -> float:
    """Return a proportional free-free emissivity scale n_e n_i sqrt(T)."""
    if electron_density_cm3 < 0 or ion_density_cm3 < 0:
        raise ValueError("densities must be non-negative")
    if temperature_kev <= 0:
        raise ValueError("temperature_kev must be positive")
    return electron_density_cm3 * ion_density_cm3 * math.sqrt(temperature_kev)
