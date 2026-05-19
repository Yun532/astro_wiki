# GRB 221009A Reproduction Workspace

This workspace connects event-specific data to the GRB afterglow theory and model code.

Current status: data-first scaffold. LT, UVOT, LAT, and Konus-Wind source-table CSV files have been extracted from paper tables. Articles without public table data are summarized and linked rather than digitized by default.

Wiki entry points:

- `wiki/20_天体源/grb/grb-221009a/数据文件索引.md`
- `wiki/20_天体源/grb/grb-221009a/模型比较.md`
- `wiki/20_天体源/grb/grb-221009a/复现入口.md`

First reproduction targets:

1. Broken power-law toy fit for TeV / early high-energy light curves when a table or user-provided data file is available.
2. Standard forward-shock closure-relation checks.
3. Radio extra-component diagnosis using Laskar et al. data.
4. Structured-jet parameter comparison scaffold.
