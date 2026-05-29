# 03 Fireball 模型

Fireball model 是 GRB 理论的基础框架：在一个很小的 central-engine 区域内释放巨大能量，初始形态可以是 radiation、pairs、magnetic field 和少量 baryons 的 optically thick plasma；随后 fireball 加速、变透明，并最终与外部介质相互作用产生 afterglow。本章只建立动力学和尺度关系，辐射谱和 closure relations 放在后续 synchrotron afterglow 章节。

## 1. Compactness problem

GRB 的 prompt emission 具有两个看似矛盾的特征：

1. variability timescale 很短，常见 `δt ~ ms–s`，意味着 emitting region 尺度若非相对论运动则约为

```tex
R \lesssim c\delta t.
```

2. isotropic-equivalent energy 极高，可达 `E_{\rm iso} ~ 10^{51}–10^{55} erg`，且光子能量常超过 pair-production threshold。

若把能量放入这样紧凑的非相对论区域，γγ pair production optical depth 会极大，源应当对高能 photon 不透明。一个量级估计是：若 photon 总能量为 `E`，源尺度为 `R`，典型 photon energy 为 `\langle E_\gamma \rangle`，photon number density 量级为

```tex
n_\gamma \sim \frac{E}{(4\pi/3)R^3\langle E_\gamma \rangle}.
```

光深量级为

```tex
\tau_{\gamma\gamma} \sim n_\gamma \sigma_T R.
```

对 GRB prompt 的典型观测量，这个值远大于 1。观测到非热谱和高能 photon 说明 emitting material 必须以 relativistic bulk Lorentz factor 向观测者运动。

相对论运动缓解 compactness problem 的原因包括：

- emitting radius 不是 `cδt`，而是约 `R \sim 2\Gamma^2 c\delta t`；
- comoving photon energy 降低，pair production threshold 更难满足；
- comoving photon density 降低；
- relativistic beaming 改变 observed luminosity 与 comoving luminosity 的关系。

因此 prompt GRB 通常要求

```tex
\Gamma \gtrsim 10^2,
```

具体下限依赖最高观测 photon energy、spectrum、variability timescale 和 emission radius 假设。

## 2. Baryon loading 与 dimensionless entropy

设 central engine 初始释放总能量 `E_0`，同时带出 baryonic mass `M_0`。定义 dimensionless entropy：

```tex
\eta \equiv \frac{E_0}{M_0 c^2}.
```

若能量最终主要转化为 bulk kinetic energy，且辐射损失暂时忽略，则 terminal Lorentz factor 量级为

```tex
\Gamma_\infty \sim \eta.
```

这给出 baryon loading 的核心限制：

- 若 `M_0` 太大，`η` 太小，outflow 无法达到 compactness problem 要求的 `Γ ≳ 100`。
- 若 `M_0` 太小，fireball 可能过早透明，能量转换和 prompt radiation efficiency 会改变。

因此 GRB fireball 需要“足够干净但不完全无 baryon”的 relativistic outflow。

## 3. Acceleration phase

在 radiation-dominated baryonic fireball 中，初始半径记为 `R_0`。在 optically thick acceleration phase，radiation pressure 推动 baryons 加速，常用量级关系为

```tex
\Gamma(R) \sim \frac{R}{R_0}, \quad R < R_s,
```

其中 saturation radius 为

```tex
R_s \sim \eta R_0.
```

在 `R < R_s` 时，internal energy 持续转化为 bulk kinetic energy；当 `Γ` 增长到 `η` 附近后，加速基本结束。

## 4. Coasting phase

在 saturation radius 之后，若尚未与外部介质显著相互作用，outflow 进入 coasting phase：

```tex
\Gamma(R) \sim \eta, \quad R > R_s.
```

此时 fireball 的大部分能量已是 baryonic kinetic energy。后续 prompt emission 模型会在这个 coasting outflow 中引入 internal dissipation，例如 internal shocks、magnetic reconnection 或 photospheric dissipation；afterglow 则来自更大半径处的 external shock。

## 5. Photosphere radius

Fireball 初期光深很大，photon 被困在 plasma 中。随着 expansion，Thomson optical depth 降低到约 1 的半径称为 photosphere radius `R_ph`。在 baryonic coasting outflow 的简单量级估计中，若 isotropic-equivalent luminosity 为 `L`，

```tex
R_{\rm ph} \sim \frac{L\sigma_T}{8\pi m_p c^3\Gamma^3}.
```

这里的数值系数依赖 outflow geometry、steady wind / shell 假设和 `Γ` 定义。重要的物理意义是：

- `R_ph` 内部 radiation 与 matter 耦合，可能产生 thermal / photospheric component。
- `R_ph` 外部光子可逃逸，非热 prompt emission 若发生在更大半径，可避免完全热化。
- `R_ph` 与 `R_s` 的相对大小决定 photospheric spectrum 和 acceleration history 是否能被观测到。

## 6. Deceleration radius

当 relativistic shell 扫过足够多外部介质后，bulk kinetic energy 开始显著转移给 shocked external medium，进入 afterglow external shock 阶段。

对 uniform ISM，外部 number density 为 `n`，初始 Lorentz factor 为 `Γ_0`，当 swept-up rest mass 满足

```tex
m_{\rm sw} \sim \frac{E}{\Gamma_0^2 c^2}
```

时开始显著 deceleration。由于

```tex
m_{\rm sw} \sim \frac{4\pi}{3}R^3 n m_p,
```

得到 deceleration radius：

```tex
R_{\rm dec,ISM} \sim \left(\frac{3E}{4\pi n m_p c^2\Gamma_0^2}\right)^{1/3}.
```

对应 observer-frame deceleration time 为

```tex
t_{\rm dec,ISM} \sim (1+z)\frac{R_{\rm dec,ISM}}{2c\Gamma_0^2}.
```

对 wind-like medium，密度常写作

```tex
\rho(R) = A R^{-2},
```

swept-up mass 量级为 `m_sw \sim 4π A R`，因此

```tex
R_{\rm dec,wind} \sim \frac{E}{4\pi A c^2\Gamma_0^2},
```

```tex
t_{\rm dec,wind} \sim (1+z)\frac{R_{\rm dec,wind}}{2c\Gamma_0^2}.
```

这些公式是把 prompt / coasting outflow 连接到 afterglow onset 的入口。

## 7. Thin shell 与 thick shell 图像

若 prompt engine duration 的 source-frame shell width 记为

```tex
\Delta \sim \frac{cT}{1+z},
```

则 shell crossing / deceleration behavior 可分成 thin shell 与 thick shell 两类。粗略地说：

- **thin shell**：shell duration 较短，afterglow peak 主要由 external deceleration time 决定。
- **thick shell**：shell duration 较长，reverse shock crossing 与 prompt duration 同量级，afterglow onset 更接近 central-engine activity duration。

本章暂不展开 reverse shock；后续 energy injection / refreshed shock 章节会回到 shell stratification 对光变曲线的影响。

## 8. 和事件页面的接口

- GRB 221009A：异常高 `E_iso` 和 early multiwavelength onset 需要明确 `E_iso` 是观测等效量，真正影响 external shock 的是 kinetic energy、`Γ_0`、外部密度和几何结构。
- GRB 080319B：Racusin et al. 使用 wind-like environment；因此 `R_dec` 和 `t_dec` 的介质依赖不能直接套用 ISM scaling。
- GRB 030329：radio calorimetry 约束 late kinetic energy；它和 prompt gamma-ray `E_iso` 之间隔着 radiative efficiency、beaming correction 和 component assignment。

## 9. 常见误区

- **把 `η`、`Γ_0`、shock Lorentz factor 混为一谈**：`η` 是初始能量 / baryon rest mass 比；`Γ_0` 是 coasting shell 初始 Lorentz factor；afterglow modeling 中的 `Γ(t)` 是 shocked flow 随时间演化的量。
- **把 fireball photosphere 当成所有 prompt emission 的唯一来源**：photosphere 是必然存在的透明面，但 prompt emission 可以包含 photospheric、internal shock、magnetic dissipation 等成分。
- **用 ISM deceleration formula 解释 wind-like source**：wind medium 的 `R_dec` 和 `t_dec` 标度不同。
- **把 `E_iso` 直接放入 true-energy dynamics**：动力学需要明确使用 isotropic-equivalent kinetic energy 还是 beaming-corrected true energy。
- **忽略 shell width / engine duration**：afterglow onset 不只由 `R_dec` 决定，也可能受 central-engine duration 和 reverse shock crossing 影响。

## 10. 和后续章节的接口

- External shock dynamics：从 `R_dec` 之后进入 Blandford-McKee self-similar evolution。
- Synchrotron spectrum：shocked electrons 和 magnetic field 给出 `ν_m`、`ν_c`、`F_{ν,max}`。
- Jet break：当 spherical-like deceleration 使 `Γ(t)` 降到 `θ_j^{-1}` 时，几何效应显现。
- Structured / two-component jet：不同 angular component 可有不同 `E(θ)`、`Γ_0(θ)`、`η(θ)` 和 deceleration time。

## 来源

- P. Mészáros, “The Fireball Model of Gamma-Ray Bursts,” Progress of Theoretical Physics Supplement 143, 33-50 (2001), arXiv:astro-ph/0010176。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
- Tsvi Piran, “The Physics of Gamma-Ray Bursts,” Reviews of Modern Physics 76, 1143-1210 (2004), arXiv:astro-ph/0405503。
- P. Mészáros and M. J. Rees, “Relativistic Fireballs and Their Impact on External Matter: Models for Cosmological Gamma-Ray Bursts,” ApJ 405, 278-284 (1993)。
- J. L. Racusin et al., “Broadband observations of the naked-eye gamma-ray burst GRB 080319B,” Nature 455, 183-188 (2008), arXiv:0805.1557, DOI: 10.1038/nature07270。
