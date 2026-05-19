"""Plot the Phase 3 GRB 221009A multiband preview table.

Input:
  outputs/grb221009a_multiband_preview.csv

Output:
  outputs/grb221009a_multiband_preview.png

The plot is a data QA figure only. It does not place different wavebands on a
shared physical flux scale.
"""

from __future__ import annotations

import csv
import os
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
EVENT_DIR = ROOT / "reproduce" / "grb" / "events" / "grb_221009a"
PREVIEW_CSV = EVENT_DIR / "outputs" / "grb221009a_multiband_preview.csv"
OUT_PNG = EVENT_DIR / "outputs" / "grb221009a_multiband_preview.png"


def load_rows() -> list[dict[str, str]]:
    with PREVIEW_CSV.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def rows_by_panel(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["panel"]].append(row)
    return dict(grouped)


def plot_panel(ax, rows: list[dict[str, str]], *, ylabel: str, title: str, log_y: bool = False, invert_y: bool = False) -> None:
    series = defaultdict(list)
    for row in rows:
        series[row["series_label"]].append(row)
    for label in sorted(series):
        values = sorted(series[label], key=lambda item: float(item["time_days_since_fermi_gbm"]))
        detections = [row for row in values if row["is_upper_limit"].lower() != "true"]
        upper_limits = [row for row in values if row["is_upper_limit"].lower() == "true"]
        if detections:
            x = [float(row["time_days_since_fermi_gbm"]) for row in detections]
            y = [float(row["value"]) for row in detections]
            yerr = [float(row["value_err"]) if row["value_err"] else 0.0 for row in detections]
            ax.errorbar(x, y, yerr=yerr, marker="o", linestyle="none", markersize=4, capsize=2, label=label)
        if upper_limits:
            x = [float(row["time_days_since_fermi_gbm"]) for row in upper_limits]
            y = [float(row["value"]) for row in upper_limits]
            ax.scatter(x, y, marker="v", s=36, label=f"{label} upper limit")
    ax.set_xscale("log")
    if log_y:
        ax.set_yscale("log")
    if invert_y:
        ax.invert_yaxis()
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(fontsize=7, ncols=2)


def main() -> None:
    try:
        os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix="grb221009a-mpl-"))
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise SystemExit(
            "matplotlib is required to create grb221009a_multiband_preview.png; "
            "install matplotlib or run only build_multiband_inventory.py."
        ) from exc

    rows = load_rows()
    if not rows:
        raise RuntimeError(f"no rows found in {PREVIEW_CSV}")
    grouped = rows_by_panel(rows)
    expected_panels = {"photometry_mag", "energy_flux", "prompt_epeak"}
    missing = expected_panels - set(grouped)
    if missing:
        raise RuntimeError(f"preview table missing panels: {sorted(missing)}")

    fig, axes = plt.subplots(3, 1, figsize=(9, 10), sharex=True, constrained_layout=True)
    plot_panel(
        axes[0],
        grouped["photometry_mag"],
        ylabel="Magnitude",
        title="Optical/UV photometry (observed systems)",
        invert_y=True,
    )
    plot_panel(
        axes[1],
        grouped["energy_flux"],
        ylabel="Energy flux (erg s^-1 cm^-2)",
        title="Fermi/LAT 100 MeV-100 GeV",
        log_y=True,
    )
    plot_panel(
        axes[2],
        grouped["prompt_epeak"],
        ylabel="Band Epeak (keV)",
        title="Konus-Wind prompt Band fits",
        log_y=True,
    )
    axes[2].set_xlabel("Observer-frame days since Fermi/GBM trigger or source trigger reference")
    fig.suptitle("GRB 221009A Phase 3 multiband data preview", fontsize=14)
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PNG, dpi=180)
    plt.close(fig)
    print(f"wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
