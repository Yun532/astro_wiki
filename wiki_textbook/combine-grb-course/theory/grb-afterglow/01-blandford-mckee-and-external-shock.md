# 01 Blandford-McKee and External Shock Dynamics

状态：v0.1 课程讲义草案。本页是余晖动力学主线的第一课，按 `physical picture -> reference frame -> general expression -> detailed derivation block -> exact analytic status -> approximation hierarchy -> code convention` 组织。目标是从 external shock 的能量守恒、swept-up mass、shock jump conditions 和 observer-time mapping 推到 Blandford-McKee 标度，为后续 synchrotron breaks、closure relations、reverse shock、structured jet 和 EATS 建立共同动力学底座。

## 1. 物理图像

GRB prompt 阶段之后，relativistic ejecta 继续向外传播并扫过 circumburst medium。外部介质被 forward shock 加热，ejecta 本身可能被 reverse shock 穿过。标准 forward-shock afterglow 的核心链条是：

```text
relativistic ejecta with kinetic energy
  -> swept-up external mass
  -> forward shock jump conditions
  -> adiabatic Blandford-McKee blast wave
  -> Gamma(t), R(t), e'(t), n'(t)
  -> synchrotron / SSC / opacity modules
  -> observed multi-band afterglow
```

本页只处理动力学和局域 shock 后物理量，不推导 \(\nu_m\)、\(\nu_c\)、\(F_{\nu,\max}\) 和 closure relations；这些放到下一页。

## 2. 参考系与变量表

默认使用 burster / lab frame 描述半径 \(R\)、observer time \(t_{\rm obs}\)、外部介质密度 \(\rho_{\rm ext}\)。带撇号的量为 shocked fluid comoving frame 中的量。当前页默认 on-axis、spherical-equivalent、adiabatic、ultra-relativistic forward shock。

| 符号 | 含义 | 单位或量纲 |
| --- | --- | --- |
| \(E\) | blast-wave kinetic energy，通常为 isotropic-equivalent | erg |
| \(R\) | shock / emitting radius | cm |
| \(\Gamma\) | shocked fluid bulk Lorentz factor | dimensionless |
| \(\Gamma_{\rm sh}\) | shock front Lorentz factor | dimensionless |
| \(\Gamma_0\) | initial coasting Lorentz factor | dimensionless |
| \(\rho_{\rm ext}(R)\) | external mass density | g cm\(^{-3}\) |
| \(n_{\rm ext}(R)\) | external number density | cm\(^{-3}\) |
| \(A\) | power-law density normalization in \(\rho=A R^{-k}\) | g cm\(^{k-3}\) |
| \(k\) | external density index | dimensionless |
| \(m_{\rm sw}\) | swept-up mass | g |
| \(e'\) | shocked comoving internal energy density | erg cm\(^{-3}\) |
| \(n'\) | shocked comoving number density | cm\(^{-3}\) |
| \(z\) | redshift | dimensionless |

两种常用介质：

| 介质 | \(k\) | 密度 |
| --- | --- | --- |
| uniform ISM | 0 | \(\rho_{\rm ext}=n m_p\) |
| stellar wind | 2 | \(\rho_{\rm ext}=A R^{-2}\), \(A=5\times10^{11}A_\ast\ {\rm g\,cm^{-1}}\) |

## 3. General Expression

### 3.1 Power-law external medium

把外部介质写成统一形式：

$$
\rho_{\rm ext}(R)
=
A R^{-k},
\qquad
0\le k<3.
$$

Formula ID：`AG-DYN-RHO-K-001`。

swept-up mass 是：

$$
m_{\rm sw}(R)
=
\int_0^R 4\pi r^2\rho_{\rm ext}(r)\,dr.
$$

Formula ID：`AG-DYN-MSW-001`。

### 3.2 Adiabatic blast-wave energy

在 ultra-relativistic adiabatic phase，blast wave energy 的标度是：

$$
E
\sim
\Gamma^2 m_{\rm sw}c^2.
$$

更精细的 Blandford-McKee self-similar solution 会给出与 \(k\)、shock-front Lorentz factor、fluid Lorentz factor 有关的 order-unity 系数。本页先推标度，再在代码约定中说明数值归一化。

### 3.3 Observer-time mapping

on-axis observer 的 arrival time 量级为：

$$
t_{\rm obs}
\sim
(1+z)\frac{R}{C_t c\Gamma^2},
$$

其中 \(C_t\) 是 convention factor，常见取值为 2、4 或含 \(4-k\) 的 BM 系数。差异来自是否使用 shock front Lorentz factor、shocked-fluid Lorentz factor，以及是否已代入 self-similar equal-arrival-time structure。

Formula ID：`AG-KIN-TOBS-001`。

### 3.4 Shock jump conditions

对 cold external medium 的 ultra-relativistic strong shock，shocked fluid 中：

$$
n'
\simeq
4\Gamma n_{\rm ext},
\qquad
e'
\simeq
4\Gamma^2 n_{\rm ext}m_pc^2.
$$

它们是辐射模块的入口：

$$
\frac{B'^2}{8\pi}
=
\epsilon_B e',
$$

随后才能定义 electron injection Lorentz factor、cooling Lorentz factor 和 synchrotron break frequencies。

## 4. Detailed Derivation I：Observer-Time Mapping

### 4.1 目标公式

目标不是把 \(C_t\) 固定成唯一数字，而是推出为什么 relativistic afterglow 的观测时间总会带有 \(R/(c\Gamma^2)\) 压缩：

$$
t_{\rm obs}
\simeq
(1+z)\left[t_{\rm lab}-{R\cos\theta\over c}\right],
$$

并在 on-axis、small-angle、ultra-relativistic limit 下化为

$$
t_{\rm obs}
\sim
(1+z){R\over C_t c\Gamma^2}.
$$

### 4.2 Photon arrival-time difference

设 shock / emitting element 在 lab frame 中从中心出发，到半径 \(R\) 时发出光子。远处观测者只关心相对于中心同时出发的参考光子的到达时间差。若 emitting element 与视线夹角为 \(\theta\)，几何路径差给出：

$$
t_{\rm obs}
=
(1+z)\left(t_{\rm lab}-{R\cos\theta\over c}\right).
$$

对沿视线运动的 material，\(dR/dt_{\rm lab}=\beta c\)，所以 \(t_{\rm lab}\simeq R/(\beta c)\)。代入：

$$
t_{\rm obs}
\simeq
{1+z\over c}R\left({1\over\beta}-\cos\theta\right).
$$

当 \(\theta=0\) 时：

$$
t_{\rm obs}
\simeq
{1+z\over c}R\left({1\over\beta}-1\right)
=
{1+z\over c}R{1-\beta\over\beta}.
$$

ultra-relativistic limit 中：

$$
\beta
=
\sqrt{1-\Gamma^{-2}}
\simeq
1-{1\over2\Gamma^2},
\qquad
1-\beta
\simeq
{1\over2\Gamma^2}.
$$

因此最简单的 coasting shell 几何给出：

$$
t_{\rm obs}
\simeq
(1+z){R\over2c\Gamma^2}.
$$

这说明 \(R/c\) 的 lab-frame 时间被 photon chasing effect 压缩了 \(\sim\Gamma^{-2}\)。

### 4.3 为什么代码常用 factor 4

上式的 factor 2 来自最简 coasting point-source geometry。实际 afterglow 文献中常见 factor 4 或含 \(4-k\) 的系数，来源包括：

- \(\Gamma\) 取 shocked-fluid Lorentz factor，而不是 shock-front Lorentz factor。
- blast wave 在 \(R\) 变化时已经 decelerate，不能简单取 \(t_{\rm lab}=R/(\beta c)\) 的常数 \(\Gamma\) 形式。
- equal-arrival-time surface 上不同 \(\theta\) 的贡献会改变特征 emission time 的代表系数。
- BM self-similar solution 的 energy normalization 和 arrival-time convention 一起进入数值前因子。

因此本课程把

$$
t_{\rm obs}
\sim
(1+z){R\over C_t c\Gamma^2}
$$

作为 general convention form；本地代码 `bm_radius()` 默认 `arrival_factor=4`，属于 literature-scale convention，不是从代码反向规定理论唯一系数。

Formula ID：`FS-DYN-R-001`。

## 5. Detailed Derivation II：Swept-Up Mass and Deceleration

### 5.1 目标公式

目标是推出 general-\(k\) swept-up mass：

$$
m_{\rm sw}(R)
=
\frac{4\pi A}{3-k}R^{3-k},
$$

以及 deceleration condition：

$$
m_{\rm sw}(R_{\rm dec})
\sim
\frac{E}{\Gamma_0^2c^2}.
$$

### 5.2 Swept-up mass

代入 \(\rho_{\rm ext}=A R^{-k}\)：

$$
m_{\rm sw}(R)
=
\int_0^R4\pi r^2 A r^{-k}dr
=
4\pi A
\int_0^R r^{2-k}dr.
$$

只要 \(k<3\)，积分为：

$$
\int_0^R r^{2-k}dr
=
\frac{R^{3-k}}{3-k}.
$$

所以：

$$
m_{\rm sw}(R)
=
\frac{4\pi A}{3-k}R^{3-k}.
$$

对 ISM，\(k=0\)、\(A=nm_p\)：

$$
m_{\rm sw}
=
\frac{4\pi}{3}R^3nm_p.
$$

Formula ID：`FS-DYN-ISM-001`。

对 wind，\(k=2\)：

$$
m_{\rm sw}
=
4\pi A R.
$$

### 5.3 Deceleration condition

初始 coasting phase 中 \(\Gamma\simeq\Gamma_0\)。被扫入的外部 baryon 在 shocked region 中获得的能量量级为 \(\Gamma_0^2 m_{\rm sw}c^2\)：一个 \(\Gamma_0\) 来自 bulk kinetic energy，另一个 \(\Gamma_0\) 来自 shock heating / lab-frame energy boost 的量级。

当 swept-up material 的能量达到 ejecta kinetic energy 的显著份额时，shell 开始减速：

$$
\Gamma_0^2m_{\rm sw}c^2
\sim
E.
$$

因此：

$$
m_{\rm sw}(R_{\rm dec})
\sim
\frac{E}{\Gamma_0^2c^2}.
$$

ISM deceleration radius：

$$
R_{\rm dec,ISM}
\sim
\left(
\frac{3E}{4\pi nm_pc^2\Gamma_0^2}
\right)^{1/3}.
$$

wind deceleration radius：

$$
R_{\rm dec,wind}
\sim
\frac{E}{4\pi A c^2\Gamma_0^2}.
$$

observer-frame deceleration time follows from the same arrival-time mapping:

$$
t_{\rm dec}
\sim
(1+z)\frac{R_{\rm dec}}{C_t c\Gamma_0^2}.
$$

Formula ID：`AG-DYN-DECN-001`。

## 6. Detailed Derivation III：BM Scaling for General \(k\)

### 6.1 目标公式

目标是从 adiabatic energy conservation 推到：

$$
\Gamma(R)
\propto
R^{-(3-k)/2},
$$

以及：

$$
R(t_{\rm obs})
\propto
\left(\frac{t_{\rm obs}}{1+z}\right)^{1/(4-k)},
\qquad
\Gamma(t_{\rm obs})
\propto
\left(\frac{t_{\rm obs}}{1+z}\right)^{-(3-k)/[2(4-k)]}.
$$

### 6.2 Energy conservation

BM self-similar phase 中，初始 ejecta 的细节被逐渐遗忘，blast wave 的 energy 近似守恒。标度关系为：

$$
E
\sim
\Gamma^2m_{\rm sw}c^2.
$$

代入 swept-up mass：

$$
E
\sim
\Gamma^2
\frac{4\pi A}{3-k}
R^{3-k}c^2.
$$

把常数吸收到 \(\xi_k\)：

$$
E
=
\xi_k A c^2\Gamma^2R^{3-k}.
$$

于是：

$$
\Gamma^2
\propto
\frac{E}{A c^2}R^{-(3-k)}.
$$

开平方：

$$
\Gamma(R)
\propto
\left(\frac{E}{A}\right)^{1/2}
R^{-(3-k)/2}.
$$

### 6.3 Observer-time substitution

arrival-time relation：

$$
t_{\rm obs}
\sim
(1+z)\frac{R}{C_t c\Gamma^2}.
$$

由 energy relation：

$$
\Gamma^{-2}
\propto
\frac{A c^2}{E}R^{3-k}.
$$

代入：

$$
t_{\rm obs}
\propto
(1+z)R
\left(
\frac{A}{E}R^{3-k}
\right).
$$

因此：

$$
t_{\rm obs}
\propto
(1+z)\frac{A}{E}R^{4-k}.
$$

反解：

$$
R(t_{\rm obs})
\propto
\left[
\frac{E}{A}
\frac{t_{\rm obs}}{1+z}
\right]^{1/(4-k)}.
$$

再代回 \(\Gamma(R)\)：

$$
\Gamma(t_{\rm obs})
\propto
\left(\frac{E}{A}\right)^{1/[2(4-k)]}
\left(\frac{t_{\rm obs}}{1+z}\right)^{-(3-k)/[2(4-k)]}.
$$

这条推导是 closure relations 的动力学底座。

Formula ID：`AG-DYN-BM-ENERGY-001`。

## 7. ISM and Wind Limits

### 7.1 Uniform ISM

对于 \(k=0\)：

$$
R
\propto
t_{\rm obs}^{1/4},
\qquad
\Gamma
\propto
t_{\rm obs}^{-3/8}.
$$

常用 literature-scale 归一化写成：

$$
\Gamma_{\rm ISM}(t)
\sim
6
\left(\frac{E_{\rm iso,52}}{n_0}\right)^{1/8}
\left(\frac{t_{\rm obs}}{1\,{\rm day}}\right)^{-3/8}
(1+z)^{3/8}.
$$

代码中的 `bm_lorentz_factor(..., medium="ism")` 采用同类 Sari et al. 1998 归一化，系数为 literature-scale convention，不是 hydrodynamic solver。

Formula ID：`FS-DYN-BM-ISM-001`。

### 7.2 Stellar wind

对于 \(k=2\)：

$$
R
\propto
t_{\rm obs}^{1/2},
\qquad
\Gamma
\propto
t_{\rm obs}^{-1/4}.
$$

wind density convention：

$$
\rho
=
AR^{-2},
\qquad
A
=
5\times10^{11}A_\ast\ {\rm g\,cm^{-1}}.
$$

number density：

$$
n(R)
=
\frac{A}{m_pR^2}.
$$

代码中的 `bm_lorentz_factor(..., medium="wind")` 采用 Chevalier-Li / standard afterglow convention 的 literature-scale normalization。

Formula IDs：`FS-DYN-WIND-001`、`FS-DYN-WIND-002`、`FS-DYN-BM-WIND-001`。

## 8. Detailed Derivation IV：Shock Jump Conditions to Radiation Inputs

### 8.1 Shock compression

对 cold upstream medium 和 ultra-relativistic strong shock，shock jump conditions 给出 shocked comoving number density：

$$
n'
\simeq
4\Gamma n_{\rm ext}.
$$

这里 \(\Gamma\) 是 shocked fluid 相对 upstream lab frame 的 Lorentz factor。若文献使用 shock-front Lorentz factor \(\Gamma_{\rm sh}\)，数值系数会改变；这属于 convention 差异。

### 8.2 Internal energy density

每个 upstream proton 在 downstream comoving frame 中获得的 internal energy 量级为 \(\Gamma m_pc^2\)，而 downstream comoving number density 又被压缩为 \(4\Gamma n_{\rm ext}\)。因此：

$$
e'
\simeq
(4\Gamma n_{\rm ext})(\Gamma m_pc^2)
=
4\Gamma^2 n_{\rm ext}m_pc^2.
$$

代码：

```text
shocked_internal_energy_density(gamma, number_density_cm3)
```

Formula ID：`FS-DYN-JUMP-001`。

### 8.3 Magnetic field parameterization

afterglow 模型通常把 shock 后一部分 internal energy 放入 magnetic field：

$$
\frac{B'^2}{8\pi}
=
\epsilon_B e'.
$$

因此：

$$
B'
=
\sqrt{8\pi\epsilon_Be'}.
$$

这个式子是 phenomenological microphysics parameterization，不是从 first-principles plasma instability 解出来的磁场演化。

代码：

```text
post_shock_magnetic_field(energy_density_erg_cm3, epsilon_b)
```

Formula ID：`SYN-B-001`。

## 9. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| swept-up mass for \(k<3\) | 闭式 | \(m_{\rm sw}=4\pi A R^{3-k}/(3-k)\) |
| deceleration radius | 闭式量级 | depends on \(\Gamma_0\), \(E\), density convention |
| BM self-similar solution | 有解析 self-similar 解 | exact under ultra-relativistic, adiabatic, spherical, power-law density assumptions |
| \(\Gamma(t)\), \(R(t)\) scaling | 闭式幂律 | coefficient convention depends on Lorentz-factor and arrival-time definitions |
| shock jump conditions | 闭式 ideal limit | cold upstream, strong relativistic shock |
| radiative blast wave | 一般需 energy evolution | \(E(t)\) no longer constant |
| jet break / structured jet / EATS | 一般无短闭式通用解 | requires angular structure and equal-arrival-time integration |
| non-relativistic transition | BM invalid | switch to trans-relativistic / Sedov-Taylor-like dynamics |

因此，本页的 BM 幂律是强大的课程底座，但不是完整 afterglow hydrodynamics。

## 10. Approximation Hierarchy

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| coasting estimate | \(\Gamma=\Gamma_0\), \(R\simeq2c\Gamma_0^2t/(1+z)\) | afterglow onset scale | deceleration dynamics |
| BM scaling | \(E\simeq{\rm const}\), \(\rho=A R^{-k}\) | \(\Gamma(t)\), \(R(t)\) power laws | radiative losses, jet geometry |
| literature normalization | Sari / Chevalier-Li coefficients | practical sanity estimates | convention-dependent factors |
| semi-analytic light curve | BM + synchrotron breaks + closure relations | broadband trends | full EATS, angular hydrodynamics |
| hydrodynamic / structured-jet solver | numerical dynamics + EATS | geometry and transition effects | code/model dependence |

## 11. 从推导到代码的实现约定

当前本地代码是 convention-explicit sanity layer，不是 hydrodynamic solver。

| 层级 | 内容 | 代码 | 边界 |
| --- | --- | --- | --- |
| dynamics helper | ISM/wind density, BM \(\Gamma(t)\), \(R(t)\), \(e'\), \(B'\) | `reproduce/grb/core/dynamics/blastwave.py` | literature-scale candidate |
| model composition | build forward-shock state and synchrotron breaks | `reproduce/grb/models/forward_shock/model.py` | sanity / event-trend |
| source-adapter local zone | map BM state into source-agnostic radiation screening inputs | `reproduce/grb/models/forward_shock/local_zone.py` | literature-scale candidate / source-adapter smoke |
| closure helpers | \(\alpha,\beta,p\) relations | `reproduce/grb/models/forward_shock/analytic_scalings.py` | pre-jet, adiabatic, optically thin |
| EATS toy | angular delay and Doppler weighting | `core/dynamics/equal_arrival.py` | not full light-curve integral |
| external benchmark | `afterglowpy`, `VegasAfterglow` adapters | `validation_lab/benchmark_adapters` | benchmark-output only |

代码约定：

- `bm_lorentz_factor()` 输入 observer time in seconds，energy in erg。
- `medium="ism"` 使用 density in cm\(^{-3}\)。
- `medium="wind"` 使用 \(A_\ast\) convention。
- `bm_radius()` 使用 \(R={\rm factor}\,ct_{\rm obs}\Gamma^2/(1+z)\)，默认 `arrival_factor=4`。
- 旧 snapshot `wiki-textbook-snapshot/04-external-shock动力学.md` 只作为迁移来源；当前 dynamics 和 EATS 代码文档已逐步迁到 `theory/grb-afterglow/01-blandford-mckee-and-external-shock.md` 与 `theory/grb-afterglow/04-jet-break-structured-jet-and-eats.md`。

### 11.1 BM state 到 radiation local-zone adapter

第一版 GRB source adapter 是：

```text
reproduce/grb/models/forward_shock/local_zone.py
```

Formula ID：`AG-FS-LOCAL-ZONE-001`。

代码函数：

- `forward_shock_local_zone_state(time_s, params, ...)`
- `forward_shock_local_zone_series(time_grid_s, params, ...)`
- `forward_shock_radiation_screening_summary(time_grid_s, params, ...)`

它不新增 BM 或 synchrotron 公式，而是把本页的 \(R(t)\)、\(\Gamma(t)\)、\(e'(t)\) 和 `SYN-B-001` 的 \(B'\) 映射成 source-agnostic radiation workbench 的局域输入：

$$
R'_{\rm screen}
=
f_R{R\over\Gamma},
\qquad
U'_{\rm ph}
=
f_{\rm ph}e'.
$$

其中 `comoving_size_factor = f_R`，`photon_energy_density_fraction = f_ph`。单位约定为：`time_s` in seconds；`radius_cm` / `local_size_cm` in cm；`magnetic_field_gauss` in gauss；`internal_energy_density_erg_cm3` 与 `photon_energy_density_erg_cm3` in erg cm\(^{-3}\)；radiation workbench 输出的 screening energies in eV，cooling / escape times in seconds。

课程差异必须写清：\(R/\Gamma\) 是 local screening size convention，不是唯一几何厚度；\(U'_{\rm ph}=f_{\rm ph}e'\) 是 caller-controlled envelope，不是 self-consistent SSC photon transfer。当前验证只检查 ISM/wind BM 幂律能否按预期传递到 \(B'\)、\(R'\)、\(U'_{\rm ph}\) 和 Hillas screening，不是观测光变拟合。

验证入口：

```powershell
python -m reproduce.grb.validation_lab.check_forward_shock_local_zone_v1
```

输出：

- `reproduce/grb/validation_lab/outputs/tables/forward_shock_local_zone_v1_summary.csv`
- `reproduce/grb/validation_lab/outputs/tables/forward_shock_local_zone_v1_checks.csv`
- `reproduce/grb/validation_lab/outputs/figures/forward_shock_local_zone_v1.png`

### 11.2 Cooling / acceleration time-series screening

在同一 provenance 之上，代码还提供：

```text
forward_shock_cooling_acceleration_timeseries(time_grid_s, params, ...)
```

Formula ID：`AG-FS-COOL-ACC-SCREEN-001`。

该函数沿用 \(R'_{\rm screen}=f_RR/\Gamma\)、\(U'_{\rm ph}=f_{\rm ph}e'\) 和 \(B'^2/8\pi=\epsilon_Be'\)，再把固定 probe Lorentz factors 的 cooling、Bohm-like acceleration、escape 和 Hillas screening 写成随 observer time 的表。单位为：`time_grid_s` in seconds；`electron_gamma_probe` / `proton_gamma_probe` dimensionless；cooling / acceleration / escape times in seconds；Hillas energies in eV。

验证入口：

```powershell
python -m reproduce.grb.validation_lab.check_forward_shock_cooling_acceleration_v1
```

它检查 ISM/wind 中 \(t_{\rm syn}\)、\(t_{\rm IC}\)、\(t_{\rm acc}\)、\(t_{\rm esc}\)、\(\gamma_{\rm syn}\) 和 Hillas energy 的 BM log-time slopes。它仍然不是 electron continuity solver、shock acceleration solver、EATS-integrated light curve 或事件拟合。

常见差异来源：

- \(\Gamma\) 是 shock-front Lorentz factor 还是 shocked-fluid Lorentz factor。
- arrival-time coefficient 取 2、4 或 BM self-similar 系数。
- \(E\) 是 isotropic-equivalent kinetic energy 还是 beaming-corrected true energy。
- wind \(A_\ast\) convention 和 composition。
- 是否包含 radiative loss、energy injection、jet break 或 density variation。

## 12. Benchmark Boundary

`afterglowpy`、`VegasAfterglow`、BOXFIT 类工具可用于 mature-method / benchmark-output 对照，但不能反向定义本页课程公式。benchmark 只回答同参数、同 geometry convention 下趋势是否一致；它不能证明某个 GRB 事件的唯一模型。

本地当前可以声称：

- BM \(\Gamma(t)\) 在 ISM/wind 中按预期单调下降。
- \(R(t)\)、\(e'\)、\(B'\) 能作为 forward-shock sanity model 的输入。
- EATS 当前只是 toy geometry helper。

不能声称：

- 已完成 full relativistic hydrodynamics。
- 已完成 self-consistent jet spreading。
- 已完成 structured-jet EATS light-curve integral。
- 已完成 paper-level afterglow fit。

## 13. Interfaces to Later Pages

后续课程页将从本页取用：

- \(e'(t)\) 和 \(B'(t)\)：进入 synchrotron \(\nu_m\)、\(\nu_c\)、\(F_{\nu,\max}\)。
- \(R(t)\) 和 \(\Gamma(t)\)：进入 observer time、EATS、jet-break condition。
- ISM/wind/general-\(k\) 标度：进入 closure relations。
- \(m_{\rm sw}\) 和 \(R_{\rm dec}\)：进入 reverse shock / early optical flash。
- BM invalid boundaries：进入 jet break、energy injection、non-relativistic transition。

## 14. 不声称

- 不声称 BM scaling 是所有 afterglow 阶段的完整解。
- 不把 coasting、deceleration、BM self-similar、jet break 和 Newtonian phase 混成一条单一幂律。
- 不把 ISM closure relation 套到 wind，或反过来。
- 不把 benchmark-output 写成事件结论。
- 不把 GRB 221009A、GRB 080319B、GRB 030329 的某个模型解释写成唯一答案。

## 15. 参考来源

- Blandford & McKee 1976, *Fluid dynamics of relativistic blast waves*.
- Sari, Piran & Narayan 1998, *Spectra and Light Curves of Gamma-Ray Burst Afterglows*.
- Chevalier & Li 2000, *Wind Interaction Models for Gamma-Ray Burst Afterglows*.
- Piran 2004, *The Physics of Gamma-Ray Bursts*.
- Zhang 2014, *The Physics of Gamma-Ray Bursts & Relativistic Jets*.
- Granot & Sari 2002, *The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows*.
- Salafia & Ghirlanda 2022, structured jet review.
