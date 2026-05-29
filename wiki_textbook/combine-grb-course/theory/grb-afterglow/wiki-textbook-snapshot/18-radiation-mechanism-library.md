# 18 Radiation mechanism library

本章把 GRB 复现代码中需要的辐射机制拆成独立模块。它不是替代前面的 afterglow 主线，而是为“模型怎么组合代码”建立接口：轻子、强子、热过程和传播吸收先各自写清楚，再由 forward shock、SSC TeV afterglow、structured jet 或 hadronic afterglow 去组合。

## 1. 共同约定

默认采用 cgs 单位。函数接口必须说明输入量是否在 comoving frame、source frame 或 observer frame。事件脚本不得在没有记录的情况下做 redshift、extinction、absorption、EBL 或 bolometric correction。

最小代码映射：

| 机制层 | Python reference | C++ 候选 | 备注 |
| --- | --- | --- | --- |
| synchrotron / SSA | `reproduce/grb/core/radiation/synchrotron.py` | 后置 | 当前已有 sharp-break toy spectrum；后续补 emissivity / absorption coefficient。 |
| inverse Compton / SSC | `reproduce/grb/core/radiation/inverse_compton.py`、`ssc.py` | 高维谱积分后置 | 第一轮只做 Thomson/KN 数量级与 cooling 修正。 |
| hadronic | `reproduce/grb/core/radiation/hadronic.py` | cascade 后置 | 第一轮只做 pp / p-gamma / pion decay / neutrino 能量尺度。 |
| thermal / bremsstrahlung | `reproduce/grb/core/radiation/bremsstrahlung.py`、`thermal.py` | 后置 | 第一轮只做 emissivity 数量级和 blackbody/photosphere 工具。 |
| propagation / opacity | `reproduce/grb/core/radiation/gamma_gamma.py` | `reproduce/grb/cpp/` | gamma-gamma、EBL 和 structured-jet angular integral 是 C++ 候选。 |

## 2. 轻子机制

### 2.1 Synchrotron 与 self-absorption

给定电子 Lorentz factor `γ_e`、comoving magnetic field `B'` 和 redshift `z`，单电子特征频率的数量级为

```text
ν_syn,obs ≈ Γ / (1+z) * (3 e B' / 4π m_e c) * γ_e²
```

幂律电子 `N(γ_e) ∝ γ_e^{-p}` 产生的 optically thin spectrum 在 slow cooling 下常用谱段：

```text
F_ν ∝ ν^(1/3)                 ν < ν_m
F_ν ∝ ν^(-(p-1)/2)            ν_m < ν < ν_c
F_ν ∝ ν^(-p/2)                ν > ν_c
```

SSA 需要吸收系数 `α_ν` 和源大小，第一轮只保留接口，不把 radio turnover 自动解释成 SSA。V2 增加慢冷两种 SSA ordering：`ν_a<ν_m<ν_c` 和 `ν_m<ν_a<ν_c`。代码只给 toy optically thick slope 和 suppression factor，仍不提供完整 absorption coefficient 或 source-size fit。

### 2.2 Inverse Compton、SSC 和 Klein-Nishina

Thomson regime 中，seed photon 频率 `ν_seed` 被电子散射到

```text
ν_IC ≈ 2 γ_e² ν_seed
```

SSC 是 seed photon 来自同一 synchrotron population 的特例：

```text
ν_m^IC ≈ 2 γ_m² ν_m
ν_c^IC ≈ 2 γ_c² ν_c
```

Compton parameter 的常用数量级为

```text
Y ≈ [-1 + sqrt(1 + 4 η ε_e / ε_B)] / 2
```

其中 `η` 表示电子 radiative efficiency。进入 KN regime 时，上式会高估 IC cooling 和 TeV flux；代码必须允许单独记录 KN suppression。V2 的 SSC 接口加入 `Y` 与 `ν_c` 的 toy fixed-point iteration：先由 `η(ν_m,ν_c,p)` 估计 `Y`，再用 `ν_c=ν_{c,0}/(1+Y)^2` 更新 cooling break。KN 仍只是 scalar suppression，不是完整 energy-dependent KN spectrum。

## 3. 强子机制

强子模型不能只写“hadronic component”。至少区分：

- proton synchrotron：高能 proton 在强磁场中辐射，冷却时间长、能量预算通常严苛。
- `pp` interaction：目标质子密度 `n` 和路径 `l` 给出薄靶效率 `f_pp ≈ n σ_pp l`。
- `pγ` interaction：阈值由 proton energy 和 photon field 决定，常连接 neutrino 与 gamma-ray cascade。
- `π0 -> γγ`：每个 gamma-ray 的特征能量约为 pion 能量的一半。
- charged pion / muon decay：给出 neutrino channel，事件页应主要记录 upper limit 或无显著探测。

第一轮代码只做能量尺度和效率上限，不声称完整 cascade。

`pγ` interaction 的阈值可用 invariant `s` 的数量级表示。对 head-on collision：

```text
E_p ε_γ ≳ 0.3 GeV^2 Γ^2 / (1+z)^2
```

代码中的 toy 接口只返回给定 target photon energy 时的 proton threshold，不处理 photon spectrum、inelasticity 或 cascade。

Proton synchrotron 的 characteristic frequency 与 electron synchrotron 形式相同，但用 proton mass：

```text
ν_p,syn ∝ Γ/(1+z) * (q_e B' / m_p c) * γ_p²
```

由于 `m_p >> m_e`，同样 Lorentz factor 下 proton synchrotron frequency 更低，若要解释高能 photon 通常需要极高 `γ_p` 和强磁场。

## 4. 热过程与 photosphere

### 4.1 Thermal / non-thermal bremsstrahlung

热 bremsstrahlung emissivity 的数量级可写成

```text
ε_ff ∝ n_e n_i T^{1/2}
```

在 GRB afterglow 中它通常不是标准 radio-to-TeV afterglow 的主导机制，但可作为热等离子体或周围介质诊断的独立模块。

### 4.2 Blackbody / photosphere

Fireball photosphere 半径和 blackbody component 用于 prompt / thermal component 讨论。对于观测到的温度 `T_obs` 和 flux `F_bb`，可先建立 luminosity 和 photospheric radius 的数量级接口，再决定是否进入事件页。

最小接口：

```text
L_bb = 4π R_bb² σ_SB T⁴
R_bb = sqrt(L_bb / 4πσ_SB T⁴)
```

Fireball photosphere 的 toy baryonic coasting radius 可写为

```text
R_ph ~ L σ_T / (8π m_p c^3 Γ^3)
```

系数依赖 wind/shell geometry；事件页必须说明采用 convention。

## 5. 传播和吸收

TeV photon 必须检查：

- internal `γγ` opacity：源内高能 photon 与低能 photon 相互作用。
- EBL attenuation：传播过程中被 extragalactic background light 吸收。
- redshift 和 luminosity distance：影响能量、时间和 flux conversion。

Pair-production threshold 的最小检查为：

```text
E_γ ε_target (1 - cosθ) ≳ 2 (m_e c²)^2
```

代码中 `pair_threshold_target_energy_kev` 只处理 threshold；真实 optical depth 还需要 photon field、geometry 和 cross section integral。V2 把 internal opacity 和 EBL attenuation 拆开：internal `τ_γγ` 需要 source photon density 和 path length；EBL attenuation 只接受外部给定的 `τ_EBL(E,z)`，代码不内置 EBL model。

GRB 221009A 的 TeV 解释不能自动等同于 SSC；需要把 synchrotron maximum energy、SSC、hadronic/cascade、EBL 和 internal opacity 都列为可查替代项。

## 6. 事件接口

对于 GRB 221009A：

- `radio/mm`：先用 synchrotron/SSA 和 forward-shock closure 做基线，再记录 extra component 需求。
- `GeV/TeV`：先用 synchrotron maximum energy、SSC、gamma-gamma/EBL 三个模块做 sanity check。
- `neutrino`：只把 IceCube/GCN 的 upper limit 或 non-detection 作为 hadronic constraint，不把它写成电磁数据点。
- `structured jet`：辐射机制只给局部 emission；角向积分属于 geometry / dynamics 模型层。

## 7. 最小验证点

| 机制 | 验证点 | 验证等级 |
| --- | --- | --- |
| synchrotron | `p=2.2` 时 slow-cooling slope `β=(p-1)/2=0.6`、`β=p/2=1.1` | formula-only |
| SSC | Thomson regime `ν_IC / ν_seed ≈ 2γ²` | formula-only |
| SSC feedback | positive `Y` lowers `ν_c` relative to synchrotron-only value | toy-model |
| SSA regime | `ν_a<ν_m<ν_c` and `ν_m<ν_a<ν_c` return distinct toy slopes | toy-model |
| EATS geometry | constant emissivity returns constant weighted average; delay is positive | toy-model |
| pp | `f_pp=min(n σ_pp l, 1)` 在薄靶极限线性增长 | toy-model |
| blackbody | `L=4πR²σ_SB T⁴` 数量级一致 | formula-only |
| gamma-gamma | pair threshold 随 soft photon energy 反比变化 | toy-model |
| `pγ` | target photon energy 越高，proton threshold 越低 | toy-model |
| photosphere | `R_ph ∝ L Γ^{-3}` | toy-model |

## 来源

- Rybicki & Lightman 1979，用于辐射机制基础。
- Sari, Piran & Narayan 1998；Granot & Sari 2002，用于 synchrotron afterglow。
- Sari & Esin 2001，用于 SSC afterglow。
- Zhang 2014 review，用于 GRB radiation mechanism 和 afterglow framework。
- Piran 2004、Mészáros 2001，用于 fireball/photosphere 背景。
- LHAASO Collaboration 2023，用于 GRB 221009A TeV caveat。
