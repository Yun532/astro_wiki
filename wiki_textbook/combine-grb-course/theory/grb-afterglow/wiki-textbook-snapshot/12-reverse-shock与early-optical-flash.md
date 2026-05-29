# 12 Reverse shock 与 early optical flash

前面章节主要使用 forward shock 解释 long-lived afterglow。实际早期余辉中，relativistic ejecta 撞入外部介质时会同时形成 forward shock 和 reverse shock：forward shock 向外扫过 circumburst medium，reverse shock 向内穿过 ejecta。Reverse shock 的价值在于它直接探测 ejecta 本身的 Lorentz factor、磁化程度和 shell 厚度，因此是连接 prompt emission 与 afterglow onset 的关键环节。

但 reverse shock 不是“看到早期光学闪光就自动成立”的标签。Early optical flash、radio flare、早期 bump 也可能来自 prompt optical、forward-shock onset、density variation、energy injection 或多成分 jet。Reverse-shock interpretation 必须同时检查时间尺度、谱段、衰减斜率和 forward-shock component 的一致性。

## 1. Shock structure

爆发 ejecta 与外部介质相互作用后，可粗略分成四个区域：

1. 未受扰动 external medium；
2. forward-shocked external medium；
3. reverse-shocked ejecta；
4. 未受扰动 ejecta。

区域 2 和区域 3 之间由 contact discontinuity 分开。Forward shock 的长期 emission 构成标准 afterglow 主体；reverse shock 则通常在 shock crossing time 附近最亮，随后快速衰减。

如果 ejecta 初始 Lorentz factor 为 `Γ_0`，shell 宽度由 central-engine duration `T` 决定，那么 reverse shock 是否 relativistic、何时穿过 shell，取决于 shell thickness 与 deceleration scale 的比较。

## 2. Deceleration time 与 crossing time

Forward-shock afterglow onset 中的 deceleration time 仍是核心时间尺度。Uniform ISM 中量级为

```tex
t_{dec}\sim (1+z)
\left(\frac{3E}{32\pi n m_p c^5 Γ_0^8}\right)^{1/3}.
```

Wind medium 中则近似为

```tex
t_{dec}\sim (1+z)\frac{E}{8\pi A c^3 Γ_0^4}.
```

Reverse shock crossing time 记作 `t_\times`。量级上可以写成

```tex
t_\times \sim \max(T,t_{dec}).
```

这里 `T` 是 prompt duration 或 engine activity timescale 的 source/observer-frame 约定量，使用时必须说明是否包含 `(1+z)`。

- **Thin shell**：`T < t_{dec}`，reverse shock 在 deceleration time 附近穿过 shell，通常是 Newtonian 或 mildly relativistic reverse shock。
- **Thick shell**：`T > t_{dec}`，reverse shock 在 prompt duration 附近穿过 shell，可为 relativistic reverse shock。

在 crossing 附近，blast wave Lorentz factor 已显著低于初始 ejecta Lorentz factor，常用量级判断为

```tex
Γ(t_{dec})\sim \frac{Γ_0}{2}.
```

这个关系用于估计 `Γ_0`，但系数依赖介质、shell structure 和具体 light-curve definition。

## 3. Reverse shock 的 synchrotron 标度

Reverse shock 与 forward shock 共享 contact discontinuity 附近的 pressure，因此二者磁场量级可相近；但 reverse-shocked ejecta 中 electron Lorentz factor 通常低于 forward shock。若 microphysical parameters 类似，shock crossing time 附近有经典量级关系：

```tex
ν_{m,r}(t_\times)\sim Γ_0^{-2}ν_{m,f}(t_\times),
```

```tex
F_{ν,\max,r}(t_\times)\sim Γ_0 F_{ν,\max,f}(t_\times).
```

这说明 reverse shock 的 characteristic frequency 较低，但 peak flux 较高；因此它更容易在 optical 或 radio band 显现，而不是长期主导 X-ray afterglow。

这些关系不是精确拟合公式。若 reverse shock 与 forward shock 的 `ε_e`、`ε_B` 不同，或 ejecta magnetization 较高，比例会改变。

## 4. Early optical flash

Reverse shock 最著名的观测表现是 early optical flash：在几十秒到几百秒尺度出现 bright optical peak，随后快速衰减。经典图像中，peak time 接近 `t_\times`，peak 后 reverse-shock emission 因为没有新的 ejecta 被 shock 加热而快速 fading。

一个常用的经验判断是：若 optical light curve 在早期出现 steep decay，且 forward-shock component 在稍后以较浅斜率接管，则 reverse shock 是自然解释之一。但这需要同时检查：

- optical peak 是否与 prompt gamma-ray temporal structure 相关；
- peak 后 decay slope 是否比 forward shock closure relation 更陡；
- optical 与 X-ray 是否属于同一个 spectral component；
- radio band 是否有 delayed flare；
- 是否存在 prompt optical 或 internal emission 的证据。

GRB 990123 是 reverse-shock optical flash 的经典案例；GRB 080319B 的 prompt optical 极亮，但 optical/gamma spectral mismatch 表明它不能只靠简单 reverse-shock afterglow onset 解释。

## 5. Radio flare

由于 `ν_{m,r}` 通常低于 forward shock，reverse shock 可在 optical flash 后向低频移动，在 radio band 产生 delayed flare。Radio flare 的诊断价值在于：

- 它可能追踪同一 reverse-shock component 从 optical 到 radio 的 spectral evolution；
- radio band 受 self-absorption 和 scintillation 影响明显；
- early radio source size 很小，interstellar scintillation 可改变 apparent variability；
- reverse shock radio flare 与 wide-component radio rise、density bump 或 refreshed shock 可能简并。

因此 radio flare 不能单独作为 reverse shock 的唯一证据，必须结合 broadband SED 和 temporal evolution。

## 6. Magnetization `σ`

Reverse shock 对 ejecta magnetization 很敏感。常用 magnetization parameter 表示 Poynting flux 与 matter energy flux 的比值：

```tex
σ \equiv \frac{L_{Poynting}}{L_{matter}}.
```

当 `σ` 很低时，ejecta 近似 baryonic，reverse shock 容易形成；当 `σ` 较高时，磁压会改变 shock strength，甚至抑制明显 reverse shock。中等 magnetization 也可能增强 ordered magnetic field，从而提高 polarization 或改变 reverse-shock brightness。

这使 reverse shock 成为 prompt outflow composition 的探针，但也带来 degeneracy：没有 bright optical flash 不一定意味着没有 reverse shock，也可能意味着磁化、观测时间覆盖不足、dust extinction、频段不合适或 forward shock 淹没。

## 7. 和 forward-shock onset 的区别

Forward-shock onset 也会在 early optical 中产生 peak。两者的直观区别是：

| 诊断 | Forward-shock onset | Reverse shock |
| --- | --- | --- |
| 物理区域 | shocked external medium | shocked ejecta |
| peak time | `t_dec` 附近 | `t_\times` 附近 |
| peak 后行为 | 进入标准 afterglow decay | 通常更快衰减 |
| 频段 | optical/X-ray/radio 可连续演化 | optical flash / radio flare 常见 |
| 对 ejecta composition | 间接 | 直接敏感 |

但实际数据中二者可能叠加，必须做 forward+reverse decomposition，而不是只用单波段 peak 判断。

## 8. 和 energy injection / density variation 的区别

Reverse shock 解释的是 ejecta 被 reverse shock crossing 加热后的 emission；energy injection 或 refreshed shock 则是 later slower shells 给 blast wave 补充能量；density variation 是 external medium 改变 forward-shock emission。三者都能产生 bump 或 flattening。

区分线索包括：

- bump 是否伴随 spectral evolution；
- optical、X-ray、radio 是否同步变化；
- radio 是否有 self-absorbed flare；
- peak time 是否接近 deceleration / prompt duration；
- 后续 forward-shock energy 是否需要增加；
- 是否需要改变 external density profile。

## 9. 事件接口

- **GRB 990123**：经典 bright optical flash，常作为 reverse-shock prototype。
- **GRB 080319B**：prompt optical 极亮，但 optical/gamma spectral mismatch 要求多 spectral components；reverse shock 只能作为 early afterglow component 的候选，不能解释全部 prompt optical phenomenology。
- **GRB 221009A**：极早期高能与多波段数据丰富，但 TeV、X-ray、radio/mm extra component 的解释需要 forward shock、SSC、structured jet、extra component 并列比较，不能把 early excess 自动归入 reverse shock。

## 10. 常见误区

- **把所有 early optical peak 都叫 reverse shock**：forward-shock onset 也会产生 peak。
- **忽略 shell regime**：thin/thick shell 决定 `t_\times` 与 `T`、`t_dec` 的关系。
- **把 lack of flash 当作 lack of ejecta**：高 `σ`、dust、观测 cadence、频段选择都可隐藏 reverse shock。
- **只看单波段 decay slope**：reverse shock 需要 broadband spectral / temporal consistency。
- **混用 observer-frame 和 source-frame `T`**：涉及 `(1+z)` 时必须说明约定。

## 11. 公式 ID 与代码映射

| formula ID | 内容 | Python reference | C++ kernel | 验证 |
| --- | --- | --- | --- | --- |
| `RS-TDEC-ISM-001` | ISM deceleration time | `models/reverse_shock/analytic.py::deceleration_time_s` | none | `reverse_shock_afterglow_program_check.md` |
| `RS-TDEC-WIND-001` | wind deceleration time | `models/reverse_shock/analytic.py::deceleration_time_s` | none | `reverse_shock_afterglow_program_check.md` |
| `RS-SHELL-001` | thin/thick shell classifier | `models/reverse_shock/analytic.py::shell_regime` | none | `reverse_shock_afterglow_program_check.md` |
| `RS-CROSS-001` | `t_x ~= max(T,t_dec)` | `models/reverse_shock/analytic.py::crossing_time_s` | none | `reverse_shock_afterglow_program_check.md` |
| `RS-NU-M-001` | `nu_m,r ~= Gamma0^-2 nu_m,f` | `models/reverse_shock/analytic.py::reverse_scales_from_forward` | none | `reverse_shock_afterglow_program_check.md` |
| `RS-FMAX-001` | `Fmax,r ~= Gamma0 Fmax,f` | `models/reverse_shock/analytic.py::reverse_scales_from_forward` | none | `reverse_shock_afterglow_program_check.md` |
| `RS-SPEC-TOY-001` | reverse-shock scales mapped into unified synchrotron spectrum | `models/reverse_shock/analytic.py::spectral_breaks_from_reverse` and `reverse_flux_density` | none | `reverse_shock_afterglow_program_check.md` |

## 来源

- R. Sari and T. Piran, early afterglow / reverse shock optical flash papers。
- S. Kobayashi, “Light Curves of Gamma-Ray Burst Optical Flashes,” ApJ 545, 807-812 (2000), arXiv:astro-ph/0009319。
- B. Zhang, S. Kobayashi and P. Mészáros, reverse shock and magnetized ejecta work。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
- J. L. Racusin et al., “Broadband observations of the naked-eye gamma-ray burst GRB 080319B,” Nature 455, 183-188 (2008), arXiv:0805.1557。
