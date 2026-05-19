"""Extract Liverpool Telescope photometry from Laskar et al. 2023.

Source:
  raw/arxiv/2302.04388/2302.04388-source.tar.gz
  GRB221009A_astroph_v2.tex, table labelled tab:data:lt

Outputs:
  reproduce/grb/events/grb_221009a/data/laskar_lt_photometry.csv
  reproduce/grb/events/grb_221009a/data/laskar_lt_photometry.md

The extracted AB magnitudes are not corrected for Milky Way extinction, host
extinction, or host-galaxy light, following the table note in the paper.
"""

from __future__ import annotations

import csv
import re
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SOURCE_TAR = ROOT / "raw" / "arxiv" / "2302.04388" / "2302.04388-source.tar.gz"
TEX_MEMBER = "GRB221009A_astroph_v2.tex"
OUT_CSV = ROOT / "reproduce" / "grb" / "events" / "grb_221009a" / "data" / "laskar_lt_photometry.csv"
OUT_MD = OUT_CSV.with_suffix(".md")

ROW_RE = re.compile(
    r"^\s*([0-9]+\.[0-9]+)\s*&\s*([griz])\s*&\s*([0-9]+\.[0-9]+)\s*&\s*([0-9]+\.[0-9]+)\s*&\s*([0-9]+)\s*&\s*([0-9]+\.[0-9]+)\s*\\\\"
)


def read_tex() -> str:
    with tarfile.open(SOURCE_TAR, "r:gz") as archive:
        member = archive.getmember(TEX_MEMBER)
        handle = archive.extractfile(member)
        if handle is None:
            raise RuntimeError(f"could not read {TEX_MEMBER} from {SOURCE_TAR}")
        return handle.read().decode("utf-8", errors="replace")


def extract_table_block(tex: str) -> str:
    label_pos = tex.find(r"\label{tab:data:lt}")
    if label_pos == -1:
        raise RuntimeError("table label tab:data:lt not found")
    start = tex.rfind(r"\startdata", 0, label_pos)
    end = tex.find(r"\enddata", label_pos)
    if start == -1 or end == -1:
        raise RuntimeError("could not locate startdata/enddata for tab:data:lt")
    return tex[start:end]


def parse_rows(block: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in block.splitlines():
        match = ROW_RE.match(line)
        if not match:
            continue
        time_d, filt, mag, mag_err, tint_s, seeing = match.groups()
        rows.append(
            {
                "time_days_since_fermi_gbm": time_d,
                "filter": filt,
                "ab_mag": mag,
                "ab_mag_err": mag_err,
                "integration_s": tint_s,
                "seeing_arcsec": seeing,
                "source_arxiv": "2302.04388",
                "source_table": "tab:data:lt",
                "notes": "Not corrected for Milky Way extinction, host extinction, or host-galaxy light.",
            }
        )
    if not rows:
        raise RuntimeError("no LT photometry rows parsed")
    return rows


def write_outputs(rows: list[dict[str, str]]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    OUT_MD.write_text(
        "\n".join(
            [
                "# Laskar et al. 2023 Liverpool Telescope photometry",
                "",
                f"CSV: `{OUT_CSV.name}`",
                "",
                "Source: T. Laskar et al., arXiv:2302.04388, `GRB221009A_astroph_v2.tex`, table `tab:data:lt`.",
                "",
                "Columns:",
                "",
                "- `time_days_since_fermi_gbm`: mid-time since Fermi/GBM trigger, days.",
                "- `filter`: Liverpool Telescope IO:O filter (`g`, `r`, `i`, `z`).",
                "- `ab_mag`: AB magnitude.",
                "- `ab_mag_err`: magnitude uncertainty.",
                "- `integration_s`: integration time, seconds.",
                "- `seeing_arcsec`: seeing, arcsec.",
                "",
                "Caveat: the table note states that the data have not been corrected for Milky Way extinction, host extinction, or host-galaxy light.",
                "",
                "Processing status: extracted from LaTeX source; model-ready for simple optical light-curve tests after extinction policy is chosen.",
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