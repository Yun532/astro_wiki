---
title: 来源质量
type: metadata
status: growing
last_updated: 2026-05-10
tags: [source-quality, arXiv, journal, LHAASO, Fermi-GBM, Konus-Wind, SRG-ART-XC, INTEGRAL, multiwavelength, radio, structured-jet, two-component-jet, IACT]
source_count: 12
confidence: medium
related:
  - literature-index.md
  - ../20_天体源/grb/grb-221009a/观测总结.md
---

# 来源质量

## 已评估 source

### de Naurois / IACT analysis methods / arXiv:astro-ph/0607247

- source 类型：IACT method review / proceedings source with arXiv PDF and TeX source package。
- 适合支持：Hillas-parameter based analysis、scaled cuts、stereoscopic reconstruction、Model analysis、3D Model analysis、off-axis efficiency、night-sky-background sensitivity 和方法比较。
- 可作为高权重证据的 claim：Hillas analysis is robust and efficient；Model and 3D Model analyses can improve gamma-ray efficiency by about 20% in the presented comparison but may retain more background；Model analysis uses pixel-level likelihood without requiring image cleaning；3D Model analysis generalizes Hillas parameters to a 3D Gaussian photosphere; different methods use different shower information and can be combined.
- 使用 caveat：这是 proceedings-level method comparison，具体性能依赖 instrument、event selection 和 simulation setup；数值 efficiency / sensitivity 不应推广为所有 IACT 阵列的通用性能。

### Hillas / Cerenkov light images / NASA NTRS 19850026666

- source 类型：foundational IACT image-morphology conference paper, available as NASA NTRS scanned PDF。
- 适合支持：Hillas-style image parameters、Cherenkov image width / length / orientation、early single-telescope gamma/hadron separation logic、Whipple 10 m telescope focal-plane camera context。
- 可作为高权重证据的 claim：TeV gamma-ray point-source showers can be distinguished from hadronic background using image morphology；LENGTH and WIDTH describe angular spread along/across image major axis；MISS, DISTANCE, AZWIDTH and FRAC(2) encode source alignment, centroid offset and image concentration；multi-parameter cuts can reject a substantial fraction of proton background while retaining many gamma-ray showers。
- 使用 caveat：PDF 是扫描件且无可用 text layer；本次从渲染页面图像人工读取。精确 cut 数值不应在未复核清晰文本前使用；现代 IACT 性能、stereo reconstruction 和 instrument response 需要后续 source 支持。

### Salafia & Ghirlanda / GRB jet structure review / arXiv:2206.11088

- source 类型：pedagogical review source with arXiv version and TeX source package。
- 适合支持：GRB jet structure 的术语谱系、top-hat / structured / two-component / quasi-universal jet 比较、angular energy profile dE/dΩ(θ,t)、Γ(θ,t)、prompt / afterglow viewing-angle effects、luminosity function imprint，以及 GW170817 / GRB170817A 作为 off-axis structured jet test bed 的 review-level 背景。
- 可作为高权重证据的 claim：jet structure and orientation strongly affect observed GRB appearance；common angular description uses dE/dΩ(θ,t) and average Γ(θ,t) when radial structure is not central；simulations broadly find a narrow core plus wider wings / cocoon-dominated material；off-core afterglow can transition from line-of-sight dominated emission to core-dominated decay；VLBI centroid motion can help break light-curve degeneracies.
- 使用 caveat：review-level source 不替代原始模型论文和事件论文；不同 source 的 angular profile 定义、prompt emission assumptions 和 microphysical assumptions 可能不一致；GW170817 / GRB170817A 结论是 review synthesis，需要在事件级页面引用原始 event papers 时再细化。

### Racusin et al. / GRB 080319B naked-eye burst / arXiv:0805.1557

- source 类型：event-specific broadband GRB observation and modeling paper with arXiv version and Nature DOI。
- 适合支持：GRB 080319B 的 naked-eye optical brightness、prompt optical/gamma-ray mismatch、broadband afterglow、narrow-core / wide-jet 事件解释，以及 two-component / structured outflow 案例比较。
- 可作为高权重证据的 claim：GRB 080319B prompt optical emission reached about visual magnitude 5.3；redshift z ≈ 0.937；prompt optical flux is far above a simple low-energy extrapolation of the gamma-ray spectrum；the source interprets afterglow behavior with a very narrow core plus wider component；model opening angles are about 0.2° for the narrow core and about 4° for the wider component。
- 使用 caveat：two-component geometry、opening angles、Lorentz factors、density and wind-like environment are model-dependent interpretations；optical/gamma mismatch rules out a simple one-component extrapolation but does not uniquely determine the emission mechanism；arXiv e-print source package was not available in this session, so figure filenames/captions need later provenance checks before embedding.

### Berger et al. / GRB 030329 calorimetry / arXiv:astro-ph/0308187

- source 类型：event-specific GRB afterglow / radio calorimetry paper with arXiv version and Nature DOI。
- 适合支持：GRB 030329 的 radio calorimetry、radio jet break、early optical/X-ray break、late optical resurgence、SN 2003dh subtraction caveat 和 two-component explosion 事件级解释。
- 可作为高权重证据的 claim：GRB 030329 redshift z = 0.1685；radio observations began about 13.8 h after burst；radio modeling requires t_j,rad ≈ 9.8 d and θ_j,rad ≈ 0.3 rad ≈ 17°；radio component beaming-corrected kinetic energy E_K ≈ 2.5×10^50 erg；early optical/X-ray break occurs at t ≈ 0.55 d；narrow component opening angle ≈ 0.09 rad ≈ 5° in the source model；narrow component beaming-corrected E_gamma ≈ 5×10^49 erg。
- 使用 caveat：two-component assignment、opening angles and energy partition are Berger et al. model interpretation；source notes residual fit discrepancies and need for accurate SN 2003dh subtraction；some optical data in figure caption were preliminary GCN-derived data。

### Peng, Königl & Granot / two-component jet / arXiv:astro-ph/0410384

- source 类型：theoretical GRB afterglow model paper with arXiv version and ApJ DOI。
- 适合支持：two-component jet 的模型定义、narrow / wide component 参数范围、R-band afterglow light curve prediction、t_dec,w 与 t_jet,n 的关系、jet-break masking 和 X-ray flash / GRB brightening 的模型解释。
- 可作为高权重证据的 claim：narrow component 可具有 η_n ≳ 10^2 并产生 prompt gamma-ray emission；wide component 可具有 η_w ~ 10、θ_j,w ≲ 3 θ_j,n；当 E_w/E_n >1 且 E_iso,w/E_iso,n <1 时，wide component 可在 t_dec,w 后接管 afterglow；t_dec,w 典型为 ~0.1-1 d。
- 使用 caveat：这是模型 source；GRB 021004、GRB 030329 和 XRF 解释是作者的模型应用，不是本 source 独立提供的观测事实。

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
