# Frederiks et al. 2023 Konus-Wind Band spectral fits

CSV: `konus_band_spectral_fits.csv`

Source: D. Frederiks et al., arXiv:2302.13383, `grb221009a.tex`, table `TableSpec`.

Columns:

- `spectrum_id`, `emission_phase`: spectrum bin label and prompt-emission phase heading from the source table.
- `time_interval_s_since_trigger`, `time_start_s_since_trigger`, `time_stop_s_since_trigger`: accumulation interval in seconds since the Konus-Wind trigger reference used by the paper.
- `band_alpha*`, `band_beta*`, `epeak_kev*`: Band-function parameters, raw LaTeX cell plus parsed central value and asymmetric errors where available.
- `band_beta_is_upper_limit`: true when the source table gives only an upper limit for beta.
- `flux_erg_cm2_s_20kev_10mev*`: time-averaged energy flux and asymmetric errors in the 20 keV-10 MeV band.
- `chi2`, `dof`: source-table fit statistic.
- `spectral_model`, `source_arxiv`, `source_tex_path`, `source_table`: model/provenance fields.

Caveat: these are prompt-emission spectral fits. Fluxes are kept in the paper's 20 keV-10 MeV observer-frame band and are not converted to isotropic energetics, rest-frame quantities, or bolometric values.

Processing status: extracted from LaTeX source; suitable for prompt spectral-parameter comparisons and later energetics calculations once cosmology and integration conventions are fixed.
