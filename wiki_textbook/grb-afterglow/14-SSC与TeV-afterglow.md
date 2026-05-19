# 14 SSC 与 TeV afterglow

标准 synchrotron forward shock 可以解释许多 radio–X-ray afterglow，但 GeV–TeV 能段经常需要额外考虑 inverse-Compton process。Synchrotron self-Compton（SSC）是最直接的扩展：同一批 shock-accelerated electrons 先产生 synchrotron photons，再把这些 photons inverse-Compton scatter 到更高能量。

SSC 的重要性不只是“多一个高能成分”。它会改变 electron cooling，从而影响 synchrotron cooling frequency `ν_c`，也会参与解释 GeV–TeV afterglow、maximum synchrotron photon energy、Klein-Nishina suppression、internal γγ absorption 和 EBL absorption 等问题。

## 1. 从 synchrotron 到 SSC

在 comoving frame 中，relativistic electrons 在 magnetic field `B'` 中辐射 synchrotron photons。若这些 photons 的能量密度足够高，同一批 electrons 可继续 inverse-Compton scatter 它们。这个过程称为 synchrotron self-Compton：

```tex
e^- + hν_{syn} \rightarrow e^- + hν_{IC}.
```

Thomson regime 下，若 electron Lorentz factor 为 `γ_e`，被散射 photon frequency 的量级为

```tex
ν_{IC}\sim 2γ_e^2ν_{syn}.
```

因此 synchrotron spectrum 的 `ν_m` 和 `ν_c` 会对应产生 SSC breaks。

## 2. Compton parameter `Y`

SSC cooling 的强弱常用 Compton parameter `Y` 描述：

```tex
Y \equiv \frac{P_{IC}}{P_{syn}}
\sim \frac{U_{ph}}{U_B},
```

其中 `U_ph` 是 seed photon energy density，`U_B=B'^2/8π` 是 magnetic energy density。

在简单 Thomson-regime、one-zone approximation 下，常用量级表达式为

```tex
Y \sim \frac{-1+\sqrt{1+4η\epsilon_e/\epsilon_B}}{2}.
```

这里 `η` 表示 electrons radiated energy fraction，快冷却中可近似为 `η\sim 1`，慢冷却中依赖 `ν_m/ν_c` 和 `p`。这个公式的适用条件很强：忽略 Klein-Nishina suppression，假设 photon field 与 electron population 同区，且不考虑 pair cascade。

## 3. IC-corrected cooling

Synchrotron-only cooling Lorentz factor 在第五章已经给出。若加入 inverse-Compton cooling，总 cooling rate 增加一个 `(1+Y)` 因子，因此

```tex
γ_c =
\frac{6πm_ec}{σ_T B'^2 t'(1+Y)}.
```

对应 cooling frequency 也被降低：

```tex
ν_c \propto γ_c^2 B' Γ
\propto (1+Y)^{-2}.
```

这意味着即使不直接观测 SSC component，SSC 也会通过改变 `ν_c` 影响 optical/X-ray closure relation。若忽略 `Y`，可能误判 cooling regime、density 或 microphysical parameters。

## 4. SSC characteristic breaks

Thomson regime 下，SSC characteristic frequency 量级为

```tex
ν_m^{IC}\sim 2γ_m^2ν_m,
```

```tex
ν_c^{IC}\sim 2γ_c^2ν_c.
```

SSC peak flux 的精确表达依赖 optical depth 和 spectral shape；量级上可以理解为 synchrotron photons 被 electrons 再散射一次，因此与 Thomson optical depth 有关：

```tex
F_{ν,\max}^{IC}\sim τ_e F_{ν,\max}.
```

这里 `τ_e` 是 emitting region 的 electron scattering optical depth。这个表达只适合 order-of-magnitude intuition，实际 fitting 需要完整 SSC spectrum 和 equal-arrival-time integration。

## 5. Klein-Nishina suppression

Thomson approximation 要求 electron rest frame 中 seed photon energy 远小于 `m_ec^2`。若

```tex
γ_e hν'_{syn} \gtrsim m_ec^2,
```

散射进入 Klein-Nishina regime，cross section 下降，IC cooling 和 high-energy flux 都会被抑制。

KN suppression 的后果包括：

- `Y` 不再是简单常数，而依赖 electron energy；
- high-energy SSC spectrum 会变软或截断；
- cooling frequency 的修正不再能用简单 `(1+Y)` 表达；
- TeV afterglow 的 flux 对 `ε_B`、`p`、`Γ` 和 seed photon spectrum 更敏感。

因此在 GRB 221009A 这类 TeV event 中，不能只把 Thomson SSC 公式外推到 TeV。

## 6. Maximum synchrotron photon energy

高能 afterglow 也可能来自 synchrotron 而非 SSC。判断时常比较 acceleration time 与 cooling time。若 Bohm-like acceleration，maximum synchrotron photon energy 在 comoving frame 有一个量级上限，observer frame 中还会乘以 bulk Doppler boost。

当观测 photon energy 达到 GeV–TeV 时，simple synchrotron interpretation 可能面临挑战，但这个判断依赖 acceleration efficiency、bulk Lorentz factor、emission time 和 KN/γγ effects。稳妥写法是：TeV detection 强烈要求检查 SSC、external inverse Compton、hadronic 或 cascade alternatives，而不是自动排除 synchrotron。

## 7. γγ absorption 与 EBL absorption

TeV photons 还会受到 pair production absorption。内部吸收可写成 optical depth：

```tex
τ_{γγ}(E)\sim n_{ph} σ_{γγ} R,
```

量级上，target photon energy 与 high-energy photon 满足 threshold：

```tex
E_γ E_t (1-\cos\theta) \gtrsim 2(m_ec^2)^2.
```

传播到地球途中，TeV photons 还会被 extragalactic background light（EBL）吸收。观测 flux 与 intrinsic flux 的关系常写成

```tex
F_{obs}(E,z)=F_{int}(E)\exp[-τ_{EBL}(E,z)].
```

因此 TeV afterglow interpretation 必须说明是否做了 EBL correction，以及使用了哪种 EBL model。

## 8. GRB 190114C 与 GRB 221009A 接口

GRB 190114C 是 TeV afterglow / SSC interpretation 的关键事件之一，MAGIC detection 强化了 afterglow SSC component 的观测地位。GRB 221009A 中，LHAASO 探测到大量 TeV photons，使 TeV afterglow、narrow jet、structured jet core、SSC 和 EBL/γγ absorption 都成为模型比较核心。

在本 wiki 中，GRB 221009A 的写法应保持并列：

- TeV narrow-jet interpretation 是 LHAASO 等 source 的模型解释；
- X-ray long decay 可与 shallow structured jet 联系；
- radio/mm extra component 在 Laskar et al. 中不能由若干 simple prescriptions 解释；
- SSC 是高能余辉候选机制之一，但不是自动唯一解释。

## 9. 常见误区

- **把 TeV photon 自动等同于 SSC**：synchrotron extreme、external IC、hadronic/cascade 都需作为 alternatives 说明。
- **忽略 KN suppression**：Thomson `ν_{IC}\sim2γ^2ν` 不能无限外推。
- **忽略 SSC 对 `ν_c` 的反作用**：即使不拟合 TeV，`Y` 也影响 synchrotron cooling。
- **把 observed TeV flux 当作 intrinsic flux**：必须考虑 EBL absorption。
- **混用 photon index 和 spectral index**：高能论文常用不同谱指数定义，需核对。

## 来源

- R. Sari and E. Esin, “On the Synchrotron Self-Compton Emission from Relativistic Shock Waves and Its Implications for Gamma-Ray Burst Afterglows,” ApJ 548, 787-799 (2001), arXiv:astro-ph/0005253。
- J. Granot and R. Sari, “The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows,” ApJ 568, 820-829 (2002), arXiv:astro-ph/0108027。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
- MAGIC Collaboration GRB 190114C TeV afterglow papers。
- LHAASO Collaboration, “A tera-electronvolt afterglow from a narrow jet in an extremely bright gamma-ray burst 221009A,” Science 380, 1390-1396 (2023), arXiv:2306.06372。
- T. Laskar et al., “The Radio to GeV Afterglow of GRB 221009A,” ApJL, arXiv:2302.04388。
