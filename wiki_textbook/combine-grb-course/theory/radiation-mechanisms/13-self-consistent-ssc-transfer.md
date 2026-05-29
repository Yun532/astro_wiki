# 13 Self-Consistent SSC Transfer

状态：v0.1 课程讲义草稿。本页补充 02 页和 12 页之间的缺口：如何从 synchrotron transfer、seed photon density、IC kernel 和 electron cooling feedback 构造 self-consistent SSC transfer 的理论起点。这里的 self-consistent 不是“已经有本地 solver”，而是说理论链条必须闭合：电子产生 synchrotron photons，photons 经过 escape / absorption 形成 \(n_{\rm syn}\)，同一群电子再 inverse-Compton scattering 这些 photons，IC cooling 又反过来改变 electron distribution。

核心原则：不能从 \(\nu_{\rm IC}\sim\gamma^2\nu_{\rm syn}\)、\(Y={\rm const}\)、broken-power-law SSC peak 或 `agnpy` 输出开始。那些都是后置 sanity / benchmark layer。安全起点是 photon transfer 与 IC kernel 的 coupled problem。

## 1. 物理图像

SSC 的最小闭环是：

```text
electron distribution n_e(gamma)
  -> synchrotron emissivity j_syn and absorption alpha_syn
  -> local synchrotron photon density n_syn(epsilon)
  -> IC/KN scattering kernel
  -> SSC emissivity and IC cooling
  -> updated electron distribution / cooling break
```

Formula ID：`SSC-SC-PICTURE-001`。

这比 one-shot IC 多一个反馈环。若 \(n_{\rm syn}\) 被外部表格直接给定，问题只是 supplied-seed IC；若 \(n_{\rm syn}\) 由同一群 electrons 的 synchrotron transfer 决定，才是 SSC。若 cooling 再反过来改变 \(n_e(\gamma)\)，才进入 self-consistent SSC。

## 2. 变量与参考系

本页默认使用 homogeneous one-zone comoving frame。带 prime 的源内 comoving 量在公式中省略 prime，只在跨到 observer frame 时再写 Doppler / redshift。更复杂的 EATS、anisotropic seed field 或 structured geometry 应另加角度和空间变量。

| 符号 | 含义 |
| --- | --- |
| \(n_e(\gamma,t)\) | electron number-density spectrum per \(\gamma\) |
| \(B\) | local magnetic field |
| \(j_\epsilon^{\rm syn}\) | synchrotron energy emissivity per energy per steradian |
| \(\alpha_\epsilon^{\rm syn}\) | synchrotron absorption coefficient |
| \(n_{\rm syn}(\epsilon,t)\) | synchrotron photon number-density spectrum per energy |
| \(R\) | effective source size |
| \(t_{\rm esc,\gamma}\) | photon escape time |
| \(d\sigma_{\rm IC}/d\epsilon_s\) | IC / KN differential cross-section |
| \(Q_e(\gamma)\) | electron injection rate |
| \(\dot\gamma_{\rm syn}\), \(\dot\gamma_{\rm IC}\) | synchrotron and IC cooling rates |

Formula ID：`SSC-SC-VARIABLES-001`。

重要约定：\(n_e\) 是体密度谱。如果使用 total spectrum \(N_e=\int dV\,n_e\)，则 emissivity / photon density 公式必须显式除以体积或改写成 total luminosity convention。

## 3. 一般表达式：从 transfer 到 seed photon density

synchrotron emissivity 从单粒子功率积分开始：

$$
j_\epsilon^{\rm syn}
=
{1\over4\pi}
\int d\gamma\,n_e(\gamma)
P_\epsilon^{\rm syn}(\gamma,B).
$$

absorption coefficient 由 SSA 页给出，记为 \(\alpha_\epsilon^{\rm syn}\)。在 homogeneous slab / sphere 的 teaching layer 中，source function 为

$$
S_\epsilon
=
{j_\epsilon^{\rm syn}\over\alpha_\epsilon^{\rm syn}},
$$

transfer 给出局域强度量级

$$
I_\epsilon
\sim
S_\epsilon\left(1-e^{-\tau_\epsilon}\right),
\qquad
\tau_\epsilon=\alpha_\epsilon^{\rm syn}R.
$$

若辐射场近似各向同性，energy density spectrum 与 mean intensity 满足

$$
u_\epsilon^{\rm syn}
=
{4\pi\over c}J_\epsilon,
\qquad
n_{\rm syn}(\epsilon)
=
{u_\epsilon^{\rm syn}\over\epsilon}.
$$

Formula ID：`SSC-SC-SEED-TRANSFER-001`。

在 optically thin escape-time approximation 中，这一步常被压缩为

$$
n_{\rm syn}(\epsilon)
\sim
{4\pi t_{\rm esc,\gamma}\over\epsilon}
j_\epsilon^{\rm syn},
\qquad
t_{\rm esc,\gamma}\sim {R\over c}.
$$

但这只是一个 closure，不是 SSC 的定义。若 \(\tau_\epsilon\gtrsim1\)，SSA 会改变 seed photon density，并进一步改变 SSC spectrum 和 cooling。

## 4. Photon balance form

更适合数值实现的写法是 photon balance equation：

$$
{\partial n_{\rm syn}(\epsilon,t)\over\partial t}
=
{4\pi j_\epsilon^{\rm syn}\over\epsilon}
-
{n_{\rm syn}(\epsilon,t)\over t_{\rm esc,\gamma}(\epsilon)}
-
c\alpha_\epsilon^{\rm syn}n_{\rm syn}(\epsilon,t)
+Q_{\rm reproc}(\epsilon,t).
$$

Formula ID：`SSC-SC-PHOTON-BALANCE-001`。

其中 \(Q_{\rm reproc}\) 可包含 pair cascade、higher-order scattering 或外部 reprocessing。最小 first-order SSC 可以令 \(Q_{\rm reproc}=0\)，但必须把这个省略写出来。steady state 下，

$$
n_{\rm syn}
\simeq
{4\pi j_\epsilon^{\rm syn}/\epsilon
\over
t_{\rm esc,\gamma}^{-1}+c\alpha_\epsilon^{\rm syn}}.
$$

这个式子比简单 \(R/c\) escape 多保留了 SSA loss term，因此可以解释为什么 self-absorption 会影响 SSC seed field。

## 5. SSC emissivity：保留 IC / KN kernel

first-order SSC 的 photon volume production rate 为

$$
{d\dot n_\gamma^{\rm SSC}\over d\epsilon_s}
=
c
\int d\gamma\,n_e(\gamma)
\int d\epsilon\,n_{\rm syn}(\epsilon)
{d\sigma_{\rm IC}\over d\epsilon_s}(\gamma,\epsilon,\epsilon_s).
$$

对应 energy emissivity 是

$$
j_{\epsilon_s}^{\rm SSC}
=
{\epsilon_s\over4\pi}
c
\int d\gamma\,n_e(\gamma)
\int d\epsilon\,n_{\rm syn}(\epsilon)
{d\sigma_{\rm IC}\over d\epsilon_s}.
$$

Formula ID：`SSC-SC-EMISSIVITY-001`。

这里 \(d\sigma_{\rm IC}/d\epsilon_s\) 应优先使用 Blumenthal-Gould / KN kernel。Thomson kernel 和 delta approximation 是从这个式子降阶得到的近似，不能作为理论起点。

## 6. Cooling feedback：从 emissivity 回到 electron distribution

单电子 IC cooling rate 应写成 energy-loss integral：

$$
\left.{d\gamma\over dt}\right|_{\rm IC}
=
-
{1\over m_ec^2}
\int d\epsilon\,n_{\rm syn}(\epsilon)
\int d\epsilon_s\,
(\epsilon_s-\epsilon)c
{d\sigma_{\rm IC}\over d\epsilon_s}.
$$

synchrotron cooling rate 为

$$
\left.{d\gamma\over dt}\right|_{\rm syn}
=
-
{4\sigma_T\over3m_ec}
U_B\gamma^2
$$

在 isotropic pitch-angle Thomson limit 下成立。总 cooling 进入 electron continuity equation：

$$
{\partial n_e(\gamma,t)\over\partial t}
=
Q_e(\gamma,t)
-
{\partial\over\partial\gamma}
\left[
\dot\gamma_{\rm syn+IC}(\gamma,t)n_e(\gamma,t)
\right]
-
{n_e\over t_{\rm esc,e}}
.
$$

Formula ID：`SSC-SC-COOLING-FEEDBACK-001`。

self-consistency 的数学含义就在这里：\(n_e\to j_{\rm syn}\to n_{\rm syn}\to \dot\gamma_{\rm IC}\to n_e\)。若只更新 \(Y\) 而不更新 spectrum，得到的是 toy feedback；若更新 \(n_e(\gamma)\) 和 \(n_{\rm syn}(\epsilon)\)，才是 radiative transfer / kinetic feedback。

## 7. Generalized \(Y(\gamma)\)

在 Thomson one-zone limit，\(Y=U_{\rm syn}/U_B\)。但在 KN regime 中，每个 \(\gamma\) 看到的有效 seed photon field 不同，因此应写成

$$
Y(\gamma)
=
{|\dot\gamma_{\rm IC}(\gamma)|
\over
|\dot\gamma_{\rm syn}(\gamma)|}.
$$

Formula ID：`SSC-SC-Y-GAMMA-001`。

如果 \(Y(\gamma)\) 变化很快，就不能把 \(\nu_c\) 简单改成 \(\nu_{c,0}/(1+Y)^2\)。此时 cooling break 的位置来自 electron continuity equation，而不是一个全局 scalar \(Y\)。

## 8. Thomson one-zone 作为降阶极限

若满足：

1. source optically thin, \(\alpha_\epsilon R\ll1\)；
2. \(t_{\rm esc,\gamma}\sim R/c\) 且不随 \(\epsilon\) 变；
3. IC 处于 Thomson regime；
4. electron distribution 用 broken power law 近似；
5. first-order SSC dominates, higher-order scattering omitted；

则

$$
n_{\rm syn}(\epsilon)
\sim
{4\pi R\over c\epsilon}j_\epsilon^{\rm syn},
$$

并可得到 familiar estimates：

$$
Y
\simeq
{U_{\rm syn}\over U_B},
\qquad
\nu_{\rm IC}\sim \gamma^2\nu_{\rm syn}.
$$

Formula ID：`SSC-SC-THOMSON-LIMIT-001`。

这说明 one-zone \(Y\) 不是错，而是 self-consistent SSC 的一个窄极限。课程和代码必须写清自己处在哪一层。

## 9. Iteration ladder

从最简单到最完整，可以按以下层级实现：

| 层级 | 更新对象 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| supplied-seed IC | fixed \(n_{\rm syn}\) | IC / KN kernel | seed field self-consistency |
| one-zone SSC | \(j_{\rm syn}\to n_{\rm syn}\to j_{\rm SSC}\) | seed-field origin | cooling feedback |
| \(Y\)-toy feedback | scalar \(Y,\nu_c\) | cooling intuition | KN and spectral curvature |
| spectral fixed point | \(n_e(\gamma)\), \(n_{\rm syn}(\epsilon)\) | cooling-spectrum coupling | geometry / EATS |
| time-dependent transfer | \(n_e,n_\gamma\) with escape and absorption | transient feedback | expensive |
| geometry / EATS SSC | space, angle, time | afterglow observable realism | production complexity |

Formula ID：`SSC-SC-ITERATION-LADDER-001`。

## 10. 当前代码实现约定

当前本地代码已经有：

```text
reproduce/grb/core/radiation/ssc.py
reproduce/grb/core/radiation/inverse_compton.py
reproduce/grb/core/radiation/synchrotron.py
reproduce/grb/core/radiation/cooling_angle.py
```

对应层级：

| 函数 / helper | 层级 | 说明 |
| --- | --- | --- |
| `synchrotron_seed_density_from_luminosity_per_erg` | supplied luminosity -> seed density | 只做几何和单位转换 |
| `synchrotron_seed_field_from_luminosity_grid` | tabulated seed builder | 调用方给 synchrotron luminosity |
| `ssc_one_zone_tabulated_sed_erg_cm2_s` | supplied-seed IC / one-zone SSC kernel | 不自洽求 synchrotron transfer |
| `iterate_compton_y_and_cooling_frequency` | \(Y\)-toy feedback | scalar \(Y\)，不是 \(Y(\gamma)\) |
| `ssc_breaks_with_cooling_feedback` | break-level toy | 不给 full spectrum |
| `ic_kn_suppressed_cooling_power_erg_s` | KN envelope | characteristic seed only |

Formula ID：`SSC-SC-CODE-BOUNDARY-001`。

因此，当前代码可以支持 “supplied seed-field SSC” 和 “toy \(Y\) cooling feedback” 的教学 / sanity / benchmark 层；不能声称 full self-consistent SSC transfer。

## 11. Exact analytic status

| 对象 | 状态 | 说明 |
| --- | --- | --- |
| synchrotron emissivity integral | formal / semi-analytic | power-law 可闭合，任意 spectrum 数值 |
| SSA transfer | closed for homogeneous slab | geometry dependent |
| photon balance steady state | algebraic if coefficients fixed | \(n_e\) fixed时成立 |
| SSC emissivity with BG/KN kernel | numerical | nested kernel integral |
| IC cooling feedback | numerical | requires \(n_{\rm syn}\) and kinematic limits |
| scalar \(Y\) | closed only in Thomson one-zone | KN gives \(Y(\gamma)\) |
| self-consistent kinetic solution | generally numerical | coupled \(n_e,n_\gamma\) |

## 12. Benchmark boundary

| Benchmark | 可检查 | 不能证明 |
| --- | --- | --- |
| `agnpy` one-zone SSC | same-convention one-zone SED | self-consistent transfer |
| `naima` IC | supplied-seed IC kernel behavior | SSC feedback |
| local `ssc.py` tabulated seed | unit / geometry convention | photon transfer |
| afterglow TeV event sanity | trend and candidate consistency | unique TeV origin |

Formula ID：`SSC-SC-BENCHMARK-BOUNDARY-001`。

Benchmark 要记录 electron distribution、seed photon convention、source size、Doppler / distance convention、geometry factor 和是否包含 SSA。否则 ratio 的意义不清楚。

## 13. 不声称

- 不声称本页实现了 self-consistent SSC solver。
- 不声称 scalar \(Y\) 可以描述 KN-dominated cooling。
- 不声称 supplied synchrotron luminosity grid 等于 self-consistent seed photon density。
- 不声称 `agnpy` one-zone SSC parity 等于 afterglow SSC transfer。
- 不声称 \(\nu_{\rm IC}\sim\gamma^2\nu_{\rm syn}\) 足以预测 TeV spectrum。
- 不声称 first-order SSC 自动排除 external IC、hadronic cascade 或 extreme synchrotron alternatives。

## 14. 参考入口

- `01-synchrotron-and-ssa.md`
- `02-inverse-compton-and-ssc.md`
- `03-gamma-gamma-opacity.md`
- `12-missing-process-interface-roadmap.md`
- `../grb-afterglow/10-ssc-and-tev-afterglow.md`
