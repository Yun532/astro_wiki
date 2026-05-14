---
title: Optical Intensity Interferometry with the Cherenkov Telescope Array
source_type: arxiv-paper
status: collected
last_updated: 2026-05-14
arxiv: "1204.3624"
doi: "10.1016/j.astropartphys.2012.04.017"
arxiv_doi: "10.48550/arXiv.1204.3624"
local_pdf: raw/arxiv/1204.3624/1204.3624.pdf
local_source_package: raw/arxiv/1204.3624/1204.3624-source.tar.gz
---

# Optical Intensity Interferometry with the Cherenkov Telescope Array

- Source：D. Dravins, S. LeBohec, H. Jensen and P. D. Nuñez for the CTA Consortium, “Optical Intensity Interferometry with the Cherenkov Telescope Array,” arXiv:1204.3624, DOI: 10.1016/j.astropartphys.2012.04.017。
- arXiv comment：Astroparticle Physics, in press; 47 pages, 10 figures, 124 references。
- 本地保存：PDF 和 arXiv source package。
- source package 主文件：`Dravins_Astropart_ms_120405.tex`；图像文件为 EPS。

## 适合支持的 claim

- CTA 的大 collecting area 和多 telescope array 可作为 optical stellar intensity interferometer 使用，用二阶相干测量实现 sub-milliarcsecond imaging。
- Intensity interferometry 测量不同望远镜记录的光强涨落 cross correlation，而不是直接测相位；它对 atmospheric turbulence 和 telescope optical imperfections 实际上不敏感。
- 对 chaotic / thermal light，线偏振情形下有 `⟨I1 I2⟩ = ⟨I1⟩⟨I2⟩(1 + |γ12|²)`，因此 `⟨ΔI1 ΔI2⟩ = ⟨I1⟩⟨I2⟩ |γ12|²`。
- CTA 设想中的 50–100 台、约 5–25 m aperture、分布在约 2–3 km² 面积上的望远镜，可合成大量 optical baseline pairs。
- 若 2 km baseline 在 λ = 350 nm 使用，angular resolution 可接近 30 μas。
- 对 N 台望远镜，baseline pair 数为 `N(N-1)/2`；多望远镜和 Earth rotation 可填充 `(u,v)` plane，有利于 aperture synthesis 和 image reconstruction。
- 论文比较 CTA candidate layouts B、D、I：B 为 42 telescopes / 253 unique baselines / 32–759 m baseline；D 为 57 telescopes / 487 baselines / 170–2180 m；I 为 77 telescopes / 1606 baselines / 90–2200 m。
- 强度干涉 pair 的 RMS signal-to-noise 可写作 `(S/N)_RMS = A α n |γ12(r)|² Δf^{1/2} (T/2)^{1/2}`。
- 该 source 给出 two-dimensional imaging 的 conservative practical limit around `m_V = 6`；若只测一维量如 stellar diameter 或 limb darkening，可更暗一些。
- VERITAS 12 m telescopes 的测试性观测已用数字相关器连接 telescope pairs，处理过最高约 30 MHz continuous count rates；这些实验不是 astrophysical measurement，而是验证 full-scale observatory 操作可行性。

## 公式 / 数值候选

```tex
\langle I(t) \rangle = \langle E(t)E^*(t) \rangle
```

```tex
\langle I_1(t) I_2(t) \rangle = \langle I_1 \rangle \langle I_2 \rangle (1 + |\gamma_{12}|^2)
```

```tex
\langle \Delta I_1(t) \Delta I_2(t) \rangle = \langle I_1 \rangle \langle I_2 \rangle |\gamma_{12}|^2
```

```tex
\Gamma(u,v) = \iint I(l,m) e^{-2\pi i(ul+vm)} dl dm
```

```tex
I_\nu(l,m) = \iint V(u,v) e^{2\pi i(ul+vm)} du dv
```

```tex
(S/N)_{RMS} = A \alpha n |\gamma_{12}(\mathbf{r})|^2 \Delta f^{1/2} (T/2)^{1/2}
```

```tex
|\gamma|^2 = \frac{\langle \Delta I_1 \Delta I_2 \rangle}{\langle I_1 \rangle \langle I_2 \rangle}
```

```tex
g^{(2)} = \frac{N_{AB}}{N_A N_B} N
```

## 使用 caveat

- 这是 CTA prospective / design-stage source，不是已经建成的 CTA intensity interferometry instrument paper。
- 二阶相干只直接给出 Fourier amplitude squared，不直接给出 phase；二维成像需要 phase-recovery / image-reconstruction algorithms，且可能存在 mirror-image degeneracy。
- 适用对象主要是亮星；two-dimensional imaging 的 conservative limit 约 `m_V = 6`，不能推广到一般 faint optical targets。
- 望远镜 detector、central pixel、filter、timing、correlator、delay unit 和 data handling 都是实现约束；不应只写 angular resolution 潜力而忽略 signal-processing requirements。
- 文章中的 CTA layout B/D/I 和 telescope assumptions 来自当时 CTA design study，应与后续 CTA construction baseline 和现代 SII demonstrations 分开。
