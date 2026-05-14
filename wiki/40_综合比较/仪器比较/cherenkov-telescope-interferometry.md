---
title: Cherenkov 望远镜光学强度干涉比较
type: instrument-comparison
status: growing
last_updated: 2026-05-14
tags: [IACT, CTA, VERITAS, MAGIC, H.E.S.S., intensity-interferometry, optical-interferometry, SII]
source_count: 5
confidence: medium
related:
  - ../../30_仪器/iact/index.md
  - ../../30_仪器/iact/相关文献.md
  - iact-array-design.md
---

# Cherenkov 望远镜光学强度干涉比较

## 页面定位

本页整理把 IACT / Cherenkov telescope array 用作 optical stellar intensity interferometer 的思路、公式、阵列尺度、实验证明和限制。Dravins et al. 2012 提供 CTA prospective design-stage 分析；Acciari et al. 2019 / MAGIC 给出双 17 m IACT 的 correlation-detection demonstration；Abeysekara et al. 2020 / VERITAS Collaboration 给出现代 IACT 阵列完成真实 stellar angular diameter measurements 的 demonstration；MAGIC Collaboration / Abe et al. 2024 则把 MAGIC-SII 推进到 upgraded system performance、GPU correlator 和 22 个 stellar diameter measurements；Zmija et al. 2023 / H.E.S.S. 补充南天 H.E.S.S. Phase I telescopes 上的 first intensity interferometry measurements、zero-baseline channel 和 tracking-correction hardware。

该主题和常规 IACT gamma-ray 观测不同：IACT 页面主要讨论 atmospheric Cherenkov image reconstruction；本页讨论在 optical band 对恒星做二阶相干测量。

## 强度干涉的观测量

Dravins et al. 2012 采用 Hanbury Brown–Twiss 型 optical intensity interferometry 框架。它不是直接合成电场相位，而是比较不同望远镜记录的 intensity fluctuations 的 cross correlation。对 chaotic / thermal light，线偏振情形可写成：

```tex
\langle I_1(t) I_2(t) \rangle = \langle I_1 \rangle \langle I_2 \rangle (1 + |\gamma_{12}|^2)
```

因此强度涨落相关为：

```tex
\langle \Delta I_1(t) \Delta I_2(t) \rangle = \langle I_1 \rangle \langle I_2 \rangle |\gamma_{12}|^2
```

VERITAS demonstration 使用等价的 second-order coherence 表述：

```tex
g^{(2)}(\tau, \mathbf{r}) = \frac{\langle I_1(t) I_2(\mathbf{r}, t+\tau) \rangle}{\langle I_1(t) \rangle \langle I_2(t) \rangle}
```

```tex
g^{(2)}(\tau, \mathbf{r}) = 1 + |g^{(1)}(\tau, \mathbf{r})|^2
```

实际可见度幅度平方可由归一化相关得到：

```tex
|\gamma|^2 = \frac{\langle \Delta I_1 \Delta I_2 \rangle}{\langle I_1 \rangle \langle I_2 \rangle}
```

这种方法只直接给出 Fourier amplitude squared，不直接给出 phase；二维成像需要 phase-recovery / image-reconstruction algorithms，并可能存在 mirror-image degeneracy。

## 与 aperture synthesis 的关系

在小视场近似下，source brightness distribution 和 complex visibility 之间满足 Fourier-transform 关系。Dravins et al. 2012 使用如下形式说明 `(u,v)` plane 与成像的联系：

```tex
\Gamma(u,v) = \iint I(l,m) e^{-2\pi i(ul+vm)} dl dm
```

```tex
I_\nu(l,m) = \iint V(u,v) e^{2\pi i(ul+vm)} du dv
```

对 N 台望远镜，instantaneous baseline pair 数为：

```tex
N_\mathrm{pairs} = \frac{N(N-1)}{2}
```

多望远镜 baseline、不同 position angles 和 Earth rotation 可共同填充 `(u,v)` plane，但强度干涉缺少直接相位信息，因此 image reconstruction 的约束弱于传统 amplitude / phase interferometry。

## CTA design-stage 潜力

Dravins et al. 2012 把当时 CTA 设想中的 50–100 台、约 5–25 m aperture、分布在约 2–3 km² 面积上的 Cherenkov telescopes 视作潜在 optical intensity interferometer。若 2 km baseline 在 `λ = 350 nm` 使用，angular resolution 可接近 `30 μas`。

| CTA candidate layout | telescope 数 | unique baselines | baseline range | 说明 |
| --- | ---: | ---: | --- | --- |
| B | 42 | 253 | 32–759 m | 较少望远镜和较短最大 baseline。 |
| D | 57 | 487 | 170–2180 m | 最大 baseline 到约 2.18 km，但短 baseline 覆盖较弱。 |
| I | 77 | 1606 | 90–2200 m | baseline 数最多，`(u,v)` coverage 更适合成像。 |

这些 layout 是当时 CTA design study 的 candidate layouts，不应直接等同于后续 CTA construction baseline 或发布的 instrument performance。

## VERITAS 四望远镜 demonstration

Abeysekara et al. 2020 / VERITAS Collaboration 报告了四台 12 m VERITAS IACT 上的 stellar intensity interferometry demonstration。该系统观测两颗 bright hot B stars：`β CMa` 和 `ε Ori`，并用 high-speed streaming + post-observation off-line correlations 测得 stellar angular diameters。

| target | source 中的目标性质 | uniform disk diameter | limb-darkened diameter | 对比 |
| --- | --- | --- | --- | --- |
| `β CMa` | BII/III，`B = 1.73`。 | `θ_UD = 0.523 ± 0.017 mas` | `θ_LD = 0.542 ± 0.018 mas` | 与 NSII `0.50 ± 0.03 mas` 一致。 |
| `ε Ori` | B0Ia，`B = 1.51`。 | `θ_UD = 0.631 ± 0.017 mas` | `θ_LD = 0.660 ± 0.018 mas` | 与 NSII `0.67 ± 0.04 mas` 一致。 |

论文报告这两次 angular diameter measurements 的 uncertainty better than 5%，并指出 VSII 相比 NSII sensitivity improved by factor 6。对 equivalent observation time，当前系统可对 magnitude 2.5 stars 达到 squared visibility precision 4.0%，对 magnitude 3.5 stars 达到 10%；未来 duty cycle 和 filter collimation 改进可能带来 factor 2–3 sensitivity gain，并有潜力测量 `m_B ~ 5` stars。

## VERITAS SII 系统实现要点

VERITAS SII hardware 安装在 gamma-ray camera 前方的 aluminum plate 上，用 45° mirror 将主镜光重定向到 diaphragm 和 narrowband filter。source 给出的关键实现参数包括：

- 四台 VERITAS telescopes：每台 12 m Davies-Cotton design，345 个 hexagonal mirror facets，f/1 optics。
- filter：SEMROCK 420/5；由于大入射角，effective bandpass 约 centered at 416 nm、effective width 约 13 nm，并使 throughput / S/N 约降低 factor 2。
- detector：Hamamatsu R10650 PMT，观测波长处 quantum efficiency 约 30%。
- digitization：250 MS/s、14-bit ADC；数据以约 250 MB/s per telescope 写入 12 TB RAID。
- timing：各望远镜 ADC clock phase-locked 到 common external 10 MHz clock，并通过 White Rabbit optical fiber 分发。
- correlation：观测后 FPGA-based correlator 处理 stored data；64 time-lag channels 覆盖 `-128` 到 `+124 ns`，step `4 ns`。

这个实现把 Dravins et al. 2012 的 prospective operating concept 推进到真实 stellar measurement，但目标仍限于 bright stars，且原始 high-speed time-stream 数据量超过 40 TB。

## MAGIC 双望远镜 correlation observations

Acciari et al. 2019 使用两台 MAGIC 17 m IACT 做 optical intensity interferometry observations。该系统只使用每台 telescope 的 central PMT signal，在 analog mode 下连续采样 PMT current fluctuations；source 报告对三颗 `θ ~ 0.5–1 mas` 的恒星检测到 photon-intensity fluctuation correlations。

MAGIC setup 的关键参数包括：

- MAGIC 位于 La Palma Roque de los Muchachos Observatory，两台望远镜 mirror dish diameter 为 17 m，PMT camera 有 1039 pixels。
- central pixel 前安装 Semrock 432/36 nm BrightLine filter；由于入射角效应，effective transmission center shifted to `~427 nm`，sensitivity 降低约 15%。
- sampling frequency explored 250 MSps–1 GSps；在 500 MSps 时 duty cycle 约 10%。
- MAGIC observation 使用 Pearson correlation coefficient 和 normalized contrast `c` 来比较不同 baseline 下的 visibility。

source 的候选星和检测结果包括：

| star | source 给出的 `m_B` / angular diameter | baseline / expected visibility 示例 | correlation detection |
| --- | --- | --- | --- |
| Adhara (`ε CMa`) | `m_B = 1.29`，`θ = 0.77 ± 0.05 mas`。 | 21:00 时 baseline `34.1 m`，`V² = 0.80`，expected `T_5σ = 36 s`，measured `38 / 35 s`。 | day 1: 5.3σ；day 3: 15.4σ；day 4: 12.6σ。 |
| Benetnasch (`η UMa`) | `m_B = 1.67`，`θ = 0.82 ± 0.03 mas`。 | baseline examples 55.3–78.6 m，`V²` 约 0.50 到 0.22。 | 5.8σ、4.9σ、7.3σ、5.1σ。 |
| Mirzam (`β CMa`) | `m_B = 1.73`，`θ = 0.50 ± 0.03 mas`。 | 21:00 时 baseline `41.3 m`，`V² = 0.87`，expected `T_5σ = 60 s`，measured `73 s`。 | day 5: 9.3σ。 |

MAGIC paper 的结论是：MAGIC can already be used as an optical intensity interferometer，并估计在 current sensitivity 下，unresolved `m_B = 5` star 的 5σ signal 约需 3 h。作者同时明确提示：当时只在 few nights 取得 few minutes of data，systematics control 很弱；产生 scientific results 前还需要 longer data samples、more stars up to at least magnitude 4、whole-sky / different-condition sampling。

## MAGIC-SII performance / first measurements

MAGIC Collaboration / Abe et al. 2024 把 Acciari et al. 2019 的 few-minute feasibility test 升级为可常规切换的 MAGIC Stellar Intensity Interferometer。该系统在 2021 年后加入实时、dead-time-free、4-channel、GPU-based correlator；从 VHE gamma-ray mode 切换到 optical interferometry mode 可在少于约 1 min 内完成，并利用 bright-Moon periods 在 2022 年累计 `192 h` observations。

MAGIC-SII 的实现重点是尽量复用 MAGIC 原有 gamma-ray camera 和 signal chain：

- 每台 MAGIC camera 有 1039 个 PMT；SII 使用少数既有 camera pixels，而非额外安装独立 photodetectors。
- signal 通过 850 nm VCSEL analog optical transmission 到 receiver / digitizer；receiver 使用 multimode-fiber-coupled photodiode 和 Femto HSA-Y-2-40 amplifier。
- Semrock 425-26 nm filters 放在 PMT 前；当前每台 telescope 有两个 signal pixels 接 correlator、一个 background pixel 做 simultaneous background DC measurement。
- digitizers 为两块 Spectrum M4i.4450-x8 PCIe 2.0 boards；每块处理两路 channels，最高 500 MS/s simultaneous sampling，14-bit resolution，并用 RDMA 直接传输到 GPU memory。
- correlator server 使用 Nvidia Tesla V100 GPU；software 对 4 channels 计算 6 个 cross-correlations 和 4 个 autocorrelations，delay window 为 `±2048 ns`，double-buffering 使 live-time 约 `100%`。
- Active Mirror Control 支持 full-mirror、chess-board 和 sub-reflector modes；后两者可用同一对 MAGIC telescopes 采集 close-to-zero-baseline 或 1–17 m 级短 baseline 信息。

2024 source 报告 `22` 个 stellar diameter measurements：9 个 reference stars 与 NSII / VERITAS / CHARA 等已有 direct measurements 对比，13 个 stars 是 MAGIC 在 400–440 nm band 的 first direct diameter measurements。例子包括：

| target | role | MAGIC-SII measured `θ_UD` | measured `θ_LD` | 对比 / caveat |
| --- | --- | --- | --- | --- |
| `eps CMa` / Adhara | reference star | `0.768 ± 0.023 ± 0.019 mas` | `0.792 ± 0.023 ± 0.020 mas` | 与 NSII `0.77 ± 0.05 mas` 对比；also used to constrain zero-baseline correlation。 |
| `eps Ori` | reference star | `0.606 ± 0.020 ± 0.018 mas` | `0.630 ± 0.022 ± 0.019 mas` | 与 VERITAS `0.631 ± 0.017 mas` 对比。 |
| `eta UMa` | reference star | `0.800 ± 0.017 ± 0.011 mas` | `0.828 ± 0.018 ± 0.011 mas` | 与 CHARA `0.818 ± 0.06 mas` 对比。 |
| `bet CMa` / Mirzam | reference star | `0.560 ± 0.026 ± 0.023 mas` | `0.576 ± 0.026 ± 0.023 mas` | 与 VERITAS `0.523 ± 0.017 mas` 对比。 |

当前 MAGIC-SII realistic target limit 约为 `B ~ 4 mag`，已能在 reasonable observing times 下达到 few-percent-level stellar diameter relative errors；但只有两台 telescopes 的 `(u,v)` coverage 仍限制非径向对称模型、fast rotator oblateness 和 image reconstruction。future LST-1 / LST2-4 / Northern CTAO extension 可提升 mirror area、QE、optical efficiency 和 simultaneous baseline coverage；source 将 `7–8 mag` 量级视为 simple CTAO-class implementation 的 future sensitivity scale，而不是当前 MAGIC-SII 实测能力。

## H.E.S.S. first intensity interferometry measurements

Zmija et al. 2023 报告 H.E.S.S. telescopes 的 first intensity interferometry measurements。2022 年 4 月 moonlight break 期间，作者在 Namibia Khomas Highlands 的两台 H.E.S.S. Phase I telescopes 上安装外部 optical setup；该 setup 固定在 Cherenkov camera lid 上，把进入的光分到两个 PMTs，因此可以同时测量同一望远镜内的 zero-baseline correlation 和两望远镜之间的 cross-correlation。

H.E.S.S. setup 的实现重点包括：

- 每套外部结构约 `(50 × 63) cm²`，安装在 Phase I camera lid 上，光路为 2-inch tube system。
- 光学元件包括 `F = -75 mm` concave lens、LC-HBP465/2-50 narrowband interference filter（465 nm CWL, 2 nm width）和 beam splitter。
- detector 为 Hamamatsu R11265U-300 PMT；peak sensitivity 在 420 nm，peak QE 约 39%，在 465 nm 约 33%。
- optical elements motorized，可在观测中通过 photon-rate scan 修正 tracking / pointing inaccuracies。
- correlation 在 April 2022 campaign 中离线完成：每台 telescope 一个 binary file、每个文件含两个 acquisition channels，四路 waveform channels 读盘后计算 channel pairs；当时一个 `3.436 s` measurement 需要约 `13 s` analysis。
- PMT current Fourier spectra 和 `g^(2)` functions 中有 narrow noise peaks；analysis 使用 `200 MHz` low-pass filter 和 notch filtering 清理。

H.E.S.S. source 使用的 coherence-time 表述是：

```tex
\tau_c(b) = 0.5\, k_\mathrm{s}(b) k_\mathrm{T} \frac{\lambda_0^2}{c\Delta\lambda}
```

其中 `0.5` 来自 unpolarized light，`k_s(b)` 是 spatial coherence factor，`k_T` 是 spectral transmission profile correction。对于 465 nm、2 nm filter，zero-baseline 期望值写作：

```tex
\tau_c(b=0) = 0.5 \times 0.842 \times \frac{(465\,\mathrm{nm})^2}{c\times 2\,\mathrm{nm}} = 152\,\mathrm{fs}
```

uniform-disc spatial coherence fit 使用：

```tex
f(x) = a \left[ \frac{2J_1(\pi x\varphi/\lambda)}{\pi x\varphi/\lambda} \right]^2
```

source 的目标和结果包括：

| target | role | H.E.S.S. result / use | caveat |
| --- | --- | --- | --- |
| `σ Sgr` / Nunki | single-star approximation target | `φ_Nunki = (0.52 ± 0.07) mas`；source 也与 literature photometric `0.68 mas` 对比。 | fitted zero-baseline constant `a_Nunki = (43.76 ± 10.40) fs`，低于 expected `152 fs`，显示 coherence loss。 |
| `λ Sco` / Shaula | southern multiple-star target | simplified equal-diameter assumption 下得到 `φ_Shaula = (0.49 ± 0.06) mas`。 | Shaula 是 triple star system；single-star / equal-diameter interpretation 应谨慎。 |
| `α Cru` / Acrux | systematic / multiple-star case | 用于 zero-baseline correlations 和 systematics studies；large-baseline data 指向 complex source geometry。 | multiple components mean single-star fit 不适合。 |

这篇 source 的主要价值是扩展南天 IACT 阵列的 SII demonstration，并把 zero-baseline channel、motorized tracking correction 和 moonlight-break observing mode 加入系统比较；但它还不是 MAGIC-SII 2024 那种 real-time production-like correlator paper。

## Signal-to-noise 与目标限制

强度干涉 pair 的 RMS signal-to-noise 在 CTA prospective source 中写作：

```tex
(S/N)_\mathrm{RMS} = A \alpha n |\gamma_{12}(\mathbf{r})|^2 \Delta f^{1/2} (T/2)^{1/2}
```

VERITAS demonstration 使用同类一阶近似：

```tex
S/N = A\,\alpha\,n\,|g^{(1)}(r)|^2\sqrt{\frac{\Delta f T_0}{2}}
```

MAGIC 2019 paper 把 mirror area、PMT quantum efficiency、剩余光学效率、effective cross-correlation electrical bandwidth、PMT excess-noise factor 和 filter 后谱形也写入 S/N：

```tex
S/N = A \alpha(\lambda_0) q(\lambda_0) n(\lambda_0) |V|^2(\lambda_0,d) \sqrt{b_v} F^{-1}\sqrt{T/2}\sigma
```

MAGIC-SII performance paper 进一步加入 background-to-starlight correction：

```tex
S/N = A\cdot \alpha(\lambda_0) \cdot q(\lambda_0) \cdot n(\lambda_0) \cdot |V|^2(\lambda_0, d) \cdot \sqrt{b_\nu} \cdot F^{-1} \cdot \sqrt{T/2} \cdot (1+\beta)^{-1} \cdot \sigma
```

其中 `A` 是 telescope collecting / mirror area，`α` 是 detector quantum efficiency，`n` 是 spectral photon flux density，`|γ12|²`、`|g^(1)|²` 或 `|V|²` 是 baseline 上的 coherence / visibility amplitude squared，`Δf` 或 `b_v` / `b_ν` 是 electronic bandwidth，`T` / `T0` 是 integration time，`β` 表示 background-to-starlight ratio。MAGIC-SII 2024 给出的 current setup parameters 是：mirror area `236 m²`、`α(λ0)=0.295`、`q(λ0)=0.304`、`b_ν=125 MHz`、`σ=0.87`、PMT noise factor `F=1.15`。

Dravins et al. 2012 给出的 conservative practical limit 是：CTA-type large array 做 two-dimensional imaging 的目标亮度约到 `m_V = 6`；若只测一维量如 stellar diameter 或 limb darkening，可以稍暗一些。Abeysekara et al. 2020 的 VERITAS result 已实现 bright-star angular diameter measurements，并把未来改进后的潜力表述为 `m_B ~ 5`。MAGIC-SII 2024 的 current system realistic target limit 约为 `B ~ 4 mag`；`7–8 mag` 是加入 LST / CTAO-class telescopes 后的 future extrapolation。

## 和 IACT 操作的接口

强度干涉使用 Cherenkov telescope 的大 collecting area 和长 baseline，但它对 detector、central pixel、optical filter、timing、correlator、delay unit 和 data handling 有独立要求。Dravins et al. 2012 提到 VERITAS 12 m telescopes 的早期测试性观测已用数字相关器连接 telescope pairs，处理过最高约 30 MHz continuous count rates；Abeysekara et al. 2020 则展示了后续 VERITAS SII system 已完成真实 stellar measurements。

强度干涉对 atmospheric turbulence 和 telescope optical imperfections 相对不敏感，这是它适合利用 Cherenkov telescopes 的关键原因；但这种鲁棒性不等于可以忽略 photon statistics、bandwidth、delay calibration 和 correlation electronics。

## 后续 source 对比框架

| source 类别 | 本页需要区分的问题 | 当前状态 |
| --- | --- | --- |
| CTA prospective design paper | baseline 数、`(u,v)` coverage、理论 S/N 和 limiting magnitude。 | Dravins et al. 2012 已 ingest。 |
| VERITAS demonstration | 是否完成真实 stellar intensity interferometry measurement。 | Abeysekara et al. 2020 已 ingest。 |
| MAGIC observations | 双 17 m IACT 的 central-pixel correlation detection、filter / duty-cycle / systematics 限制。 | Acciari et al. 2019 已 ingest。 |
| MAGIC-SII performance | upgraded MAGIC-SII system、GPU correlator、22 个 stellar diameter measurements、systematics 和 LST / CTAO extension。 | MAGIC Collaboration / Abe et al. 2024 已 ingest。 |
| H.E.S.S. demonstration | 南天 IACT 阵列强度干涉平台、zero-baseline channel、motorized tracking correction 和 Shaula / Nunki / Acrux measurements。 | Zmija et al. 2023 已 ingest。 |

## 使用 caveat

- Dravins et al. 2012 是 CTA prospective / design-stage source，不是已经建成的 CTA intensity interferometry instrument paper。
- Abeysekara et al. 2020 是 VERITAS demonstration / measurement paper，可支持真实 stellar angular diameter measurements；但目标是 very bright hot B stars，不能外推到一般 faint targets。
- Acciari et al. 2019 是 MAGIC correlation-detection / technical demonstration source，适合支持 MAGIC feasibility 和 sensitivity estimate；作者明确说当时 systematics control 不足以产出成熟 scientific results。
- MAGIC Collaboration / Abe et al. 2024 是 MAGIC-SII performance / first-measurements source，适合支持 upgraded GPU correlator、22 个 stellar diameter measurements 和 systematics budget；但 current target limit 仍约 `B ~ 4 mag`，LST / CTAO extension 属于 future capability。
- Zmija et al. 2023 / H.E.S.S. 是 first-measurements / demonstration source，适合支持 H.E.S.S. moonlight-break SII setup、zero-baseline channel 和 motorized tracking correction；但 April 2022 analysis 是 offline correlation，coherence loss 原因未完全解决，Shaula / Acrux multiple-star fits 不能当作稳健 single-star diameter measurements。
- 二阶相干只直接给出 Fourier amplitude squared；二维成像必须说明 phase-recovery / image-reconstruction 假设。
- `m_V ≈ 6` 是 CTA-type large array two-dimensional imaging 的 conservative practical limit；`m_B ~ 5` 是 VERITAS source 对 future improvements 的潜力表述。
- VERITAS angular diameter 结果依赖 uniform disk / limb-darkened model、filter bandpass、background correction、zero-baseline normalization 和 baseline coverage。
- 本页中的 B / D / I layout 数值来自当时 CTA design study，应与后续 CTA construction baseline、CTA Observatory IRFs 和现代 SII demonstrations 分开。

## 相关页面

- [IACT](../../30_仪器/iact/index.md)
- [IACT 相关文献](../../30_仪器/iact/相关文献.md)
- [IACT 阵列设计比较](iact-array-design.md)

## 来源

- D. Dravins, S. LeBohec, H. Jensen and P. D. Nuñez for the CTA Consortium, “Optical Intensity Interferometry with the Cherenkov Telescope Array,” arXiv:1204.3624, DOI: 10.1016/j.astropartphys.2012.04.017。
- A. U. Abeysekara et al. / VERITAS Collaboration, “Demonstration of stellar intensity interferometry with the four VERITAS telescopes,” arXiv:2007.10295, DOI: 10.1038/s41550-020-1143-y。
- V. A. Acciari et al., “Optical intensity interferometry observations using the MAGIC imaging atmospheric Cherenkov telescopes,” arXiv:1911.06029, DOI: 10.1093/mnras/stz3171。
- MAGIC Collaboration, S. Abe et al., “Performance and first measurements of the MAGIC Stellar Intensity Interferometer,” arXiv:2402.04755, DOI: 10.1093/mnras/stae697。
- A. Zmija, N. Vogel, F. Wohlleben, G. Anton, A. Zink and S. Funk, “First Intensity Interferometry Measurements with the H.E.S.S. Telescopes,” arXiv:2312.08015, DOI: 10.1093/mnras/stad3676。
