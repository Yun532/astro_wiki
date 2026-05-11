---
title: IACT 重建方法比较
type: instrument-comparison
status: growing
last_updated: 2026-05-11
tags: [IACT, reconstruction, Hillas-parameters, model-analysis, likelihood, gamma-hadron-separation]
source_count: 3
confidence: medium
related:
  - index.md
  - 成像原理.md
  - 重建方法.md
  - 分析流程.md
  - 相关文献.md
---

# IACT 重建方法比较

## 比较范围

本页比较已 ingest source 中出现的 IACT event reconstruction / gamma-hadron separation 方法。当前证据链覆盖 Hillas 1985 的 image-parameter 判别、de Naurois 2006 的 Hillas / Model / 3D Model review，以及 de Naurois & Rolland 2009 的 H.E.S.S. pixel-likelihood Model Analysis。

## 方法对照

| 方法 | 使用的 shower 信息 | 主要输出 | gamma/hadron separation | 已 ingest 支持 | caveat |
| --- | --- | --- | --- | --- | --- |
| Hillas-style moments | camera image 的二阶矩、orientation、concentration。 | source direction consistency、shape cuts、早期 event selection。 | WIDTH、LENGTH、MISS、DISTANCE、FRAC(2) 等多参数 cut。 | Hillas 1985。 | 早期单望远镜 context；cut 数值和现代 sensitivity 不可混用。 |
| Hillas scaled cuts / stereo | width / length 与 Monte Carlo expectation 的差异，结合 telescope impact 和 image charge。 | stereo direction、impact、energy weighted average。 | Scaled Width、Scaled Length、Mean Scaled Width / Length。 | de Naurois 2006。 | 数值性能依赖 instrument、cuts 和 simulation；仍可能受 truncated image、missing pixels 和 NSB 影响。 |
| Model Analysis / pixel likelihood | semi-analytical shower image model 与所有 camera pixels 的 likelihood comparison。 | direction、impact、first interaction depth、energy、parameter uncertainties、log-likelihood。 | goodness-of-fit `G`、ShowerGoodness、BackgroundGoodness、primary interaction depth。 | de Naurois 2006；de Naurois & Rolland 2009。 | H.E.S.S. 2009 性能数值不应直接推广到所有 IACT；模型、calibration 和计算复杂度更高。 |
| 3D Model Analysis | 把 shower 近似为大气中的 Gaussian photosphere，并通过 line-of-sight integral 预测 pixel light。 | mean altitude、impact、direction、3D width / length、luminosity。 | 3D width / rescaled width；fit 过程本身利用 rotational symmetry。 | de Naurois 2006。 | 目前仅有 proceedings-level comparison；需要后续 H.E.S.S. / CTA source 支撑现代实现细节。 |

## Model Analysis 的 2009 细化

de Naurois & Rolland 2009 将 Model Analysis 的核心 likelihood 写成 pixel-level probability：

```tex
P(s|\mu,\sigma_p,\sigma_\gamma) = \sum_n \frac{\mu^n e^{-\mu}}{n!\sqrt{2\pi(\sigma_p^2+n\sigma_\gamma^2)}} \exp\left[-\frac{(s-n)^2}{2(\sigma_p^2+n\sigma_\gamma^2)}\right].
```

这里 `s` 是 observed pixel signal，`μ` 是 shower model expectation，`σ_p` 是包含 electronics noise 和 NSB contribution 的 pedestal width，`σ_γ` 是 single-photoelectron resolution。这个形式让每个 pixel 的 noise / calibration 状态进入 likelihood，而不是先做 image cleaning 后再只用 moments。

Goodness-of-fit 定义为：

```tex
G = \frac{\sum_i[\ln L(s_i|\mu_i)-\langle\ln L\rangle|_{\mu_i}]}{\sqrt{2\,\mathrm{NdF}}}.
```

该量衡量 event 与 gamma-ray shower model 的相容性。实际 background rejection 还使用 ShowerGoodness、BackgroundGoodness 和 first interaction depth；因此 “likelihood reconstruction” 同时是参数重建方法和事件选择框架。

## 性能数值的使用边界

- de Naurois & Rolland 2009 报告 Model Analysis 在 H.E.S.S. data 中相对 Hillas standard reconstruction 有接近 factor 2 的 sensitivity improvement，并有更好的 low-energy gamma efficiency、background rejection、angular resolution 和 energy resolution。
- 该 source 报告 energy resolution 在约 80 GeV 到 >20 TeV 范围内优于 15%，在 500 GeV 到 >10 TeV 的核心能段优于 10%，最低约 7–8%。
- Angular resolution 使用 68% containment radius，许多能段约 0.06 deg。
- 这些数值应写作 H.E.S.S. Model Analysis 的 source-specific performance，不应作为 IACT class-wide 或 CTA 设计指标。

## 稳健性与系统效应

- Night-sky background：de Naurois & Rolland 2009 把 NSB 稳定性归因于逐 pixel 使用 measured `σ_p` 和 `σ_γ`；其 simulated gamma-ray ShowerGoodness distribution 在约 300 MHz 内无强演化。
- Missing pixels / bright stars：Model Analysis 可忽略 missing pixels；Crab field 中 bright star `ζ`-Tauri 的例子显示 Hillas significance map 可能出现 artificial excess，而 Model Analysis 在同位置未见对应偏差。
- Off-axis：2009 source 中 off-axis section 大段为注释内容；本页暂不把其中表格数值作为正式 claim。
- Method combination：de Naurois 2006 强调不同方法使用的信息不同，可组合；de Naurois & Rolland 2009 则指出改进后的 ShowerGoodness cut 已吸收大部分 Mean Scaled Width / Length 的额外判别能力。

## 后续待补

- VERITAS gamma/hadron separation source 用于补充 boosted decision trees / Random Forest / parameter cuts 等更现代背景抑制方法。
- CTA Monte Carlo design source 用于区分 reconstruction method、array layout、trigger / telescope class 和 instrument response 的贡献。

## 相关页面

- [IACT](index.md)
- [IACT 成像原理](成像原理.md)
- [IACT 重建方法](重建方法.md)
- [IACT 分析流程](分析流程.md)
- [IACT 相关文献](相关文献.md)

## 来源

- A. M. Hillas, “Cerenkov Light Images of EAS Produced by Primary Gamma Rays and by Nuclei,” 19th International Cosmic Ray Conference, Vol. 3, OG-9.5-3 (1985), NASA NTRS 19850026666。
- M. de Naurois, “Analysis methods for Atmospheric Cerenkov Telescopes,” arXiv:astro-ph/0607247。
- M. de Naurois and L. Rolland, “A high performance likelihood reconstruction of gamma-rays for IACTs,” Astroparticle Physics 32, 231-252 (2009), arXiv:0907.2610, DOI: 10.1016/j.astropartphys.2009.09.001。
