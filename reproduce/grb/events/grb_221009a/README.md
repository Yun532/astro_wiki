# GRB 221009A Reproduction Workspace

This workspace connects event-specific data to the GRB afterglow theory and model code.

Current status: Phase 3 data-first scaffold. LT, UVOT, LAT, and Konus-Wind source-table CSV files have been extracted, inventoried, and connected to a first-pass multiband preview plot.

Wiki entry points:

- `wiki/20_天体源/grb/grb-221009a/数据文件索引.md`
- `wiki/20_天体源/grb/grb-221009a/模型比较.md`
- `wiki/20_天体源/grb/grb-221009a/复现入口.md`

First reproduction targets:

1. Data inventory and preview: `scripts/build_multiband_inventory.py` and `scripts/plot_multiband_preview.py`.
2. Broken power-law toy fit for TeV / early high-energy light curves.
3. Standard forward-shock closure-relation checks.
4. Radio extra-component diagnosis using Laskar et al. data.
5. Structured-jet parameter comparison scaffold.

Current outputs:

- `outputs/grb221009a_data_inventory.csv`
- `outputs/grb221009a_multiband_preview.csv`
- `outputs/grb221009a_multiband_preview.png`
