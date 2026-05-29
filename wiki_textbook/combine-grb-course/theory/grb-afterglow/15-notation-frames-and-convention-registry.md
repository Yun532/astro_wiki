# 15 符号、参考系与约定注册表

状态：v0.1 章节收口页。本页不是新的物理机制，而是为 01-14 页统一符号、参考系、单位和实现约定。后续理论页、代码 helper、事件报告和 agent 审稿都应优先对照本页，避免同一个符号在不同页面中悄悄换义。

核心原则：约定差异不是小事。GRB afterglow 中常见的 factor 2、factor 4、\((4-k)\)、Doppler factor、redshift、per energy / per log energy、\(E_{\rm iso}\) / true energy、comoving / observer frame 差异，足以改变归一化、break time、光深和能量预算。课程可以保留不同文献约定，但必须把差异写清。

## 1. 参考系总览

本课程默认区分四个层级：

| 参考系 | 标记 | 常用对象 | 说明 |
| --- | --- | --- | --- |
| lab / burster frame | 无 prime，常写 \(t_{\rm lab},R\) | blast-wave radius, swept-up mass | 中心源静止系或宿主系近似 |
| shocked-fluid comoving frame | prime \( '\) | \(B'\), \(e'\), \(n'\), \(N'(\gamma)\), \(t'\) | 局域辐射与冷却默认在此写 |
| source rest frame | subscript src | \(\nu_{\rm src},t_{\rm src}\) | 去除宇宙学红移后的源系观测量 |
| observer frame | subscript obs 或无标注 | \(t_{\rm obs},\nu_{\rm obs},F_\nu\) | 实际数据所在参考系 |

Formula ID：`AG-CONV-FRAME-REGISTRY-001`。

除非页面特别说明，带 prime 的量都在 shocked-fluid comoving frame；观测量必须经过 bulk Lorentz / Doppler 和 redshift 转换，不能把 comoving photon energy 直接当 observed photon energy。

## 2. 时间约定

最基础的到达时间关系是

$$
t_{\rm obs}
=
(1+z)\left(t_{\rm lab}-{R\cos\theta\over c}\right).
$$

对 on-axis ultra-relativistic motion，有量级关系

$$
t_{\rm obs}
\sim
(1+z){R\over C_t c\Gamma^2}.
$$

其中 \(C_t\) 是 convention factor，常见选择包括 2、4 或含 \((4-k)\) 的 BM 自相似系数。课程页应写出自己使用的 \(C_t\)，代码 helper 应把它作为参数或在文档中固定说明。

Formula ID：`AG-CONV-TOBS-FACTOR-001`。

本地代码中 `bm_radius()` 使用的 arrival-factor convention 是实现约定，不是唯一理论定义。比较不同文献或外部包时，优先检查这个因子。

## 3. 频率与能量转换

源系频率和观测频率满足

$$
\nu_{\rm src}
=
(1+z)\nu_{\rm obs}.
$$

局域 comoving emitted frequency 到 observer frame 的常用近似是

$$
\nu_{\rm obs}
=
{\delta_D\over1+z}\nu',
$$

其中

$$
\delta_D
=
{1\over\Gamma(1-\beta\cos\psi)}.
$$

on-axis 球面对称量级估计中常写 \(\delta_D\sim\Gamma\) 或 \(2\Gamma\)。这两者差一个 factor 2，影响特征频率归一化，但不改变 \(\nu\propto \gamma^2B'\) 这类标度。

Formula ID：`AG-CONV-FREQ-DOPPLER-001`。

能量转换同理：

$$
E_{\rm obs}
=
{\delta_D\over1+z}E'.
$$

在 TeV、neutrino、maximum-energy 页中，若讨论的是源内粒子能量、comoving 粒子能量或地球观测能量，必须写明。

## 4. 密度与外部介质

统一采用 power-law 外部介质写法：

$$
\rho(R)=A R^{-k}.
$$

常见特例：

| 环境 | \(k\) | 参数 |
| --- | --- | --- |
| ISM | 0 | \(n={\rm const}\), \(\rho=nm_p\) |
| wind | 2 | \(A=5\times10^{11}A_\ast\,{\rm g\,cm^{-1}}\) |

swept-up mass 为

$$
m_{\rm sw}(R)
=
{4\pi A\over3-k}R^{3-k},
\qquad k<3.
$$

Formula ID：`AG-CONV-DENSITY-K-001`。

不要把 wind 的 \(A\)、\(A_\ast\)、number density \(n(R)\) 混写。wind 中

$$
n(R)
=
{A\over m_pR^2}
$$

是由 mass density 除以 proton mass 得到的 number-density convention。

## 5. 能量约定

课程中常见三种能量：

| 符号 | 含义 | 边界 |
| --- | --- | --- |
| \(E_{\rm iso}\) | isotropic-equivalent kinetic energy | 不是真实喷流能量 |
| \(E_{\rm true}\) | beaming-corrected true energy | 依赖几何和单/双边约定 |
| \(E'\) | comoving particle / photon energy | 需 Doppler 转换到 observer |

top-hat 小角近似下，若使用双边喷流 convention，

$$
E_{\rm true}
\simeq
{ \theta_j^2\over2}E_{\rm iso}.
$$

Formula ID：`AG-CONV-ENERGY-ISOTRUE-001`。

如果只讨论一个 jet lobe 或者文献定义的 \(E_j\) 是单边能量，前面的系数会不同。事件报告必须写清 one-sided / two-sided convention。

## 6. Shock 与微物理量

ultra-relativistic cold upstream strong shock 的常用近似为

$$
n'\simeq4\Gamma n,
\qquad
e'\simeq4\Gamma^2 n m_pc^2.
$$

磁场参数化为

$$
{B'^2\over8\pi}
=
\epsilon_B e'.
$$

电子能量分配给出

$$
\gamma_m
\simeq
{p-2\over p-1}
{\epsilon_e\over\xi_e}
{m_p\over m_e}\Gamma,
\qquad p>2.
$$

Formula ID：`AG-CONV-MICROPHYSICS-001`。

这里 \(\epsilon_e,\epsilon_B,\xi_e,p\) 是 phenomenological microphysical parameters，不是标准 afterglow 理论从 first principles 预测出的唯一值。

## 7. Synchrotron Break 符号

本课程统一使用：

| 符号 | 含义 |
| --- | --- |
| \(\nu_a\) | self-absorption frequency |
| \(\nu_m\) | injection / minimum-electron break |
| \(\nu_c\) | cooling break |
| \(F_{\nu,\max}\) | peak flux density scale |

不要把 single-particle critical frequency 与 afterglow cooling break 混用。单粒子的特征频率应写成

$$
\nu_{\rm syn}'(\gamma)
\simeq
{3eB'\over4\pi m_ec}\gamma^2,
$$

而 afterglow 的 \(\nu_c\) 是由 \(\gamma_c\) 代入该频率后得到的 break。

Formula ID：`AG-CONV-BREAK-SYMBOLS-001`。

## 8. Cooling 与 Compton \(Y\)

电子冷却 Lorentz factor 写成

$$
\gamma_c
=
{6\pi m_ec(1+z)\over
\sigma_TB'^2\Gamma t_{\rm obs}(1+Y)}.
$$

这里 \(Y\) 是 Compton cooling correction。Thomson one-zone 中可写

$$
Y\simeq{U'_{\rm syn}\over U'_B},
$$

但进入 Klein-Nishina 后 \(Y\) 一般应为 \(Y(\gamma)\)。

Formula ID：`AG-CONV-COMPTON-Y-001`。

不能把 constant \(Y\) 的 \(\nu_c\) 修正直接用于 KN-dominated TeV cooling。

## 9. 光深与传播约定

source-local gamma-gamma absorption 的一般形式是

$$
\tau_{\gamma\gamma}^{\rm int}(E)
=
\int ds
\int d\epsilon
\int d\Omega\,
n(\epsilon,\Omega,s)(1-\mu)
\sigma_{\gamma\gamma}(E,\epsilon,\mu).
$$

EBL attenuation 写成

$$
F_{\rm obs}(E,z)
=
F_{\rm int}(E,z)
\exp[-\tau_{\gamma\gamma}^{\rm int}(E)-\tau_{\rm EBL}(E,z)].
$$

Formula ID：`AG-CONV-OPACITY-TAU-001`。

\(\tau=n\sigma l\) 只能作为 effective compactness sanity check。它不包含 spectrum、angle、threshold、source geometry，也不包含 cascade reprocessed flux。

## 10. 粒子分布与归一化

课程中 \(N(E)\)、\(N(\gamma)\)、\(n(E)\) 的含义必须分清：

| 符号 | 推荐含义 |
| --- | --- |
| \(N(\gamma)\) | total number distribution per Lorentz factor |
| \(N'_e(\gamma)\) | comoving total electron number distribution, \(\int dV'\,n'_e(\gamma)\) |
| \(n'_e(\gamma)\) | comoving electron number-density spectrum per volume per \(\gamma\) |
| \(n(\epsilon)\) | number density spectrum per energy |
| \(n'_{\rm ph}(\epsilon')\), \(n'_{\rm syn}(\epsilon')\) | comoving photon number-density spectrum per energy |
| \(Q(E)\) | injection rate per energy per time |
| \(F_\nu\) | observed flux density |
| \(\nu F_\nu\) or \(E^2 dN/dE\) | SED-like quantity |

Formula ID：`AG-CONV-DISTRIBUTION-NORM-001`。

per energy、per frequency、per log energy 之间差一个 Jacobian。若代码输入的是 SED 或 luminosity density，不能直接当 number density 塞进 opacity 或 IC kernel。尤其在 SSC 页中，\(j_{\epsilon'}\) 与 \(d\dot n_\gamma/d\epsilon_s'\) 使用 \(n'_e\)；若实现层使用 \(N'_e\)，结果应解释为 total luminosity / total production rate 或显式说明体积归一化。

## 11. High-Energy 与 Cascade 约定

最大能量从 timescale competition 起步：

$$
t'_{\rm acc}(\gamma_{\max})
=
\min_i t_i'(\gamma_{\max}).
$$

hadronic / cascade 页中的 \(E_\nu\simeq0.05E_p\) 只是能量尺度，不是 neutrino spectrum。cascade 中

$$
F_{\rm esc}
=
F_{\rm int}e^{-\tau}+F_{\rm cas}
$$

也只是结构式，\(F_{\rm cas}\) 必须由 pair injection、cooling、IC/synch emission 和 escape 共同决定。

Formula ID：`AG-CONV-HE-BOUNDARY-001`。

高能页常用符号统一如下：

| 符号 | 推荐含义 | 使用边界 |
| --- | --- | --- |
| \(b_{\rm KN}=4\gamma\epsilon'/(m_ec^2)\) | KN entry parameter | 只是 regime indicator，不替代 full KN kernel |
| \(\epsilon''\) | electron rest-frame photon energy | 不等于 observer photon energy |
| \(\epsilon_s'\) | scattered photon energy in comoving frame | IC kernel 的输出变量 |
| \(\tau_e\) | Thomson scattering optical depth of emitting electrons | one-zone scattering probability |
| \(\eta_{\rm acc}\) | acceleration gyro / efficiency factor | phenomenological，不是 shock theory 预测 |
| \(\bar\epsilon'\) | proton rest-frame target photon energy | \(p\gamma\) threshold 与 kernel 变量 |
| \(K_{p\gamma}\), \(\kappa\) | inelasticity / energy-loss fraction | 不能替代 differential secondary yield |
| \(f_\pi\) | proton energy fraction entering pions | 能量尺度，不是 spectrum |
| \(\tau_0\) | particle rest-frame lifetime | pion / muon cooling-decay 比较 |
| \(P_{\alpha\beta}\) | neutrino flavor mixing probability | source ratio 到 Earth ratio 的传播矩阵 |
| \(A_{\rm eff}(E_\nu)\) | detector effective area | detector-specific external input |

Formula ID：`AG-CONV-HE-SYMBOL-REGISTRY-001`。

## 12. 代码约定注册

当前本地代码与课程的关系应按层级写：

| 层级 | 含义 |
| --- | --- |
| `course-derived` | 课程推导得到 |
| `teaching-code` | 教学 helper，可做 fixed point |
| `toy-code` | 趋势或 sanity helper |
| `partial-code` | 实现了子问题，不是完整 solver |
| `benchmark-output` | 外部包同 convention 对照 |
| `theory-only` | 仅理论页或边界 |
| `future-helper` | 适合未来实现 |

Formula ID：`AG-CONV-CODE-LAYER-LABELS-001`。

如果代码采用的 convention 与课程 general expression 不同，理论页必须写：

$$
\text{course expression}
\rightarrow
\text{implemented approximation}
\rightarrow
\text{difference source}
\rightarrow
\text{affected quantity}.
$$

Formula ID：`AG-CONV-DIFFERENCE-REPORT-001`。

常见 difference source 包括 arrival-time factor、Doppler convention、pitch-angle average、seed photon convention、cross-section kernel、integration grid、KN approximation、EBL model、density normalization、component sum 和 upper-limit likelihood。

新增 source-adapter local-zone 约定也必须按这个格式注册。`AG-FS-LOCAL-ZONE-001` 使用：

| 约定 | 本地写法 | 不能替代 |
| --- | --- | --- |
| local size | `local_size_cm = comoving_size_factor * R / Gamma` | 唯一 shell thickness、EATS geometry 或 hydrodynamic width |
| local fields | `B'` in gauss, \(e'\) and \(U'_{\rm ph}\) in erg cm\(^{-3}\) | observed-frame energy density |
| photon provenance | `photon_energy_density_fraction * e'` or caller-supplied local field | self-consistent SSC seed photon transfer |
| screening output | cooling / escape times in seconds, Hillas energies in eV | observed flux, event fit, complete maximum-energy solver |

`AG-FS-GG-OPACITY-SCREEN-001` adds an opacity-specific provenance line:

| 约定 | 本地写法 | 不能替代 |
| --- | --- | --- |
| gamma-ray energy | `gamma_energy_grid_kev` in the same local opacity frame as the kernel input | observed energy without Doppler/redshift conversion |
| mono target energy | `characteristic_seed_photon_energy_ev * 1e-3` converted to keV | synchrotron target spectrum or EBL table |
| target density | \(n'_{\rm target}=U'_{\rm ph}/\epsilon'_{\rm seed}\), cm\(^{-3}\) | observed SED inversion or self-consistent SSC photon density |
| tabulated target shape | `target_shape_per_kev` normalized to \(U'_{\rm ph}=f_{\rm ph}e'\) | a derived synchrotron/SSC photon spectrum unless provenance is supplied |
| path length | \(l'=f_RR/\Gamma\) from `forward_shock_local_zone_state()` | EATS-integrated geometry or full transfer optical depth |
| opacity output | \(\alpha_{\gamma\gamma}\) in cm\(^{-1}\), \(\tau=\alpha l\), attenuation \(\exp(-\tau)\) | cascade-reprocessed flux or event mechanism decision |

后续 AGN blob、PWN/SNR shell 或 TDE adapter 也应提交同类 local-zone provenance，不能只给一个 \(B,R,U_{\rm ph}\) 数字而不说明参考系和来源。

## 13. Exact Analytic Status

| 对象 | 状态 | 说明 |
| --- | --- | --- |
| frame conversion | closed convention | factor must be stated |
| density profile | closed for \(k<3\) | jumps require hydro |
| shock jump approximation | closed limit | ultra-relativistic cold upstream |
| synchrotron break symbols | convention registry | spectra still require ordering |
| \(Y\) correction | closed only in Thomson one-zone | KN needs kernel |
| gamma-gamma opacity | formal / numerical | target field required |
| distribution normalization | convention-dependent | Jacobian matters |
| code-layer labels | workflow convention | not physics proof |

## 14. Benchmark Boundary

外部包只能在本页约定之后进入：

- `afterglowpy` / `VegasAfterglow`：light-curve benchmark，不定义本课程参考系；
- `naima` / `agnpy`：radiation SED parity，不定义事件物理；
- `ebltable`：EBL \(\tau(E,z)\) table，不是内置宇宙传播真理；
- SOPHIA / AM3 / CRPropa / ELMAG：future mature-method candidate，不是本地已实现功能。

## 15. 不声称

- 不声称某个 factor convention 是唯一正确约定。
- 不把 \(E_{\rm iso}\) 写成 true energy，除非给出 beaming correction。
- 不把 comoving energy 直接写成 observed energy。
- 不把 per energy spectrum、SED 和 number density 混用。
- 不把 constant \(Y\) 写成 KN cooling 的完整处理。
- 不把 \(\tau=n\sigma l\) 写成完整 opacity 或 cascade。
- 不把 benchmark-output 写成理论起点。

## 16. 参考文件

- `01-blandford-mckee-and-external-shock.md`
- `02-afterglow-synchrotron-breaks-and-closure-relations.md`
- `10-ssc-and-tev-afterglow.md`
- `11-particle-acceleration-and-maximum-energy.md`
- `12-cascade-neutrino-and-propagation-boundaries.md`
- `13-event-interpretation-chain.md`
- `14-course-roadmap-and-formula-audit.md`
