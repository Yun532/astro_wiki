# 15 Photohadronic 与 Bethe-Heitler 接口

状态：v0.1 讲义级理论接口页。本页把 12 页中的 `RAD-GAP-PGAMMA-BH-INTERFACE-001` 展开为可追踪的课程推导：\(p\gamma\) pion production 与 Bethe-Heitler pair production 的共同起点是 proton rest frame 中的 photon energy、角积分、cross-section / yield kernel，而不是 threshold helper、\(E_\nu\simeq0.05E_p\) 或 delta approximation。

本页不新增 production solver。当前本地代码仍只有 \(p\gamma\) / BH threshold envelope、pp gamma-ray mature route、proton synchrotron route 和 secondary cooling-vs-decay teaching helper；没有 \(p\gamma\) spectrum、BH pair injection spectrum、photohadronic cooling table、neutrino spectrum 或 cascade solver。

## 1. 物理图像

高能 proton 穿过 photon field 时，至少有两类重要通道：

```text
p + gamma -> pion channels -> gamma / neutrino / secondary e±
p + gamma -> p + e+ + e-  (Bethe-Heitler)
```

两者都由同一个角度运动学控制：

$$
\bar\epsilon
=
\gamma_p\epsilon(1-\beta_p\mu),
$$

其中 \(\bar\epsilon\) 是 proton rest frame 中的 photon energy，\(\epsilon\) 是源区 comoving frame photon energy，\(\mu=\hat{\boldsymbol p}_p\cdot\hat{\boldsymbol k}\)。

Formula ID：`HAD-PGAMMA-BH-PICTURE-001`。

核心区别是：pion production 的 inelasticity 较高并产生 \(\pi^0,\pi^\pm\)；BH 阈值更低，但每次相互作用只损失很小 fraction 的 proton energy，并直接注入 \(e^\pm\)。因此 BH 不能只用 threshold 判断，必须用 loss / pair-injection kernel。

## 2. 变量与约定

本页默认在源区 local comoving frame 中写公式。若接 afterglow / prompt / AGN jet 等具体源，bulk Lorentz factor、Doppler factor、redshift 和 photon field 来源应由 source adapter 另行登记。

| 符号 | 含义 |
| --- | --- |
| \(E_p=\gamma_pm_pc^2\) | proton energy |
| \(\epsilon\) | target photon energy |
| \(n_\gamma(\epsilon,\Omega)\) | photon number density per energy per solid angle |
| \(n_\gamma(\epsilon)\) | angle-integrated isotropic photon spectrum |
| \(\mu\) | proton 与 photon 方向夹角余弦 |
| \(\bar\epsilon\) | proton rest-frame photon energy |
| \(\sigma_i(\bar\epsilon)\) | channel \(i\) cross-section |
| \(K_i(\bar\epsilon)\) | inelasticity |
| \(Y_s(E_s;E_p,\epsilon,\mu)\) | secondary species \(s\) 的 yield |

Formula ID：`HAD-PGAMMA-BH-VARIABLES-001`。

注意 \(n_\gamma(\epsilon)\) 的单位必须写清：若是 cm\(^{-3}\) erg\(^{-1}\)，则 rate integral 的能量变量用 erg；若使用 eV 或 GeV 网格，代码层必须显式转换。

## 3. General expression：从角积分开始

对任意 photon-target hadronic channel，最一般的相互作用率可写为

$$
t_i^{-1}(E_p)
=
c\int d\epsilon\int d\Omega\,
n_\gamma(\epsilon,\Omega)
(1-\beta_p\mu)
\sigma_i(\bar\epsilon)K_i(\bar\epsilon),
$$

其中

$$
\bar\epsilon=\gamma_p\epsilon(1-\beta_p\mu).
$$

Formula ID：`HAD-PGAMMA-BH-GENERAL-RATE-001`。

若 photon field 各向同性，则 \(n_\gamma(\epsilon,\Omega)=n_\gamma(\epsilon)/(4\pi)\)，方向积分化为

$$
t_i^{-1}(\gamma_p)
=
{c\over2}
\int d\epsilon\,n_\gamma(\epsilon)
\int_{-1}^{1}d\mu\,
(1-\beta_p\mu)
\sigma_i(\bar\epsilon)K_i(\bar\epsilon).
$$

这里的 \(K_i\) 只适合能量损失率。若目标是 secondary spectrum，不能只用 inelasticity，必须使用 differential yield。

## 4. Detailed derivation：\(\mu\to\bar\epsilon\) 换元

从

$$
\bar\epsilon=\gamma_p\epsilon(1-\beta_p\mu)
$$

出发，对固定 \(\gamma_p,\epsilon\)，有

$$
d\bar\epsilon=-\gamma_p\beta_p\epsilon\,d\mu.
$$

当 \(\mu=1\) 时，\(\bar\epsilon_{\min}=\gamma_p\epsilon(1-\beta_p)\)；当 \(\mu=-1\) 时，

$$
\bar\epsilon_{\max}
=
\gamma_p\epsilon(1+\beta_p)
\simeq 2\gamma_p\epsilon.
$$

ultrarelativistic proton 下，\(\bar\epsilon_{\min}\) 很小，可近似把下限取为 channel threshold。于是 isotropic rate 变为

$$
t_i^{-1}(\gamma_p)
=
{c\over2}
\int d\epsilon\,n_\gamma(\epsilon)
\int d\bar\epsilon\,
{1-\beta_p\mu\over\gamma_p\beta_p\epsilon}
\sigma_i(\bar\epsilon)K_i(\bar\epsilon).
$$

用 \(1-\beta_p\mu=\bar\epsilon/(\gamma_p\epsilon)\)，得到

$$
t_i^{-1}(\gamma_p)
\simeq
{c\over2\gamma_p^2}
\int d\epsilon\,{n_\gamma(\epsilon)\over\epsilon^2}
\int_{\bar\epsilon_{\rm thr}}^{2\gamma_p\epsilon}
d\bar\epsilon\,
\bar\epsilon\,\sigma_i(\bar\epsilon)K_i(\bar\epsilon).
$$

交换积分次序，得到常见形式：

$$
t_i^{-1}(\gamma_p)
=
{c\over2\gamma_p^2}
\int_{\bar\epsilon_{\rm thr}}^\infty
d\bar\epsilon\,
\bar\epsilon\,\sigma_i(\bar\epsilon)K_i(\bar\epsilon)
\int_{\bar\epsilon/(2\gamma_p)}^\infty
d\epsilon\,{n_\gamma(\epsilon)\over\epsilon^2}.
$$

Formula ID：`HAD-PGAMMA-BH-ISOTROPIC-RATE-001`。

这就是 05 页 `HAD-PGAMMA-RATE-INTEGRAL-001` 的详细换元来源。它也说明了为什么 threshold helper 只是一层：真正的 rate 还需要 photon spectrum、cross-section、inelasticity 和积分范围。

## 5. \(p\gamma\) secondary yield

若要 gamma、neutrino 或 secondary electron spectrum，必须写成 yield integral：

$$
Q_s(E_s)
=
\int dE_p\,N_p(E_p)
\int d\epsilon\int d\mu\,
{1-\beta_p\mu\over2}c\,n_\gamma(\epsilon)
{d\sigma_{p\gamma\to s}\over dE_s}
(E_s;E_p,\epsilon,\mu).
$$

Formula ID：`HAD-PGAMMA-SECONDARY-YIELD-001`。

更通用地，把 channel 分解为 resonance、direct pion、multi-pion、kaon 等：

$$
{d\sigma_{p\gamma\to s}\over dE_s}
=
\sum_a
\sigma_a(\bar\epsilon)
{dN_{s,a}\over dE_s}
(E_s;E_p,\bar\epsilon).
$$

Formula ID：`HAD-PGAMMA-CHANNEL-SUM-001`。

Delta approximation 是把这一组 yield 压成

$$
{dN_s\over dE_s}
\rightarrow
N_s\delta(E_s-k_sE_p),
$$

只适合 sanity check 或数量级教学。它不能替代 SOPHIA / NeuCosmA / AM3 或文献参数化中的多通道 yield。

## 6. Bethe-Heitler pair injection 与 loss rate

BH 通道：

$$
p+\gamma\to p+e^++e^-.
$$

阈值为

$$
\bar\epsilon_{\rm BH,thr}\simeq2m_ec^2.
$$

Formula ID：`HAD-BH-REST-THRESHOLD-001`。

但阈值低不代表能量损失一定占优。BH 的典型 inelasticity 很小，通常需要 loss rate：

$$
t_{\rm BH}^{-1}(\gamma_p)
=
{c\over2\gamma_p^2}
\int_{\bar\epsilon_{\rm BH,thr}}^\infty
d\bar\epsilon\,
\bar\epsilon\,\sigma_{\rm BH}(\bar\epsilon)K_{\rm BH}(\bar\epsilon)
\int_{\bar\epsilon/(2\gamma_p)}^\infty
d\epsilon\,{n_\gamma(\epsilon)\over\epsilon^2}.
$$

Formula ID：`HAD-BH-LOSS-RATE-001`。

pair injection 则必须保留 electron / positron 的 differential distribution：

$$
Q_{e^\pm}(E_e)
=
\int dE_p\,N_p(E_p)
\int d\epsilon\int d\mu\,
{1-\beta_p\mu\over2}c\,n_\gamma(\epsilon)
{d\sigma_{\rm BH}\over dE_e}.
$$

Formula ID：`HAD-BH-PAIR-INJECTION-001`。

这也是当前 `bethe_heitler_threshold_proton_energy_gev()` 与完整 BH solver 的差异来源：前者只问“有没有达到运动学阈值”，后者还要回答“损失率多大、pair 注入到哪个能段、这些 pair 如何 synchrotron / IC cooling”。

## 7. 与 neutrino / cascade 的连接

\(p\gamma\) 与 BH 不是孤立发射机制。\(p\gamma\) 产生的 \(\pi^0\) photons 会遭遇 \(\gamma\gamma\) absorption；\(\pi^\pm\) 与 \(\mu^\pm\) 可能在衰变前 synchrotron cooling；BH pairs 会进入 electron / positron transport。

最小连接式可以写成

$$
Q_{\gamma,e,\nu}^{\rm had}
=
Q^{p\gamma}_{\gamma,e,\nu}
+Q^{\rm BH}_{e^\pm}
+Q^{pp}_{\gamma,e,\nu},
$$

然后进入 coupled transport：

$$
{\partial N_\gamma\over\partial t}
=Q_\gamma-c\alpha_{\gamma\gamma}N_\gamma+\cdots,
\qquad
{\partial N_e\over\partial t}
=Q_e-{\partial\over\partial\gamma}(\dot\gamma N_e)+\cdots.
$$

Formula ID：`HAD-PGAMMA-BH-CASCADE-ENTRY-001`。

本页只建立入口，不声称完成 cascade。若没有 transport 方程，不能把 \(p\gamma\) yield 或 BH pair injection 直接写成 escaped photon spectrum。

## 8. 接口契约

未来 \(p\gamma\) / BH solver 至少需要：

| 类别 | 必需输入 / 输出 | 说明 |
| --- | --- | --- |
| primary spectrum | \(N_p(E_p)\) 或 \(n_p(E_p)\) | total / density convention 必须登记 |
| photon field | \(n_\gamma(\epsilon)\) 或 \(n_\gamma(\epsilon,\Omega)\) | anisotropic photon field 需要保留角度 |
| channel kernels | \(\sigma(\bar\epsilon)\), \(K(\bar\epsilon)\), yield tables | 不能只给 threshold |
| output species | \(\gamma,\nu,e^\pm,n,p\) 等 | 不同成熟库覆盖 species 不同 |
| cooling / transport hooks | pion/muon cooling、BH pair cooling、gamma-gamma opacity | 决定 escaped spectrum |
| benchmark convention | SOPHIA / NeuCosmA / AM3 / Kelner-Aharonian / CRPropa 等 | 必须记录版本、能区、单位和 channel coverage |

Formula ID：`HAD-PGAMMA-BH-INTERFACE-CONTRACT-001`。

代码层建议拆成：

```text
target photon field builder
  -> p-gamma / BH kernel table
  -> secondary yield integrator
  -> cooling / cascade connector
  -> benchmark adapter
```

不要把 yield、cooling、cascade 和 detector event-rate 混在一个函数里，否则课程页无法解释差异来源。

## 9. 当前代码边界

| 函数 / 文件 | 当前层级 | 边界 |
| --- | --- | --- |
| `hadronic.py::pgamma_threshold_proton_energy_gev` | teaching threshold | 不给 rate 或 spectrum |
| `hadronic.py::bethe_heitler_threshold_proton_energy_gev` | teaching threshold | 不给 pair injection |
| `cooling_angle.py::photohadronic_threshold_loss_envelope_gev` | threshold envelope | 不是 cooling table |
| `teaching.py::teaching_pgamma_threshold_envelope_gev` | teaching wrapper | 只用于课程图示 |
| `hadronic.py::pp_kafexhiu_lut_pion_decay_sed_erg_cm2_s` | pp gamma mature route | 不含 \(p\gamma\) / BH |
| `production.py` hadronic registry | production dispatch for implemented pieces | 不注册 \(p\gamma\) spectrum 或 BH injection |

Formula ID：`HAD-PGAMMA-BH-CODE-BOUNDARY-001`。

因此当前可声称：已有 threshold / envelope、pp gamma package-compatible route、proton synchrotron route、secondary decay-vs-cooling regime helper。不能声称：已有 photohadronic Monte Carlo、BH pair injection spectrum、neutrino spectrum、photohadronic cooling table 或 hadronic cascade。

## 10. Exact analytic status

| 对象 | 状态 | 说明 |
| --- | --- | --- |
| \(\bar\epsilon=\gamma_p\epsilon(1-\beta\mu)\) | closed | 纯运动学 |
| isotropic rate 换元 | formal closed integral | 仍需数值积分 |
| \(p\gamma\) cross-section / yields | table / parameterization / Monte Carlo | 多通道，无简单闭式 |
| BH loss rate | table / numerical integral | 小 inelasticity，连续损失常用 |
| BH pair injection | differential kernel / table | 需要 pair energy distribution |
| neutrino / gamma escaped spectrum | transport problem | 需要 cooling、opacity、cascade |

Formula ID：`HAD-PGAMMA-BH-EXACT-STATUS-001`。

## 11. Benchmark boundary

| Benchmark route | 可检查 | 不能证明 |
| --- | --- | --- |
| SOPHIA | \(p\gamma\) event/yield behavior | 本地源几何或 cascade 完成 |
| NeuCosmA / AM3 | photohadronic neutrino / cascade convention | 唯一物理标准 |
| Kelner-Aharonian-style parameterization | analytic / tabulated yield trend | 全能区完整 channel coverage |
| CRPropa loss tables | propagation / BH loss scale | source-local pair spectrum |
| local threshold helper | kinematic scale | spectrum / cooling / event rate |

Formula ID：`HAD-PGAMMA-BH-BENCHMARK-BOUNDARY-001`。

最低验证路线应包括：threshold 随 photon energy 反比下降；BH threshold 低于 pion threshold；isotropic rate 对 photon density 线性；monoenergetic photon field 下积分限与 \(\bar\epsilon_{\rm thr}/(2\gamma_p)\) 一致；外部 benchmark 只在 same-input convention 下比较。

## 12. 不声称

- 不声称本页实现 \(p\gamma\) 或 BH solver。
- 不声称 \(E_\nu\simeq0.05E_p\) 是 neutrino spectrum。
- 不声称 threshold helper 可以给 cooling time。
- 不声称 BH threshold 低就代表 BH luminosity 大。
- 不声称 SOPHIA、NeuCosmA、AM3、CRPropa 或任意外部表格是唯一理论标准。
- 不声称 hadronic gamma / neutrino 是 GRB 221009A 或任何事件的唯一解释。

## 13. 参考入口

- `05-hadronic-order-of-magnitude.md`
- `12-missing-process-interface-roadmap.md`
- `03-gamma-gamma-opacity.md`
- `../grb-afterglow/11-particle-acceleration-and-maximum-energy.md`
- `../grb-afterglow/12-cascade-neutrino-and-propagation-boundaries.md`
- `reproduce/grb/core/radiation/hadronic.py`
- `reproduce/grb/core/radiation/cooling_angle.py`
