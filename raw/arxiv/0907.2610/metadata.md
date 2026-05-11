---
title: A high performance likelihood reconstruction of gamma-rays for IACTs
source_type: arxiv-paper
status: collected
last_updated: 2026-05-11
arxiv: "0907.2610"
doi: "10.1016/j.astropartphys.2009.09.001"
arxiv_doi: "10.48550/arXiv.0907.2610"
local_pdf: raw/arxiv/0907.2610/0907.2610.pdf
local_source_package: raw/arxiv/0907.2610/0907.2610-source.tar.gz
---

# A high performance likelihood reconstruction of gamma-rays for IACTs

- 作者：Mathieu de Naurois, Loïc Rolland。
- arXiv：0907.2610。
- DOI：10.1016/j.astropartphys.2009.09.001。
- 本地 PDF：`raw/arxiv/0907.2610/0907.2610.pdf`。
- 本地 source package：`raw/arxiv/0907.2610/0907.2610-source.tar.gz`。
- TeX 主文件：`model.tex`。

## Source package contents

Source package 包含 `model.tex`、`elsart.cls`、`elsart-num.bst` 和多张 EPS figure，包括 `Likelihood2D.eps`、`LikelihoodAverage.eps`、`Goodness` / `ShowerGoodness` 相关图、`EffectiveArea.eps`、`EnergyResolution.eps`、`AngularResolution.eps`、`Theta2_Model_Crab.eps`、`Theta2_Hillas_Std_Crab.eps`、`Crab_Template_Model.eps` 等。

## Key claims extracted

- 该 paper 提出一种用于 Imaging Atmospheric Cherenkov Telescopes 的 gamma-ray likelihood reconstruction technique，将 raw Cherenkov camera pixel images 与 semi-analytical shower model 逐 pixel 比较。
- 方法在 CAT experiment 的 model-image 思路基础上扩展，加入 log-likelihood minimisation using all pixels、night-sky-background noise treatment、stereoscopy 和 first interaction depth 作为模型参数。
- Fit 输出 6 个 shower 参数：direction 2 个参数、impact 2 个参数、first interaction depth 和 energy，并给出 correlation matrix / parameter uncertainties 和 final log-likelihood。
- Pixel likelihood 将 photoelectron number 的 Poisson 分布与 PMT resolution 的 Gaussian 卷积；pedestal width `sigma_p` 每个 pixel 不同，并随 NSB 变化。
- Goodness-of-fit `G` 用实际 pixel log-likelihood 与其 expectation value 的差，对所有 pixels 求和后按 `sqrt(2 NdF)` 归一化，用于检验事件与 gamma-ray hypothesis 的相容性。
- Gamma / hadron separation 主要使用 ShowerGoodness 和 reconstructed primary interaction depth，并辅以 BackgroundGoodness、pure-NSB consistency 和 point-source `theta^2` cut。
- H.E.S.S. data 中，Model Analysis 相对 Hillas-parameter based standard reconstruction 给出更好的 direction / energy reconstruction、低能 gamma efficiency 和 background rejection；作者报告 sensitivity 接近提升 factor 2。
- Energy resolution 在约 80 GeV 到 >20 TeV 范围内优于 15%，在 500 GeV 到 >10 TeV 的核心能段优于 10%，最低约 7–8%。
- Angular resolution 以 68% containment radius 定义，在多数能段约 0.06 deg，并优于类似 image-amplitude 条件下的 Hillas reconstruction。
- NSB 方面，ShowerGoodness distribution 对 simulated gamma rays 在约 300 MHz 以内无强演化；paper 强调使用 measured `sigma_p` 和 `sigma_gamma` 是 Model Analysis 对 NSB 稳定的重要原因。
- Missing pixels / bright stars 方面，Model Analysis 直接忽略 missing pixels，因此比 Hillas-moment analysis 更不易被 truncated images 影响；Crab / zeta-Tauri 例子中 Hillas significance map 出现 artificial excess，而 Model Analysis 未见同位置偏差。

## Formula candidates

### Pixel likelihood

```tex
P(s|\mu,\sigma_p,\sigma_\gamma) = 
\sum_n \frac{\mu^n e^{-\mu}}{n!\sqrt{2\pi (\sigma_p^2 + n \sigma_\gamma^2)}} \exp\left(  - \frac{(s - n)^2}{2 (\sigma_p^2 + n \sigma_\gamma^2)} \right)
```

Variables:

- `s`: observed pixel signal in photoelectron units。
- `mu`: expected signal from shower image model。
- `n`: photoelectron number。
- `sigma_p`: pedestal width, including electronic noise and NSB contribution。
- `sigma_gamma`: single-photoelectron peak width / PMT resolution。

### Goodness-of-fit

```tex
G = \frac{\sum_{\mathrm{pixel}\ i} [ \ln L(s_i|\mu_i) - \langle\ln L\rangle|_{\mu_i} ]}{\sqrt{2 \times \mathrm{NdF}}}
```

Expected asymptotic behavior:

```tex
\langle G\rangle = 0, \qquad \sigma^2(G)=1
```

Variables:

- `NdF`: number of degrees of freedom, defined in the source as number of pixels minus 6。
- `L(s_i|mu_i)`: pixel likelihood for observed signal and model expectation。

## Figure / data candidates

- `Likelihood2D.eps`, `LikelihoodAverage.eps`：pixel likelihood / expectation value。
- `Goodness` / `ShowerGoodness` figures：fit-quality and gamma/hadron discrimination variables。
- `EffectiveArea.eps`：effective area compared with Hillas analyses。
- `EnergyResolution.eps`：energy resolution and bias。
- `AngularResolution.eps`, `AngularResolution_Zenith.eps`：angular resolution vs energy / zenith angle。
- `Theta2_Hillas_Std_Crab.eps`, `Theta2_Model_Crab.eps`：Hillas vs Model theta-square comparison。
- `Crab_Template_Hillas_Std.eps`, `Crab_Template_Model.eps`：bright-star / missing-pixel artifact comparison。

## Caveats

- 性能数值来自 H.E.S.S. analysis context、specific cuts、simulation 和 source data set；不应直接推广为所有 IACT 或 CTA 的通用性能。
- Model Analysis 更高性能伴随更复杂的 semi-analytical model、calibration 和 likelihood fit；与 Hillas / scaled cuts 比较时需区分 reconstruction method、event selection、instrument 和 energy range。
- Paper 中 off-axis observation subsection 大段被注释，相关 off-axis 数值不作为正式 ingest claim 使用。
- Source 使用 “Cerenkov” 拼写；wiki 正文保留现代仪器术语 “Cherenkov”，引用原题时保留原拼写。
