"""Extract Swift/UVOT and Fermi/LAT tables from Laskar et al. 2023.

Source:
  raw/arxiv/2302.04388/2302.04388-source.tar.gz
  GRB221009A_astroph_v2.tex, tables labelled tab:data:uvot and tab:data:LAT

Outputs:
  reproduce/grb/events/grb_221009a/data/laskar_uvot_photometry.csv
  reproduce/grb/events/grb_221009a/data/laskar_uvot_photometry.md
  reproduce/grb/events/grb_221009a/data/laskar_lat_flux.csv
  reproduce/grb/events/grb_221009a/data/laskar_lat_flux.md

The extracted rows preserve the source table definitions. No extinction,
absorption, host-light, or unit correction is applied.
"""

from __future__ import annotations

import csv
import re
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SOURCE_TAR = ROOT / "raw" / "arxiv" / "2302.04388" / "2302.04388-source.tar.gz"
TEX_MEMBER = "GRB221009A_astroph_v2.tex"
DATA_DIR = ROOT / "reproduce" / "grb" / "events" / "grb_221009a" / "data"
UVOT_CSV = DATA_DIR / "laskar_uvot_photometry.csv"
LAT_CSV = DATA_DIR / "laskar_lat_flux.csv"

TEX_NUMBER = r"[0-9]+(?:\.[0-9]*)?"
UVOT_ROW_RE = re.compile(
    rf"^\s*({TEX_NUMBER})\s*&\s*({TEX_NUMBER})\s*&\s*\$([^$]+)\$\s*&\s*({TEX_NUMBER})\s*&\s*({TEX_NUMBER})\s*\\\\"
)
LAT_ROW_RE = re.compile(
    rf"^\s*({TEX_NUMBER})\s*&\s*({TEX_NUMBER})\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*([0-9]+)\s*\\\\"
)


def read_tex() -> str:
    with tarfile.open(SOURCE_TAR, "r:gz") as archive:
        member = archive.getmember(TEX_MEMBER)
        handle = archive.extractfile(member)
        if handle is None:
            raise RuntimeError(f"could not read {TEX_MEMBER} from {SOURCE_TAR}")
        return handle.read().decode("utf-8", errors="replace")


def extract_table_block(tex: str, label: str) -> str:
    label_pos = tex.find(rf"\label{{{label}}}")
    if label_pos == -1:
        raise RuntimeError(f"table label {label} not found")
    start = tex.find(r"\startdata", label_pos)
    end = tex.find(r"\enddata", start)
    if start == -1 or end == -1:
        raise RuntimeError(f"could not locate startdata/enddata for {label}")
    return tex[start:end]


def clean_tex_cell(value: str) -> str:
    value = value.strip()
    value = value.replace(r"\ldots", "")
    value = value.replace("$", "")
    value = value.replace(r"\,", "")
    return value.strip()


def tex_sci_to_float_text(value: str) -> str:
    value = clean_tex_cell(value)
    if not value or value.startswith("<"):
        return ""
    value = value.replace(r"\times10^{", "e").replace("}", "")
    return f"{float(value):.8g}"


def tex_sci_limit_to_float_text(value: str) -> str:
    value = clean_tex_cell(value)
    if not value.startswith("<"):
        return ""
    value = value[1:].replace(r"\times10^{", "e").replace("}", "")
    return f"{float(value):.8g}"


def parse_uvot_rows(block: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in block.splitlines():
        match = UVOT_ROW_RE.match(line)
        if not match:
            continue
        start_s, stop_s, filt, mag, mag_err = match.groups()
        start_fermi = float(start_s) + 3199.0
        stop_fermi = float(stop_s) + 3199.0
        mid_fermi = 0.5 * (start_fermi + stop_fermi)
        rows.append(
            {
                "time_start_s_since_swift_bat": start_s,
                "time_stop_s_since_swift_bat": stop_s,
                "time_start_s_since_fermi_gbm": f"{start_fermi:.1f}",
                "time_stop_s_since_fermi_gbm": f"{stop_fermi:.1f}",
                "time_mid_s_since_fermi_gbm": f"{mid_fermi:.1f}",
                "time_days_since_fermi_gbm": f"{mid_fermi / 86400.0:.8g}",
                "swift_uvot_filter": filt,
                "native_uvot_mag": mag,
                "native_uvot_mag_err": mag_err,
                "mag_system": "native Swift/UVOT system",
                "source_arxiv": "2302.04388",
                "source_tex_path": TEX_MEMBER,
                "source_table": "tab:data:uvot",
                "notes": "Times in source table are since Swift/BAT trigger; add 3199 s for Fermi/GBM. Not corrected for Milky Way or host extinction.",
            }
        )
    if not rows:
        raise RuntimeError("no UVOT rows parsed")
    return rows


def parse_lat_rows(block: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    logical_lines = []
    pending = ""
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(r"\startdata"):
            continue
        pending = f"{pending} {line}".strip()
        if line.endswith(r"\\"):
            logical_lines.append(pending)
            pending = ""
    for line in logical_lines:
        match = LAT_ROW_RE.match(line)
        if not match:
            continue
        (
            start_s,
            stop_s,
            energy_flux_raw,
            energy_flux_err_raw,
            photon_flux_raw,
            photon_flux_err_raw,
            photon_index_raw,
            photon_index_err_raw,
            ts,
        ) = match.groups()
        energy_flux_text = clean_tex_cell(energy_flux_raw)
        photon_flux_text = clean_tex_cell(photon_flux_raw)
        is_upper = "true" if energy_flux_text.startswith("<") or photon_flux_text.startswith("<") else "false"
        rows.append(
            {
                "time_start_s_since_trigger": start_s,
                "time_stop_s_since_trigger": stop_s,
                "time_mid_s_since_trigger": f"{0.5 * (float(start_s) + float(stop_s)):.1f}",
                "time_days_since_fermi_gbm": f"{0.5 * (float(start_s) + float(stop_s)) / 86400.0:.8g}",
                "energy_band": "100 MeV-100 GeV",
                "energy_flux_erg_s_cm2_text": energy_flux_text,
                "energy_flux_erg_s_cm2": tex_sci_to_float_text(energy_flux_raw),
                "energy_flux_upper_limit_erg_s_cm2": tex_sci_limit_to_float_text(energy_flux_raw),
                "energy_flux_err_erg_s_cm2": tex_sci_to_float_text(energy_flux_err_raw),
                "photon_flux_ph_s_cm2_text": photon_flux_text,
                "photon_flux_ph_s_cm2": tex_sci_to_float_text(photon_flux_raw),
                "photon_flux_upper_limit_ph_s_cm2": tex_sci_limit_to_float_text(photon_flux_raw),
                "photon_flux_err_ph_s_cm2": tex_sci_to_float_text(photon_flux_err_raw),
                "photon_index": clean_tex_cell(photon_index_raw),
                "photon_index_err": clean_tex_cell(photon_index_err_raw),
                "test_statistic": ts,
                "is_upper_limit": is_upper,
                "source_arxiv": "2302.04388",
                "source_tex_path": TEX_MEMBER,
                "source_table": "tab:data:LAT",
                "notes": "Times are with respect to the Fermi/GBM trigger. Photon index convention is F_E proportional to E^-Gamma.",
            }
        )
    if not rows:
        raise RuntimeError("no LAT rows parsed")
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_sidecars() -> None:
    UVOT_CSV.with_suffix(".md").write_text(
        "\n".join(
            [
                "# Laskar et al. 2023 Swift/UVOT photometry",
                "",
                f"CSV: `{UVOT_CSV.name}`",
                "",
                "Source: T. Laskar et al., arXiv:2302.04388, `GRB221009A_astroph_v2.tex`, table `tab:data:uvot`.",
                "",
                "Columns:",
                "",
                "- `time_start_s_since_swift_bat`, `time_stop_s_since_swift_bat`: source table exposure bounds, seconds since Swift/BAT trigger.",
                "- `time_start_s_since_fermi_gbm`, `time_stop_s_since_fermi_gbm`, `time_mid_s_since_fermi_gbm`: same exposure bounds and midpoint after adding 3199 s to use the Fermi/GBM trigger zero point.",
                "- `time_days_since_fermi_gbm`: midpoint time in observer-frame days since Fermi/GBM trigger.",
                "- `swift_uvot_filter`: UVOT band label from the source table.",
                "- `native_uvot_mag`, `native_uvot_mag_err`: magnitude and uncertainty in the native Swift/UVOT system.",
                "- `mag_system`: magnitude system note copied from the table comment.",
                "- `source_arxiv`, `source_tex_path`, `source_table`: provenance fields.",
                "",
                "Caveat: the source table states that magnitudes are not corrected for extinction in the Milky Way or GRB host galaxy. No host-light correction or conversion to flux density is applied here.",
                "",
                "Processing status: extracted from LaTeX source; ready for plotting and for later conversion once an extinction and photometric-system policy is chosen.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    LAT_CSV.with_suffix(".md").write_text(
        "\n".join(
            [
                "# Laskar et al. 2023 Fermi/LAT flux table",
                "",
                f"CSV: `{LAT_CSV.name}`",
                "",
                "Source: T. Laskar et al., arXiv:2302.04388, `GRB221009A_astroph_v2.tex`, table `tab:data:LAT`.",
                "",
                "Columns:",
                "",
                "- `time_start_s_since_trigger`, `time_stop_s_since_trigger`, `time_mid_s_since_trigger`: LAT bin bounds and midpoint, seconds since Fermi/GBM trigger.",
                "- `time_days_since_fermi_gbm`: midpoint time in observer-frame days since Fermi/GBM trigger.",
                "- `energy_band`: source-analysis LAT energy band, 100 MeV-100 GeV.",
                "- `energy_flux_erg_s_cm2_text`, `photon_flux_ph_s_cm2_text`: raw source-table flux cells, preserving upper-limit notation.",
                "- `energy_flux_erg_s_cm2`, `energy_flux_err_erg_s_cm2`: numeric detection energy flux and 1 sigma uncertainty, erg s^-1 cm^-2.",
                "- `energy_flux_upper_limit_erg_s_cm2`: numeric upper-limit value when the row is an upper limit.",
                "- `photon_flux_ph_s_cm2`, `photon_flux_err_ph_s_cm2`: numeric detection photon flux and 1 sigma uncertainty, ph s^-1 cm^-2.",
                "- `photon_flux_upper_limit_ph_s_cm2`: numeric upper-limit value when the row is an upper limit.",
                "- `photon_index`, `photon_index_err`: power-law photon index and uncertainty. The source defines the convention as F_E proportional to E^-Gamma.",
                "- `test_statistic`, `is_upper_limit`: LAT likelihood TS and extraction-stage upper-limit flag.",
                "- `source_arxiv`, `source_tex_path`, `source_table`: provenance fields.",
                "",
                "Caveat: LAT rows preserve the paper's likelihood-analysis energy band and spectral convention. The final low-TS row is kept as an upper limit and is not forced into a detection flux.",
                "",
                "Processing status: extracted from LaTeX source; usable for first-pass GeV afterglow comparisons after upper-limit handling is chosen.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    tex = read_tex()
    uvot_rows = parse_uvot_rows(extract_table_block(tex, "tab:data:uvot"))
    lat_rows = parse_lat_rows(extract_table_block(tex, "tab:data:LAT"))
    write_csv(UVOT_CSV, uvot_rows)
    write_csv(LAT_CSV, lat_rows)
    write_sidecars()
    print(f"wrote {UVOT_CSV} rows={len(uvot_rows)}")
    print(f"wrote {LAT_CSV} rows={len(lat_rows)}")


if __name__ == "__main__":
    main()
