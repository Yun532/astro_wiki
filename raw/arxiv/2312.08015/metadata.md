---
title: First Intensity Interferometry Measurements with the H.E.S.S. Telescopes
source_type: arxiv-paper
status: collected
last_updated: 2026-05-14
arxiv: "2312.08015"
doi: "10.1093/mnras/stad3676"
arxiv_doi: "10.48550/arXiv.2312.08015"
local_pdf: raw/arxiv/2312.08015/2312.08015.pdf
local_source_package: raw/arxiv/2312.08015/2312.08015-source.tar.gz
local_arxiv_api: raw/arxiv/2312.08015/2312.08015-api.xml
---

# First Intensity Interferometry Measurements with the H.E.S.S. Telescopes

## Source

Andreas Zmija, Naomi Vogel, Frederik Wohlleben, Gisela Anton, Adrian Zink and Stefan Funk, “First Intensity Interferometry Measurements with the H.E.S.S. Telescopes,” arXiv:2312.08015, DOI: 10.1093/mnras/stad3676。

## Local raw files

- PDF：`raw/arxiv/2312.08015/2312.08015.pdf`
- arXiv source package：`raw/arxiv/2312.08015/2312.08015-source.tar.gz`
- arXiv API XML：`raw/arxiv/2312.08015/2312.08015-api.xml`

Source package contains `main.tex`, bibliography files and figure files under `images/`, including setup, path-delay, night-sky-background, Shaula / Nunki spatial-correlation and Acrux systematic figures.

## Why this source matters

该论文报告 H.E.S.S. telescopes 的 first intensity interferometry measurements，把南天 H.E.S.S. IACT 阵列纳入 Cherenkov telescope optical SII comparison。它补充了 VERITAS、MAGIC 和 MAGIC-SII 之外的实现路线：在 H.E.S.S. Phase I telescope camera lid 上安装外部光学系统，用双 PMT 同时测量单望远镜 zero-baseline correlation 和两望远镜 cross-correlation。

## Key claims / facts

- 观测在 April 2022 的 H.E.S.S. moonlight break / bright-Moon period 进行；gamma observations 在 Moon brightness 达到 full Moon intensity 的 60% 后停止，因此该时段可用于 optical intensity interferometry。
- 使用 H.E.S.S. Namibia site 的两台 Phase I telescopes；site 位于 Khomas Highlands，altitude 1835 m。H.E.S.S. array 包括四台 12 m Phase I telescopes 和 2012 年加入的 central 28 m telescope。
- 外部 II setup 安装在 H.E.S.S. Phase I camera lid 上，是约 `(50 × 63) cm²` 的 aluminum structure；每台 telescope 的 setup 相同。
- optical path 为 2-inch tube system，包含 parallelising concave lens `F = -75 mm`、LC-HBP465/2-50 interference filter（465 nm CWL, 2 nm width）和 beam splitter / two-PMT readout。
- detector 为 Hamamatsu R11265U-300 PMT；peak sensitivity at 420 nm，peak QE 约 39%，在 465 nm 约 33%。
- setup 的 optical elements 可 motorized motion，用于 live pointing / tracking correction；scan photon rates 后找 optimal motor positions。
- data correlation 是 offline procedure：每台 telescope 一个 binary file，每个文件含两个 acquisition channels；四路 waveform channel 读盘后计算 all channel pairs。
- 2022 April correlation mechanism 下，一个 3.436 s measurement 需要约 13 s analysis，因此当时只能分析部分 accumulated data；later campaigns 可作为改进方向。
- Fourier transforms of PMT currents and resulting `g^(2)` functions show sharp noise peaks at several frequencies；analysis 使用 200 MHz low-pass filter 和 notch filtering 清理。
- 论文把单望远镜内两个通道的 zero-baseline correlation 称作 “auto-correlation”，但作者明确说明这不是通常意义上的 autocorrelation terminology。
- targets：`λ Sco` / Shaula、`σ Sgr` / Nunki；`α Cru` / Acrux 用于 systematics studies。
- Measurement segments total：Shaula 16 h 0 min、Nunki 10 h 14 min、Acrux 11 h 52 min。
- Nunki 在 single-star approximation 下得到 angular diameter `φ_Nunki = (0.52 ± 0.07) mas`；source later compares `(0.51 ± 0.05) mas` with literature `φ_Nunki = 0.68 mas` from photometric estimates。
- Shaula 是 triple star system；在简化 single-star / equal-diameter assumption 下给出 `φ_Shaula = (0.49 ± 0.06) mas`，但 source 明确要求谨慎使用。
- Acrux 是 multiple star system，主要用于检查 zero-baseline / systematics；large-baseline data show indications of complex source geometry。
- Future campaign changes include broadening interference filters to 10 nm instead of 2 nm, because narrow filters with angular incidence may broaden/shift the transmitted spectrum and reduce temporal coherence.

## Formulae / quantitative relations

Second-order coherence definition used in the source:

```tex
g^{(2)}(\mathbf{R}, \tau) = \frac{\langle I(\mathbf{R}, t) I(\mathbf{R} + \mathbf{b}, t + \tau) \rangle}{\langle I(\mathbf{R}, t) \rangle \langle I(\mathbf{R} + \mathbf{b}, t + \tau) \rangle}
```

Coherence time definition:

```tex
\tau_c := \int_{-\infty}^{+\infty} \left(g^{(2)}(\tau) - 1\right)\,d\tau
```

Expected observed coherence time at baseline `b`:

```tex
\tau_c(b) = 0.5\, k_\mathrm{s}(b) k_\mathrm{T} \frac{\lambda_0^2}{c\Delta\lambda}
```

Here `0.5` is from unpolarized light, `k_s(b)` is the spatial coherence factor, and `k_T` corrects for exact spectral transmission profile. The source reports numerical spectral-profile corrections `k_T,1 = 0.842` and `k_T,2 = 0.848` for perpendicular incident light.

Zero-baseline expected coherence-time example:

```tex
\tau_c(b=0) = 0.5 \times 0.842 \times \frac{(465\,\mathrm{nm})^2}{c\times 2\,\mathrm{nm}} = 152\,\mathrm{fs}
```

Uniform-disc spatial-coherence fit:

```tex
f(x) = a \left[ \frac{2J_1(\pi x\varphi/\lambda)}{\pi x\varphi/\lambda} \right]^2
```

with `x` the baseline, `λ = 465 nm`, `J_1` the Bessel function of first kind, `a` the zero-baseline coherence-time constant and `φ` the angular diameter.

## Caveats

- This is a demonstration / first-measurement source, not yet a mature H.E.S.S. production SII performance paper.
- H.E.S.S. April 2022 analysis was offline and correlation speed limited; it should not be equated with MAGIC-SII 2024 real-time GPU correlator performance.
- The source reports coherence loss: for Nunki, expected `a_exp = 152 fs` but fitted `a_Nunki = (43.76 ± 10.40) fs`, a loss factor about 3.5; the cause is not yet settled.
- Zero-baseline “auto-correlation” is source terminology and should be quoted with caveat.
- Shaula and Acrux are multiple-star systems; single-star angular-diameter fits are simplified diagnostics and should not be used as robust stellar-parameter measurements.
- Nunki single-star approximation is more justified, but source notes deviation from a literature photometric angular diameter.
- Filter bandwidth / incidence-angle effects may reduce temporal coherence; future 10 nm filters are an instrumental mitigation, not a result from the April 2022 campaign.

## Wiki integration targets

- `wiki/40_综合比较/仪器比较/cherenkov-telescope-interferometry.md`
- `wiki/30_仪器/iact/index.md`
- `wiki/30_仪器/iact/相关文献.md`
- `wiki/90_元信息/literature-index.md`
- `wiki/90_元信息/source-quality.md`
- `wiki/90_元信息/open-questions.md`
