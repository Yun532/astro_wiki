# 03 Gamma-Gamma Opacity

状态：v2.3 课程讲义草案。本页按 `physical picture -> reference frame -> general expression -> detailed derivation block -> exact analytic status -> approximation hierarchy -> code convention` 组织。核心规则是：先从 radiative transfer 的吸收项和 two-photon collision kernel 出发，再推阈值、角权重、Breit-Wheeler cross-section 和光深积分；`tau=n sigma l` 只能作为最后的量级近似，不能反过来当作理论起点。

## 1. 物理图像

高能 photon 可以和低能 target photon 湮灭成 electron-positron pair：

```text
gamma(E) + gamma(epsilon) -> e+ + e-.
```

这不是新的发射机制，而是传播和源内吸收机制。它在辐射转移方程中扮演 absorption coefficient 的角色：

```text
intrinsic high-energy spectrum
  -> internal gamma-gamma absorption
  -> EBL / IGM attenuation during propagation
  -> observed attenuated spectrum
```

两光子对产生有一个非常重要的角度事实：只有相向碰撞才有效。两束 photon 若完全平行，中心质心能量为零，不会产生 pair；head-on collision 的阈值最低。因此 gamma-gamma opacity 的课程推导必须保留角积分，不能只写成一个固定截面。

## 2. 参考系与变量表

本页默认在 target photon field 的局域静止系中推导。对源内 opacity，这通常是发射等离子体共动系；对 EBL opacity，则是随红移演化的宇宙学局域系。若要接观测能量，需要额外处理 Doppler factor、redshift 和路径长度，这些属于应用模型，不属于 two-photon kernel 本身。

| 符号 | 含义 | 单位或量纲 |
| --- | --- | --- |
| \(E\) | high-energy photon energy | erg / eV / keV |
| \(\epsilon\) | target photon energy | erg / eV / keV |
| \(\theta\) | 两光子传播方向夹角 | rad |
| \(\mu=\cos\theta\) | collision angle cosine | dimensionless |
| \(n(\epsilon,\Omega)\) | target photon number density per energy per solid angle | cm\(^{-3}\) erg\(^{-1}\) sr\(^{-1}\) |
| \(n(\epsilon)\) | 已对方向积分的 isotropic target spectrum | cm\(^{-3}\) erg\(^{-1}\) |
| \(\sigma_{\gamma\gamma}\) | Breit-Wheeler cross-section | cm\(^2\) |
| \(x\) | threshold parameter \(E\epsilon(1-\mu)/[2(m_ec^2)^2]\) | dimensionless |
| \(\beta\) | pair center-of-mass frame 中 \(e^\pm\) speed / \(c\) | dimensionless |
| \(\alpha_{\gamma\gamma}\) | absorption coefficient | cm\(^{-1}\) |
| \(\tau_{\gamma\gamma}\) | optical depth | dimensionless |

## 3. General Expression：吸收系数和光深

radiative transfer 的纯吸收形式为：

$$
\frac{dI_E}{ds}
=
-\alpha_{\gamma\gamma}(E,s)I_E .
$$

若沿光路积分：

$$
I_E(s)
=
I_E(0)\exp[-\tau_{\gamma\gamma}(E)],
\qquad
\tau_{\gamma\gamma}(E)
=
\int_0^s \alpha_{\gamma\gamma}(E,s')\,ds' .
$$

对各向异性 target photon field，吸收系数的一般表达式是：

$$
\alpha_{\gamma\gamma}(E)
=
\int_0^\infty d\epsilon
\int d\Omega\,
n(\epsilon,\Omega)\,
(1-\mu)\,
\sigma_{\gamma\gamma}(E,\epsilon,\mu).
$$

这里的 \((1-\mu)\) 来自两束 photons 的相对通量。更直观地说，一个 high-energy photon 穿过 target photon bath 时，来自方向 \(\Omega\) 的 photon encounter rate 正比于 \(c(1-\mu)\)；把每单位时间的碰撞率除以路径速度 \(c\)，就得到每单位长度的吸收概率。

若 target photon field 各向同性，且 \(n(\epsilon)\) 已经是对全部方向积分后的 number density spectrum，则：

$$
n(\epsilon,\Omega)
=
\frac{n(\epsilon)}{4\pi}.
$$

利用 \(d\Omega=2\pi d\mu\)，得到：

$$
\alpha_{\gamma\gamma}(E)
=
\frac{1}{2}
\int_{-1}^{1}d\mu\,(1-\mu)
\int_0^\infty d\epsilon\,n(\epsilon)\,
\sigma_{\gamma\gamma}(E,\epsilon,\mu).
$$

如果另一本教材把 \(n(\epsilon)\) 定义为每单位立体角的 density，则前面的 \(1/2\) 或 \(4\pi\) 会重新分配。这是 convention 差异，不是物理差异。

Formula ID：`GG-ABS-COEFF-FORMAL-001`，状态：course-derived / theory-only for full anisotropic field。

## 4. 详细解析推导：从不变量到各向同性吸收核

本节把 gamma-gamma opacity 中常被压缩的步骤展开：不从 `n sigma l` 开始，而是从四动量不变量、阈值、角变量换元和 Breit-Wheeler kernel 推到可数值计算的吸收系数。

### 4.1 目标公式

目标是推出各向同性 monoenergetic target photon bath 的吸收系数：

$$
\alpha_{\gamma\gamma}(E)
=
\frac{n_0}{2}
\int_{-1}^{1}d\mu\,(1-\mu)\,
\sigma_{\gamma\gamma}[x(E,\epsilon_0,\mu)],
$$

并通过换元 \(x=E\epsilon_0(1-\mu)/[2(m_ec^2)^2]\) 写成：

$$
\alpha_{\gamma\gamma}(E)
=
\frac{n_0}{2A^2}
\int_1^{2A}x\,\sigma_{\gamma\gamma}(x)\,dx,
\qquad
A=\frac{E\epsilon_0}{2(m_ec^2)^2},
$$

其中当 \(2A<1\) 时积分为零。这个式子已经比 \(\tau=n\sigma_{\rm eff}l\) 多保留了阈值、角权重和截面形状。

### 4.2 物理设定

考虑一个能量为 \(E\) 的 test photon 穿过均匀、各向同性、单能 target photon bath：

$$
n(\epsilon)
=
n_0\delta(\epsilon-\epsilon_0).
$$

这里 \(n_0\) 是总 number density，单位 cm\(^{-3}\)。各向同性意味着每个方向上的 photon density 为 \(n_0/(4\pi)\)，不是说碰撞角无关。碰撞角仍然通过 \((1-\mu)\) 和阈值进入。

### 4.3 四动量不变量和阈值

两 photons 的四动量为 \(p_1\)、\(p_2\)。在使用能量平方作为不变量单位的写法中：

$$
s
=
(p_1+p_2)^2c^2
=
2E\epsilon(1-\mu).
$$

单个 photon 的不变量为零，因此只剩交叉项。pair production 的阈值要求中心质心能量至少等于两个 electron rest energy：

$$
s_{\rm thr}
=
(2m_ec^2)^2
=
4m_e^2c^4.
$$

因此：

$$
2E\epsilon(1-\mu)
\ge
4m_e^2c^4.
$$

解出 target photon threshold：

$$
\epsilon_{\rm thr}
=
\frac{2(m_ec^2)^2}{E(1-\mu)}.
$$

head-on collision 中 \(\mu=-1\)，于是：

$$
\epsilon_{\rm thr,head-on}
=
\frac{(m_ec^2)^2}{E}.
$$

这就是常用的 TeV photon 对 IR/optical EBL 敏感、GeV photon 对 X-ray/soft-gamma target 更敏感的来源。

代码：`pair_threshold_target_energy_kev()`  
Formula ID：`GG-PAIR-THRESHOLD-001`。

### 4.4 阈值参数、反函数和 Jacobian

定义无量纲 threshold parameter：

$$
x
=
\frac{E\epsilon(1-\mu)}
{2(m_ec^2)^2}.
$$

pair production allowed 当且仅当：

$$
x\ge1.
$$

固定 \(E\) 与 \(\epsilon\)，定义：

$$
A
=
\frac{E\epsilon}{2(m_ec^2)^2},
\qquad
x=A(1-\mu).
$$

反解角变量：

$$
\mu
=
1-\frac{x}{A}.
$$

微分给出 Jacobian：

$$
d\mu
=
-\frac{dx}{A}.
$$

同时角权重满足：

$$
1-\mu
=
\frac{x}{A}.
$$

因此：

$$
(1-\mu)d\mu
=
-\frac{x}{A^2}dx.
$$

当 \(\mu\) 从 \(-1\) 到 \(1\) 时，\(x\) 从 \(2A\) 到 \(0\)。翻转积分限后：

$$
\frac{1}{2}
\int_{-1}^{1}d\mu\,(1-\mu)\sigma_{\gamma\gamma}(x)
=
\frac{1}{2A^2}
\int_0^{2A}x\,\sigma_{\gamma\gamma}(x)\,dx.
$$

由于 \(\sigma_{\gamma\gamma}=0\) for \(x<1\)，真正的下限是 \(1\)：

$$
\frac{1}{2}
\int_{-1}^{1}d\mu\,(1-\mu)\sigma_{\gamma\gamma}(x)
=
\frac{1}{2A^2}
\int_1^{2A}x\,\sigma_{\gamma\gamma}(x)\,dx,
\qquad
2A\ge1.
$$

这一步是 gamma-gamma opacity 的关键 Jacobian：完整 isotropic opacity 不是固定 cross-section，而是角度、阈值和 Breit-Wheeler kernel 的卷积。

代码：`gamma_gamma_invariant_threshold_parameter()`  
Formula ID：`GG-INVARIANT-S-001`。

### 4.5 Breit-Wheeler cross-section

当 \(x\ge1\)，pair center-of-mass frame 中电子或正电子速度为：

$$
\beta
=
\sqrt{1-\frac{1}{x}}.
$$

Breit-Wheeler total cross-section 为：

$$
\sigma_{\gamma\gamma}(\beta)
=
\frac{3}{16}\sigma_T(1-\beta^2)
\left[
(3-\beta^4)\ln\frac{1+\beta}{1-\beta}
-2\beta(2-\beta^2)
\right].
$$

这条公式来自 QED two-photon pair-production amplitude 的总截面积分。本页不重推 QED amplitude；课程层需要追踪的是：它作为 two-photon numerical kernel，被阈值变量 \(x\) 和角积分调用。

三个极限可直接从式子看出：

threshold 附近，\(\beta\to0\)，使用：

$$
\ln\frac{1+\beta}{1-\beta}
=
2\left(\beta+\frac{\beta^3}{3}+\cdots\right),
$$

可得：

$$
\sigma_{\gamma\gamma}
\simeq
\frac{3}{8}\sigma_T\beta
+O(\beta^3),
$$

所以刚过阈值时截面从零线性升起。

在中间能量，截面达到最大值，约为 \(0.25\sigma_T\)，位置在 \(x\) 为几的量级。这就是 effective-opacity 估计常取 \(f_\sigma\sigma_T\)、且 \(f_\sigma\sim0.1\) 到 \(0.2\) 的原因；但这个数值只是角度和谱平均后的量级，不是完整 kernel。

高能端，\(\beta\to1\)，可得：

$$
\sigma_{\gamma\gamma}
\simeq
\frac{3\sigma_T}{8x}
\left[\ln(4x)-1\right].
$$

因此远高于阈值的目标 photon 并不会无限提高 opacity；截面大致按 \(\ln x/x\) 下降。

代码：`gamma_gamma_cross_section_cgs()`、`breit_wheeler_cross_section_cgs()`  
Formula ID：`GG-BREIT-WHEELER-SIGMA-001`。

### 4.6 对 target photon spectrum 的积分

把 monoenergetic target 推广到任意各向同性 target spectrum：

$$
\alpha_{\gamma\gamma}(E)
=
\frac{1}{2}
\int_{-1}^{1}d\mu\,(1-\mu)
\int_0^\infty d\epsilon\,n(\epsilon)
\sigma_{\gamma\gamma}[x(E,\epsilon,\mu)].
$$

对每个 \(\epsilon\)，角积分的 allowed range 由：

$$
x=A(1-\mu)\ge1
$$

决定。若 \(2A<1\)，即使是 head-on collision 也不到阈值，该 \(\epsilon\) 对 opacity 没有贡献。若 \(2A\ge1\)，角积分下限等价于：

$$
\mu
\le
1-\frac{1}{A}.
$$

所以完整数值实现可以选择两种等价路线：

1. 在 \((\epsilon,\mu)\) 上直接积分，并让 cross-section 在 \(x<1\) 时返回 0。
2. 先对角变量换成 \(x\)，对每个 \(\epsilon\) 做 \(\int_1^{2A}x\sigma(x)dx/(2A^2)\)，再对 \(\epsilon\) 积分。

本地 `isotropic_tabulated_absorption_coefficient_cgs()` 采用第一种透明路线；未来的 mature method 可以预积分第二种 angle kernel。

Formula ID：`GG-ABS-COEFF-TABULATED-001`。

## 5. Exact Analytic Status

gamma-gamma opacity 的解析状态需要分层说明：

| 层级 | 是否有闭式表达 | 说明 |
| --- | --- | --- |
| threshold kinematics | 有 | 四动量不变量直接给出 \(\epsilon_{\rm thr}\) |
| Breit-Wheeler total cross-section | 有 | \(\sigma_{\gamma\gamma}(\beta)\) 是闭式 kernel |
| monoenergetic isotropic absorption coefficient | 一维半解析 | 可化成 \(\int_1^{2A}x\sigma(x)dx\)，通常数值积分 |
| arbitrary isotropic target spectrum | 一般无短闭式解 | 需要对 target spectrum 与 angle kernel 卷积 |
| anisotropic / spatially varying source | 一般无闭式解 | 还要积分方向、位置、路径、时间和几何 |
| EBL optical depth | 模型表或数值积分 | 依赖 cosmology、redshift evolution 和 EBL model |

因此，本页的“精确 kernel”不是说任意 \(\tau_{\gamma\gamma}\) 都有短解析公式，而是说基础 two-photon cross-section 和 formal absorption integral 清楚。真正的源内或宇宙学 opacity 通常属于 numerical-kernel / mature-method 层。

## 6. Analytic / Semi-Analytic Limits

### 6.1 Head-on threshold check

head-on 时：

$$
\epsilon_{\rm thr}
=
\frac{(m_ec^2)^2}{E}.
$$

若 \(E=1\,{\rm TeV}\)，则 target threshold 在 \(\epsilon\sim0.26\,{\rm eV}\) 量级，对应红外。这个估计只定位最小阈值；真正吸收最强的位置还要乘上 cross-section peak 和 target photon spectrum。

### 6.2 Monoenergetic isotropic target field

对：

$$
n(\epsilon)=n_0\delta(\epsilon-\epsilon_0),
$$

吸收系数为：

$$
\alpha_{\gamma\gamma}(E)
=
\frac{n_0}{2A^2}
\int_1^{2A}x\,\sigma_{\gamma\gamma}(x)\,dx,
\qquad
A=\frac{E\epsilon_0}{2(m_ec^2)^2}.
$$

若 \(2A<1\)，\(\alpha_{\gamma\gamma}=0\)。若 \(2A\) 只略大于 1，积分主要来自 threshold 附近，\(\sigma\propto\sqrt{1-1/x}\)。若 \(2A\gg1\)，高能端 \(\sigma\sim\ln x/x\)，但积分还受到 \(1/(2A^2)\) 的角平均前因子控制。

Formula ID：`GG-ABS-COEFF-MONO-001`。

### 6.3 Tabulated target photon field

若调用方给出 target photon spectrum \(n_i=n(\epsilon_i)\)，则：

$$
\alpha_{\gamma\gamma}(E)
\simeq
\sum_i \Delta\epsilon_i\,n(\epsilon_i)
\left[
\frac{1}{2}\int_{-1}^{1}d\mu\,(1-\mu)
\sigma_{\gamma\gamma}(E,\epsilon_i,\mu)
\right].
$$

实际代码可用 linear grid、log grid 或 adaptive quadrature。这个离散式的物理要求是：target spectrum 的单位必须是 cm\(^{-3}\) per energy，且能量单位转换不能混入 SED 或 luminosity density 的定义。

### 6.4 Effective opacity 作为最后的量级近似

若只想估计源内是否可能 optically thick，可以把 target field 压成一个有效 density 和有效 cross-section：

$$
\tau_{\rm toy}
=
n_{\rm target}\sigma_{\rm eff}l,
\qquad
\sigma_{\rm eff}=f_\sigma\sigma_T.
$$

这个式子牺牲了：

- target photon spectrum。
- collision angle distribution。
- threshold cutoff。
- Breit-Wheeler peak 和 high-energy decline。
- 空间几何和路径演化。

它保留的只有 optical depth 的量纲结构。因此它适合做 compactness sanity check，不适合做完整 TeV attenuation curve。

代码：`internal_gamma_gamma_opacity()`  
Formula ID：`GG-TAU-INTERNAL-001`。

## 7. EBL Attenuation Boundary

外部传播可写成：

$$
F_{\rm obs}(E_0)
=
F_{\rm int}(E_0)
\exp[-\tau_{\rm internal}(E_0)-\tau_{\rm EBL}(E_0,z_s)].
$$

EBL optical depth 的一般表达式为：

$$
\tau_{\rm EBL}(E_0,z_s)
=
\int_0^{z_s} dz\,
\frac{dl}{dz}
\int_0^\infty d\epsilon\,n_{\rm EBL}(\epsilon,z)
\int_{-1}^{1}\frac{d\mu}{2}(1-\mu)
\sigma_{\gamma\gamma}[E_0(1+z),\epsilon,\mu].
$$

这里 \(E_0(1+z)\) 是 photon 在红移 \(z\) 处的能量。\(n_{\rm EBL}(\epsilon,z)\)、宇宙学参数和星系演化模型决定 \(\tau_{\rm EBL}\)。本项目不把 Dominguez、Franceschini、Finke、Gilmore 或 `ebltable` 任何一个表写成唯一标准；它们只能作为 external model / benchmark-output。

代码：`ebl_attenuation_factor()`、`combined_gamma_gamma_attenuation()`  
Formula ID：`GG-EBL-ATTEN-001`。

## 8. Numerical / Code Approximation

当前本地代码分成四层：

| 层级 | 对应物理 | 代码/输出 | 边界 |
| --- | --- | --- | --- |
| two-photon kernel | threshold parameter 与 Breit-Wheeler cross-section | `gamma_gamma_cross_section_cgs()`、`breit_wheeler_cross_section_cgs()` | 不含 target spectrum 或路径积分 |
| isotropic numerical kernel | monoenergetic / tabulated target field 的角度和谱积分 | `isotropic_monoenergetic_absorption_coefficient_cgs()`、`isotropic_tabulated_absorption_coefficient_cgs()`、`production.py::evaluate_gamma_gamma_target_spectrum_opacity_curve()` | 调用方必须提供 photon field |
| source-agnostic local opacity workbench | 局域区给出 tabulated target spectrum 与 path length | `evaluate_local_gamma_gamma_opacity_screening()` / `RAD-ZONE-GG-TABULATED-OPACITY-SCREEN-001` | target spectrum 与 path length provenance 由调用方负责 |
| source-adapter screen | 具体源模型给出局域路径长度与 target photon envelope | `forward_shock_gamma_gamma_opacity_screening()` / `AG-FS-GG-OPACITY-SCREEN-001`; `forward_shock_gamma_gamma_target_spectrum_screening()` / `AG-FS-GG-TARGET-SPECTRUM-SCREEN-001` | mono 或 tabulated target envelope；仍不是 self-consistent photon transfer |
| angle convention helpers | 教学和动力学接口用的角权重与 angle-averaged cross-section | `gamma_gamma_angle_weight()`、`gamma_gamma_angle_averaged_cross_section_cgs()`、`head_on_gamma_gamma_cross_section_cgs()` | monoenergetic isotropic 或 head-on kernel |
| toy/event diagnostic | \(\tau=n\sigma_{\rm eff}l\) 与 \(\exp(-\tau)\) | `internal_gamma_gamma_opacity()`、`ebl_attenuation_factor()` | 只做量级和 attenuation factor |

当前代码没有完成：

- full anisotropic angular-spectral transfer。
- 从 observed SED 自动反演源内 target photon density。
- EBL model 内置、宇宙学 EBL 积分或 EBL uncertainty propagation。
- pair cascade、secondary pair injection 和 reprocessed emission。

## 9. 从推导到代码的实现约定

课程推导采用的是：

$$
\alpha_{\gamma\gamma}(E)
=
\int d\epsilon\int d\Omega\,
n(\epsilon,\Omega)(1-\mu)
\sigma_{\gamma\gamma}[x(E,\epsilon,\mu)].
$$

本地 reference helpers 的实际约定是：

- photon energies 在 `gamma_gamma.py` 中用 keV 输入。
- `gamma_gamma_invariant_threshold_parameter()` 返回本页的 \(x\)，即 \(s/s_{\rm thr}\)。
- `gamma_gamma_cross_section_cgs()` 是 two-photon kernel，不负责 target spectrum。
- `isotropic_monoenergetic_absorption_coefficient_cgs()` 实现

$$
\alpha_{\gamma\gamma}
=
\frac{n_0}{2}
\int_{-1}^{1}d\mu\,(1-\mu)\sigma_{\gamma\gamma}.
$$

- `isotropic_tabulated_absorption_coefficient_cgs()` 实现

$$
\alpha_{\gamma\gamma}
=
\frac{1}{2}\int d\mu(1-\mu)\int d\epsilon\,
n(\epsilon)\sigma_{\gamma\gamma}.
$$

- `gamma_gamma_angle_weight(mu)` 返回 \((1-\mu)/2\)，它是 isotropic angular average convention 下的权重 helper，不是完整 opacity。
- `production.py::gamma_gamma_target_spectrum_absorption_coefficient_cgs()` 与 `production.py::evaluate_gamma_gamma_target_spectrum_opacity_curve()` 只把同一 numerical kernel 接成后续动力学可调用的绿色 API，并输出 `alpha`、`tau=alpha*l` 与 `exp(-tau)`；这不是新的物理公式。
- `production.py::evaluate_local_gamma_gamma_opacity_screening()` 是 source-agnostic local-zone workbench：调用方已给出 target spectrum 和 path length，它只批量输出局域 opacity curve。
- `models/forward_shock/local_zone.py::forward_shock_gamma_gamma_opacity_screening()` 只把 BM local-zone 的 \(l'=f_RR/\Gamma\) 和调用方给定的 \(U'_{\rm ph},\epsilon'_{\rm seed}\) 组合成 mono target density \(n'=U'_{\rm ph}/\epsilon'_{\rm seed}\)，再调用 `GG-ABS-COEFF-MONO-001`。它没有从 observed flux 反演 photon density，也没有生成 synchrotron target spectrum。
- `models/forward_shock/local_zone.py::forward_shock_gamma_gamma_target_spectrum_screening()` 接受 caller-supplied target spectral shape，并在每个时间点归一化到 \(U'_{\rm ph}=f_{\rm ph}e'\)，再调用 `RAD-ZONE-GG-TABULATED-OPACITY-SCREEN-001`。这仍是 target-envelope screen，不是 SSC photon transfer。
- EBL helper 只接收外部给定的 \(\tau_{\rm EBL}\)，然后返回 \(\exp(-\tau_{\rm EBL})\)。

如果后续代码采用 mature method，例如预积分 angle kernel、tabulated EBL、log-grid target spectrum integration、GPU/table interpolation 或外部传播软件，课程页必须说明替换了哪一步：

$$
\int d\epsilon\int d\mu\,(1-\mu)\sigma_{\gamma\gamma}
\rightarrow
\text{tabulated / pre-integrated / package-compatible kernel}.
$$

曲线差异常来自：

- \(n(\epsilon)\) 是 per energy、per log energy、energy density 还是 SED。
- isotropic \(1/2\) convention 是否已吸收到 angular density。
- source comoving frame、observer frame 和 redshift/Doppler 的转换。
- EBL model、cosmology 和 optical-depth interpolation。
- energy grid、角度 grid 和 threshold 附近的采样。

这些差异主要影响归一化、turnover 位置、cutoff 形状和高能尾，不应被写成课程推导错误。

## 10. Benchmark Boundary

可对照的外部来源包括 EBL tables、`ebltable`、Gammapy 生态、CRPropa/ELMAG 类传播工具，以及文献给出的 \(\tau_{\rm EBL}(E,z)\)。这些 benchmark 只能回答：

- 给定同一个 EBL model 和同一组参数，attenuation factor 是否一致。
- 给定同一个 target photon field，angle/spectrum kernel 是否在数值上合理。
- 阈值、peak、小 \(x\) 和大 \(x\) fixed points 是否正确。

它们不能反推出 source intrinsic TeV mechanism，也不能把 observed TeV photon 写成某个唯一的辐射机制结论。

## 11. 代码映射与验证

代码：

```text
reproduce/grb/core/radiation/gamma_gamma.py
reproduce/grb/core/radiation/kernels.py
reproduce/grb/core/radiation/production.py
reproduce/grb/core/radiation/cooling_angle.py
reproduce/grb/core/radiation/production.py
```

验证：

```text
python -m reproduce.grb.validation.check_radiation_mechanisms_v1
python -m reproduce.grb.validation_lab.check_radiation_cooling_angle_v1
python -m reproduce.grb.validation_lab.check_radiation_production_suite_v1
```

验证重点：

- below threshold 时 cross-section 为 0。
- Breit-Wheeler cross-section 在阈值处为 0、在中间能量出现峰、在高能端下降。
- head-on collision 比 parallel collision 更容易过阈值。
- isotropic angle average 保留 \((1-\mu)/2\) convention。
- toy attenuation 严格为 \(\exp(-\tau)\)。

## 12. 不声称

- 不声称完成 full angular-spectral transfer。
- 不声称从 observed SED 自动构造真实 \(n_{\rm target}\)。
- 不内置任何 EBL model 为默认事实。
- 不声称 pair cascade 或 secondary emission 已经实现。
- 不声称某个 TeV photon 的 intrinsic origin。

## 13. 参考资料

- Breit & Wheeler 1934, *Collision of Two Light Quanta*.
- Gould & Schreder 1967, *Opacity of the Universe to High-Energy Photons*.
- Rybicki & Lightman, *Radiative Processes in Astrophysics*.
- Jauch & Rohrlich, *The Theory of Photons and Electrons*, two-photon pair production.
- Dwek & Krennrich 2013, EBL review.
- Dominguez, Franceschini, Finke, Gilmore 等 EBL model 文献。
