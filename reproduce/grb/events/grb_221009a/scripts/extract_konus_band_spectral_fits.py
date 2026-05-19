"""Extract Konus-Wind Band spectral fits from Frederiks et al. 2023.

Source:
  raw/arxiv/2302.13383/2302.13383-source.tar.gz
  grb221009a.tex, table labelled TableSpec

Outputs:
  reproduce/grb/events/grb_221009a/data/konus_band_spectral_fits.csv
  reproduce/grb/events/grb_221009a/data/konus_band_spectral_fits.md

The extraction keeps the paper's Band-function parameterization, time
intervals, and 20 keV-10 MeV flux definition. No bolometric correction or
rest-frame transformation is applied.
"""

from __future__ import annotations

import csv
import re
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SOURCE_TAR = ROOT / "raw" / "arxiv" / "2302.13383" / "2302.13383-source.tar.gz"
TEX_MEMBER = "grb221009a.tex"
OUT_CSV = ROOT / "reproduce" / "grb" / "events" / "grb_221009a" / "data" / "konus_band_spectral_fits.csv"
OUT_MD = OUT_CSV.with_suffix(".md")

ROW_RE = re.compile(
    r"^\s*(.+?)\s*&\s*([0-9.]+)--([0-9.]+)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*\$?([0-9]+)/([0-9]+)\$?\s*&\s*(.+?)\s*\\\\"
)
PHASE_RE = re.compile(r"\\multicolumn\{7\}\{c\}\{(.+?)\}")
VALUE_ERR_RE = re.compile(
    r"^<?\s*([-+]?[0-9]+(?:\.[0-9]+)?)\s*(?:_\{([-+]?[0-9]+(?:\.[0-9]+)?)\}\^\{([-+]?[0-9]+(?:\.[0-9]+)?)\})?$"
)
SCI_ERR_RE = re.compile(
    r"^([-+]?[0-9]+(?:\.[0-9]+)?)_\{([-+]?[0-9]+(?:\.[0-9]+)?)\}\^\{([-+]?[0-9]+(?:\.[0-9]+)?)\}\\times10\^\{([-+]?[0-9]+)\}$"
)


def read_tex() -> str:
    with tarfile.open(SOURCE_TAR, "r:gz") as archive:
        member = archive.getmember(TEX_MEMBER)
        handle = archive.extractfile(member)
        if handle is None:
            raise RuntimeError(f"could not read {TEX_MEMBER} from {SOURCE_TAR}")
        return handle.read().decode("utf-8", errors="replace")


def extract_table_block(tex: str) -> str:
    label_pos = tex.find(r"\label{TableSpec}")
    if label_pos == -1:
        raise RuntimeError("table label TableSpec not found")
    start = tex.find(r"\startdata", label_pos)
    end = tex.find(r"\enddata", start)
    if start == -1 or end == -1:
        raise RuntimeError("could not locate startdata/enddata for TableSpec")
    return tex[start:end]


def clean_tex_cell(value: str) -> str:
    value = value.strip()
    value = re.sub(r"\\tablenotemark\{[^}]+\}", "", value)
    value = value.replace("$", "")
    return value.strip()


def normalize_phase(value: str) -> str:
    return clean_tex_cell(value).replace("\\", "").strip()


def parse_value_with_errors(value: str) -> tuple[str, str, str, str, str]:
    """Return raw, value, minus error, plus error, upper-limit flag."""
    raw = clean_tex_cell(value)
    upper = "true" if raw.startswith("<") else "false"
    match = VALUE_ERR_RE.match(raw)
    if not match:
        return raw, "", "", "", upper
    central, err_minus, err_plus = match.groups()
    return raw, central, err_minus or "", err_plus or "", upper


def parse_sci_value_with_errors(value: str) -> tuple[str, str, str, str]:
    raw = clean_tex_cell(value)
    match = SCI_ERR_RE.match(raw)
    if not match:
        return raw, "", "", ""
    central, err_minus, err_plus, exponent = match.groups()
    scale = 10.0 ** int(exponent)
    return (
        raw,
        f"{float(central) * scale:.8g}",
        f"{float(err_minus) * scale:.8g}",
        f"{float(err_plus) * scale:.8g}",
    )


def parse_rows(block: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    phase = ""
    for line in block.splitlines():
        phase_match = PHASE_RE.search(line)
        if phase_match:
            phase = normalize_phase(phase_match.group(1))
            continue
        match = ROW_RE.match(line)
        if not match:
            continue
        spectrum, start_s, stop_s, alpha_raw, beta_raw, epeak_raw, chi2, dof, flux_raw = match.groups()
        alpha = parse_value_with_errors(alpha_raw)
        beta = parse_value_with_errors(beta_raw)
        epeak = parse_value_with_errors(epeak_raw)
        flux = parse_sci_value_with_errors(flux_raw)
        rows.append(
            {
                "spectrum_id": clean_tex_cell(spectrum),
                "emission_phase": phase,
                "time_interval_s_since_trigger": f"{start_s}--{stop_s}",
                "time_start_s_since_trigger": start_s,
                "time_stop_s_since_trigger": stop_s,
                "band_alpha_raw": alpha[0],
                "band_alpha": alpha[1],
                "band_alpha_err_minus": alpha[2],
                "band_alpha_err_plus": alpha[3],
                "band_beta_raw": beta[0],
                "band_beta": beta[1],
                "band_beta_err_minus": beta[2],
                "band_beta_err_plus": beta[3],
                "band_beta_is_upper_limit": beta[4],
                "epeak_kev_raw": epeak[0],
                "epeak_kev": epeak[1],
                "epeak_kev_err_minus": epeak[2],
                "epeak_kev_err_plus": epeak[3],
                "flux_erg_cm2_s_20kev_10mev_raw": flux[0],
                "flux_erg_cm2_s_20kev_10mev": flux[1],
                "flux_erg_cm2_s_20kev_10mev_err_minus": flux[2],
                "flux_erg_cm2_s_20kev_10mev_err_plus": flux[3],
                "chi2": chi2,
                "dof": dof,
                "spectral_model": "Band",
                "source_arxiv": "2302.13383",
                "source_tex_path": TEX_MEMBER,
                "source_table": "TableSpec",
                "notes": "Flux averaged over the spectrum accumulation interval in the 20 keV-10 MeV band. No rest-frame or bolometric correction applied.",
            }
        )
    if not rows:
        raise RuntimeError("no Konus Band spectral-fit rows parsed")
    return rows


def write_outputs(rows: list[dict[str, str]]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    OUT_MD.write_text(
        "\n".join(
            [
                "# Frederiks et al. 2023 Konus-Wind Band spectral fits",
                "",
                f"CSV: `{OUT_CSV.name}`",
                "",
                "Source: D. Frederiks et al., arXiv:2302.13383, `grb221009a.tex`, table `TableSpec`.",
                "",
                "Columns:",
                "",
                "- `spectrum_id`, `emission_phase`: spectrum bin label and prompt-emission phase heading from the source table.",
                "- `time_interval_s_since_trigger`, `time_start_s_since_trigger`, `time_stop_s_since_trigger`: accumulation interval in seconds since the Konus-Wind trigger reference used by the paper.",
                "- `band_alpha*`, `band_beta*`, `epeak_kev*`: Band-function parameters, raw LaTeX cell plus parsed central value and asymmetric errors where available.",
                "- `band_beta_is_upper_limit`: true when the source table gives only an upper limit for beta.",
                "- `flux_erg_cm2_s_20kev_10mev*`: time-averaged energy flux and asymmetric errors in the 20 keV-10 MeV band.",
                "- `chi2`, `dof`: source-table fit statistic.",
                "- `spectral_model`, `source_arxiv`, `source_tex_path`, `source_table`: model/provenance fields.",
                "",
                "Caveat: these are prompt-emission spectral fits. Fluxes are kept in the paper's 20 keV-10 MeV observer-frame band and are not converted to isotropic energetics, rest-frame quantities, or bolometric values.",
                "",
                "Processing status: extracted from LaTeX source; suitable for prompt spectral-parameter comparisons and later energetics calculations once cosmology and integration conventions are fixed.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    tex = read_tex()
    rows = parse_rows(extract_table_block(tex))
    write_outputs(rows)
    print(f"wrote {OUT_CSV} rows={len(rows)}")


if __name__ == "__main__":
    main()
