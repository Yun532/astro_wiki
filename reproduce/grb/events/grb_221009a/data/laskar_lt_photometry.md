# Laskar et al. 2023 Liverpool Telescope photometry

CSV: `laskar_lt_photometry.csv`

Source: T. Laskar et al., arXiv:2302.04388, `GRB221009A_astroph_v2.tex`, table `tab:data:lt`.

Columns:

- `time_days_since_fermi_gbm`: mid-time since Fermi/GBM trigger, days.
- `filter`: Liverpool Telescope IO:O filter (`g`, `r`, `i`, `z`).
- `ab_mag`: AB magnitude.
- `ab_mag_err`: magnitude uncertainty.
- `integration_s`: integration time, seconds.
- `seeing_arcsec`: seeing, arcsec.

Caveat: the table note states that the data have not been corrected for Milky Way extinction, host extinction, or host-galaxy light.

Processing status: extracted from LaTeX source; model-ready for simple optical light-curve tests after extinction policy is chosen.
