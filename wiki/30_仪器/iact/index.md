---
title: IACT
type: instrument
status: growing
last_updated: 2026-05-10
tags: [IACT, Cherenkov, gamma-ray, air-shower]
source_count: 2
confidence: medium
related:
  - 成像原理.md
  - 重建方法.md
  - 分析流程.md
  - 相关文献.md
---

# IACT

## 页面定位

IACT（Imaging Atmospheric Cherenkov Telescope）通过地面望远镜记录 extensive air shower 在大气中产生的 Cherenkov light image，并利用图像形态、方向和亮度等信息重建 primary gamma ray 的方向、能量并区分 hadronic background。

当前已 ingest 的 foundational source 是 Hillas 1985 conference paper，它建立了用 image length、width、orientation 等参数区分 gamma-ray shower 和 hadronic shower 的基础图像语言。de Naurois 2006 进一步比较了 Hillas-parameter based analysis、Model analysis 和 3D Model analysis，提供了现代 IACT 分析流程的过渡框架。

## 当前已整理内容

- [成像原理](成像原理.md)：Cherenkov light image morphology、Hillas-style image parameters、gamma/hadron separation 的早期判据。
- [重建方法](重建方法.md)：从 Hillas geometry 到 stereoscopic reconstruction、Model analysis 和 3D Model analysis 的基础接口。
- [分析流程](分析流程.md)：image parametrization、scaled cuts、likelihood goodness、off-axis / NSB caveats 等流程节点。
- [相关文献](相关文献.md)：IACT 方法 source 队列和已 ingest 文献。

## 使用 caveat

- Hillas 1985 是 foundational method source，适合支持 image-parameter language 和早期判别逻辑。
- de Naurois 2006 是 method review / proceedings source，适合支持 Hillas scaled cuts、Model analysis、3D Model analysis 的比较框架。
- 现代 IACT 阵列分析还需要后续 source 支持，包括 machine-learning gamma/hadron separation、instrument response functions 和 CTA-scale simulations。

## 相关页面

- [成像原理](成像原理.md)
- [重建方法](重建方法.md)
- [分析流程](分析流程.md)
- [相关文献](相关文献.md)
- [知识库总览](../../00_总览/index.md)

## 来源

- A. M. Hillas, “Cerenkov Light Images of EAS Produced by Primary Gamma Rays and by Nuclei,” 19th International Cosmic Ray Conference, Vol. 3, OG-9.5-3 (1985), NASA NTRS 19850026666。
- M. de Naurois, “Analysis methods for Atmospheric Cerenkov Telescopes,” arXiv:astro-ph/0607247。
