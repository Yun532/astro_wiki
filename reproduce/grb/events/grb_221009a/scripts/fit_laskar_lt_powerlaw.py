"""Fit simple per-filter optical power-law decays to Laskar LT photometry.

Model:
  F_nu(t) proportional to t^-alpha
  m_AB(t) = m_ref + 2.5 alpha log10(t / 1 day)

This is a phenomenological sanity check, not a physical afterglow fit. The input
magnitudes are not corrected for Milky Way extinction, host extinction, or host
light, following the source table note.
"""

from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "reproduce" / "grb" / "events" / "grb_221009a" / "data" / "laskar_lt_photometry.csv"
OUT = ROOT / "reproduce" / "grb" / "events" / "grb_221009a" / "outputs" / "laskar_lt_powerlaw_fit.csv"
VALIDATION = ROOT / "reproduce" / "grb" / "validation" / "laskar_lt_powerlaw_fit.md"


def weighted_line_fit(points: list[tuple[float, float, float]]) -> dict[str, float]:
    """Weighted fit y = a + b x with sigma_y errors."""
    if len(points) < 3:
        raise ValueError("need at least three points")
    s = sx = sy = sxx = sxy = 0.0
    for x, y, sigma in points:
        if sigma <= 0:
            raise ValueError("sigma must be positive")
        w = 1.0 / (sigma * sigma)
        s += w
        sx += w * x
        sy += w * y
        sxx += w * x * x
        sxy += w * x * y
    delta = s * sxx - sx * sx
    if delta <= 0:
        raise ValueError("singular fit")
    a = (sxx * sy - sx * sxy) / delta
    b = (s * sxy - sx * sy) / delta
    sigma_a = math.sqrt(sxx / delta)
    sigma_b = math.sqrt(s / delta)
    chi2 = 0.0
    for x, y, sigma in points:
        chi2 += ((y - (a + b * x)) / sigma) ** 2
    dof = len(points) - 2
    return {
        "m_ref_ab_at_1d": a,
        "m_ref_ab_err": sigma_a,
        "slope_mag_per_log10_day": b,
        "slope_err": sigma_b,
        "alpha_flux_decay": b / 2.5,
        "alpha_err": sigma_b / 2.5,
        "chi2": chi2,
        "dof": float(dof),
        "chi2_dof": chi2 / dof if dof > 0 else float("nan"),
    }


def read_points() -> dict[str, list[tuple[float, float, float]]]:
    groups: dict[str, list[tuple[float, float, float]]] = defaultdict(list)
    with DATA.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            time_d = float(row["time_days_since_fermi_gbm"])
            mag = float(row["ab_mag"])
            mag_err = float(row["ab_mag_err"])
            filt = row["filter"]
            groups[filt].append((math.log10(time_d), mag, mag_err))
    return dict(groups)


def write_outputs(results: list[dict[str, str]]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "filter",
        "n_points",
        "m_ref_ab_at_1d",
        "m_ref_ab_err",
        "slope_mag_per_log10_day",
        "slope_err",
        "alpha_flux_decay",
        "alpha_err",
        "chi2",
        "dof",
        "chi2_dof",
        "notes",
    ]
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    lines = [
        "# Laskar LT photometry power-law sanity check",
        "",
        "验证对象：Liverpool Telescope optical AB magnitudes fitted with a single per-filter power-law decay.",
        "",
        "模型：`F_nu(t) proportional to t^-alpha`, so `m_AB(t) = m_ref + 2.5 alpha log10(t / 1 day)`.",
        "",
        f"Input: `{DATA.relative_to(ROOT).as_posix()}`",
        f"Output: `{OUT.relative_to(ROOT).as_posix()}`",
        "",
        "Caveat: this is a phenomenological sanity check only. The input table is not corrected for Milky Way extinction, host extinction, or host-galaxy light. It does not model color evolution, spectral breaks, supernova/host contamination, or multi-component afterglow physics.",
        "",
        "## Results",
        "",
        "| filter | n | alpha | alpha_err | chi2/dof |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in results:
        lines.append(
            f"| {row['filter']} | {row['n_points']} | {row['alpha_flux_decay']} | {row['alpha_err']} | {row['chi2_dof']} |"
        )
    lines.extend(
        [
            "",
            "人工检查：待用户验证。",
            "",
            "下一步：加入 extinction policy，把 AB mag 转为 flux density，并与 radio / X-ray 数据做 first-pass multi-band comparison。",
            "",
        ]
    )
    VALIDATION.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    groups = read_points()
    results: list[dict[str, str]] = []
    for filt in sorted(groups):
        fit = weighted_line_fit(groups[filt])
        result = {
            "filter": filt,
            "n_points": str(len(groups[filt])),
            "notes": "single power-law in observed AB magnitudes; no extinction or host correction",
        }
        for key, value in fit.items():
            result[key] = f"{value:.6g}"
        results.append(result)
    write_outputs(results)
    print(f"wrote {OUT} filters={','.join(row['filter'] for row in results)}")


if __name__ == "__main__":
    main()