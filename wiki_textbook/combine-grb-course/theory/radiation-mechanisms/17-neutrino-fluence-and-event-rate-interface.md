# 17 Neutrino Fluence 与 Event-Rate 接口

状态：v0.1 讲义级理论接口页。本页把 12 页中的 `RAD-GAP-NU-EVENT-INTERFACE-001` 展开为源类无关的 neutrino detector-convolution 接口。它不是 neutrino event-rate predictor，也不新增 production code；目标是把 source-side neutrino fluence、flavor mixing、Earth fluence、detector effective area、time window、event class 和 non-detection claim boundary 分开。

核心原则：不能从 \(E_\nu\simeq0.05E_p\)、一个 total neutrino energy、一次 non-detection 或 detector upper limit 开始。安全起点是 source neutrino spectrum / fluence；经过 flavor mixing 与传播后，才与 detector response 做卷积。探测器响应是 external boundary，不是源端辐射机制。

## 1. 物理图像

neutrino event-rate 链条至少有四层：

```text
hadronic source model
  -> source-frame neutrino production Q_nu(E,t,flavor)
  -> propagation and flavor mixing
  -> Earth fluence Phi_nu(E,Omega,t,flavor)
  -> detector effective area / selection / time window
  -> expected event count
```

Formula ID：`NU-EVENT-PICTURE-001`。

这条链条和 gamma-ray / cascade 有联系，但不能互相替代。gamma-ray opacity、cascade reprocessing 和 neutrino event count 都是不同 observables 的 forward maps；任何一个 non-detection 都不能单独证明 hadronic channel 不存在。

## 2. 变量与约定

本页使用 source-side 和 Earth-side 两套量。源端产生率可以在 comoving frame 或 lab/source frame 给出；进入 detector 前必须统一成 Earth fluence。

| 符号 | 含义 |
| --- | --- |
| \(Q_{\nu_\alpha}(E,t)\) | source-side neutrino production rate |
| \(L_{\nu_\alpha}(E,t)\) | source spectral luminosity |
| \(\mathcal F_{\nu_\alpha}(E)\) | source fluence at Earth before mixing or after specified propagation |
| \(\Phi_{\nu_\alpha}^\oplus(E,\Omega,t)\) | Earth differential fluence / flux for flavor \(\alpha\) |
| \(P_{\alpha\beta}\) | flavor-transition probability from source \(\beta\) to Earth \(\alpha\) |
| \(A_{\rm eff}(E,\Omega,{\rm class})\) | detector effective area |
| \(T_{\rm win}\) | analysis time window |
| \(P_{\rm sel}\) | event selection / detection efficiency |
| \(N_{\rm ev}\) | expected event count |

Formula ID：`NU-EVENT-VARIABLES-001`。

必须写清 \(\Phi_\nu\) 是 flux 还是 fluence。若 \(\Phi_\nu(E,t)\) 是 flux，事件数积分要包含 \(dt\)；若 \(\mathcal F_\nu(E)=\int dt\,\Phi_\nu(E,t)\) 是 fluence，则不再额外乘同一个时间窗。

## 3. Source fluence：先从 neutrino spectrum 开始

source-side neutrino production 不能由 \(E_\nu=0.05E_p\) 单独定义。一般应来自 hadronic yield：

$$
Q_{\nu_\beta}(E_\nu,t)
=
\int dE_p\,N_p(E_p,t)
\int d\chi\,n_{\rm target}(\chi,t)c\,
\mathcal R(E_p,\chi)
Y_{\nu_\beta}(E_\nu;E_p,\chi).
$$

Formula ID：`NU-SOURCE-YIELD-001`。

若使用 isotropic-equivalent spectral luminosity \(L_{\nu_\beta}(E,t)\)，在不考虑传播损失的简化 cosmological flux convention 下，Earth flux 可写成

$$
\phi_{\nu_\beta}(E_{\rm obs},t_{\rm obs})
=
{1+z\over4\pi d_L^2}
L_{\nu_\beta}\!\left(E_{\rm src},t_{\rm src}\right),
$$

其中

$$
E_{\rm src}=(1+z)E_{\rm obs},
\qquad
t_{\rm src}={t_{\rm obs}\over1+z}.
$$

Formula ID：`NU-SOURCE-TO-EARTH-FLUX-001`。

不同文献会把 \(E L_E\)、\(E^2 dN/dE\)、fluence 或 time-integrated luminosity 作为基础量。课程页和代码接口必须记录使用哪一种，否则 event-rate normalization 会差一个能量或时间因子。

## 4. Flavor mixing

若 source flavor vector 为

$$
\boldsymbol\phi^{\rm src}
=
(\phi_e,\phi_\mu,\phi_\tau)_{\rm src},
$$

长基线真空振荡后的 Earth flavor 为

$$
\phi_\alpha^\oplus(E)
=
\sum_\beta P_{\alpha\beta}(E)\phi_\beta^{\rm src}(E).
$$

在天体物理长基线、相干项平均掉的近似下，

$$
P_{\alpha\beta}
=
\sum_i |U_{\alpha i}|^2|U_{\beta i}|^2.
$$

Formula ID：`NU-FLAVOR-MIXING-MATRIX-001`。

经典 pion chain 若没有 strong cooling，常给出

$$
(\nu_e:\nu_\mu:\nu_\tau)_{\rm src}
\simeq
(1:2:0),
$$

地球附近近似为

$$
(\nu_e:\nu_\mu:\nu_\tau)_\oplus
\sim
(1:1:1).
$$

Formula ID：`NU-FLAVOR-PION-LIMIT-001`。

但 muon damping、neutron beam、charm / kaon channels、source magnetic field 和 energy-dependent cooling 都会改变 source flavor ratio。\(1:1:1\) 是常用近似，不是 detector convolution 的必然输入。

## 5. Detector event-count convolution

对给定 detector、sky direction、event class 和 analysis window，期望事件数为

$$
N_{\rm ev}
=
\sum_\alpha
\int dt\int dE_\nu\int d\Omega\,
\Phi_{\nu_\alpha}^\oplus(E_\nu,\Omega,t)
A_{{\rm eff},\alpha}(E_\nu,\Omega,{\rm class},t)
P_{\rm sel}(E_\nu,\Omega,t).
$$

Formula ID：`NU-EVENT-CONVOLUTION-001`。

如果 detector product 已经给出针对某个 event class 的 effective area，\(P_{\rm sel}\) 可能已经吸收在 \(A_{\rm eff}\) 中；如果不是，就必须显式给出 selection efficiency。不能同时把 \(P_{\rm sel}\) 乘两次。

对 transient search，常使用 time-integrated fluence：

$$
N_{\rm ev}
=
\sum_\alpha
\int dE_\nu\,
\mathcal F_{\nu_\alpha}^\oplus(E_\nu)
A_{{\rm eff},\alpha}(E_\nu,\Omega_{\rm src},{\rm class};T_{\rm win}).
$$

Formula ID：`NU-EVENT-FLUENCE-CONVOLUTION-001`。

这里 \(T_{\rm win}\) 是 analysis choice，不是源物理量。不同时间窗会改变 background、selection 和 upper limit。

## 6. Upper limit 与 non-detection

若观测到 \(n_{\rm obs}\) 个事件、期望背景为 \(b\)，Poisson likelihood 是

$$
\mathcal L(\mu_\nu)
=
{(\mu_\nu+b)^{n_{\rm obs}}\over n_{\rm obs}!}
\exp[-(\mu_\nu+b)],
$$

其中 \(\mu_\nu=N_{\rm ev}\)。若 \(n_{\rm obs}=0\) 且 \(b\simeq0\)，常见 90% confidence upper limit 的数量级为

$$
\mu_{90}\simeq2.3.
$$

Formula ID：`NU-EVENT-POISSON-LIMIT-001`。

这条统计式只能约束 event expectation。要把它转成 source fluence upper limit，需要反解 detector convolution：

$$
\mathcal F_{\nu}^{90}(E)
\quad{\rm such\ that}\quad
\int dE\,\mathcal F_{\nu}^{90}(E)A_{\rm eff}(E)=\mu_{90},
$$

并且通常要假设一个 spectral shape，例如 \(E^{-2}\)、cutoff power law 或 model-predicted spectrum。

Formula ID：`NU-FLUENCE-UPPER-LIMIT-001`。

所以 non-detection 不是“无 hadronic emission”的证明；它是在 detector response、time window、sky direction、spectrum assumption 和 background model 下对 fluence 或模型参数的约束。

## 7. 与 gamma / cascade 的关系

hadronic source 同时可能产生 gamma rays、pairs 和 neutrinos：

$$
Q_{\rm had}
\rightarrow
\{Q_\gamma,Q_{e^\pm},Q_\nu\}.
$$

但 gamma rays 可能被 internal \(\gamma\gamma\)、EBL 或 EM cascade 重处理；neutrinos 基本不受这些电磁传播过程影响。因此

$$
F_\gamma^{\rm obs}
\ne
{\rm direct\ proxy\ for}\ \Phi_\nu^\oplus
$$

除非模型同时指定 hadronic yield、cascade transport、attenuation 和 detector response。

Formula ID：`NU-GAMMA-CASCADE-RELATION-001`。

用 gamma-ray upper limit 限制 neutrino 需要模型闭合；用 neutrino non-detection 限制 gamma-ray cascade 也需要模型闭合。二者都不是单行比例关系。

## 8. 接口契约

未来 neutrino event-rate helper 至少需要：

| 类别 | 输入 / 输出 | 说明 |
| --- | --- | --- |
| source fluence | \(\mathcal F_{\nu_\alpha}(E)\) or flux \(\Phi_{\nu_\alpha}(E,t)\) | 必须说明 flavor、time integration 和单位 |
| flavor handling | source flavor vector or \(P_{\alpha\beta}\) | 可默认 averaged PMNS，但必须可替换 |
| direction | sky position / zenith / declination | \(A_{\rm eff}\) 强依赖方向 |
| detector response | \(A_{\rm eff}(E,\Omega,{\rm class})\) | external product；版本和 event class 必须记录 |
| time window | \(T_{\rm win}\) or time grid | transient search 的核心选择 |
| selection/background | \(P_{\rm sel}\), \(b\), likelihood convention | 不能混成源模型 |
| outputs | \(N_{\rm ev}\), optional fluence upper limit | 输出必须标注 detector-specific |

Formula ID：`NU-EVENT-INTERFACE-CONTRACT-001`。

建议代码层级：

```text
source neutrino fluence builder
  -> flavor mixing reducer
  -> detector response loader
  -> event-count convolution
  -> Poisson / likelihood wrapper
```

不要把 hadronic yield、cascade、flavor mixing、effective area 和 Poisson upper limit 写进一个黑箱函数。

## 9. 当前代码边界

当前本地代码有：

| 代码 | 层级 | 边界 |
| --- | --- | --- |
| `hadronic.py::neutrino_energy_from_proton_gev` | energy scale helper | \(E_\nu\sim0.05E_p\)，不是 spectrum |
| `hadronic.py` pion / muon decay helpers | decay/cooling regime | no neutrino yield |
| `15-photohadronic-and-bethe-heitler-interface.md` | \(p\gamma\) yield interface | no production solver |
| `16-electromagnetic-cascade-transport-interface.md` | EM cascade interface | no neutrino detector response |
| validation outputs | fixed-point / parity checks | no IceCube/KM3NeT event-rate prediction |

Formula ID：`NU-EVENT-CODE-BOUNDARY-001`。

因此当前可声称：已有 neutrino characteristic energy scale、pion/muon cooling-vs-decay regime、source-side formal yield boundary。不能声称：已有 neutrino spectrum、flavor-mixing helper、detector effective-area convolution、event-rate prediction 或 non-detection likelihood。

## 10. Exact analytic status

| 对象 | 状态 | 说明 |
| --- | --- | --- |
| pion-chain energy scale | closed scale | not a spectrum |
| source neutrino yield | parameterized / Monte Carlo / table | depends on hadronic channel |
| flavor mixing | closed linear map after source spectrum known | source flavor may be energy-dependent |
| event-count convolution | numerical integral | detector product external |
| Poisson upper limit | analytic for simple cases | realistic analyses include background/systematics |
| model exclusion | statistical inference | requires priors and source model |

Formula ID：`NU-EVENT-EXACT-STATUS-001`。

## 11. Benchmark boundary

| Benchmark / external product | 可检查 | 不能证明 |
| --- | --- | --- |
| IceCube public effective areas | event-count convolution under stated class | source neutrino flux |
| KM3NeT effective areas | detector response comparison | universal detector standard |
| published GRB neutrino upper limits | fluence-limit reproduction under assumptions | no hadronic emission |
| AM3 / NeuCosmA neutrino spectra | source-side yield benchmark | detector event prediction without \(A_{\rm eff}\) |
| local energy-scale helper | band intuition | spectrum or event rate |

Formula ID：`NU-EVENT-BENCHMARK-BOUNDARY-001`。

任何 benchmark 都必须记录 detector、data release、effective-area units、flavor convention、event class、sky direction、time window 和 spectral assumption。

## 12. 不声称

- 不声称本页实现 neutrino event-rate predictor。
- 不声称 \(E_\nu\simeq0.05E_p\) 是 neutrino spectrum。
- 不声称 non-detection 等于 hadronic process 不存在。
- 不声称 IceCube / KM3NeT effective area 是源端理论。
- 不声称 gamma-ray flux 和 neutrino flux 可以无模型地互相换算。
- 不声称当前本地代码能预测任何 GRB 的 neutrino event count。

## 13. 参考入口

- `05-hadronic-order-of-magnitude.md`
- `12-missing-process-interface-roadmap.md`
- `15-photohadronic-and-bethe-heitler-interface.md`
- `16-electromagnetic-cascade-transport-interface.md`
- `../grb-afterglow/12-cascade-neutrino-and-propagation-boundaries.md`
- `reproduce/grb/core/radiation/hadronic.py`
