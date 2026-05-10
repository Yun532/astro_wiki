---
title: 来源质量
type: metadata
status: growing
last_updated: 2026-05-10
tags: [source-quality, arXiv, journal, LHAASO, Fermi-GBM, Konus-Wind, SRG-ART-XC, INTEGRAL, multiwavelength, radio, structured-jet]
source_count: 6
confidence: medium
related:
  - literature-index.md
  - ../20_天体源/grb/grb-221009a/观测总结.md
---

# 来源质量

## 已评估 source

### Laskar et al. / radio-to-GeV afterglow / arXiv:2302.04388

- source 类型：multiwavelength afterglow paper with arXiv version and ApJL DOI。
- 适合支持：GRB 221009A radio-to-GeV afterglow 数据范围、radio/mm 观测约束、multiwavelength light curve / SED figure provenance、forward-shock model 边界和额外 radio component 问题。
- 可作为高权重证据的 claim：multiwavelength observations 覆盖 radio 到 gamma rays、横跨约 15 个数量级 photon energy；观测延伸到约 100 d；radio/mm 数据对 forward-shock model 提供强约束；单一 standard forward shock model 不能完整解释 radio/mm 数据，需要额外 emission component。
- 使用 caveat：forward shock、low-density wind-like medium、EK ~ 4×10^50 erg、equipartition mass ≤6×10^-7 M_sun、Γ ≥ 9、kinetic energy ≥10^49 erg 都是模型解释；ATCA 数据被作者提示 calibration 限制，不应未复核即作为强约束。

### O'Connor et al. / structured jet / arXiv:2302.07906

- source 类型：multiwavelength afterglow and modeling paper with arXiv version and Science Advances DOI。
- 适合支持：GRB 221009A 前三个月 multiwavelength afterglow evolution、long-lived X-ray decay、structured jet 模型解释和与其他 GRB 的 energetic / jet-structure 比较。
- 可作为高权重证据的 claim：GRB 221009A 在该 source 框架中是已观测到的最亮 burst；Eiso ≈ 10^55 erg、z ≈ 0.15；multiwavelength observations 覆盖 first three months of afterglow evolution；X-ray brightness 以约 t^-1.66 的 power-law slope 衰减。
- 使用 caveat：X-ray decay 是观测约束；shallow energy profile、shallow structured jet、common central engine 是作者解释，不应写成直接观测事实。

### Frederiks et al. / Konus-Wind + SRG-ART-XC / arXiv:2302.13383

- source 类型：instrument-team paper with arXiv version and ApJL DOI。
- 适合支持：Konus-Wind / SRG-ART-XC 对 GRB 221009A 的 prompt light curve、fluence、peak flux、Ep、extended decay 和 isotropic-equivalent energetics。
- 可作为高权重证据的 claim：Konus-Wind 超过 28 年观测中最亮 GRB；pulsed prompt phase 约 600 s；steady power-law decay 超过 25 ks；time-averaged Ep ≈ 2.6 MeV；最亮 peak 的 Ep ≈ 3.0 MeV；20 keV–10 MeV fluence ≈ 0.22 erg cm^-2；peak energy flux ≈ 0.031 erg cm^-2 s^-1；z = 0.151 下 Eiso ≈ 1.2×10^55 erg、64 ms Liso ≈ 3.4×10^54 erg s^-1。
- 使用 caveat：Eiso / Liso 是 isotropic-equivalent，依赖 redshift 和能段；normal-long-GRB、Amati / Yonetoku consistency 是作者解释；ART-XC 是 off-axis / through-structure detection，不可写成视场内直接成像观测。

### Lesage et al. / Fermi-GBM / arXiv:2303.14172

- source 类型：instrument-team paper with arXiv version and ApJL DOI。
- 适合支持：Fermi-GBM 对 GRB 221009A 的 trigger、prompt emission、GBM-band afterglow、能段和 energetics。
- 可作为高权重证据的 claim：trigger time 2022-10-09 13:16:59.99 UTC；trigger 前未探测到 emission；prompt emission 超过 600 s；afterglow 在 8 keV–40 MeV 可见；trigger pulse 到约 15 MeV；z = 0.151 下 Eγ,iso = 1.0×10^55 erg、Lγ,iso = 9.9×10^53 erg/s。
- 使用 caveat：shock-breakout、external shock onset 和 plateau 是作者解释或表征，需要归因。

### Rodi & Ubertini / INTEGRAL-IBIS-PICsIT / arXiv:2303.16943

- source 类型：instrument-analysis paper with arXiv version and A&A DOI。
- 适合支持：INTEGRAL/IBIS-PICsIT 对 GRB 221009A 的 200–2600 keV soft gamma-ray temporal / spectral evolution、prompt pulses、flux-tracking behavior、early afterglow dominance 和 figure provenance。
- 可作为高权重证据的 claim：PICsIT 使用 200–2600 keV spectral-timing data；prompt emission 超过 600 s；spectrum 在更亮时更 soft；spectral-index / flux relation 在 burst 中改变；afterglow emission 约 T0 + 630 s 开始占主导；decay slope 1.6 ± 0.2；作者报告 PICsIT 未受 pile-up effects 影响。
- 使用 caveat：bright prompt pulses 存在 telemetry gaps；flux-tracking 的物理解释需要归因，不应写成直接观测事实。

### LHAASO Collaboration / Science / arXiv:2306.06372

- source 类型：peer-reviewed journal article with arXiv version。
- 适合支持：LHAASO 对 GRB 221009A 的 TeV afterglow 观测事实，包括 photon count、能量阈值、时间行为和 light curve break。
- 可作为高权重证据的 claim：最初 3000 s 内超过 64,000 个 >0.2 TeV 光子；TeV flux trigger 后数分钟开始；开始后约 10 s 达峰；约峰后 650 s 衰减变快。
- 使用 caveat：narrow jet、structured jet core、unusually high isotropic energy 的解释应标为 LHAASO Collaboration 的模型解释，不应写成独立观测事实。
- 图像 caveat：正文图片需先从 arXiv source 包核对 figure 文件和 caption；PDF crop 必须记录 provenance。

## 相关页面

- [文献索引](literature-index.md)
- [GRB 221009A 观测总结](../20_天体源/grb/grb-221009a/观测总结.md)
