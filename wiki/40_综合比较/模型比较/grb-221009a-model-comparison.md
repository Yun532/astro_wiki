---
title: GRB 221009A model comparison
type: comparison
status: growing
last_updated: 2026-05-10
tags: [GRB 221009A, model-comparison, structured-jet, LHAASO, forward-shock, radio, shallow-jet]
source_count: 3
confidence: medium
related:
  - ../../20_天体源/grb/grb-221009a/模型解释.md
  - ../../20_天体源/grb/grb-221009a/余辉.md
  - ../../20_天体源/grb/grb-221009a/多波段数据.md
---

# GRB 221009A model comparison

## 当前已 ingest 模型解释

### LHAASO narrow jet / structured jet core

LHAASO Collaboration 使用 GRB 221009A 的 TeV afterglow 行为提出 narrow relativistic jet 解释，给出半张角约 0.8°。论文认为该 narrow jet 可与 structured jet core 一致，并可能解释该 GRB unusually high isotropic energy。

### O'Connor et al. shallow structured jet

O'Connor et al. 使用前三个月 multiwavelength afterglow evolution，提出 GRB 221009A 的 afterglow implies a shallow structured jet。该 source 的关键观测约束是 X-ray brightness 以约 t^-1.66 的 power-law slope 衰减；作者认为该行为不符合 standard predictions for jetted emission，并将其解释为 relativistic jet 的 shallow energy profile。

### Laskar et al. forward shock / extra radio component

Laskar et al. 使用 radio-to-GeV afterglow 数据讨论 forward-shock model。该 source 认为 multiwavelength 数据可由 highly collimated relativistic jet 与 low-density wind-like medium 相互作用产生的 forward shock 部分解释，对应 beaming-corrected kinetic energy EK ~ 4×10^50 erg。

同一 source 强调 radio/mm 数据需要额外 emission component。equipartition arguments 给出该 component 的推断参数：质量 ≤6×10^-7 M_sun、Γ ≥ 9、kinetic energy ≥10^49 erg；但其 temporal evolution 不符合 reverse shock、two-component jet、single-power-law synchrotron prescriptions 或 thermal electron population 的简单解释。

## 与观测事实的边界

| 类型 | 内容 | 状态 |
| --- | --- | --- |
| 观测事实 | >64,000 个 >0.2 TeV 光子，最初 3000 s；TeV flux trigger 后数分钟开始，约 10 s 达峰，约峰后 650 s 衰减变快。 | LHAASO source-backed |
| 观测事实 | 前三个月 multiwavelength afterglow evolution；X-ray brightness 以约 t^-1.66 衰减。 | O'Connor et al. source-backed |
| 观测事实 | radio-to-GeV afterglow observations 横跨约 15 个数量级 photon energy，观测延伸到约 100 d。 | Laskar et al. source-backed |
| 模型解释 | 半张角约 0.8° 的 narrow relativistic jet。 | LHAASO Collaboration interpretation |
| 模型解释 | 与 structured jet core 一致，并可能解释 unusually high isotropic energy。 | LHAASO Collaboration interpretation |
| 模型解释 | shallow structured jet 和 shallow energy profile。 | O'Connor et al. interpretation |
| 模型解释 | highly collimated jet + low-density wind-like medium 的 forward shock；EK ~ 4×10^50 erg。 | Laskar et al. interpretation |
| 模型解释 | 额外 radio component 的 equipartition mass、Lorentz factor 和 kinetic energy。 | Laskar et al. interpretation |

## 当前比较问题

- LHAASO narrow jet / structured jet core、O'Connor et al. shallow structured jet 与 Laskar et al. forward-shock / wind-like medium 是否可被同一 angular energy profile 同时解释？
- O'Connor et al. 的 long-lived X-ray t^-1.66 decay 与 Laskar et al. radio/mm 额外 component 是否指向同一 structured outflow，还是不同 emission component？
- Laskar et al. 排除的 simple reverse shock / two-component jet / thermal electron population 是否与后续 structured jet source 的参数空间存在重叠？
- TeV light curve break、X-ray/optical/radio break 和 radio/mm SED evolution 是否指向同一几何 break，还是不同 emission component？

## 相关页面

- [GRB 221009A 模型解释](../../20_天体源/grb/grb-221009a/模型解释.md)
- [GRB 221009A 余辉](../../20_天体源/grb/grb-221009a/余辉.md)
- [GRB 221009A 多波段数据](../../20_天体源/grb/grb-221009a/多波段数据.md)

## 来源

- B. O'Connor et al., “A structured jet explains the extreme GRB 221009A,” Science Advances 9, eadi1405 (2023), arXiv:2302.07906, DOI: 10.1126/sciadv.adi1405。
- T. Laskar et al., “The Radio to GeV Afterglow of GRB 221009A,” ApJL, arXiv:2302.04388, DOI: 10.3847/2041-8213/acbfad。
- LHAASO Collaboration, “A tera-electronvolt afterglow from a narrow jet in an extremely bright gamma-ray burst 221009A,” Science 380, 1390-1396 (2023), arXiv:2306.06372, DOI: 10.1126/science.adg9328。
