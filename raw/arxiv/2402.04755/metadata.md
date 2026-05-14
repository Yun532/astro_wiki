---
title: Performance and first measurements of the MAGIC Stellar Intensity Interferometer
source_type: arxiv-paper
status: collected
last_updated: 2026-05-14
arxiv: "2402.04755"
doi: "10.1093/mnras/stae697"
arxiv_doi: "10.48550/arXiv.2402.04755"
local_pdf: raw/arxiv/2402.04755/2402.04755.pdf
local_source_package: raw/arxiv/2402.04755/2402.04755-source.tar.gz
local_arxiv_api: raw/arxiv/2402.04755/2402.04755-api.xml
---

# Performance and first measurements of the MAGIC Stellar Intensity Interferometer

- Source：MAGIC Collaboration, S. Abe et al., “Performance and first measurements of the MAGIC Stellar Intensity Interferometer,” arXiv:2402.04755, DOI: 10.1093/mnras/stae697。
- 本地保存：PDF、arXiv source package 和 arXiv API XML。
- source package 主文件：`mnras_template.tex`；图像文件包括 `SII_setup_larger.pdf`、`optical_passband.pdf`、`Filter_holder.pdf`、`signal_to_noise_evaluation.pdf`、`Relative_diameter_errors.pdf`、`reference_stars.pdf`、`candidates.pdf`、`sensitivity_simulation.pdf` 等。

## 适合支持的 claim

- MAGIC-SII 是安装在 MAGIC 两台 17 m IACT 上的 Stellar Intensity Interferometer；它使用窄带 optical filters、连续 digitization 和 GPU-based correlator，把标准 VHE gamma-ray observation mode 与 optical interferometry mode 的切换压到少于约 1 分钟。
- 2019 MAGIC demonstration 受低 duty cycle 和 filter mechanical installation 限制；2021 后的 MAGIC-SII 升级支持实时、dead-time-free、4-channel、GPU-based correlation，并在 2022 年 1–12 月获得 192 h bright-Moon-time observations。
- MAGIC-SII 使用 MAGIC 原有 PMT camera 中的少数像素，而不是额外安装独立 photodetectors；PMT signal 经 850 nm VCSEL analog optical transmission 到接收器和 digitizers。
- 每台 MAGIC camera 有 1039 个 PMT；PMT diameter 25.4 mm，6 dynodes，pixel pitch 30 mm，对应 0.1 deg FoV。
- SII receiver 使用 multimode-fiber-coupled photodiode 和 Femto HSA-Y-2-40 amplifier；pixel preamplifier、optical transmission 和 receiver 的 combined transfer function bandwidth >400 MHz，但实际 channel bandwidth 主要受 PMT pulse response 与 digitizer anti-aliasing filter 限制，约 110–125 MHz。
- Semrock 425-26 nm optical filter 用于保护 PMT 并提供窄 optical bandpass；平行光 transmission center 为 425 nm、FWHM 26 nm，但 MAGIC f/D 接近 1 的大入射角分布会改变有效 passband。
- filter holder 可远程部署，通常数秒内把 filter 放到 PMT 前方；每个 telescope 目前有 3 个 Semrock 425-26 nm filters，其中两个 signal pixels 接 correlator，一个 background pixel 用于同 passband 的 simultaneous background DC measurement。
- Active Mirror Control 使 MAGIC-SII 可工作在 full-mirror、chess-board 和 sub-reflector modes：full-mirror 是标准模式；chess-board 可把每台 telescope 变成两个 virtual overlapping telescopes；sub-reflectors 可用 1–17 m 级短 baseline 采样 bright / large stars 的 Fourier space。
- correlator 使用两块 Spectrum M4i.4450-x8 PCIe 2.0 digitizer boards；每块 digitizer 处理两个 channels，最高 500 MS/s simultaneous sampling，14-bit resolution，支持 RDMA 直接传输到 GPU memory。
- correlator server 使用 off-the-shelf hardware，包括 20 CPU cores、SSD/HDD 和 Nvidia Tesla V100 GPU（5120 cores、32 GB HBM2、14 TFLOPs single precision）。
- correlation code 可实时处理来自两块 digitizer 的 4 GB/s 数据；GPU software 计算 4 channels 的 6 cross-correlations 和 4 autocorrelations，delay window 为 ±2048 ns，通常每 2^18 samples per channel 做 FFT，500 frames 累积后写出。
- double-buffering data loop 使 correlator live-time 约为 100%；raw-signal dump mode 可保存一个 digitizer 的两路 14-bit / 2 ns samples，但每路 raw data rate 约 1 Gb/s，因此只适合短测试。
- analysis 从 Pearson correlation `rho(tau)` 得到 contrast / squared visibility，并用 PMT gain、DC star / NSB、background correction `beta`、time-delay correction 和 weighted averaging 校准。
- MAGIC-SII 2022 results 报告 22 个 stellar diameter measurements：9 个 reference stars 与 NSII / VERITAS / CHARA 等已有 comparable measurements 对比，13 个 stars 在 400–440 nm band 首次直接测量直径。
- reference-star examples：`eps CMa` measured `theta_UD = 0.768 ± 0.023 ± 0.019 mas`；`eps Ori` measured `theta_UD = 0.606 ± 0.020 ± 0.018 mas`；`eta UMa` measured `theta_UD = 0.800 ± 0.017 ± 0.011 mas`；`bet CMa` measured `theta_UD = 0.560 ± 0.026 ± 0.023 mas`。
- candidate-star sample 覆盖 mostly early-type stars，`B` magnitude 约 2.12–3.73，estimated angular diameters 约 0.3–1.3 mas；`phi Sgr` 的大误差主要来自仅 15 min observing time。
- sensitivity evaluation 表明经过 signal weighting 后 measured signal-to-noise 与 equation expectation 一致；diameter relative uncertainties 与 expected trend 一致，但受 exposure time、UV coverage 和 night-sky brightness 差异影响。
- 当前 MAGIC-SII realistic target limit 约为 `B ~ 4 mag`，因此还不能与 CHARA 等 classical long-baseline optical interferometers 竞争。
- current setup performance parameters：mirror area 236 m²，photo-detector QE `alpha(lambda0)=0.295`，optical efficiency `q(lambda0)=0.304`，electronic bandwidth `b_nu=125 MHz`，normalized spectral distribution `sigma=0.87`，PMT noise factor `F=1.15`。
- systematics table 给出 squared visibility 主要系统误差：electronic bandwidth 0.5%，optical bandwidth <1%，gain drift after DC jump 1%，long-term degradation 0.8%，DC NSB subtraction 1.5/3%（faint stars defined as `B_mag > 3.5`），residual electronic noise negligible after mitigation。
- source 结论：MAGIC-SII 已能在 reasonable observing times 下达到 few-percent-level stellar diameter relative errors；这可开始支持 fast-rotating-star oblateness 等 science case，但非径向对称模型需要更多 baseline / orientation 和标准化数据产品。
- future improvements：next-generation digitizers could improve sensitivity by about `sqrt(2)`；LST-1 / LST2-4 integration would raise mirror area / QE / optical efficiency and improve UV coverage；full Northern CTAO integration could make IACT SII competitive in blue wavelengths, though simple implementations may not go beyond magnitude 7–8 because of IACT optical PSF limitations。

## 公式 / 数值候选

```tex
V^2 \propto c = K \frac{\rho({\tau_0}) \sqrt{G_1 G_2}}{\sqrt{DC_1 DC_2}}
```

```tex
c = K \frac{\rho({\tau_0}) \beta \sqrt{G_1 G_2}}{\sqrt{DC(Star)_1 DC(Star)_2}}
```

```tex
\beta = \sqrt{\frac{(DC(Star)_1 + DC(NSB)_1)(DC(Star)_2 + DC(NSB)_2)}{DC(Star)_1 DC(Star)_2}}
```

```tex
V(d)=2\frac{J_1(\pi d \theta_{UD}/\lambda)}{\pi d \theta_{UD}/\lambda}
```

```tex
V(d)^2 = \left(\frac{1-u_\lambda}{2} + \frac{u_\lambda}{3}\right)^{-2} \left( (1-u_\lambda) \frac{J_1(x_{LD})}{x_{LD}} + u_{\lambda} \sqrt{\pi/2} \frac{J_{3/2}(x_{LD})}{(x_{LD})^{3/2}} \right)
```

```tex
x_{LD} = \pi d \theta_{LD}/\lambda
```

```tex
S/N = A\cdot \alpha(\lambda_0) \cdot q(\lambda_0) \cdot n(\lambda_0) \cdot |V|^2(\lambda_0, d) \cdot \sqrt{b_\nu} \cdot F^{-1} \cdot \sqrt{T/2} \cdot (1+\beta)^{-1} \cdot \sigma
```

## 使用 caveat

- 这是 MAGIC-SII performance / first-measurements source，适合从 D3 的 feasibility / correlation detection 升级到 instrument performance、stellar diameter measurement 和 systematics control；不要把它与 2019 few-minutes demonstration 等同。
- 22 个 stellar diameters 主要是 bright stars；current realistic target limit 约 `B ~ 4 mag`，future `7–8 mag` 是加入 LST / CTAO-class telescopes 后的 extrapolation，不是当前 MAGIC-SII 实测限制。
- 当前 MAGIC 只有两台 telescopes，UV coverage 和 baseline orientation coverage 受限；非径向对称模型、fast rotator oblateness 和 image reconstruction 需要更多 baselines / orientations。
- `V(d)` uniform-disc / limb-darkened fits 假设 radial symmetry；candidate sample 中不少 fast rotators 可能偏离这一假设。
- S/N 公式中的 `beta` 用于 background-to-starlight correction；fainter stars 中 NSB subtraction uncertainty 更重要。
- source 明确表示当前结果尚不能与 CHARA 等 classical optical interferometers 竞争；竞争力来自 planned digitizer / photodetector / LST / CTAO extension。
