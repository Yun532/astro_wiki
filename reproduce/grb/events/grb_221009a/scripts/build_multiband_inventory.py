"""Build a compact data inventory and plotting preview for GRB 221009A.

Inputs:
  data/laskar_lt_photometry.csv
  data/laskar_uvot_photometry.csv
  data/laskar_lat_flux.csv
  data/konus_band_spectral_fits.csv

Outputs:
  outputs/grb221009a_data_inventory.csv
  outputs/grb221009a_multiband_preview.csv

This is a data-check layer only. It does not apply extinction, host,
absorption, bolometric, rest-frame, or cross-band normalization corrections.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
EVENT_DIR = ROOT / "reproduce" / "grb" / "events" / "grb_221009a"
DATA_DIR = EVENT_DIR / "data"
OUTPUT_DIR = EVENT_DIR / "outputs"
INVENTORY_CSV = OUTPUT_DIR / "grb221009a_data_inventory.csv"
PREVIEW_CSV = OUTPUT_DIR / "grb221009a_multiband_preview.csv"

PREVIEW_FIELDS = [
    "dataset_id",
    "instrument",
    "panel",
    "series_label",
    "time_days_since_fermi_gbm",
    "time_s_since_trigger",
    "value",
    "value_err",
    "value_unit",
    "is_upper_limit",
    "source_arxiv",
    "source_table",
    "source_file",
    "notes",
]

INVENTORY_FIELDS = [
    "dataset_id",
    "source_file",
    "source_arxiv",
    "source_table",
    "instrument",
    "observable",
    "value_unit",
    "n_rows",
    "time_min_days_since_fermi_gbm",
    "time_max_days_since_fermi_gbm",
    "series_values",
    "upper_limit_rows",
    "processing_status",
    "caveat",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def float_or_empty(value: str) -> float | None:
    if value == "":
        return None
    return float(value)


def mean_abs_error(err_minus: str, err_plus: str) -> str:
    minus = float_or_empty(err_minus)
    plus = float_or_empty(err_plus)
    if minus is None and plus is None:
        return ""
    if minus is None:
        return f"{abs(plus):.8g}"
    if plus is None:
        return f"{abs(minus):.8g}"
    return f"{0.5 * (abs(minus) + abs(plus)):.8g}"


def inventory_row(
    *,
    dataset_id: str,
    rows: list[dict[str, str]],
    source_file: str,
    instrument: str,
    observable: str,
    value_unit: str,
    time_column: str,
    time_divisor: float,
    series_column: str,
    upper_limit_column: str | None,
    processing_status: str,
    caveat: str,
) -> dict[str, str]:
    times = [float(row[time_column]) / time_divisor for row in rows if row.get(time_column)]
    series_values = sorted({row[series_column] for row in rows if row.get(series_column)})
    upper_limits = 0
    if upper_limit_column:
        upper_limits = sum(1 for row in rows if row.get(upper_limit_column, "").lower() == "true")
    first = rows[0]
    return {
        "dataset_id": dataset_id,
        "source_file": source_file,
        "source_arxiv": first.get("source_arxiv", ""),
        "source_table": first.get("source_table", ""),
        "instrument": instrument,
        "observable": observable,
        "value_unit": value_unit,
        "n_rows": str(len(rows)),
        "time_min_days_since_fermi_gbm": f"{min(times):.8g}" if times else "",
        "time_max_days_since_fermi_gbm": f"{max(times):.8g}" if times else "",
        "series_values": ";".join(series_values),
        "upper_limit_rows": str(upper_limits),
        "processing_status": processing_status,
        "caveat": caveat,
    }


def lt_preview(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        out.append(
            {
                "dataset_id": "laskar_lt_photometry",
                "instrument": "Liverpool Telescope IO:O",
                "panel": "photometry_mag",
                "series_label": f"LT {row['filter']}",
                "time_days_since_fermi_gbm": row["time_days_since_fermi_gbm"],
                "time_s_since_trigger": f"{float(row['time_days_since_fermi_gbm']) * 86400.0:.8g}",
                "value": row["ab_mag"],
                "value_err": row["ab_mag_err"],
                "value_unit": "AB mag",
                "is_upper_limit": "false",
                "source_arxiv": row["source_arxiv"],
                "source_table": row["source_table"],
                "source_file": "laskar_lt_photometry.csv",
                "notes": "Observed magnitude; no Milky Way extinction, host extinction, or host light correction.",
            }
        )
    return out


def uvot_preview(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        out.append(
            {
                "dataset_id": "laskar_uvot_photometry",
                "instrument": "Swift/UVOT",
                "panel": "photometry_mag",
                "series_label": f"UVOT {row['swift_uvot_filter']}",
                "time_days_since_fermi_gbm": row["time_days_since_fermi_gbm"],
                "time_s_since_trigger": row["time_mid_s_since_fermi_gbm"],
                "value": row["native_uvot_mag"],
                "value_err": row["native_uvot_mag_err"],
                "value_unit": "native Swift/UVOT mag",
                "is_upper_limit": "false",
                "source_arxiv": row["source_arxiv"],
                "source_table": row["source_table"],
                "source_file": "laskar_uvot_photometry.csv",
                "notes": "Native Swift/UVOT magnitude; no Milky Way or host extinction correction.",
            }
        )
    return out


def lat_preview(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        is_upper = row["is_upper_limit"].lower() == "true"
        out.append(
            {
                "dataset_id": "laskar_lat_flux",
                "instrument": "Fermi/LAT",
                "panel": "energy_flux",
                "series_label": "LAT 100 MeV-100 GeV",
                "time_days_since_fermi_gbm": row["time_days_since_fermi_gbm"],
                "time_s_since_trigger": row["time_mid_s_since_trigger"],
                "value": row["energy_flux_upper_limit_erg_s_cm2"] if is_upper else row["energy_flux_erg_s_cm2"],
                "value_err": "" if is_upper else row["energy_flux_err_erg_s_cm2"],
                "value_unit": "erg s^-1 cm^-2",
                "is_upper_limit": row["is_upper_limit"],
                "source_arxiv": row["source_arxiv"],
                "source_table": row["source_table"],
                "source_file": "laskar_lat_flux.csv",
                "notes": "Energy flux in the source LAT band; upper limits are preserved as upper limits.",
            }
        )
    return out


def konus_preview(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        start_s = float(row["time_start_s_since_trigger"])
        stop_s = float(row["time_stop_s_since_trigger"])
        mid_s = 0.5 * (start_s + stop_s)
        out.append(
            {
                "dataset_id": "konus_band_spectral_fits",
                "instrument": "Konus-Wind",
                "panel": "prompt_epeak",
                "series_label": f"KW {row['emission_phase']}",
                "time_days_since_fermi_gbm": f"{mid_s / 86400.0:.8g}",
                "time_s_since_trigger": f"{mid_s:.8g}",
                "value": row["epeak_kev"],
                "value_err": mean_abs_error(row["epeak_kev_err_minus"], row["epeak_kev_err_plus"]),
                "value_unit": "keV",
                "is_upper_limit": "false",
                "source_arxiv": row["source_arxiv"],
                "source_table": row["source_table"],
                "source_file": "konus_band_spectral_fits.csv",
                "notes": "Prompt Band-function Epeak; no rest-frame or energetics conversion.",
            }
        )
    return out


def main() -> None:
    lt_rows = read_csv(DATA_DIR / "laskar_lt_photometry.csv")
    uvot_rows = read_csv(DATA_DIR / "laskar_uvot_photometry.csv")
    lat_rows = read_csv(DATA_DIR / "laskar_lat_flux.csv")
    konus_rows = read_csv(DATA_DIR / "konus_band_spectral_fits.csv")

    inventory = [
        inventory_row(
            dataset_id="laskar_lt_photometry",
            rows=lt_rows,
            source_file="laskar_lt_photometry.csv",
            instrument="Liverpool Telescope IO:O",
            observable="observed optical magnitude",
            value_unit="AB mag",
            time_column="time_days_since_fermi_gbm",
            time_divisor=1.0,
            series_column="filter",
            upper_limit_column=None,
            processing_status="preview-ready; no extinction or host correction",
            caveat="Observed AB magnitudes are not corrected for Milky Way extinction, host extinction, or host-galaxy light.",
        ),
        inventory_row(
            dataset_id="laskar_uvot_photometry",
            rows=uvot_rows,
            source_file="laskar_uvot_photometry.csv",
            instrument="Swift/UVOT",
            observable="native UVOT magnitude",
            value_unit="native Swift/UVOT mag",
            time_column="time_days_since_fermi_gbm",
            time_divisor=1.0,
            series_column="swift_uvot_filter",
            upper_limit_column=None,
            processing_status="preview-ready; no extinction correction",
            caveat="Source table uses Swift/BAT time; CSV also gives Fermi/GBM-converted times by adding 3199 s.",
        ),
        inventory_row(
            dataset_id="laskar_lat_flux",
            rows=lat_rows,
            source_file="laskar_lat_flux.csv",
            instrument="Fermi/LAT",
            observable="energy flux",
            value_unit="erg s^-1 cm^-2",
            time_column="time_days_since_fermi_gbm",
            time_divisor=1.0,
            series_column="energy_band",
            upper_limit_column="is_upper_limit",
            processing_status="preview-ready; upper limits preserved",
            caveat="Energy flux is kept in the paper's 100 MeV-100 GeV band and photon-index convention.",
        ),
        inventory_row(
            dataset_id="konus_band_spectral_fits",
            rows=konus_rows,
            source_file="konus_band_spectral_fits.csv",
            instrument="Konus-Wind",
            observable="prompt Band Epeak",
            value_unit="keV",
            time_column="time_start_s_since_trigger",
            time_divisor=86400.0,
            series_column="emission_phase",
            upper_limit_column=None,
            processing_status="preview-ready for prompt spectral-parameter checks",
            caveat="Prompt Epeak is kept in observer frame; no rest-frame, bolometric, or energetics conversion.",
        ),
    ]

    preview = []
    preview.extend(lt_preview(lt_rows))
    preview.extend(uvot_preview(uvot_rows))
    preview.extend(lat_preview(lat_rows))
    preview.extend(konus_preview(konus_rows))

    write_csv(INVENTORY_CSV, inventory, INVENTORY_FIELDS)
    write_csv(PREVIEW_CSV, preview, PREVIEW_FIELDS)
    print(f"wrote {INVENTORY_CSV} rows={len(inventory)}")
    print(f"wrote {PREVIEW_CSV} rows={len(preview)}")


if __name__ == "__main__":
    main()
