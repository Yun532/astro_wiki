---
title: Demonstration of stellar intensity interferometry with the four VERITAS telescopes
source_type: arxiv-paper
status: collected
last_updated: 2026-05-14
arxiv: "2007.10295"
doi: "10.1038/s41550-020-1143-y"
arxiv_doi: "10.48550/arXiv.2007.10295"
local_pdf: raw/arxiv/2007.10295/2007.10295.pdf
local_source_package: raw/arxiv/2007.10295/2007.10295-source.tar.gz
---

# Demonstration of stellar intensity interferometry with the four VERITAS telescopes

- Source：A. U. Abeysekara et al. / VERITAS Collaboration, “Demonstration of stellar intensity interferometry with the four VERITAS telescopes,” arXiv:2007.10295, DOI: 10.1038/s41550-020-1143-y。
- 本地保存：PDF 和 arXiv source package。
- source package 主文件：`main.tex`；图像文件包括 `array_and_topview.png`、`fig2.pdf`、`ext_fig_1.pdf`。

## 适合支持的 claim

- VERITAS 四台 12 m Davies-Cotton IACT 上安装的 stellar intensity interferometry system 已用于真实 astrophysical measurements，而不仅是 operation test。
- 该系统观测两颗 bright hot B stars：`β CMa` 和 `ε Ori`，目标亮度为 `m_v < 2.1`、温度 `T > 22000 K`。
- VSII 使用 high-speed streaming + post-observation / off-line correlations：各望远镜记录 starlight intensity fluctuations，观测后用 FPGA-based correlator 计算 pair correlations。
- VERITAS SII hardware 使用 420/5 filter；由于入射角导致 effective bandpass 约 centered at 416 nm、effective width 约 13 nm；该效应使 spectral density throughput 和 S/N 约降低 factor 2。
- PMT 为 Hamamatsu R10650，观测波长处 quantum efficiency 约 30%；ADC 以 250 MS/s、14-bit digitization 连续采样；数据以约 250 MB/s per telescope 写入 12 TB RAID；各望远镜 ADC clock 锁定到 common external 10 MHz clock / White Rabbit 分发。
- correlator 使用 64 time-lag channels，对应 `-128` 到 `+124 ns`，step `4 ns`。
- 对 `β CMa`，uniform disk angular diameter 为 `θ_UD = 0.523 ± 0.017 mas`，与 NSII 的 `0.50 ± 0.03 mas` 一致。
- 对 `ε Ori`，uniform disk angular diameter 为 `θ_UD = 0.631 ± 0.017 mas`，与 NSII 的 `0.67 ± 0.04 mas` 一致。
- limb-darkened diameters 为 `θ_LD = 0.542 ± 0.018 mas` (`β CMa`) 和 `θ_LD = 0.660 ± 0.018 mas` (`ε Ori`)。
- 论文报告 angular diameter measurement uncertainty better than 5%，并称 VSII 相比 NSII sensitivity improved by factor 6。
- 在 equivalent observation time 下，current capability 可对 magnitude 2.5 stars 达到 squared visibility precision 4.0%，对 magnitude 3.5 stars 达到 10%；未来 duty cycle 和 filter collimation 改进可能带来 factor 2–3 sensitivity gain，并有潜力测量 `m_B ~ 5` stars。
- 论文将该 demonstration 作为 CTA-SII 的技术路径证据：future CTA-SII 可达到 tens of micro-arcsecond scale angular resolution，且可在 bright moonlight conditions 下增加 IACT observatory science output。
- 论文数据量超过 40 TB，因此只有 post-correlation data can reasonably be made available。

## 公式 / 数值候选

```tex
g^{(2)}(\tau, \mathbf{r}) = \frac{\langle I_1(t) I_2(\mathbf{r}, t+\tau) \rangle}{\langle I_1(t) \rangle \langle I_2(t) \rangle}
```

```tex
g^{(2)}(\tau, \mathbf{r}) = 1 + |g^{(1)}(\tau, \mathbf{r})|^2
```

```tex
|g^{(1)}_\ast(\tau=0, r)|^2 = N_0 \left|2\frac{J_1(x_{UD})}{x_{UD}}\right|^2
```

```tex
x_{UD} = \pi \theta_{UD} r / \lambda
```

```tex
|g_\ast^{(1)}|^2 = |g^{(1)}|^2 (1+\beta_1)(1+\beta_2)
```

```tex
S/N = A\,\alpha\,n\,|g^{(1)}(r)|^2\sqrt{\frac{\Delta f T_0}{2}}
```

## 使用 caveat

- 这是 VERITAS SII demonstration / measurement paper，可支持真实 stellar angular diameter measurements；与 Dravins et al. 2012 的 CTA prospective design source 证据等级不同。
- 目标是 very bright hot B stars，不能外推到一般 faint stellar targets；论文中的 `m_B ~ 5` 是改进后潜力表述。
- angular diameter 结果依赖 uniform disk / limb-darkened model、filter bandpass、background correction、zero-baseline normalization `N0` 和 baseline coverage。
- 原始 high-speed time-stream 数据超过 40 TB，公开可得性主要限于 post-correlation data。
- CTA extrapolation 是 future capability statement，应与实际 VERITAS measurement 分开。
