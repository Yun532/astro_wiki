# 01 Synchrotron and Synchrotron Self-Absorption

状态：v2.2 课程讲义草案。本页按 `physical picture -> single-particle kernel -> detailed derivation block -> analytic limits -> transfer/SSA -> numerical boundary` 组织。同步辐射先作为基础辐射机制本身处理：带电粒子在磁场中被洛伦兹力弯曲，轨道加速度产生辐射；相对论粒子的辐射被压缩到窄角锥内，于是出现特征频率、单粒子核函数、非热电子谱和自吸收。

## 1. 物理图像

一个电荷在磁场中运动时受到洛伦兹力：

$$
\frac{d\mathbf p}{dt}
=
\frac{q}{c}\,\mathbf v \times \mathbf B .
$$

力总是垂直于速度的垂直分量，所以磁场不直接改变粒子能量，只改变动量方向。非相对论情形下，粒子绕磁力线做 Larmor 回旋；相对论情形下，辐射被 beaming 到角宽约 $1/\gamma$ 的方向锥内。观察者接收到的脉冲宽度比回旋周期短得多，因此辐射主频不在回旋频率本身，而被提升到大约 $\gamma^2$ 倍。

同步辐射的核心逻辑链是：

$$
\text{magnetic deflection}
\rightarrow
\text{transverse acceleration}
\rightarrow
\text{single-particle spectrum }P_\nu(\gamma)
\rightarrow
\text{integrate over }N(\gamma)
\rightarrow
j_\nu,\ \alpha_\nu,\ I_\nu,\ F_\nu .
$$

## 2. 参考系与符号

本页默认在发射等离子体共动系中推导，带撇号的量如 $B'$、$\nu'$ 表示共动系。若之后要接到观测者频率，只需额外乘 Doppler 因子并除以红移因子：

$$
\nu_{\rm obs}
=
\frac{\delta_D}{1+z}\,\nu' .
$$

| 符号 | 含义 | 单位或量纲 |
| --- | --- | --- |
| $q$ 或 $e$ | 电荷量，电子取绝对值 $e$ | statC |
| $m_e$ | 电子质量 | g |
| $c$ | 光速 | cm s$^{-1}$ |
| $\gamma$ | 粒子 Lorentz factor | dimensionless |
| $\beta$ | $v/c$ | dimensionless |
| $B'$ | 共动系磁场 | G |
| $\alpha$ | pitch angle，即速度与磁场夹角 | rad |
| $\nu_B'$ | 非相对论 gyro frequency | Hz |
| $\nu_c'$ | 单粒子 critical frequency | Hz |
| $P_\nu'$ | 单粒子谱功率 | erg s$^{-1}$ Hz$^{-1}$ |
| $N(\gamma)$ | 总粒子数分布或密度分布，依上下文说明 | per $\gamma$ |
| $j_\nu$ | emission coefficient | erg s$^{-1}$ cm$^{-3}$ Hz$^{-1}$ sr$^{-1}$ |
| $\alpha_\nu$ | absorption coefficient | cm$^{-1}$ |

## 3. 回旋频率到特征频率

先从非相对论回旋出发。动量垂直分量满足：

$$
\frac{p_\perp v_\perp}{r_L}
=
\frac{e v_\perp B'}{c}.
$$

非相对论时 $p_\perp=m_ev_\perp$，所以：

$$
r_L
=
\frac{m_e c v_\perp}{eB'},
\qquad
\omega_B'
=
\frac{v_\perp}{r_L}
=
\frac{eB'}{m_ec}.
$$

对应频率为：

$$
\nu_B'
=
\frac{\omega_B'}{2\pi}
=
\frac{eB'}{2\pi m_e c}.
$$

对相对论粒子，轨道角频率因惯性增加变成 $\omega_B'/\gamma$，但辐射被 beaming。粒子方向转过约 $1/\gamma$ 时，辐射束扫过观察者方向；再考虑到光行程时间压缩，接收脉冲宽度约比回旋时间短 $\gamma^2$ 量级。因此特征角频率满足：

$$
\omega_{\rm syn}'
\sim
\gamma^2 \omega_B' \sin\alpha .
$$

严格单粒子谱的常用 critical frequency 写作：

$$
\nu_c'
=
\frac{3eB'\sin\alpha}{4\pi m_ec}\,\gamma^2
=
\frac{3}{2}\gamma^2\sin\alpha\,\nu_B' .
$$

这里的 $\nu_c'$ 是单个电子的 critical frequency，不是冷却 break frequency。两者常用同一个下标 $c$，容易混淆。

## 4. 总辐射功率

相对论 Larmor 公式给出带电粒子加速辐射的总功率。对于磁场中只有横向加速度的运动，可写成 Thomson 形式：

$$
P_{\rm syn}'
=
\frac{4}{3}\sigma_T c\,\beta^2\gamma^2 U_B'\sin^2\alpha ,
$$

其中磁场能量密度为：

$$
U_B'
=
\frac{B'^2}{8\pi}.
$$

强相对论电子 $\beta\simeq1$ 时：

$$
P_{\rm syn}'
\simeq
\frac{4}{3}\sigma_T c\,\gamma^2
\frac{B'^2}{8\pi}\sin^2\alpha .
$$

若 pitch angle 各向同性，

$$
\langle \sin^2\alpha\rangle = \frac{2}{3}.
$$

若只是做最大量级估计，也常取 $\sin\alpha=1$。这类 pitch-angle convention 会直接影响与公开库的绝对归一化比较。

## 5. 单粒子谱核

同步辐射不是单色辐射。标准单粒子谱功率为：

$$
P_\nu'(\gamma,\alpha)
=
\frac{\sqrt{3}e^3B'\sin\alpha}{m_ec^2}
F\!\left(\frac{\nu'}{\nu_c'}\right),
$$

其中：

$$
F(x)
=
x\int_x^\infty K_{5/3}(\xi)\,d\xi .
$$

$K_{5/3}$ 是 modified Bessel function。这个表达式来自对相对论圆周运动的 retarded potential 作 Fourier 分解；课程层面最重要的是两个极限：

$$
x\ll1:
\quad
F(x)\propto x^{1/3},
$$

$$
x\gg1:
\quad
F(x)\propto x^{1/2}e^{-x}.
$$

低频 $x^{1/3}$ 是许多 optically thin synchrotron 谱低频端 $F_\nu\propto\nu^{1/3}$ 的来源；高频指数衰减说明单个电子不会在远高于 $\nu_c'$ 的频率上贡献太多。

数值实现边界：实际计算 $F(x)$ 时，如果对 $K_{5/3}$ 从极小 $x$ 积到无穷，容易出现慢收敛。当前 reference kernel 在 $x<10^{-4}$ 使用解析低频渐近：

$$
F(x)
\simeq
2^{2/3}\Gamma\!\left(\frac{2}{3}\right)x^{1/3},
$$

其余区间用数值积分。这个处理是数值稳定化，不是新的物理近似。

## 6. 详细解析推导：从单粒子核到 power-law emissivity

这一节补上同步辐射讲义里最容易被压缩的一步：不要只说“对 power-law 电子积分可得”，而是展示变量替换、Jacobian、积分限和 Gamma function 常数如何出现。

### 6.1 目标公式

目标是在 optically thin、均匀、给定 pitch angle \(\alpha\) 的条件下，从单粒子谱功率推出 power-law electrons 的 emission coefficient：

$$
j_\nu
\propto
K\,B_\perp^{(p+1)/2}\nu^{-(p-1)/2},
\qquad
B_\perp=B\sin\alpha.
$$

更完整地，若：

$$
n(\gamma)=K\gamma^{-p},
$$

并且积分区间足够宽，使目标频率不贴近 \(\gamma_{\min}\) 或 \(\gamma_{\max}\) cutoff，则：

$$
j_\nu
=
\frac{\sqrt{3}e^3B_\perp}{8\pi m_ec^2}
K
\left(
\frac{\nu}{C_B}
\right)^{(1-p)/2}
\mathcal I(p),
$$

其中：

$$
C_B
=
\frac{3eB_\perp}{4\pi m_ec},
$$

以及：

$$
\mathcal I(p)
=
\int_0^\infty
x^{(p-3)/2}F(x)\,dx.
$$

下面要做的事就是把 \(\mathcal I(p)\) 展开，而不是把它藏进“标准结果”。

### 6.2 物理设定

在发射等离子体共动系中考虑电子。磁场为 \(B\)，电子速度与磁场夹角为 pitch angle \(\alpha\)，所以真正提供横向加速度和辐射的磁场分量是：

$$
B_\perp
=
B\sin\alpha.
$$

电子分布取 Lorentz factor 空间中的体密度分布：

$$
n(\gamma)d\gamma
=
K\gamma^{-p}d\gamma.
$$

这里 \(K\) 的单位是 cm\(^{-3}\) per \(\gamma\)。若之后使用总粒子数分布 \(N(\gamma)\)，只需把 \(j_\nu\) 换成体积积分后的 \(L_\nu\)。

### 6.3 基础公式：单粒子谱功率与 emissivity

单个电子的同步谱功率为：

$$
P_\nu(\gamma,\alpha)
=
\frac{\sqrt{3}e^3B_\perp}{m_ec^2}
F\!\left(\frac{\nu}{\nu_c}\right).
$$

这里：

$$
\nu_c
=
C_B\gamma^2
=
\frac{3eB_\perp}{4\pi m_ec}\gamma^2.
$$

核函数为：

$$
F(x)
=
x\int_x^\infty K_{5/3}(\xi)\,d\xi.
$$

这个 \(F(x)\) 来自相对论圆周运动的远区辐射场 Fourier 分解。更具体地说，电子束扫过观察者方向时给出一个短脉冲；对这个脉冲的频域分解会出现 modified Bessel functions，垂直偏振和水平偏振分量组合后得到 \(K_{5/3}\) 的积分核。这里不把 retarded potential 的全部推导展开到电动力学教材级，但要保留它的角色：\(F(x)\) 是单粒子时域辐射脉冲的频域形状，不是人为拟合函数。

辐射转移的源项是 \(j_\nu\)。对各向同性发射方向，单个立体角上的 emission coefficient 为：

$$
j_\nu'
=
\frac{1}{4\pi}
\int n(\gamma)\,P_\nu'(\gamma)\,d\gamma .
$$

这里 \(1/4\pi\) 表示把总功率平均到单位立体角。若使用总粒子数分布 \(N(\gamma)\)，则对应 luminosity density：

$$
L_\nu'
=
\int N(\gamma)\,P_\nu'(\gamma)\,d\gamma .
$$

二者只差体积积分是否已经吸收到粒子分布里。

### 6.4 变量替换和 Jacobian

把 power-law electrons 代入 \(j_\nu\)：

$$
j_\nu
=
\frac{\sqrt{3}e^3B_\perp}{4\pi m_ec^2}
K
\int \gamma^{-p}
F\!\left(\frac{\nu}{C_B\gamma^2}\right)d\gamma .
$$

定义无量纲变量：

$$
x
=
\frac{\nu}{C_B\gamma^2}.
$$

反解：

$$
\gamma
=
\left(
\frac{\nu}{C_Bx}
\right)^{1/2}.
$$

对 \(x\) 求微分：

$$
d\gamma
=
-\frac{1}{2}
\left(
\frac{\nu}{C_B}
\right)^{1/2}
x^{-3/2}dx.
$$

因此：

$$
\gamma^{-p}d\gamma
=
-\frac{1}{2}
\left(
\frac{\nu}{C_B}
\right)^{(1-p)/2}
x^{(p-3)/2}dx.
$$

当 \(\gamma\) 从 \(0\) 到 \(\infty\) 时，\(x\) 从 \(\infty\) 到 \(0\)。负号正好翻转积分限，所以：

$$
j_\nu
=
\frac{\sqrt{3}e^3B_\perp}{8\pi m_ec^2}
K
\left(
\frac{\nu}{C_B}
\right)^{(1-p)/2}
\int_0^\infty
x^{(p-3)/2}F(x)\,dx.
$$

这一步已经给出谱指数：因为 \(C_B\propto B_\perp\)，前因子中有一个 \(B_\perp\)，而括号中有 \(C_B^{(p-1)/2}\)，所以：

$$
j_\nu
\propto
K\,B_\perp^{(p+1)/2}\nu^{-(p-1)/2}.
$$

### 6.5 核函数积分如何变成 Gamma functions

现在展开：

$$
\mathcal I(p)
=
\int_0^\infty x^{(p-3)/2}F(x)\,dx.
$$

代入：

$$
F(x)
=
x\int_x^\infty K_{5/3}(\xi)d\xi.
$$

于是：

$$
\mathcal I(p)
=
\int_0^\infty
x^{(p-1)/2}
\left[
\int_x^\infty K_{5/3}(\xi)d\xi
\right]dx.
$$

交换积分次序。原来的积分区域是 \(0<x<\infty\)、\(x<\xi<\infty\)。交换后是 \(0<\xi<\infty\)、\(0<x<\xi\)，所以：

$$
\mathcal I(p)
=
\int_0^\infty K_{5/3}(\xi)
\left[
\int_0^\xi x^{(p-1)/2}dx
\right]d\xi.
$$

先做内层积分：

$$
\int_0^\xi x^{(p-1)/2}dx
=
\frac{2}{p+1}\xi^{(p+1)/2}.
$$

因此：

$$
\mathcal I(p)
=
\frac{2}{p+1}
\int_0^\infty
\xi^{(p+1)/2}K_{5/3}(\xi)d\xi.
$$

使用标准 Bessel 积分：

$$
\int_0^\infty x^{\mu-1}K_\nu(x)dx
=
2^{\mu-2}
\Gamma\!\left(\frac{\mu-\nu}{2}\right)
\Gamma\!\left(\frac{\mu+\nu}{2}\right),
$$

其中本例：

$$
\mu-1=\frac{p+1}{2},
\qquad
\mu=\frac{p+3}{2},
\qquad
\nu=\frac{5}{3}.
$$

于是：

$$
\mathcal I(p)
=
\frac{2}{p+1}
2^{(p-1)/2}
\Gamma\!\left(\frac{3p-1}{12}\right)
\Gamma\!\left(\frac{3p+19}{12}\right).
$$

代回 \(j_\nu\)，得到固定 pitch angle 下的解析表达式：

$$
j_\nu
=
\frac{\sqrt{3}e^3B_\perp}{8\pi m_ec^2}
K
\left(
\frac{\nu}{C_B}
\right)^{(1-p)/2}
\frac{2^{(p+1)/2}}{p+1}
\Gamma\!\left(\frac{3p-1}{12}\right)
\Gamma\!\left(\frac{3p+19}{12}\right).
$$

其中：

$$
C_B=\frac{3eB_\perp}{4\pi m_ec}.
$$

这个公式保留了谱斜率、磁场标度和依赖 \(p\) 的归一化常数。若做各向同性 pitch-angle 平均，需要再对 \(\sin\alpha\) 的幂次做角平均；这会改变绝对归一化，但不会改变 \(\nu^{-(p-1)/2}\) 的谱指数。

### 6.6 delta approximation 作为快速检查

delta approximation 仍然有用，但它应该放在完整核积分之后。令：

$$
P_\nu(\gamma)
\approx
P_{\rm syn}(\gamma)\,
\delta\!\left(\nu-C\gamma^2\right),
$$

其中 \(P_{\rm syn}\propto \gamma^2B_\perp^2\)。于是：

$$
j_\nu
\propto
\int K\gamma^{-p}\gamma^2
\delta(\nu-C\gamma^2)\,d\gamma .
$$

利用：

$$
\delta(\nu-C\gamma^2)
=
\frac{\delta\!\left[\gamma-(\nu/C)^{1/2}\right]}
{|2C\gamma|},
$$

得到：

$$
j_\nu
\propto
\frac{\gamma^{-p}\gamma^2}{\gamma}
=
\gamma^{1-p}.
$$

又因为 \(\gamma\propto\nu^{1/2}\)，所以：

$$
j_\nu
\propto
\nu^{-(p-1)/2}.
$$

delta approximation 保留了谱指数和量级关系，但丢掉了真实 \(F(x)\) 核的宽度和 Gamma function 归一化，因此它只能作为解析 sanity check，而不是最终精确谱核。

## 7. 冷却与谱陡化

电子能量为：

$$
E_e'
=
\gamma m_ec^2.
$$

同步辐射冷却时间：

$$
t_{\rm syn}'
=
\frac{E_e'}{P_{\rm syn}'}
=
\frac{6\pi m_ec}
{\sigma_T B'^2\gamma\sin^2\alpha}.
$$

忽略 pitch-angle 常数时，标度是：

$$
t_{\rm syn}'\propto B'^{-2}\gamma^{-1}.
$$

定义 cooling Lorentz factor 为在给定动力学时间 $t'$ 内刚好冷却的粒子：

$$
t_{\rm syn}'(\gamma_c)=t',
$$

因此：

$$
\gamma_c
=
\frac{6\pi m_ec}
{\sigma_TB'^2t'}.
$$

若 inverse Compton 也参与冷却，用 Compton parameter $Y$ 表示额外冷却功率：

$$
\gamma_c
=
\frac{6\pi m_ec}
{\sigma_TB'^2t'(1+Y)}.
$$

持续注入的 power-law 电子在 $\gamma>\gamma_c$ 处会从 $p$ 陡化为 $p+1$，于是辐射谱从：

$$
F_\nu\propto\nu^{-(p-1)/2}
$$

变成：

$$
F_\nu\propto\nu^{-p/2}.
$$

## 8. 自吸收的来源

同步自吸收不是额外辐射机制，而是同一群电子对低频同步光子的吸收。辐射转移方程为：

$$
\frac{dI_\nu}{ds}
=
j_\nu-\alpha_\nu I_\nu .
$$

若均匀 slab 中 $j_\nu$ 与 $\alpha_\nu$ 近似常数，解为：

$$
I_\nu
=
I_\nu(0)e^{-\tau_\nu}
+
S_\nu(1-e^{-\tau_\nu}),
$$

其中：

$$
\tau_\nu=\alpha_\nu R,
\qquad
S_\nu=\frac{j_\nu}{\alpha_\nu}.
$$

两个极限是：

$$
\tau_\nu\ll1:
\quad
I_\nu\simeq j_\nu R,
$$

$$
\tau_\nu\gg1:
\quad
I_\nu\rightarrow S_\nu.
$$

对 power-law electrons，同步自吸收系数可写成：

$$
\alpha_\nu
\propto
-\nu^{-2}
\int P_\nu(\gamma)\gamma^2
\frac{d}{d\gamma}
\left[
\frac{n(\gamma)}{\gamma^2}
\right]d\gamma .
$$

若：

$$
n(\gamma)=K\gamma^{-p},
$$

则：

$$
\frac{d}{d\gamma}
\left[
\frac{n(\gamma)}{\gamma^2}
\right]
=
-(p+2)K\gamma^{-(p+3)}.
$$

完成核函数积分后得到经典标度：

$$
\alpha_\nu
\propto
K\,B'^{(p+2)/2}\nu^{-(p+4)/2}.
$$

于是 source function 的频率标度为：

$$
S_\nu
=
\frac{j_\nu}{\alpha_\nu}
\propto
B'^{-1/2}\nu^{5/2}.
$$

这解释了均匀同步源在 optically thick 区域常见的：

$$
I_\nu\propto\nu^{5/2}.
$$

如果低频端还受到低能电子 cutoff、几何、非均匀磁场或多个 emitting zones 影响，实际低频 slope 可以偏离 $5/2$。因此自吸收公式常作为诊断工具，而不是单独决定全部低频谱形的完整模型。

## 9. 可观测谱段

把单粒子低频尾、电子 power law 和冷却陡化合在一起，可得到常用 optically thin 谱段。

Slow cooling，$\nu_m<\nu_c$：

| 频段 | 物理来源 | 谱形 |
| --- | --- | --- |
| $\nu<\nu_m$ | 单电子低频尾 | $F_\nu\propto\nu^{1/3}$ |
| $\nu_m<\nu<\nu_c$ | 未冷却电子 power law | $F_\nu\propto\nu^{-(p-1)/2}$ |
| $\nu>\nu_c$ | 冷却后电子谱陡化 | $F_\nu\propto\nu^{-p/2}$ |

Fast cooling，$\nu_c<\nu_m$：

| 频段 | 物理来源 | 谱形 |
| --- | --- | --- |
| $\nu<\nu_c$ | 单电子低频尾 | $F_\nu\propto\nu^{1/3}$ |
| $\nu_c<\nu<\nu_m$ | 冷却电子分布 | $F_\nu\propto\nu^{-1/2}$ |
| $\nu>\nu_m$ | 注入谱加冷却 | $F_\nu\propto\nu^{-p/2}$ |

若再加入自吸收，低于 $\nu_a$ 的谱段要用 transfer solution 和 source function 替代 optically thin 公式。

## 10. 可以直接计算的表达式

本节把前面的推导压缩成几组可直接代入的表达式。它们分成两层：第一层是单粒子核积分，适合数值计算 SED；第二层是 broken-power-law 解析近似，适合手算谱段和冷却趋势。

### 10.1 单粒子核积分形式

给定磁场 $B'$、pitch angle $\alpha$、电子 Lorentz factor $\gamma$，先算：

$$
\nu_c'
=
\frac{3eB'\sin\alpha}{4\pi m_ec}\gamma^2 .
$$

单粒子谱功率：

$$
P_\nu'(\gamma)
=
\frac{\sqrt{3}e^3B'\sin\alpha}{m_ec^2}
F\!\left(\frac{\nu'}{\nu_c'}\right).
$$

若电子分布是总粒子数谱 $N(\gamma)$，则：

$$
L_\nu'
=
\int_{\gamma_{\min}}^{\gamma_{\max}}
N(\gamma)P_\nu'(\gamma)\,d\gamma .
$$

若输入是粒子能量谱 $dN/dE_e$，用 $E_e=\gamma m_ec^2$：

$$
L_\nu'
=
\int
\frac{dN}{dE_e}
P_\nu'(E_e)\,dE_e .
$$

距离为 $d$ 时，忽略 beaming 和 cosmological correction 的教学版观测通量为：

$$
F_\nu
=
\frac{L_\nu}{4\pi d^2},
\qquad
\nu F_\nu
=
\frac{\nu L_\nu}{4\pi d^2}.
$$

这是本地课程 reference SED 的直接计算形式。外部软件对照只能在单独 benchmark 页中说明，不能反过来改变这里的物理推导。

### 10.2 Power-law 解析谱段

若：

$$
n(\gamma)=K\gamma^{-p},
\qquad
\gamma\ge\gamma_m,
$$

则 optically thin power-law 段：

$$
j_\nu
=
C_j(p)\,
K\,B'^{(p+1)/2}\nu^{-(p-1)/2}.
$$

$C_j(p)$ 是只依赖 $p$ 的常数，完整形式含 Gamma functions；如果只比较谱斜率和相对变化，可以把它作为 normalization 常数处理。

冷却时间：

$$
t_{\rm syn}'
=
\frac{6\pi m_ec}
{\sigma_TB'^2\gamma}.
$$

给定年龄或动力学时间 $t'$：

$$
\gamma_c
=
\frac{6\pi m_ec}
{\sigma_TB'^2t'}.
$$

对应特征频率：

$$
\nu_m'
=
\frac{3eB'}{4\pi m_ec}\gamma_m^2,
\qquad
\nu_c'
=
\frac{3eB'}{4\pi m_ec}\gamma_c^2.
$$

在 slow cooling，$\nu_m<\nu_c$，若峰值为 $F_{\nu,\max}$：

$$
F_\nu
=
F_{\nu,\max}
\begin{cases}
(\nu/\nu_m)^{1/3}, & \nu<\nu_m,\\
(\nu/\nu_m)^{-(p-1)/2}, & \nu_m<\nu<\nu_c,\\
(\nu_c/\nu_m)^{-(p-1)/2}(\nu/\nu_c)^{-p/2}, & \nu>\nu_c .
\end{cases}
$$

在 fast cooling，$\nu_c<\nu_m$：

$$
F_\nu
=
F_{\nu,\max}
\begin{cases}
(\nu/\nu_c)^{1/3}, & \nu<\nu_c,\\
(\nu/\nu_c)^{-1/2}, & \nu_c<\nu<\nu_m,\\
(\nu_m/\nu_c)^{-1/2}(\nu/\nu_m)^{-p/2}, & \nu>\nu_m .
\end{cases}
$$

### 10.3 自吸收计算

power-law electrons 的自吸收系数可写成：

$$
\alpha_\nu
=
C_\alpha(p)\,
K\,B'^{(p+2)/2}\nu^{-(p+4)/2}.
$$

光深：

$$
\tau_\nu
=
\alpha_\nu R.
$$

均匀 slab 的强度：

$$
I_\nu
=
I_\nu(0)e^{-\tau_\nu}
+
\frac{j_\nu}{\alpha_\nu}(1-e^{-\tau_\nu}).
$$

若背景入射可以忽略：

$$
I_\nu
=
S_\nu(1-e^{-\tau_\nu}),
\qquad
S_\nu=\frac{j_\nu}{\alpha_\nu}.
$$

在 optically thick limit：

$$
I_\nu\rightarrow S_\nu
\propto
B'^{-1/2}\nu^{5/2}.
$$

所以一个完整的手算流程是：先算 $j_\nu$ 和 $\alpha_\nu$，再算 $\tau_\nu$，最后用 transfer solution 得到 $I_\nu$ 或通量。

## 11. 从推导到代码的实现约定

本页对应的数值层分成三类，必须分开读。允许代码为了稳定性、速度或公开软件对照而采用成熟计算方法；但任何和课程推导不完全一致的地方，都必须在这里说明。

### 11.1 课程 reference code

```text
synchrotron_kernel_f()
synchrotron_single_electron_pnu_cgs()
synchrotron_sed_erg_cm2_s()
```

这一层目标是直接对应本页第 5-6 节推导，使用固定 pitch angle 的 textbook kernel：

$$
F(x)=x\int_x^\infty K_{5/3}(\xi)d\xi,
\qquad
B_\perp=B\sin\alpha.
$$

代码中的计算约定是：

- 电子谱输入是总粒子数分布 \(dN/dE_e\)，单位 particles eV\(^{-1}\)，不是空间数密度。
- 先由 \(E_e=\gamma m_ec^2\) 得到 \(\gamma\)，再计算 \(\nu_c\) 和 \(P_\nu\)。
- 对电子能量网格做数值积分：

$$
L_\nu=\int N(E_e)P_\nu(E_e)\,dE_e.
$$

- 输出 SED：

$$
\nu F_\nu
=
\nu\frac{L_\nu}{4\pi d^2}.
$$

成熟数值处理可以包括：对 \(F(x)\) 使用渐近式、表格插值、SciPy Bessel 函数积分或 log-grid quadrature。只要保留同一个 textbook kernel 和单位约定，这些都属于课程 reference code 的数值实现细节。

### 11.2 成熟数值方法与角平均层

实际天体源通常没有固定 pitch angle。若电子 pitch angle 各向同性，可以把 \(B_\perp\) 做角平均；若磁场方向随机，可以采用 random-field approximation。它们和固定 pitch angle 推导的差异主要体现在：

- 单电子 kernel 的归一化常数。
- 峰值位置和峰附近形状。
- 低频和高频渐近通常保持相同量级或相同斜率，但不会逐点完全相等。

因此代码可以新增 mature-method helper，例如 angle-averaged synchrotron kernel、random-field kernel 或 tabulated-kernel 加速；但课程网页必须说明：

$$
P_\nu^{\rm code}
\neq
P_\nu^{\rm fixed\ pitch}
$$

的原因是角平均或随机磁场 convention，而不是公式推导错误。

### 11.3 外部 benchmark compatibility code

外部 benchmark compatibility code 的目标不是重新推导物理，而是在单独 adapter 中复刻某个公开软件的数值 convention：

```text
synchrotron_sed_<package>_compatible_erg_cm2_s()
```

这一层可以使用公开软件采用的其他近似，例如 Aharonian-Kelner-Prosekin random magnetic field approximation、角平均 kernel、特定积分网格或特定单位 convention。它可以和对应外部软件在同参数下对到数值误差，但不能被误读成“本页推导只剩这一种写法”。

简短地说：

| 层级 | 目标 | 核函数 | 是否要求等于外部软件 |
| --- | --- | --- | --- |
| course/reference | 对应本页推导 | fixed pitch-angle \(F(x)\) | 不要求 |
| mature numerical method | 物理上更常用或数值更稳定 | angle-averaged / random-field / tabulated kernel | 不要求，但必须解释差异 |
| package-compatible | benchmark parity | 外部软件自己的 kernel/convention | 只要求等于对应软件 |

如果课程公式和 benchmark compatibility 代码不同，必须在文档、函数 docstring 和 benchmark CSV 中写明差异来源。当前 CSV 中应始终区分本地课程 reference 与外部软件 compatibility 输出，不能把后者当成本地物理主实现。

除此之外，本页常规数值层只应承担三类任务：

- 计算单粒子核 $F(x)$，并在极小 $x$ 区间使用解析渐近避免慢积分。
- 对给定电子分布数值积分 $L_\nu=\int N(\gamma)P_\nu d\gamma$，用于教学与 reference。
- 用 broken-power-law 谱段做快速 sanity check。

它不能声称：

## v3 代码实现约定：agnpy-compatible synchrotron

课程推导中的 synchrotron reference 使用 fixed pitch-angle / textbook kernel；`naima_compat.py` 复刻 `naima` 的 AKP2010 random-field convention；本轮新增的 `agnpy_compat.py::synchrotron_sed_agnpy_compatible_erg_cm2_s()` 则复刻 `agnpy.Synchrotron` 的 one-zone blob convention。

主要换算是：

1. 本地粒子谱为总粒子数 `dN/dE`，agnpy 使用 blob 内密度 `n_e(gamma)`，因此代码显式除以球体积并乘以 `m_e c^2` 完成变量替换。
2. 观测频率先变到 blob comoving frame，\(\epsilon'=(1+z)h\nu/(\delta_D m_e c^2)\)。
3. 输出包含 \(\delta_D^4/(4\pi d_L^2)\) 的 beaming / distance convention。

所以 v3 图里 `agnpy-compatible` 曲线应该与 `agnpy benchmark-output` 接近；`teaching-reference` 曲线若有系统归一化差异，不表示课程公式错误，而表示 pitch-angle、random-field 与 blob convention 不同。

- 已经完成 pitch-angle、空间分布、radiative transfer 的全数值解。
- 已经包含非均匀磁场、多区模型、几何投影或 equal-arrival-time surface。
- 已经对任何具体天体事件做 paper-level fit。

## Cooling / Angle-kernel v1 补充

同步辐射进入动力学时，最常用的不是先算完整 SED，而是先算单粒子的能损：

$$
P_{\rm syn}={4\over 3}\sigma_T c\gamma^2 U_B \sin^2\alpha,
\qquad
U_B={B^2\over 8\pi}.
$$

若采用各向同性 pitch-angle 分布，

$$
\langle \sin\alpha\rangle={\pi\over4},\qquad
\langle \sin^2\alpha\rangle={2\over3}.
$$

因此冷却时间和 cooling break 写成

$$
t_{\rm syn}={\gamma m_e c^2\over P_{\rm syn}},
\qquad
\gamma_c={3m_e c\over 4\sigma_T U_B t_{\rm dyn}}.
$$

其中 \(\gamma_c\) 只在 Thomson/classical cooling 形式成立时使用。若代码采用固定 pitch angle（教学层常用 \(\sin\alpha=1\)）而 package-compatible 层采用 random-field 或 pitch-angle averaged convention，二者会出现稳定的归一化差异；这不是物理错误，而是 convention 差异。

当前代码约定：

- production：`cooling_angle.py::synchrotron_cooling_time_electron_s()`、`production.py::electron_synchrotron_cooling_time_s()` 给出后续动力学可调用 cooling time。
- teaching：`teaching.py::teaching_pitch_angle_convention()` 和 `teaching_pitch_angle_cooling_factor()` 用来画 fixed pitch-angle 与 isotropic average 的差异。
- 不声称：本轮没有实现完整 polarized synchrotron transfer，也没有把 SSA feedback 自洽并入 cooling。

## 12. 应用例子

同步辐射广泛出现在射电星系、AGN jet、pulsar wind nebula、supernova remnant 和 GRB afterglow 中。应用页可以引用本页的机制链来解释观测谱段、冷却 break 或低频自吸收，但具体源的几何、粒子注入和 radiative transfer 需要在应用模型中另行说明。

## 13. 参考资料

- Rybicki & Lightman, *Radiative Processes in Astrophysics*, Chapter 6.
- Longair, *High Energy Astrophysics*, synchrotron radiation chapters.
- Pacholczyk, *Radio Astrophysics*, synchrotron emission and absorption.
- Sari, Piran & Narayan 1998, *Spectra and Light Curves of Gamma-Ray Burst Afterglows*, https://arxiv.org/abs/astro-ph/9712005.
- CAMK radiation processes lecture notes, https://camk.edu.pl/media/uploads/phd/lecture_fall_2013/rm_04_radiation_processes.pdf.
