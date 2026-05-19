# GRB 221009A Phase 3 multiband inventory check

Validation target: connect the extracted LT, UVOT, LAT, and Konus-Wind source-table CSV files into one reproducible data inventory and first-pass preview plot.

## Inputs

| dataset | file | rows | source table |
| --- | --- | ---: | --- |
| Liverpool Telescope photometry | `reproduce/grb/events/grb_221009a/data/laskar_lt_photometry.csv` | 70 | Laskar et al. `tab:data:lt` |
| Swift/UVOT photometry | `reproduce/grb/events/grb_221009a/data/laskar_uvot_photometry.csv` | 18 | Laskar et al. `tab:data:uvot` |
| Fermi/LAT flux | `reproduce/grb/events/grb_221009a/data/laskar_lat_flux.csv` | 8 | Laskar et al. `tab:data:LAT` |
| Konus-Wind Band spectral fits | `reproduce/grb/events/grb_221009a/data/konus_band_spectral_fits.csv` | 11 | Frederiks et al. `TableSpec` |

## Outputs

| output | rows / status | role |
| --- | --- | --- |
| `reproduce/grb/events/grb_221009a/outputs/grb221009a_data_inventory.csv` | 4 rows | Per-dataset inventory with time range, observable, unit, series values, upper-limit count, and provenance. |
| `reproduce/grb/events/grb_221009a/outputs/grb221009a_multiband_preview.csv` | 107 rows | Lightweight long table for plotting and first-pass data inspection. |
| `reproduce/grb/events/grb_221009a/outputs/grb221009a_multiband_preview.png` | generated | Data QA plot with separate photometry, LAT energy-flux, and Konus-Wind Epeak panels. |

## Checks Run

- Re-ran all source extraction scripts; row counts were LT 70, UVOT 18, LAT 8, Konus 11.
- Ran `scripts/build_multiband_inventory.py`; inventory and preview CSV files were regenerated.
- Verified the inventory has one row for each input dataset and non-empty provenance fields.
- Verified the preview table has 107 rows, three panels, and one explicit upper-limit row.
- Ran `scripts/plot_multiband_preview.py`; PNG output exists and is non-empty.
- Ran a light import check for `reproduce.grb.core.fitting.lightcurve.power_law_flux`.

## Caveats

- The preview figure is not a physical multi-band fit.
- LT and UVOT magnitudes are not corrected for Milky Way extinction, host extinction, host light, or photometric-system conversion.
- LAT energy flux remains in the source 100 MeV-100 GeV band; the final low-TS bin is preserved as an upper limit.
- Konus-Wind prompt `Epeak` is kept in observer-frame source-table units; no rest-frame, bolometric, or energetics conversion is applied.

Manual check: pending user review of the preview plot and whether the panel choices are useful before moving to forward-shock theory/code reproduction.
