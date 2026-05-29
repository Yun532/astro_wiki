# 00 Radiative Transfer Foundations

状态：v1.0 辐射转移公理层。

本页是后续 synchrotron、IC/SSC、free-free、gamma-gamma opacity 和 thermal component 的逻辑地基。它不先假设某个具体辐射机制，而是从“辐射场如何被描述、如何守恒、如何被介质发射/吸收、在运动介质中如何变换”推到 radiative transfer equation。

## 1. 为什么需要这一层

单个辐射机制给出的是闭合关系，例如：

```text
synchrotron: j_nu, alpha_nu 来自非热电子和磁场
free-free:   j_nu, alpha_nu 来自热电子-离子碰撞
gamma-gamma: alpha_nu 等价于 pair-production opacity
thermal:     source function 接近 Planck function
```

但这些机制都要先放进同一个转移框架：

```text
定义辐射强度 I_nu
  -> 定义 flux / pressure / energy density
  -> 定义 emission coefficient j_nu 和 absorption coefficient alpha_nu
  -> 用能量守恒推出 dI_nu/ds = j_nu - alpha_nu I_nu
  -> 用 Lorentz 不变量把静止介质公式接到运动介质
  -> 再由具体机制提供 j_nu, alpha_nu, tau_nu 或 source function
```

所以本页是“公理层”，后续机制页是“闭合关系层”。

## 2. 辐射强度 `I_nu` 的定义

考虑一束辐射穿过面积元 `dA`。面积法向与光线方向夹角为 `theta`，有效面积是：

```text
dA_perp = dA cos theta.
```

在时间 `dt`、频率间隔 `dnu`、方向立体角 `dOmega` 内穿过的能量定义为：

```text
dE = I_nu cos theta dA dOmega dnu dt.
```

因此：

```text
I_nu = dE / (cos theta dA dOmega dnu dt).
```

物理含义：单位时间、单位投影面积、单位频率、单位立体角内，沿指定方向携带的能量。

cgs 单位：

```text
erg s^-1 cm^-2 Hz^-1 sr^-1.
```

Formula ID：`RT-I-NU-001`。

## 3. 为什么真空中 `I_nu` 沿光线不变

设一束无吸收、无发射的光从面元 `dA_1` 传播到 `dA_2`。能量守恒要求：

```text
dE_1 = dE_2.
```

对同一束光，传播几何满足：

```text
dA_1 cos theta_1 dOmega_1 = dA_2 cos theta_2 dOmega_2.
```

这本质上是同一光管的 etendue / phase-space volume 守恒。若频率不变、时间间隔相同，则：

```text
I_nu,1 = I_nu,2.
```

所以在没有发射、吸收、散射、引力红移和介质折射时，specific intensity 沿 ray 保持不变。

这不是说 flux 不变。远离点源时 flux 会按 `1/r^2` 下降，因为同一源张开的 solid angle 变小；但同一束光线内部的 `I_nu` 不因几何稀释改变。

Formula ID：`RT-I-NU-CONSERVE-001`。

## 4. 光子分布函数与 `I_nu`

把辐射看成 photon gas。设 photon distribution function 为 `f(x, p, t)`，含义是相空间体元中的 photon occupation。

photon energy：

```text
epsilon = h nu.
```

photon momentum magnitude：

```text
p = h nu / c.
```

沿方向 `n` 的 photon number 与 phase-space volume 成正比。辐射强度与分布函数的关系可写成数量级/标准不变量形式：

```text
I_nu proportional h nu^3 f.
```

更重要的逻辑结论是：

```text
f invariant under Lorentz transform
=> I_nu / nu^3 invariant.
```

这给出运动介质中 Doppler boosting 的核心：

```text
I_nu / nu^3 = I'_nu' / nu'^3.
```

若定义 Doppler factor：

```text
D = nu / nu',
```

则：

```text
I_nu = D^3 I'_nu'.
```

Formula ID：`RT-INVARIANT-I-001`。

## 5. 从 `I_nu` 积分得到宏观辐射量

### 5.1 Mean intensity

平均单色强度：

```text
J_nu = (1/4pi) integral I_nu dOmega.
```

各向同性辐射场中：

```text
I_nu independent of direction
=> J_nu = I_nu.
```

### 5.2 Flux

通过面元的净辐射流量：

```text
F_nu = integral I_nu cos theta dOmega.
```

矢量形式：

```text
F_nu_vec = integral I_nu n dOmega.
```

各向同性辐射场中，正反方向抵消：

```text
F_nu_vec = 0.
```

### 5.3 Energy density

体积内沿方向 `n` 的辐射在时间 `dt` 走过 `c dt`。用强度定义可得：

```text
u_nu = (1/c) integral I_nu dOmega.
```

各向同性时：

```text
u_nu = 4 pi I_nu / c = 4 pi J_nu / c.
```

### 5.4 Radiation pressure tensor

光子携带动量，方向投影形成 pressure tensor：

```text
P_nu,ij = (1/c) integral I_nu n_i n_j dOmega.
```

各向同性时：

```text
P_nu,ij = (u_nu / 3) delta_ij.
```

因此 scalar radiation pressure：

```text
P_rad = u / 3.
```

Formula IDs：`RT-FLUX-001`、`RT-ENERGY-DENSITY-001`、`RT-PRESSURE-001`。

## 6. 发射系数 `j_nu`

定义 emission coefficient `j_nu`：单位体积、单位时间、单位频率、单位立体角发射的能量。

体元 `dV` 在 `dt`、`dnu`、`dOmega` 中发射：

```text
dE_emit = j_nu dV dt dnu dOmega.
```

若介质各向同性发射，常定义 angle-integrated emissivity：

```text
epsilon_nu = 4 pi j_nu.
```

在转移方程中，`j_nu` 是源项；具体机制页负责给出它，例如 synchrotron `j_nu`、free-free `j_nu`。

Formula ID：`RT-EMISSIVITY-001`。

## 7. 吸收系数 `alpha_nu`

辐射穿过长度 `ds` 的介质时，强度减少量定义为：

```text
dI_nu = -alpha_nu I_nu ds.
```

因此：

```text
alpha_nu = - (1/I_nu) dI_nu/ds.
```

单位：

```text
cm^-1.
```

若微观吸收截面为 `sigma_nu`，吸收粒子数密度为 `n`，则单位长度上遇到的总截面为：

```text
alpha_nu = n sigma_nu.
```

定义质量吸收系数 / opacity：

```text
kappa_nu = alpha_nu / rho.
```

单位：

```text
cm^2 g^-1.
```

Formula IDs：`RT-ABSORPTION-001`、`RT-OPACITY-001`。

## 8. Optical depth 与 source function

定义 optical depth：

```text
d tau_nu = alpha_nu ds,
tau_nu(s) = integral alpha_nu ds.
```

source function：

```text
S_nu = j_nu / alpha_nu.
```

`S_nu` 的意义是：当介质足够厚时，辐射强度趋向的局部平衡值。

若热平衡成立，Kirchhoff law 给出：

```text
S_nu = B_nu(T).
```

这就是 blackbody 和 free-free absorption 之间的桥梁。

Formula IDs：`RT-TAU-001`、`RT-SOURCE-FUNCTION-001`。

## 9. 辐射转移方程：从能量守恒推导

取一根沿 `s` 方向传播的细光束，横截面积为 `dA`，长度为 `ds`。入射强度为 `I_nu`，出射强度为 `I_nu + dI_nu`。

入射能量：

```text
dE_in = I_nu dA dOmega dnu dt.
```

出射能量：

```text
dE_out = (I_nu + dI_nu) dA dOmega dnu dt.
```

强度变化对应：

```text
dE_out - dE_in = dI_nu dA dOmega dnu dt.
```

体元体积：

```text
dV = dA ds.
```

发射贡献：

```text
dE_emit = j_nu dV dOmega dnu dt
        = j_nu dA ds dOmega dnu dt.
```

吸收贡献：

```text
dE_abs = alpha_nu I_nu ds dA dOmega dnu dt.
```

能量守恒：

```text
dE_out - dE_in = dE_emit - dE_abs.
```

消去公共因子：

```text
dI_nu = (j_nu - alpha_nu I_nu) ds.
```

得到静态介质中的 transfer equation：

```text
dI_nu/ds = j_nu - alpha_nu I_nu.
```

用 optical depth 改写：

```text
dI_nu/dtau_nu = S_nu - I_nu.
```

若 `S_nu` 常数，解为：

```text
I_nu(tau) = I_nu(0) exp(-tau) + S_nu [1 - exp(-tau)].
```

极限：

```text
tau << 1: I_nu ~= I_nu(0) + j_nu s
tau >> 1: I_nu -> S_nu
```

Formula ID：`RT-TRANSFER-001`。

## 10. 含时间项的转移方程

若辐射场随时间变化，则沿光线的 total derivative 包含：

```text
d/ds -> n dot grad + (1/c) partial/partial t.
```

所以：

```text
(1/c) partial I_nu/partial t + n dot grad I_nu
  = j_nu - alpha_nu I_nu.
```

这就是时域天文学中更自然的形式：爆发源、afterglow、flare、jet knot 都可能需要时间项。

Formula ID：`RT-TIME-DEPENDENT-001`。

## 11. 辐射力与 Eddington limit

吸收能量 `dE_abs` 对应动量：

```text
dp = dE_abs / c.
```

对所有方向和频率积分，单位体积受到的辐射力为：

```text
f_rad = (1/c) integral alpha_nu I_nu n dOmega dnu.
```

若 opacity 与频率无关且近似各向同性，可写成单位质量辐射加速度：

```text
g_rad = kappa F / c.
```

中心质量 `M` 的引力加速度：

```text
g_grav = G M / r^2.
```

球对称 luminosity：

```text
F = L / (4 pi r^2).
```

平衡 `g_rad = g_grav`：

```text
kappa L / (4 pi r^2 c) = G M / r^2.
```

得到 Eddington luminosity：

```text
L_Edd = 4 pi G M c / kappa.
```

纯电离氢中 `kappa ~= sigma_T / m_p`：

```text
L_Edd = 4 pi G M m_p c / sigma_T.
```

Formula IDs：`RT-RADIATION-FORCE-001`、`RT-EDDINGTON-001`。

## 12. Einstein coefficients 到 Kirchhoff law 的逻辑

两能级系统 `E_2 > E_1`，频率满足：

```text
h nu = E_2 - E_1.
```

三种过程：

```text
spontaneous emission: 2 -> 1, coefficient A_21
stimulated emission:  2 -> 1, coefficient B_21
absorption:           1 -> 2, coefficient B_12
```

热平衡中 upward 和 downward transition rate 平衡：

```text
n_1 B_12 J_nu = n_2 A_21 + n_2 B_21 J_nu.
```

Boltzmann distribution：

```text
n_2/n_1 = (g_2/g_1) exp(-hnu/kT).
```

要求平衡辐射场等于 Planck function，就得到 Einstein relations：

```text
g_1 B_12 = g_2 B_21,
A_21 / B_21 = 2 h nu^3 / c^2.
```

这说明在 thermodynamic equilibrium 中：

```text
j_nu / alpha_nu = B_nu(T).
```

也就是 Kirchhoff law。

Formula ID：`RT-EINSTEIN-KIRCHHOFF-001`。

## 13. Lorentz 变换和辐射不变量

设共动系量加撇号，观测者系不加撇。Doppler factor：

```text
D = 1 / [Gamma (1 - beta cos theta)].
```

频率变换：

```text
nu = D nu'.
```

solid angle 变换：

```text
dOmega = D^{-2} dOmega'.
```

由 photon distribution function 不变，得到：

```text
I_nu / nu^3 invariant.
```

因此：

```text
I_nu = D^3 I'_nu'.
```

为了让 transfer equation 形式不变，还需要：

```text
j_nu / nu^2 invariant,
alpha_nu nu invariant.
```

等价写法：

```text
j_nu = D^2 j'_nu',
alpha_nu = D^{-1} alpha'_nu'.
```

这样：

```text
dI_nu/ds = j_nu - alpha_nu I_nu
```

在运动介质中仍可用相同形式表达，只是各量要在同一参考系中使用。

Formula IDs：`RT-INVARIANT-J-001`、`RT-INVARIANT-ALPHA-001`。

## 14. 如何接到后续机制页

后续每个机制页都应回答同一个问题：它给 transfer equation 提供了什么闭合关系？

| 机制 | 提供的闭合量 | 连接到本页 |
| --- | --- | --- |
| synchrotron | `j_nu`、broken-power-law `I_nu/F_nu`、SSA `alpha_nu` | `RT-TRANSFER-001`, `RT-ABSORPTION-001` |
| IC/SSC | photon energy boost、cooling power、seed photon field feedback | `RT-INVARIANT-I-001`, energy density definitions |
| gamma-gamma | effective absorption / opacity | `RT-ABSORPTION-001`, `RT-TAU-001` |
| thermal/free-free | `B_nu(T)`、`j_nu^ff`、`alpha_nu^ff` | `RT-SOURCE-FUNCTION-001`, `RT-EINSTEIN-KIRCHHOFF-001` |
| hadronic | injection scale for secondary photons/neutrinos | transfer source terms, not full cascade |

## 15. 边界

- 本页是 classical / special-relativistic radiative transfer foundation，不包含 general relativistic ray tracing。
- 没有处理 polarization transfer。
- 没有处理 scattering integral 的完整角分布，只把 scattering 机制留给 IC/SSC 页。
- `I_nu/nu^3` 等不变量要求使用同一 photon beam 的相空间描述；不能随意混用不同 frame 的频率和系数。

## 16. 参考材料

- Rybicki & Lightman, *Radiative Processes in Astrophysics*。
- Frank Rieger, *High Energy Astrophysics - Lecture 7*，用于后续 IC/KN 推导衔接。
- 用户提供的知乎辐射转移笔记文本，用作本页中文结构化整理来源之一。
