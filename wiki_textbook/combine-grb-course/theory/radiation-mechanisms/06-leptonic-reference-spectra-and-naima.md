# 06 Leptonic Reference Spectra and Open Benchmarks

状态：v2 reference-spectra / benchmark-output。目标是把基础辐射理论接到一组可计算的本地 SED，并用同一组参数与多个公开实现做谱和比值对照。

本页不处理 GRB 221009A 事件解释，不做 MCMC，不声称本地模型已经成为 calibrated physical flux solver。

## 1. 从 `j_nu` 到观测 SED

辐射转移页定义了 emission coefficient `j_nu`，单位通常是：

```text
j_nu: erg s^-1 cm^-3 Hz^-1 sr^-1.
```

若发射各向同性，体发射率为：

```text
epsilon_nu = 4 pi j_nu.
```

对体积积分：

```text
L_nu = integral epsilon_nu dV.
```

若使用总粒子数谱 `dN/dE`，而不是体密度谱 `dn/dE`，体积积分已被吸收到 `dN/dE` 中：

```text
L_nu = integral dE_e (dN_e/dE_e) P_nu(E_e).
```

距离为 `d` 时：

```text
F_nu = L_nu / (4 pi d^2).
```

SED 写成：

```text
nu F_nu = E_gamma F_E.
```

本地与外部 SED API 对照时统一输出：

```text
SED: erg cm^-2 s^-1.
```

Formula ID：`RT-LNU-FNU-SED-001`。

## 2. 粒子分布 convention

本地 benchmark 使用 total electron distribution：

```text
dN/dE = A (E/E0)^(-alpha) exp(-E/Ecut).
```

这里：

- `A` 单位是 particles eV^-1。
- `E`、`E0`、`Ecut` 使用 eV。
- 这不是 `cm^-3 eV^-1` 的体密度谱。

代码：

```text
CutoffPowerLawElectrons.dnde_per_ev()
```

Formula ID：`LEP-ELECTRON-CUTOFF-PL-001`。

电子 Lorentz factor：

```text
gamma = E_e / (m_e c^2).
```

代码：

```text
electron_gamma_from_energy_ev()
```

Formula ID：`LEP-GAMMA-FROM-ENERGY-001`。

## 3. Synchrotron SED

单电子谱功率：

```text
P_nu(E_e) =
  sqrt(3) e^3 B sin(alpha_pitch) / (m_e c^2)
  F(nu / nu_c).
```

其中：

```text
nu_c = 3 e B sin(alpha_pitch) gamma^2 / (4 pi m_e c),
F(x) = x integral_x^infinity K_{5/3}(xi) dxi.
```

若用总电子谱：

```text
L_nu = integral dE_e (dN_e/dE_e) P_nu(E_e).
```

观测 SED：

```text
nu F_nu =
  nu / (4 pi d^2)
  integral dE_e (dN_e/dE_e) P_nu(E_e).
```

代码：

```text
synchrotron_single_electron_pnu_cgs()
synchrotron_sed_erg_cm2_s()
```

Formula ID：`LEP-SYN-PNU-001`、`LEP-SYN-SED-001`。

重要 caveat：课程 reference 默认 `sin(alpha_pitch)=1`。部分外部软件会使用 random magnetic field approximation、pitch-angle average 或自己的近似 kernel。为了让 benchmark 不混入 convention 差异，本地现在分成两层：

```text
synchrotron_sed_erg_cm2_s()
  课程/教材 reference：固定 pitch angle，使用 F(x)=x integral K_5/3。

synchrotron_sed_<package>_compatible_erg_cm2_s()
  package-compatible benchmark：复刻某个外部软件的 kernel、默认网格和单位 convention。
```

benchmark CSV 中必须区分 package-compatible 输出和课程 reference 输出。`teaching_reference_sed_erg_cm2_s` 保留课程核结果，用来显示教材 convention 与外部软件 convention 的差异。

## 4. Synchrotron cooling

磁场能量密度：

```text
U_B = B^2 / (8 pi).
```

单电子 synchrotron cooling power：

```text
P_syn = (4/3) sigma_T c gamma^2 U_B.
```

冷却时间：

```text
t_cool = gamma m_e c^2 / P_syn.
```

所以：

```text
t_syn proportional gamma^-1 B^-2.
```

代码：

```text
synchrotron_cooling_power_erg_s()
radiative_cooling_time_s()
```

Formula ID：`LEP-SYN-COOL-POWER-001`、`LEP-COOL-TIME-001`。

## 5. IC delta approximation SED

完整 IC 需要对 electron distribution、seed photon distribution、角度和 Klein-Nishina kernel 积分。本地第一版只做 Thomson delta approximation。

设 seed photon characteristic energy 为 `epsilon_seed`，energy density 为 `U_ph`：

```text
E_gamma = a gamma^2 epsilon_seed,
a = 4/3.
```

IC cooling power：

```text
P_IC = (4/3) sigma_T c gamma^2 U_ph.
```

delta approximation：

```text
L_E(E_gamma)
  = integral dE_e N(E_e) P_IC(E_e)
    delta[E_gamma - a gamma(E_e)^2 epsilon_seed].
```

利用 delta function：

```text
L_E ~= N(E_e*) P_IC(E_e*) /
       |dE_gamma/dE_e|_{E_e*}.
```

其中：

```text
gamma* = sqrt(E_gamma / [a epsilon_seed]),
dE_gamma/dE_e = 2 a epsilon_seed gamma / (m_e c^2).
```

SED：

```text
E_gamma F_E = E_gamma L_E / (4 pi d^2).
```

代码：

```text
inverse_compton_delta_sed_erg_cm2_s()
ic_thomson_cooling_power_erg_s()
```

Formula ID：`LEP-IC-DELTA-SED-001`、`LEP-IC-COOL-POWER-001`。

外部 IC 实现可能使用完整 Blumenthal-Gould kernel、Khangulyan/Aharonian/Kelner blackbody approximation、delta approximation 或各向异性 scattering kernel。为了让 benchmark 不再把不同近似硬比，本地现在也分成两层：

```text
inverse_compton_delta_sed_erg_cm2_s()
  课程/教材 reference：Thomson delta approximation。

inverse_compton_<package>_compatible_sed()
  package-compatible benchmark：复刻对应外部软件的 seed photon convention、kernel、默认 gamma-grid 和积分规则。
```

benchmark CSV 中必须区分 package-compatible 输出和课程 reference 输出。`teaching_reference_sed_erg_cm2_s` 保留 delta approximation 结果，用来检查快速解析近似和更完整近似核的差异。

## 6. CMB seed convention

本地 CMB energy density：

```text
U_CMB = a_rad T^4 = 4 sigma_SB T^4 / c.
```

characteristic photon energy：

```text
epsilon_CMB ~= 2.7 k_B T.
```

代码：

```text
cmb_energy_density_erg_cm3()
cmb_characteristic_photon_energy_erg()
```

Formula ID：`LEP-CMB-U-001`、`LEP-CMB-EPS-001`。

## 7. Nonthermal bremsstrahlung SED

完整 nonthermal bremsstrahlung 需要微分截面：

```text
dL/dE_gamma =
  n_target c integral_{E_gamma}^infinity
  dE_e (dN_e/dE_e) E_gamma (d sigma / dE_gamma).
```

本地第一版使用简化截面：

```text
d sigma / dE_gamma ~= sigma0 / E_gamma.
```

于是只保留趋势：

```text
E_gamma L_E proportional
  n_target c sigma0 integral_{E_gamma}^infinity (dN_e/dE_e) dE_e.
```

代码：

```text
nonthermal_bremsstrahlung_sed_erg_cm2_s()
```

Formula ID：`LEP-BREM-NONTHERMAL-SED-001`。

注意：这不是 thermal free-free，也不是 calibrated bremsstrahlung kernel。外部 bremsstrahlung 实现只能用作 benchmark-output；本地结果只能比较趋势和有限域 ratio，直到我们实现同级别微分截面。

## 8. same-parameter benchmark

当前第一个 adapter 使用同一组参数：

```text
ExponentialCutoffPowerLaw:
  amplitude = 1e36 / eV
  e0 = 1 TeV
  alpha = 2.2
  e_cutoff = 100 TeV

B = 1e-4 G
n_target = 1 cm^-3
distance = 1 kpc
IC seed = CMB
```

输出：

```text
benchmark_naima_local_lepton_sed_ratio.csv
benchmark_naima_local_lepton_ratio_summary.csv
benchmark_naima_local_lepton_sed_ratio.png
```

Formula ID：

```text
LEP-NAIMA-SYN-BENCHMARK-001
LEP-NAIMA-IC-BENCHMARK-001
LEP-NAIMA-COMPAT-SYN-001
LEP-NAIMA-COMPAT-IC-001
LEP-NAIMA-BREM-BENCHMARK-001
```

## 9. 验证边界

- `benchmark-output` 不是本地 API 依赖。
- Synchrotron 和 IC benchmark 的正式 ratio 可以使用 package-compatible kernel，目标是在同参数、同 convention 下数值一致。
- 课程 reference 核仍保留在 `teaching_reference_sed_erg_cm2_s`，它允许和外部软件有差异，因为它回答的是“教材公式怎么计算”，不是“某个外部软件内部近似怎么复刻”。
- bremsstrahlung v3 已新增 `naima_compat.py::nonthermal_bremsstrahlung_sed_naima_compatible_erg_cm2_s()`，使用 Baring et al. 1999 截面与 naima 默认 ionized ISM 权重；legacy simplified helper 仍保留为 order-of-magnitude。
- `PionDecay` v3 通过 `hadronic.py::pp_kafexhiu_lut_pion_decay_sed_erg_cm2_s()` 进入 package-compatible parity；它只复刻 pp Kafexhiu14 LUT，不代表完整 hadronic cascade。
- 不声称 GRB 221009A 事件拟合或观测 SED 复现。

## 10. 课程推导和代码不一致时怎么记录

如果某个代码路径和课程页中的主推导公式不同，必须同时写清四件事：

1. 课程推导使用哪一个公式或 kernel。
2. 代码实际使用哪一个 kernel、近似或外部软件 convention。
3. 差异来自哪里：pitch-angle average、random-field approximation、seed photon convention、delta approximation、积分网格、单位换算或数值加速。
4. 哪个输出列用于哪种目的。

当前同步和 IC 的对应关系是：

| 机制 | 课程 reference | package-compatible benchmark | CSV 列 |
| --- | --- | --- | --- |
| synchrotron | fixed pitch-angle \(F(x)=x\int K_{5/3}d\xi\) | 外部软件的 angle/random-field convention | `teaching_reference_sed_erg_cm2_s` vs package-compatible output |
| inverse Compton | Thomson delta approximation / Thomson kernel 推导 | 外部软件的 IC kernel / seed convention | `teaching_reference_sed_erg_cm2_s` vs package-compatible output |

因此，“和某个外部软件一样”只指 package-compatible benchmark 层；“和课程推导对应”指 teaching/reference 层。两者都保留，不能互相冒充。
