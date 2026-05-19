# Laskar et al. 2023 Fermi/LAT flux table

CSV: `laskar_lat_flux.csv`

Source: T. Laskar et al., arXiv:2302.04388, `GRB221009A_astroph_v2.tex`, table `tab:data:LAT`.

Columns:

- `time_start_s_since_trigger`, `time_stop_s_since_trigger`, `time_mid_s_since_trigger`: LAT bin bounds and midpoint, seconds since Fermi/GBM trigger.
- `time_days_since_fermi_gbm`: midpoint time in observer-frame days since Fermi/GBM trigger.
- `energy_band`: source-analysis LAT energy band, 100 MeV-100 GeV.
- `energy_flux_erg_s_cm2_text`, `photon_flux_ph_s_cm2_text`: raw source-table flux cells, preserving upper-limit notation.
- `energy_flux_erg_s_cm2`, `energy_flux_err_erg_s_cm2`: numeric detection energy flux and 1 sigma uncertainty, erg s^-1 cm^-2.
- `energy_flux_upper_limit_erg_s_cm2`: numeric upper-limit value when the row is an upper limit.
- `photon_flux_ph_s_cm2`, `photon_flux_err_ph_s_cm2`: numeric detection photon flux and 1 sigma uncertainty, ph s^-1 cm^-2.
- `photon_flux_upper_limit_ph_s_cm2`: numeric upper-limit value when the row is an upper limit.
- `photon_index`, `photon_index_err`: power-law photon index and uncertainty. The source defines the convention as F_E proportional to E^-Gamma.
- `test_statistic`, `is_upper_limit`: LAT likelihood TS and extraction-stage upper-limit flag.
- `source_arxiv`, `source_tex_path`, `source_table`: provenance fields.

Caveat: LAT rows preserve the paper's likelihood-analysis energy band and spectral convention. The final low-TS row is kept as an upper limit and is not forced into a detection flux.

Processing status: extracted from LaTeX source; usable for first-pass GeV afterglow comparisons after upper-limit handling is chosen.
