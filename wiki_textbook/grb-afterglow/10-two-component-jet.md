# 10 Two-component jet

Structured jet 章节把喷流写成连续的 angular profile `𝓔(θ)=dE/dΩ` 和 `Γ(θ)`。Two-component jet 是这个图像的离散化版本：一个窄而快的 narrow component 嵌在一个宽而慢的 wide component 中。它的价值不只是“多加一个光变成分”，而是把 prompt brightness、early afterglow break、late bump / resurgence、radio calorimetry 和 jet-break masking 放进同一个几何-动力学框架。

## 1. 基本几何定义

最简单 two-component jet 可写成两个 top-hat-like angular zones：

```tex
𝓔(θ)=\frac{dE}{dΩ}(θ)=
\begin{cases}
𝓔_n, & 0\le θ<θ_n,\\
𝓔_w, & θ_n\le θ<θ_w,\\
0, & θ\ge θ_w,
\end{cases}
```

```tex
Γ_0(θ)=
\begin{cases}
Γ_{0,n}, & 0\le θ<θ_n,\\
Γ_{0,w}, & θ_n\le θ<θ_w,\\
1, & θ\ge θ_w.
\end{cases}
```

其中：

- `n` 表示 narrow component；
- `w` 表示 wide component；
- 通常 `θ_n<θ_w`；
- 通常 `Γ_{0,n} \gg Γ_{0,w}`；
- `E_n` 与 `E_w` 可指 isotropic-equivalent kinetic energy，也可指 beaming-corrected true energy，必须在每个 source 中核对。

若把每个 component 都近似为 top-hat，则 small-angle 下 true kinetic energy 为

```tex
E_{n,true}\simeq \frac{θ_n^2}{2}E_{n,iso},
```

```tex
E_{w,true}\simeq \frac{θ_w^2}{2}E_{w,iso}.
```

因为 `θ_w` 可远大于 `θ_n`，即使 `E_{w,iso}<E_{n,iso}`，wide component 的 true energy 也可能 comparable 或更大。

## 2. 为什么需要 two components

单一 top-hat jet 的光变通常由一个 deceleration time、一个 jet-break time 和一组 microphysical parameters 描述。Two-component jet 适合处理以下现象：

- early optical / X-ray break 与 late radio behavior 不能由同一 opening angle 解释；
- late optical resurgence、bump 或 plateau 出现在 narrow component 应该衰减之后；
- radio calorimetry 指向比 prompt gamma-ray component 更宽、更慢、能量更大的 outflow；
- prompt 极端亮度需要 very narrow core，但 afterglow 需要 wider component；
- narrow component 的 jet break 被 wide component rise 掩盖。

这些现象都不是 two-component jet 的唯一证据。它们也可能来自 refreshed shock、continuous structured jet、density variation、reverse shock 或 scintillation。Two-component jet 的强项在于：它给出明确的 component timescale 和 flux-ratio 判据。

## 3. Component deceleration time

对每个 component，可以先用第三、四章的 afterglow onset 公式估计 deceleration time。Uniform ISM 中，component `i` 的 deceleration radius 量级为

```tex
R_{dec,i}\sim
\left(\frac{3E_i}{4π n m_p c^2 Γ_{0,i}^2}\right)^{1/3},
```

对应 observer-frame deceleration time

```tex
t_{dec,i}\sim (1+z)\frac{R_{dec,i}}{2cΓ_{0,i}^2}.
```

合并得到

```tex
t_{dec,i}\propto (1+z)E_i^{1/3}n^{-1/3}Γ_{0,i}^{-8/3}.
```

这里 `i=n,w`。由于 `Γ_{0,w}` 通常远小于 `Γ_{0,n}`，wide component 往往比 narrow component 晚得多 decelerate，即使二者能量同阶。

Wind medium 中，若 `ρ=AR^{-2}`，则

```tex
R_{dec,i}\sim \frac{E_i}{4π A c^2 Γ_{0,i}^2},
```

```tex
t_{dec,i}\propto (1+z)E_i A^{-1}Γ_{0,i}^{-4}.
```

因此在 GRB 080319B 这类 wind-like environment 模型中，不能把 ISM 的 `Γ_0^{-8/3}` scaling 直接套用。

## 4. Narrow component 的 jet break

Narrow component 的 jet break time 由第七章的条件给出：

```tex
Γ_n(t_{jet,n})\sim θ_n^{-1}.
```

在 ISM、adiabatic、top-hat-like approximation 下，量级关系为

```tex
t_{jet,n}\propto (1+z)E_{n,iso}^{1/3}n^{-1/3}θ_n^{8/3}.
```

Wind medium 中 exponent 不同：

```tex
t_{jet,n}\propto (1+z)E_{n,iso}A^{-1}θ_n^4.
```

Two-component jet 的关键不是单独测量 `t_{jet,n}`，而是比较它与 wide component 的 deceleration time：

```tex
t_{dec,w}\quad \text{vs.}\quad t_{jet,n}.
```

## 5. Jet-break masking 条件

Peng, Königl & Granot 的核心 insight 是：如果 wide component 在 narrow component 发生 jet break 附近开始显著发光，那么观测到的总 light curve 可能不会显示一个清晰的 narrow jet break。

总 flux 是两个 component 的和：

```tex
F_ν(t)=F_{ν,n}(t)+F_{ν,w}(t).
```

若

```tex
t_{dec,w}\sim t_{jet,n},
```

且在该时间附近

```tex
F_{ν,w}(t_{dec,w})\gtrsim F_{ν,n}(t_{jet,n}),
```

则 wide component 的 rise / peak 会填平 narrow component 的 steepening，使 total light curve 看起来像 shallow decay、plateau、bump 或 delayed break。

这个 masking 会造成两个常见偏差：

- 若把 total light curve 当成单一 jet，可能高估 narrow component 的 opening angle；
- 若用错误的 beaming correction，可能高估 prompt gamma-ray true energy 或 radiative efficiency。

## 6. Flux dominance 的物理来源

一个 component 在某个频段是否主导取决于：

- kinetic energy `E_i`；
- opening angle `θ_i`；
- initial Lorentz factor `Γ_{0,i}`；
- external medium `n` 或 `A`；
- microphysical parameters `ε_e`、`ε_B`、`p`；
- observer viewing angle `θ_obs`；
- observing frequency 相对 `ν_m`、`ν_c`、`ν_a` 的位置。

因此 “wide component 能量更大” 不自动等于 “所有频段都由 wide component 主导”。例如 radio band 受 self-absorption、source size 和 scintillation 影响更强；X-ray band 若位于 `ν>ν_c`，对 density 的敏感性较弱。

## 7. On-axis 与 off-axis 情形

### 7.1 On-axis narrow-core observer

若

```tex
θ_{obs}<θ_n,
```

observer 直接看向 narrow component。Prompt gamma-ray emission 和 early afterglow 通常由 narrow component 主导。Wide component 可能在较晚 `t_{dec,w}` 后贡献 late optical / radio flux。

这类情形适合解释 GRB 080319B 的极端 apparent brightness：very narrow core viewed close to axis 可显著提高 prompt brightness；但 prompt optical / gamma-ray spectral mismatch 仍说明辐射成分本身不能只靠几何解释。

### 7.2 Outside narrow component but inside wide component

若

```tex
θ_n<θ_{obs}<θ_w,
```

observer 不在 narrow core 内，但仍在 wide component 内。Prompt gamma-ray 可能变弱、变软，afterglow 早期可由 local wide material 主导，随后 narrow core 或 inner region 贡献变得可见。这类图像常与 X-ray flash 或 under-luminous GRB interpretation 联系在一起，但具体归因依赖 detector threshold 和 prompt spectrum。

### 7.3 Outside both components

若

```tex
θ_{obs}>θ_w,
```

prompt emission 可能非常弱或不可探测；afterglow peak 可能显著延迟。此时 two-component jet 与 continuous structured jet、cocoon afterglow 或 quasi-spherical outflow 的区分需要高质量 late-time multiwavelength light curve、polarization 或 imaging。

## 8. 和 continuous structured jet 的关系

Two-component jet 是 structured jet 的 piecewise approximation。连续 profile 写作

```tex
𝓔=𝓔(θ),\quad Γ_0=Γ_0(θ),
```

而 two-component jet 把它近似成

```tex
(𝓔_n,Γ_{0,n},θ_n) + (𝓔_w,Γ_{0,w},θ_w).
```

这种近似的优点是参数少、物理图像清楚；缺点是 component boundary 人为，不能自然描述 smooth angular wing、cocoon gradient 或 continuous energy stratification。

实际建模中，如果数据只显示一个 broad bump，two-component jet 和 Gaussian / power-law structured jet 可能高度简并。若数据能分辨出两个 dynamical timescale、两个 spectral evolution 或 radio calorimetry 指向的 wide component，two-component interpretation 才更有说服力。

## 9. 和 refreshed shock / energy injection 的区别

Two-component jet 与 refreshed shock 都能让 late afterglow 重新变亮，但它们的动力学来源不同：

- two-component jet：不同 angular zones 在不同时间主导 emission；
- refreshed shock：同一 line-of-sight outflow 中 slower shells 追上 decelerated blast wave；
- continuous energy injection：central engine 或 phenomenological luminosity 持续给 blast wave 加能。

观测上可用以下线索区分：

- late component 是否有不同 opening angle 或 jet break；
- radio calorimetry 是否要求更宽、更慢的 outflow；
- bump 是否伴随 reverse-shock-like radio flare；
- optical / X-ray / radio 是否共享同一 SED；
- polarization 或 source size 是否支持 angular structure。

## 10. GRB 030329：事件级 two-component prototype

Berger et al. 对 GRB 030329 的解释是 two-component jet 的经典事件级案例。观测事实包括 early optical / X-ray break、late optical resurgence、radio afterglow 和 SN 2003dh contamination caveat；模型解释把它们分配给两个 component：

- narrow component：opening angle 约 `5°`，解释 gamma-ray emission 和 early optical / X-ray afterglow；
- wide component：opening angle 约 `17°`，解释 radio afterglow 和 late optical component；
- radio jet break time 约 `t_{j,rad}≈9.8 d`；
- wide component carries much of the kinetic energy。

关键 caveat 是：这些角度和能量是 Berger et al. 的模型解释，不是直接观测到的几何图像。SN 2003dh subtraction、radio synchrotron modeling 和 residual discrepancies 都会影响参数解释。

## 11. GRB 080319B：naked-eye burst 的 narrow-core 图像

Racusin et al. 将 GRB 080319B 放入 narrow core + wider component 框架：

- prompt optical 达到 naked-eye brightness；
- prompt optical flux 远高于 gamma-ray spectrum 的简单低能外推；
- very narrow core opening angle 约 `0.2°`，观测者接近 core axis；
- wider component opening angle 约 `4°`，贡献 later afterglow；
- afterglow modeling favor wind-like environment。

这个案例说明 two-component geometry 可以解释极端 apparent brightness 和后续 afterglow component separation，但不能单独解释 prompt optical / gamma spectral mismatch；后者仍需要多辐射区或多谱成分。

## 12. GRB 221009A：与 structured jet 的接口

GRB 221009A 中 narrow jet、structured jet core、shallow structured jet、radio/mm extra component 和 TeV afterglow 都已进入事件页模型比较。Two-component jet 在这里应作为 candidate language 使用：

- 若 late radio/mm component 可对应 wider slower outflow，则 two-component jet 是候选；
- 若 X-ray long-lived decay 由 shallow angular energy profile 解释，则 continuous structured jet 可能更自然；
- 若 TeV afterglow 指向 very narrow energetic core，true energy correction 依赖 `θ_c`、`θ_v` 和 profile form；
- 不能只因存在 bump 或 extra component 就断言 two-component jet。

## 13. 常见误区

- **把 two-component jet 当作任意两个光变成分的同义词**：它有明确 angular geometry 和 dynamical timescales。
- **忽略 `t_{dec,w}` 与 `t_{jet,n}` 的相对时序**：break masking 的关键正是二者接近。
- **把 `E_{iso}` 和 true energy 混用**：wide component 可能 `E_{iso}` 较小但 true energy 较大。
- **忽略介质类型**：ISM 与 wind 中 `t_dec` 和 `t_jet` 对 `Γ_0`、`θ_j` 的依赖不同。
- **把事件模型参数当作普适结构**：GRB 030329 的 5°/17° 和 GRB 080319B 的 0.2°/4° 是事件级解释，不是所有 GRB 的模板。
- **忽略 prompt 辐射机制**：narrow core 可增强 apparent brightness，但不能自动解释 optical/gamma spectral mismatch。

## 14. 和后续事件应用章节的接口

后续事件应用章应把 two-component jet 拆成三层：

1. 观测事实：break time、bump、radio peak、spectral mismatch、fluence、redshift、SN contamination；
2. 模型解释：narrow / wide component 的角度、能量、Lorentz factor、介质类型；
3. 非唯一性：refreshed shock、continuous structured jet、density variation、reverse shock、scintillation 是否可替代。

这样可以避免把模型图像写成观测事实，也能把同一个理论框架持续更新到 GRB 030329、GRB 080319B 和 GRB 221009A。

## 来源

- F. Peng, A. Königl and J. Granot, “Two-Component Jet Models of Gamma-Ray Burst Sources,” ApJ 626, 966-977 (2005), arXiv:astro-ph/0410384。
- E. Berger et al., “A common origin for cosmic explosions inferred from calorimetry of GRB030329,” Nature 426, 154-157 (2003), arXiv:astro-ph/0308187。
- J. L. Racusin et al., “Broadband observations of the naked-eye gamma-ray burst GRB 080319B,” Nature 455, 183-188 (2008), arXiv:0805.1557。
- O. S. Salafia and G. Ghirlanda, “The Structure of Gamma Ray Burst Jets,” arXiv:2206.11088。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
