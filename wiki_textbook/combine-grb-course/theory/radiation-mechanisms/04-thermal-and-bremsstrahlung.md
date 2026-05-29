# 04 Thermal Components and Bremsstrahlung

状态：v2.3 课程讲义草案。本页按 `physical picture -> reference frame -> general expression -> detailed derivation block -> exact analytic status -> approximation hierarchy -> code convention` 组织。目标是把 thermal blackbody/photosphere、thermal free-free 和 nonthermal bremsstrahlung 拆清楚：blackbody 是热平衡 source function，thermal free-free 是 Maxwellian plasma 的碰撞辐射，nonthermal bremsstrahlung 是非热电子对目标气体的微分截面卷积。

## 1. 物理图像

热辐射和 bremsstrahlung 经常在同一个能段出现，但它们不是同一层概念：

- blackbody：物质和辐射达到局部热平衡，source function 变成 \(B_\nu(T)\)。
- photosphere：光深约为 1 的流体层，观测谱可能近似 thermal，但形状依赖 relativistic transfer、角结构和 subphotospheric dissipation。
- thermal free-free：Maxwellian electrons 在 ions Coulomb field 中偏转并辐射 continuum photons。
- nonthermal bremsstrahlung：power-law 或 cutoff electrons 与气体相互作用，产生 X-ray / gamma-ray continuum，必须用非热电子谱和微分截面卷积。

本页的逻辑链是：

```text
radiative transfer
  -> LTE detailed balance and Kirchhoff law
  -> Planck source function
  -> thermal free-free emissivity and absorption
  -> nonthermal bremsstrahlung cross-section integral
  -> code/reference/package-compatible boundaries
```

## 2. 参考系与变量表

本页默认在局域等离子体静止系中推导。带 bulk Lorentz factor 的 photosphere 或 GRB outflow 需要再做 Doppler、redshift、equal-arrival-time 和角度积分；这些属于动力学和观测映射，不属于本页的局域 radiation kernel。

| 符号 | 含义 | 单位或量纲 |
| --- | --- | --- |
| \(T\) | matter / radiation temperature | K 或 keV |
| \(R\) | effective emitting radius | cm |
| \(L\) | bolometric luminosity | erg s\(^{-1}\) |
| \(\Gamma\) | bulk Lorentz factor | dimensionless |
| \(n_e,n_i\) | electron / ion density | cm\(^{-3}\) |
| \(Z\) | ion charge number | dimensionless |
| \(\nu\) | photon frequency | Hz |
| \(E_\gamma=h\nu\) | photon energy | erg / eV |
| \(g_{\rm ff}\) | frequency-dependent free-free Gaunt factor | dimensionless |
| \(g_B\) | bolometric free-free Gaunt factor | dimensionless |
| \(N_e(E_e)\) | total nonthermal electron distribution | particles eV\(^{-1}\) |
| \(d\sigma_{\rm br}/dE_\gamma\) | bremsstrahlung differential cross-section | cm\(^2\) erg\(^{-1}\) |

## 3. General Expression

### 3.1 Radiative transfer and LTE

radiative transfer equation 为：

$$
\frac{dI_\nu}{ds}
=
j_\nu-\alpha_\nu I_\nu .
$$

定义 source function：

$$
S_\nu
=
\frac{j_\nu}{\alpha_\nu}.
$$

若物质和辐射处于局部热平衡，详细平衡要求吸收和发射在 Planck 辐射场中相互抵消，因此：

$$
S_\nu
=
B_\nu(T),
\qquad
j_\nu
=
\alpha_\nu B_\nu(T).
$$

这就是 Kirchhoff law。它不是任意辐射源都成立的公式；它要求 LTE 或至少局域详细平衡。thermal free-free absorption helper 正是用这一点从 emissivity 得到 absorption coefficient。

Formula ID：`RT-EINSTEIN-KIRCHHOFF-001`、`FF-ABSORPTION-KIRCHHOFF-001`。

### 3.2 Optically thin SED chain

若源区 optically thin，且 emission coefficient 为 angle-integrated emissivity \(\epsilon_\nu=4\pi j_\nu\)，则：

$$
L_\nu
=
\int \epsilon_\nu\,dV
=
\int 4\pi j_\nu\,dV.
$$

距离为 \(d\) 时：

$$
F_\nu
=
\frac{L_\nu}{4\pi d^2},
\qquad
\nu F_\nu
=
\nu\frac{L_\nu}{4\pi d^2}.
$$

若不是 optically thin，应回到 transfer solution：

$$
I_\nu
=
I_\nu(0)e^{-\tau_\nu}
+
S_\nu(1-e^{-\tau_\nu}).
$$

Formula ID：`RT-LNU-FNU-SED-001`。

### 3.3 Thermal and nonthermal bremsstrahlung formal integrals

thermal free-free 的核心是 Maxwellian average：

$$
\epsilon_\nu^{\rm ff}
=
n_en_i
\int d^3v\,f_M(\mathbf v;T)\,
\frac{dW_\nu(v,Z)}{d\nu},
$$

其中 \(dW_\nu/d\nu\) 是单个 electron-ion encounter 的辐射能量谱率。实际 textbook 公式把经典碰撞辐射、Maxwellian 平均和量子修正压缩为 Gaunt factor。

nonthermal bremsstrahlung 的一般 photon production rate 是：

$$
\frac{dN_\gamma}{dt\,dE_\gamma}
=
cn_{\rm target}
\int_{E_\gamma}^{\infty}
N_e(E_e)
\frac{d\sigma_{\rm br}}{dE_\gamma}(E_e,E_\gamma)\,
dE_e.
$$

两者不能混写：thermal free-free 的 \(T\) 来自 Maxwellian distribution；nonthermal bremsstrahlung 的谱形来自 \(N_e(E_e)\) 和微分截面。

## 4. Detailed Derivation I：Planck Function 到 Stefan-Boltzmann Law

### 4.1 目标公式

目标是从 Planck specific intensity：

$$
B_\nu(T)
=
\frac{2h\nu^3}{c^2}
\frac{1}{\exp(h\nu/kT)-1}
$$

推出 bolometric surface flux：

$$
F
=
\sigma_{\rm SB}T^4
$$

以及球面 luminosity：

$$
L
=
4\pi R^2\sigma_{\rm SB}T^4.
$$

### 4.2 频率积分和变量替换

对 Planck function 积分：

$$
\int_0^\infty B_\nu\,d\nu
=
\int_0^\infty
\frac{2h\nu^3}{c^2}
\frac{d\nu}{e^{h\nu/kT}-1}.
$$

定义：

$$
x
=
\frac{h\nu}{kT},
\qquad
\nu
=
\frac{kT}{h}x,
\qquad
d\nu
=
\frac{kT}{h}dx.
$$

代入后：

$$
\int_0^\infty B_\nu\,d\nu
=
\frac{2h}{c^2}
\left(\frac{kT}{h}\right)^4
\int_0^\infty
\frac{x^3}{e^x-1}dx.
$$

利用 Bose integral：

$$
\int_0^\infty
\frac{x^3}{e^x-1}dx
=
\frac{\pi^4}{15},
$$

得到：

$$
\int_0^\infty B_\nu\,d\nu
=
\frac{2\pi^4k^4}{15h^3c^2}T^4.
$$

定义：

$$
\frac{\sigma_{\rm SB}}{\pi}
=
\frac{2\pi^4k^4}{15h^3c^2},
$$

所以：

$$
\int_0^\infty B_\nu\,d\nu
=
\frac{\sigma_{\rm SB}}{\pi}T^4.
$$

### 4.3 角积分和 luminosity

黑体表面出射 flux 是半球投影积分：

$$
F_\nu
=
\int_{\rm hemisphere} I_\nu\cos\theta\,d\Omega.
$$

LTE blackbody 中 \(I_\nu=B_\nu(T)\) 与方向无关，于是：

$$
F_\nu
=
B_\nu
\int_0^{2\pi}d\phi
\int_0^{\pi/2}\cos\theta\sin\theta\,d\theta.
$$

内层积分：

$$
\int_0^{\pi/2}\cos\theta\sin\theta\,d\theta
=
\frac{1}{2}.
$$

因此：

$$
F_\nu
=
\pi B_\nu.
$$

再对频率积分：

$$
F
=
\pi\int_0^\infty B_\nu d\nu
=
\sigma_{\rm SB}T^4.
$$

球面半径 \(R\) 的 luminosity：

$$
L
=
4\pi R^2F
=
4\pi R^2\sigma_{\rm SB}T^4.
$$

对应 spectral luminosity：

$$
L_\nu
=
4\pi R^2F_\nu
=
4\pi^2R^2B_\nu(T).
$$

代码：`planck_function_nu_cgs()`、`blackbody_luminosity()`、`blackbody_spectral_luminosity_nu_cgs()`、`blackbody_sed_erg_cm2_s()`  
Formula IDs：`TH-BPLANCK-NU-001`、`TH-BB-L-001`、`TH-BB-LNU-001`、`TH-BB-SED-001`。

## 5. Photosphere：Optical Depth 半径标度

steady baryonic outflow 中 luminosity 与 mass flux 的数量级关系为：

$$
L
\simeq
\Gamma\dot M c^2,
\qquad
\dot M
\simeq
\frac{L}{\Gamma c^2}.
$$

coasting phase 的 comoving baryon density 取：

$$
n'
\simeq
\frac{\dot M}{4\pi R^2m_p\Gamma c}.
$$

向外传播 photon 在 lab-frame 半径 \(R\) 上看到的 comoving path length 约为 \(R/\Gamma\)，所以 Thomson optical depth：

$$
\tau_T
\simeq
n'\sigma_T\frac{R}{\Gamma}.
$$

令 \(\tau_T=1\)：

$$
1
\simeq
\frac{\dot M\sigma_T}{4\pi Rm_p\Gamma^2c}.
$$

代入 \(\dot M=L/(\Gamma c^2)\)：

$$
R_{\rm ph}
\simeq
\frac{L\sigma_T}{4\pi m_pc^3\Gamma^3}.
$$

不同 shell thickness、angular structure、acceleration phase 和 relativistic transfer 会改变数值因子。本地代码保留同一 \(\Gamma^{-3}\) 标度，但把几何因子显式暴露：

$$
R_{\rm ph}
=
\frac{L\sigma_T}{f_{\rm geom}\pi m_pc^3\Gamma^3}.
$$

默认 `geometry_factor=8` 是数量级 convention，不是 photosphere transfer 的唯一标准。

代码：`baryonic_photosphere_radius()`  
Formula ID：`TH-PHOTOSPHERE-001`。

## 6. Detailed Derivation II：Thermal Free-Free Emissivity

### 6.1 目标公式

目标是解释 nonrelativistic thermal plasma 中常用的 angle-integrated free-free emissivity：

$$
\epsilon_\nu^{\rm ff}
\simeq
6.8\times10^{-38}
Z^2n_en_iT^{-1/2}
\exp\left(-\frac{h\nu}{kT}\right)
g_{\rm ff}
\quad
{\rm erg\,s^{-1}\,cm^{-3}\,Hz^{-1}}.
$$

这里 \(\epsilon_\nu=4\pi j_\nu\)。本页不把数值常数从 Coulomb scattering 的全部经典轨道积分重推到最后一位，而是把关键的物理依赖、Maxwellian 平均、Jacobian 和 Gaunt factor 层级写清。

### 6.2 物理设定

考虑电荷为 \(Ze\) 的 ions 和 nonrelativistic thermal electrons。电子速度分布为 Maxwellian：

$$
f_M(v)dv
=
4\pi v^2
\left(\frac{m_e}{2\pi kT}\right)^{3/2}
\exp\left(-\frac{m_ev^2}{2kT}\right)dv.
$$

电子在 Coulomb field 中被加速，单次 encounter 的辐射概率与 Coulomb acceleration 的平方有关，因此出现 \(Z^2\)。碰撞对数、量子修正、低速和高频端的精细行为被收进 \(g_{\rm ff}\)。

### 6.3 从 electron energy 到 photon cutoff

电子 kinetic energy 为：

$$
E_e
=
\frac{1}{2}m_ev^2.
$$

变量替换：

$$
v
=
\left(\frac{2E_e}{m_e}\right)^{1/2},
\qquad
dv
=
\frac{dE_e}{m_ev}.
$$

Maxwellian 的能量分布含有：

$$
f_E(E_e)dE_e
\propto
E_e^{1/2}
\exp\left(-\frac{E_e}{kT}\right)dE_e.
$$

产生频率 \(\nu\) 的 photon 至少要求电子 kinetic energy 满足：

$$
E_e\ge h\nu.
$$

因此热平均中的高频端会包含：

$$
\int_{h\nu}^{\infty}
\exp\left(-\frac{E_e}{kT}\right)dE_e
\propto
\exp\left(-\frac{h\nu}{kT}\right).
$$

这就是 thermal free-free spectrum 中 exponential cutoff 的来源。它不是手工加上的 cutoff，而是 Maxwellian 高能尾。

### 6.4 为什么出现 \(T^{-1/2}\)

经典 free-free emissivity 的速度依赖可粗略理解为两体碰撞率 \(n_en_i v\) 乘以单次辐射谱权重。Coulomb scattering 中较慢电子偏转更强，频率积分前的谱率含有近似 \(1/v^2\) 型依赖；与 encounter rate 的 \(v\) 合并后，热平均中出现近似 \(1/v\) 的平均：

$$
\left\langle\frac{1}{v}\right\rangle
=
\int_0^\infty
\frac{1}{v}f_M(v)dv.
$$

代入 Maxwellian：

$$
\left\langle\frac{1}{v}\right\rangle
\propto
\left(\frac{m_e}{kT}\right)^{3/2}
\int_0^\infty v
\exp\left(-\frac{m_ev^2}{2kT}\right)dv.
$$

令：

$$
y
=
\frac{m_ev^2}{2kT},
\qquad
v\,dv
=
\frac{kT}{m_e}dy.
$$

于是：

$$
\left\langle\frac{1}{v}\right\rangle
\propto
\left(\frac{m_e}{kT}\right)^{3/2}
\frac{kT}{m_e}
\int_0^\infty e^{-y}dy
\propto
T^{-1/2}.
$$

这就是 spectral free-free emissivity 中 \(T^{-1/2}\) 标度的来源。更完整的推导会保留量子矩阵元、Coulomb logarithm 和精确常数；这些细节统一进入 \(g_{\rm ff}\) 和前面的 cgs coefficient。

### 6.5 Gaunt factor 的角色

Gaunt factor 是量子力学 free-free cross-section 与经典 Kramers 近似的比值。课程页中应该把它当作一层物理修正，而不是随手设为 1 的装饰常数：

$$
\epsilon_\nu^{\rm ff}
=
\epsilon_{\nu,{\rm Kramers}}^{\rm ff}
g_{\rm ff}(\nu,T,Z).
$$

常见层级是：

| 层级 | 做法 | 适用 |
| --- | --- | --- |
| \(g_{\rm ff}=1\) | Kramers 量级估计 | 手算和 fixed-point |
| 常数 \(g_{\rm ff}\sim1.1-1.5\) | bolometric cooling 估计 | 热 plasma cooling envelope |
| analytic approximation | 用 \(T,\nu,Z\) 的近似函数 | 更稳定的课程 reference |
| tabulated relativistic Gaunt factor | 表格插值 | 高温、宽能段、精确 plasma modeling |

当前本地 thermal free-free helper 只实现前两层；没有 relativistic Gaunt table。

代码：`thermal_cutoff_factor()`、`optically_thin_emissivity_scale()`、`free_free_spectral_emissivity_cgs()`、`free_free_bolometric_emissivity_cgs()`  
Formula IDs：`FF-CUTOFF-001`、`FF-EMISSIVITY-SCALE-001`、`FF-EMISSIVITY-SPECTRAL-001`、`FF-BOL-EMISS-001`。

## 7. Detailed Derivation III：Kirchhoff Law 到 Free-Free Absorption

### 7.1 目标公式

目标是从 LTE relation：

$$
j_\nu^{\rm ff}
=
\alpha_\nu^{\rm ff}B_\nu(T)
$$

推出常用 free-free absorption coefficient：

$$
\alpha_\nu^{\rm ff}
\simeq
3.7\times10^8
Z^2n_en_iT^{-1/2}\nu^{-3}
\left[1-\exp\left(-\frac{h\nu}{kT}\right)\right]
g_{\rm ff}
\quad {\rm cm^{-1}}.
$$

### 7.2 Emissivity per steradian

第 6 节的 \(\epsilon_\nu^{\rm ff}\) 是 angle-integrated volume emissivity。若 emission isotropic：

$$
j_\nu^{\rm ff}
=
\frac{\epsilon_\nu^{\rm ff}}{4\pi}.
$$

Kirchhoff law 给出：

$$
\alpha_\nu^{\rm ff}
=
\frac{j_\nu^{\rm ff}}{B_\nu(T)}
=
\frac{\epsilon_\nu^{\rm ff}}{4\pi B_\nu(T)}.
$$

### 7.3 频率依赖和 stimulated term

代入：

$$
\epsilon_\nu^{\rm ff}
\propto
Z^2n_en_iT^{-1/2}
e^{-h\nu/kT}
g_{\rm ff},
$$

以及：

$$
B_\nu(T)
=
\frac{2h\nu^3}{c^2}
\frac{1}{e^{h\nu/kT}-1}.
$$

于是：

$$
\alpha_\nu^{\rm ff}
\propto
Z^2n_en_iT^{-1/2}
\nu^{-3}
e^{-h\nu/kT}
\left(e^{h\nu/kT}-1\right)
g_{\rm ff}.
$$

指数项相乘：

$$
e^{-h\nu/kT}
\left(e^{h\nu/kT}-1\right)
=
1-e^{-h\nu/kT}.
$$

所以：

$$
\alpha_\nu^{\rm ff}
\propto
Z^2n_en_iT^{-1/2}
\nu^{-3}
\left[1-e^{-h\nu/kT}\right]
g_{\rm ff}.
$$

这一步说明 absorption 公式里的 \([1-e^{-h\nu/kT}]\) 不是额外经验修正，而是 thermal emission 与 Planck source function 的 detailed balance 结果，也可理解为 stimulated emission 修正后的净吸收。

### 7.4 低频极限

若 \(h\nu\ll kT\)：

$$
1-e^{-h\nu/kT}
\simeq
\frac{h\nu}{kT}.
$$

因此：

$$
\alpha_\nu^{\rm ff}
\propto
n_en_iT^{-3/2}\nu^{-2}g_{\rm ff}.
$$

低频 free-free absorption 很强，实际 radio/IR 低频端可能由 \(\tau_\nu^{\rm ff}\) 而不是 intrinsic emissivity 决定。

路径长度 \(l\) 上：

$$
\tau_\nu^{\rm ff}
=
\alpha_\nu^{\rm ff}l.
$$

代码：`free_free_absorption_from_kirchhoff_cgs()`、`free_free_absorption_coefficient_cgs()`、`free_free_optical_depth()`  
Formula IDs：`FF-ABSORPTION-KIRCHHOFF-001`、`FF-ALPHA-001`、`FF-TAU-001`。

## 8. Cooling Time

bolometric free-free cooling rate 常写为：

$$
\epsilon_{\rm ff}
\simeq
1.4\times10^{-27}
Z^2n_en_iT^{1/2}g_B
\quad
{\rm erg\,cm^{-3}\,s^{-1}}.
$$

这个 \(T^{1/2}\) 与 spectral emissivity 的 \(T^{-1/2}\) 不矛盾，因为 bolometric rate 已经对频率积分：

$$
\int_0^\infty
T^{-1/2}e^{-h\nu/kT}d\nu
=
T^{-1/2}\frac{kT}{h}
\propto
T^{1/2}.
$$

thermal energy density 取：

$$
u_{\rm th}
\simeq
\frac{3}{2}(n_e+n_i)kT.
$$

若 free-free 是主导冷却：

$$
t_{\rm cool}^{\rm ff}
=
\frac{u_{\rm th}}{\epsilon_{\rm ff}}.
$$

纯氢且 \(n_e\simeq n_i=n\) 时：

$$
t_{\rm cool}^{\rm ff}
\propto
\frac{T^{1/2}}{n}.
$$

这就是 cooling fixed-point 检查中“密度越高冷却越快、温度升高按 \(\sqrt{T}\) 增长”的来源。

代码：`free_free_cooling_time_s()`、`production.py::thermal_free_free_cooling_time()`  
Formula ID：`FF-COOL-TIME-001`。

## 9. Nonthermal Bremsstrahlung

### 9.1 完整表达式

nonthermal bremsstrahlung 的一般 photon production spectrum 是：

$$
\frac{dN_\gamma}{dt\,dE_\gamma}
=
cn_{\rm target}
\int_{E_\gamma}^{\infty}
N_e(E_e)
\frac{d\sigma_{\rm br}}{dE_\gamma}(E_e,E_\gamma)\,
dE_e.
$$

SED 为：

$$
E_\gamma^2F_{E_\gamma}
=
\frac{E_\gamma^2}{4\pi d^2}
\frac{dN_\gamma}{dt\,dE_\gamma}.
$$

积分下限 \(E_e=E_\gamma\) 来自能量守恒：electron 不能辐射出超过自身 kinetic energy 的 photon。真实 endpoint 附近的谱形由微分截面决定，不能用单纯 \(1/E_\gamma\) 截面外推。

### 9.2 成熟截面层

成熟计算通常使用 Bethe-Heitler / Koch-Motz / Blumenthal-Gould / Haug / Baring99 类微分截面，或公开软件封装的 radiative model。它们会区分：

- electron-ion 和 electron-electron bremsstrahlung。
- relativistic 与 nonrelativistic 能区。
- nuclear charge、screening 和 Coulomb correction。
- photon endpoint behavior。
- neutral gas、ionized gas、ISM composition weights。

### 9.3 当前代码层

当前本地有两条 nonthermal bremsstrahlung 路线：

1. `nonthermal_bremsstrahlung_sed_erg_cm2_s()`：legacy teaching/trend helper，使用简化截面

$$
\frac{d\sigma}{dE_\gamma}
\propto
\frac{\sigma_0}{E_\gamma},
\qquad
E_e\ge E_\gamma.
$$

它只能标为 `order-of-magnitude`，不能用于 calibrated spectrum。

2. `naima_compat.py::nonthermal_bremsstrahlung_sed_naima_compatible_erg_cm2_s()` 和 production wrapper `nonthermal_bremsstrahlung_sed_naima_parity()`：复刻 `naima.Bremsstrahlung` 的 Baring99 convention，并使用 ionized ISM weights。它是 package-compatible / benchmark-output 层，不是 thermal free-free。

Formula IDs：`LEP-BREM-NONTHERMAL-SED-001`、`LEP-NAIMA-COMPAT-BREM-001`。

### 9.4 Loss-time envelope

动力学中有时只需要判断 nonthermal brems loss 是否可能重要，可使用：

$$
t_{\rm brem,nt}
\simeq
\frac{1}{n_{\rm target}\sigma_{\rm eff}\kappa c}.
$$

这里 \(\sigma_{\rm eff}\) 和 \(\kappa\) 是调用方选择的 envelope 参数，不是从完整微分截面积分得到的谱核。因此它只能回答 regime question，不能替代 nonthermal brems SED。

代码：`cooling_angle.py::nonthermal_bremsstrahlung_loss_time_s()`  
Formula ID：`COOL-BREM-NONTHERMAL-LOSS-TIME-001`。

## 10. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| Planck function | 有闭式 | LTE photon distribution |
| Stefan-Boltzmann law | 有闭式 | Bose integral 给出 \(\pi^4/15\) |
| effective blackbody SED | 有闭式 | 静态球面，非 relativistic transfer |
| photosphere radius scale | 数量级解析 | 依赖几何 convention 和 outflow phase |
| thermal free-free spectral emissivity | 近似闭式 | nonrelativistic Kramers + Gaunt factor |
| free-free absorption | LTE 下由 Kirchhoff 闭合 | 依赖 \(B_\nu\) 和 emissivity convention |
| relativistic / tabulated Gaunt factor | 数值表或近似式 | 本地未实现 |
| nonthermal bremsstrahlung spectrum | 一般无短闭式解 | 需对 \(N_e(E)\) 和 \(d\sigma/dE_\gamma\) 积分 |
| photospheric GRB spectrum | 一般无闭式解 | 需 relativistic radiation transfer |

## 11. Analytic / Semi-Analytic Limits

### 11.1 Planck low/high frequency

Rayleigh-Jeans limit，\(h\nu\ll kT\)：

$$
B_\nu
\simeq
\frac{2\nu^2kT}{c^2}.
$$

Wien limit，\(h\nu\gg kT\)：

$$
B_\nu
\simeq
\frac{2h\nu^3}{c^2}
e^{-h\nu/kT}.
$$

### 11.2 Thermal free-free spectral limits

低频 \(h\nu\ll kT\) 且 \(g_{\rm ff}\) 变化慢时：

$$
\epsilon_\nu^{\rm ff}
\propto
n_en_iT^{-1/2}.
$$

高频 \(h\nu\gg kT\)：

$$
\epsilon_\nu^{\rm ff}
\propto
n_en_iT^{-1/2}e^{-h\nu/kT}.
$$

free-free absorption 低频：

$$
\alpha_\nu^{\rm ff}
\propto
n_en_iT^{-3/2}\nu^{-2}.
$$

### 11.3 Approximation hierarchy

| 层级 | 做法 | 牺牲 |
| --- | --- | --- |
| Kramers + \(g_{\rm ff}=1\) | 快速解析标度 | 量子修正和精确常数 |
| scalar Gaunt factor | 本地 thermal helper | 频率和温度依赖 |
| analytic Gaunt approximation | future mature helper | 表格精度 |
| tabulated relativistic Gaunt factor | plasma modeling | 需要数据表和插值 |
| package-compatible nonthermal brems | naima/Baring99 parity | 只等于对应 package convention |

## 12. 从推导到代码的实现约定

当前代码层分为四类：

| 层级 | 内容 | 代码/输出 | 边界 |
| --- | --- | --- | --- |
| course/reference thermal | Planck、blackbody inversion、static blackbody SED | `thermal.py`, `bremsstrahlung.py::planck_function_nu_cgs` | 无 relativistic photospheric transfer |
| course/reference free-free | nonrelativistic thermal free-free emissivity、Kirchhoff absorption、cooling time | `bremsstrahlung.py` | scalar Gaunt factor, cgs approximation |
| order-of-magnitude nonthermal | simplified \(d\sigma/dE_\gamma\propto1/E_\gamma\) | `leptonic_spectra.py::nonthermal_bremsstrahlung_sed_erg_cm2_s` | trend only |
| package-compatible nonthermal | Baring99 / naima convention | `naima_compat.py`, `production.py::nonthermal_bremsstrahlung_sed_naima_parity` | benchmark parity, not thermal plasma |

如果后续采用成熟参数化截面，课程页必须说明替换：

$$
\frac{\sigma_0}{E_\gamma}
\rightarrow
\frac{d\sigma_{\rm Haug/Koch\text{-}Motz/BG/Baring}}{dE_\gamma}.
$$

如果后续采用 Gaunt factor table，课程页必须说明替换：

$$
g_{\rm ff}={\rm constant}
\rightarrow
g_{\rm ff}(\nu,T,Z).
$$

曲线差异常来自 target composition、electron-electron contribution、screening、Gaunt factor、low-energy cutoff、unit convention、energy grid 和 package-specific density convention。

## 13. Benchmark Boundary

可对照的公开实现包括 `naima.Bremsstrahlung`、GAMERA、Gammapy 生态或文献表格。本地 core 不把这些包作为运行依赖；adapter 和 production parity 只表示 same-parameter benchmark 或 package-compatible route。

已经可声称：

- Planck / blackbody / free-free cgs helper 通过本地 fixed-point。
- `naima.Bremsstrahlung` parity route 是 nonthermal Baring99 convention 的 package-compatible benchmark。

不能声称：

- thermal free-free 已对齐 `naima.Bremsstrahlung`。`naima.Bremsstrahlung` 是 nonthermal radiative model。
- legacy simplified nonthermal helper 是 calibrated cross-section。
- photosphere helper 是完整 GRB thermal spectrum。
- free-free cooling 包含 line cooling、pair plasma、relativistic Gaunt factor 或 composition network。

## 14. 代码和验证

代码：

```text
reproduce/grb/core/radiation/thermal.py
reproduce/grb/core/radiation/bremsstrahlung.py
reproduce/grb/core/radiation/leptonic_spectra.py
reproduce/grb/core/radiation/naima_compat.py
reproduce/grb/core/radiation/production.py
```

验证：

```text
python -m reproduce.grb.validation.check_radiation_mechanisms_v1
python -m reproduce.grb.validation_lab.check_radiation_cooling_angle_v1
python -m reproduce.grb.validation_lab.check_radiation_package_parity_v3
python -m reproduce.grb.validation_lab.check_radiation_production_suite_v1
```

验证重点：Planck Rayleigh-Jeans limit、blackbody \(T^4\)、photosphere \(\Gamma^{-3}\)、free-free density scaling、thermal cutoff、Kirchhoff absorption、cooling-time density and \(T^{1/2}\) trend、naima-compatible nonthermal brems parity。

## 15. 不声称

- 不声称完成 relativistic photospheric transfer。
- 不声称 thermal component 已经拟合某个事件。
- 不声称 thermal free-free 已有 relativistic Gaunt table。
- 不声称 legacy nonthermal brems helper 是 Haug/Koch-Motz/BG 级精确截面。
- 不包含 line cooling、pair plasma、full transfer 或 composition network。

## 16. 参考来源

- Rybicki & Lightman, *Radiative Processes in Astrophysics*.
- Longair, *High Energy Astrophysics*.
- Draine, *Physics of the Interstellar and Intergalactic Medium*.
- Blumenthal & Gould 1970, bremsstrahlung review formulae.
- Koch & Motz 1959, bremsstrahlung cross-section review.
- Haug 1997/1998, relativistic bremsstrahlung cross-section literature.
- Baring et al. 1999, nonthermal bremsstrahlung convention used by `naima`.
- Mészáros 2001 and GRB photosphere reviews.
