---
title: Optical intensity interferometry observations using the MAGIC imaging atmospheric Cherenkov telescopes
source_type: arxiv-paper
status: collected
last_updated: 2026-05-14
arxiv: "1911.06029"
doi: "10.1093/mnras/stz3171"
arxiv_doi: "10.48550/arXiv.1911.06029"
local_pdf: raw/arxiv/1911.06029/1911.06029.pdf
local_source_package: raw/arxiv/1911.06029/1911.06029-source.tar.gz
---

# Optical intensity interferometry observations using the MAGIC imaging atmospheric Cherenkov telescopes

- Source：V. A. Acciari et al., “Optical intensity interferometry observations using the MAGIC imaging atmospheric Cherenkov telescopes,” arXiv:1911.06029, DOI: 10.1093/mnras/stz3171。
- 本地保存：PDF 和 arXiv source package。
- source package 主文件：`MN-19-3834-MJ_191024_rev2.tex`；图像文件包括 `Interferometer_sketch.png`、`Eff_Transmission_Semrock_432-36nm_root.png`、`adhara_3_pearsons.png`、`adhara_3_c_run.png`、`all_c_vs_V2.png` 等。

## 适合支持的 claim

- MAGIC 的两台 17 m IACT 可通过简单 optical setup 作为 optical intensity interferometer 使用；该 paper 报告了三颗星的 photon-intensity fluctuation correlation detections。
- IACT 具有 large mirrors 和 order-of-1 ns response to few-photo-electron optical signals，因此适合 optical intensity interferometry；MAGIC source 声称这种方法可达到 tens of microarcsec angular resolution。
- MAGIC 位于 La Palma Roque de los Muchachos Observatory，两台 telescope mirror dish diameter 为 17 m；每台 camera 有 1039-pixel PMT camera，interferometry observations 只使用 central PMT signal。
- MAGIC central pixels 使用 analog mode，连续采样 PMT signal；每个约 2–4 ns sample 对应 tens of photo-electrons。
- central pixel 前增加 Semrock 432/36 nm BrightLine filter；正常入射 transmission 在 414–450 nm >90%，但由于镜面直接入射角分布，effective transmission center shifted to ~427 nm，sensitivity 降低约 15%。
- acquisition sampling frequency considered 250 MSps–1 GSps；记录为 10×100 MS records；500 MSps 时 duty cycle 约 10%。
- 观测候选包括 Adhara (`ε CMa`)、Benetnasch (`η UMa`) 和 Mirzam (`β CMa`)；source table 给出 `m_B`、stellar angular diameter、baseline、expected visibility 和 expected/measured `T_5σ`。
- Adhara 的候选参数：`m_B = 1.29`，`θ = 0.77 ± 0.05 mas`，baseline 约 34.1 / 25.9 / 28.0 m；在 21:00 的 expected `T_5σ = 36 s`，measured `38 / 35 s`。
- Mirzam 的候选参数：`m_B = 1.73`，`θ = 0.50 ± 0.03 mas`，baseline 约 41.3 / 39.8 / 44.5 m。
- clear correlation signal 在所有 samples 中被检测到；修正 variable delay 后，固定在 `τ ~ 4 ns`。
- reported detection significances 包括 Adhara day 1: 5.3σ、day 3: 15.4σ、day 4: 12.6σ；Benetnasch day 1/3/4/5: 5.8σ / 4.9σ / 7.3σ / 5.1σ；Mirzam day 5: 9.3σ。
- source 结论：MAGIC can already be used as an intensity interferometer；但当时只有 few minutes of data on a few nights，systematics control 很弱。
- source 估计 current interferometer about 10 times more sensitive than Narrabri assuming 100% duty cycle；with this sensitivity, 5σ signal from an unresolved `m_B = 5` star would require about 3 h。
- caveat：在产生 scientific results 前，需要 longer data samples、more stars up to at least magnitude 4、whole-sky / different-observation-condition sampling 和 systematics quantification。

## 公式 / 数值候选

```tex
g^{(2)} = \frac{\langle I_1(t) I_2(t+\tau) \rangle}{\langle I_1(t) \rangle \langle I_2(t) \rangle}
```

```tex
g^{(2)} = 1 + \frac{\Delta f}{\Delta \nu} |V_{12}|^2
```

```tex
c = \frac{\langle (I_1(t)-\langle I_1\rangle)(I_2(t+\tau)-\langle I_2\rangle) \rangle}{\langle I_1(t) \rangle \langle I_2(t) \rangle}
```

```tex
c = g^{(2)} - 1 = \frac{\Delta f}{\Delta \nu}|V_{12}|^2
```

```tex
|V_{12}| = 2\frac{B_1(\pi d\theta/\lambda)}{\pi d\theta/\lambda}
```

```tex
\frac{c(d)}{c(0)} = |V_{12}(d)|^2
```

```tex
S/N = A \alpha(\lambda_0) q(\lambda_0) n(\lambda_0) |V|^2(\lambda_0,d) \sqrt{b_v} F^{-1}\sqrt{T/2}\sigma
```

```tex
S/N = 0.4 \sqrt{T_0} 10^{-0.4 m_B}
```

## 使用 caveat

- 这是 MAGIC 双望远镜 intensity-interferometry observation / technical demonstration source；它证明 correlation detection 与 instrument feasibility，但作者明确说当时还没有足够 systematics control 来给出 mature scientific results。
- 与 VERITAS paper 的 angular diameter measurement 不同，MAGIC source 主要支持 correlation detection、sensitivity estimate 和 instrumental feasibility。
- `m_B = 5` in about 3 h 是 unresolved-star 5σ signal 的 sensitivity estimate；resolved-star measurements 还需要 sample correlation function 到较低 `|V|²`。
- current setup duty cycle、filter frame、Moon effects、electronic noise、telescope tracking、PMT response 和 mirror degradation 都是 caveats。
- 公式中 `B1` 是 first-order Bessel function；`d` 是 telescope baseline，`θ` 是 uniform disk angular diameter，`λ` 是 observing wavelength。
