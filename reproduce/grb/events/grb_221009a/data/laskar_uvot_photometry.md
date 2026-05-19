# Laskar et al. 2023 Swift/UVOT photometry

CSV: `laskar_uvot_photometry.csv`

Source: T. Laskar et al., arXiv:2302.04388, `GRB221009A_astroph_v2.tex`, table `tab:data:uvot`.

Columns:

- `time_start_s_since_swift_bat`, `time_stop_s_since_swift_bat`: source table exposure bounds, seconds since Swift/BAT trigger.
- `time_start_s_since_fermi_gbm`, `time_stop_s_since_fermi_gbm`, `time_mid_s_since_fermi_gbm`: same exposure bounds and midpoint after adding 3199 s to use the Fermi/GBM trigger zero point.
- `time_days_since_fermi_gbm`: midpoint time in observer-frame days since Fermi/GBM trigger.
- `swift_uvot_filter`: UVOT band label from the source table.
- `native_uvot_mag`, `native_uvot_mag_err`: magnitude and uncertainty in the native Swift/UVOT system.
- `mag_system`: magnitude system note copied from the table comment.
- `source_arxiv`, `source_tex_path`, `source_table`: provenance fields.

Caveat: the source table states that magnitudes are not corrected for extinction in the Milky Way or GRB host galaxy. No host-light correction or conversion to flux density is applied here.

Processing status: extracted from LaTeX source; ready for plotting and for later conversion once an extinction and photometric-system policy is chosen.
