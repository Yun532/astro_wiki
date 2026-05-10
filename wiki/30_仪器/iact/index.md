---
title: IACT
type: instrument
status: growing
last_updated: 2026-05-10
tags: [IACT, Cherenkov, gamma-ray, air-shower]
source_count: 1
confidence: medium
related:
  - 成像原理.md
  - 重建方法.md
---

# IACT

## 页面定位

IACT（Imaging Atmospheric Cherenkov Telescope）通过地面望远镜记录 extensive air shower 在大气中产生的 Cherenkov light image，并利用图像形态、方向和亮度等信息重建 primary gamma ray 的方向、能量并区分 hadronic background。

当前已 ingest 的 foundational source 是 Hillas 1985 conference paper，它建立了用 image length、width、orientation 等参数区分 gamma-ray shower 和 hadronic shower 的基础图像语言。

## 当前已整理内容

- [成像原理](成像原理.md)：Cherenkov light image morphology、Hillas-style image parameters、gamma/hadron separation 的早期判据。
- [重建方法](重建方法.md)：从 image axis、source position、image concentration 到方向和背景抑制的基础接口。

## 使用 caveat

- Hillas 1985 是 foundational method source，适合支持 image-parameter language 和早期判别逻辑。
- 现代 IACT 阵列分析还需要后续 source 支持，包括 stereoscopic reconstruction、likelihood / model analysis、machine-learning gamma/hadron separation、instrument response functions 和 CTA-scale simulations。

## 相关页面

- [成像原理](成像原理.md)
- [重建方法](重建方法.md)
- [知识库总览](../../00_总览/index.md)

## 来源

- A. M. Hillas, “Cerenkov Light Images of EAS Produced by Primary Gamma Rays and by Nuclei,” 19th International Cosmic Ray Conference, Vol. 3, OG-9.5-3 (1985), NASA NTRS 19850026666。
