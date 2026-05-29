# 16 章节总结与 Must-Not-Claim 索引

状态：v0.1 章节收口页。本页把 afterglow 课程 01-15 页整理成一份中文总结和过度声称索引。它不是新的推导页，也不是事件结论页，而是后续 agent 独立审稿、缺口扫描和补充改写的基准。

核心原则：一个章节写完，不代表每个物理过程都已经有 production solver；一条机制可行，不代表它是某个事件的唯一解释；一个外部包能复现某个 SED，不代表它证明了该机制的物理起源。

## 1. 全章主线总结

本章现在以讲义级边界覆盖 GRB afterglow 理论解释链：

```text
external shock dynamics
  -> synchrotron spectrum and closure
  -> reverse shock and early optical
  -> jet / structured jet / EATS
  -> injection, density and component degeneracies
  -> NR transition, radio calorimetry
  -> polarization and VLBI diagnostics
  -> fitting workflow and event interpretation
  -> SSC / TeV / acceleration / cascade / neutrino boundaries
  -> conventions, roadmap and claim discipline
```

Formula ID：`AG-SUMMARY-SPINE-001`。

课程已经足以支撑“讲义级 afterglow 主线”：学生可以从 BM 动力学走到 closure relations，再走到几何、高能和事件解释纪律。但这里的“覆盖”指 formal derivation / theory-only boundary / partial-code mapping，不是 full numerical afterglow inference system。

## 2. 可作为课程结论的内容

以下内容可以作为本章课程结论：

| 类别 | 可声称内容 |
| --- | --- |
| dynamics | BM 标度、ISM/wind 差异、deceleration scale、shock jump 近似 |
| synchrotron | \(\gamma_m,\gamma_c,\nu_m,\nu_c,F_{\nu,\max}\) 的推导结构和 closure limits |
| reverse shock | thin/thick shell、crossing-time scale、forward/reverse ratio 的教学近似 |
| jet / geometry | top-hat jet-break condition、structured-jet angular variables、EATS delay |
| degeneracy | injection、density、component mixing 会改变 light curve interpretation |
| diagnostics | polarization、VLBI、radio calorimetry 是约束，不是单独证明 |
| high energy | SSC / KN / \(\gamma\gamma\) / EBL / acceleration / cascade 必须联合审计 |
| workflow | observed / derived / model-inferred / benchmark-output 必须分层 |

Formula ID：`AG-SUMMARY-COURSE-CLAIMS-001`。

## 3. Code-Backed、Partial-Code 与 Theory-Only 总览

| 层级 | 内容 | 允许说法 |
| --- | --- | --- |
| code-backed / fixed point | 部分 dynamics、synchrotron、gamma-gamma、SSC toy / unified spectrum checks | 本地实现符合 stated convention |
| toy / teaching | reverse shock scale、EATS weights、SSC \(Y\) feedback、hadronic energy partition | 可做 sanity check |
| partial-code | selected opacity / cooling / hadronic / acceleration screening helpers | 只覆盖子问题 |
| source-adapter smoke | forward-shock local-zone adapter `AG-FS-LOCAL-ZONE-001` | 可把 BM \(B',R',U'_{\rm ph}\) 交给 radiation workbench 做筛选 |
| source-adapter smoke | forward-shock cooling / acceleration time series `AG-FS-COOL-ACC-SCREEN-001` | 可比较 BM 局域区内 cooling、escape、Bohm-like acceleration 的时间标度 |
| source-adapter smoke | forward-shock gamma-gamma opacity screen `AG-FS-GG-OPACITY-SCREEN-001` | 可把 BM 局域区与 caller-supplied mono target envelope 接到 \(\alpha_{\gamma\gamma}\)、\(\tau\)、attenuation 筛选 |
| source-adapter smoke | forward-shock tabulated target opacity screen `AG-FS-GG-TARGET-SPECTRUM-SCREEN-001` | 可把 caller-supplied target spectral shape 归一化到 BM 局域能量密度 envelope 后做 opacity 筛选 |
| benchmark-output | `naima` / `agnpy` / EBL-style comparison | 同参数同 convention 对照 |
| theory-only | injection/density extensions、polarization/VLBI、two-component、full acceleration solver、cascade/neutrino | 课程推导或边界 |

Formula ID：`AG-SUMMARY-CODE-STATUS-001`。

这张表应成为审稿 agent 的第一张检查表：如果某页把 theory-only 内容写成 code-backed，就是高优先级问题。

## 4. Must-Not-Claim：动力学与几何

| Topic | 不应声称 |
| --- | --- |
| BM dynamics | 不声称 BM 是完整 hydrodynamic simulation |
| ISM/wind | 不声称 closure residual 可唯一判定介质 |
| jet break | 不声称一个 achromatic steepening 必然是 jet break |
| structured jet | 不声称 toy angular weighting 是 full structured-jet light curve |
| EATS | 不声称简单 delay/weight integral 等于完整图像合成 |
| two-component | 不声称任何双峰或额外成分都证明 two-component jet |
| VLBI | 不声称 centroid motion 直接等于 shock radius |
| polarization | 不声称 polarization detection 单独证明 jet geometry |

Formula ID：`AG-MNC-DYNAMICS-GEOMETRY-001`。

## 5. Must-Not-Claim：辐射与高能过程

| Topic | 不应声称 |
| --- | --- |
| synchrotron | 不声称 broken power law 是完整 kernel spectrum |
| closure | 不声称 closure relation alone 证明模型 |
| SSC | 不声称 constant \(Y\) 描述 KN-dominated cooling |
| TeV | 不声称 TeV photon 自动来自 SSC 或 hadronic |
| \(\gamma\gamma\) | 不声称 \(\tau=n\sigma l\) 是完整 opacity |
| EBL | 不声称内置了唯一 EBL model |
| acceleration | 不声称 Hillas condition 足以证明加速可行 |
| local-zone screening | 不声称 forward-shock local-zone summary 等于 observed flux、event fit、full hydrodynamics、complete maximum-energy solver 或 self-consistent SSC transfer |
| cooling / acceleration time series | 不声称 fixed-probe timescale screening 等于 particle transport、PIC shock acceleration、reconnection/turbulence model、UHECR source proof 或 neutrino/cascade prediction |
| forward-shock gamma-gamma opacity screen | 不声称 mono target envelope 等于 full source opacity transfer、observed flux inversion、self-consistent SSC target field、EATS-integrated opacity、EBL/cascade model 或事件机制判定 |
| forward-shock tabulated target opacity screen | 不声称 caller-supplied target shape 已由 synchrotron/SSC transfer 自洽产生，也不声称它是 EBL、cascade、事件拟合或 TeV 唯一起源判定 |
| proton synchrotron | 不声称 SED parity 证明 protons 可达所需能量 |
| cascade | 不声称 \(\tau_{\gamma\gamma}\) 给出 cascade reprocessed flux |
| neutrino | 不声称 \(E_\nu\simeq0.05E_p\) 是 neutrino spectrum |

Formula ID：`AG-MNC-RADIATION-HE-001`。

## 6. Must-Not-Claim：事件解释与外部包

| Topic | 不应声称 |
| --- | --- |
| best fit | 不声称 best-fit table 证明唯一物理起源 |
| benchmark | 不声称 package output 是 observation |
| GRB 221009A | 不声称某 candidate mechanism 是唯一解释 |
| upper limit | 不声称 non-detection 等价于机制排除，除非 likelihood 和 model 已写清 |
| model ladder | 不声称复杂模型必然更真实 |
| missing solver | 不声称本地没有实现就代表物理不存在 |

Formula ID：`AG-MNC-EVENT-BENCHMARK-001`。

## 7. 后续 Agent 审稿任务

本章已经进入独立审稿阶段，当前启用 agents 做三类任务：

| Agent role | 审稿重点 |
| --- | --- |
| literature-course-agent | 来源是否充分，benchmark 是否越界，事件语气是否过强 |
| derivation-agent | general expression 是否先行，推导是否跳步，delta approximation 是否后置 |
| verification-agent | Formula ID 是否同步，code convention 是否写清，must-not-claim 是否完整 |

Formula ID：`AG-SUMMARY-AGENT-REVIEW-PLAN-001`。

主写仍应保持统一整合。agent 适合独立审稿、缺口扫描和局部改写建议，不适合分散重写整章主线。

## 8. 下一批可实现内容

不做课程习题页。若进入实现阶段，建议优先实现低风险 helper：

| Priority | 内容 |
| --- | --- |
| done | Larmor radius、Bohm acceleration time、Hillas energy、synchrotron-limited gamma 的 source-agnostic screening helpers |
| P2 | pion/muon cooling break、neutrino flavor mixing、closure report row |
| P3 | maximum-energy timescale registry、secondary emissivity kernel interface |

Formula ID：`AG-SUMMARY-NEXT-IMPLEMENTATION-001`。

暂不建议直接写 full cascade、full \(p\gamma\) spectrum、BH pair injection、neutrino event-rate 或 MCMC inference。它们需要成熟核函数、外部模型或统计架构，过早实现会让代码近似反向决定理论起点。

## 9. 章节完成度

| 维度 | 完成度 |
| --- | --- |
| 中文课程主线 | 已建立 |
| 公式可追踪性 | 已有 Formula ID index |
| 理论/代码边界 | 已在各页和 14 页注册 |
| 高能边界 | 以 formal boundary / partial-code 形式覆盖 SSC、KN、opacity、acceleration、cascade、neutrino |
| 事件解释纪律 | 以报告规则和 must-not-claim 形式覆盖 |
| 代码完整实现 | 未完成，也不应伪装完成 |
| 独立 agent 审稿 | 已启动，并进入缺口整合 |

Formula ID：`AG-SUMMARY-COMPLETION-001`。

## 10. Exact Analytic Status

| 对象 | 状态 | 说明 |
| --- | --- | --- |
| chapter summary | qualitative audit | 随章节变化更新 |
| must-not-claim index | workflow rule | 审稿时逐项检查 |
| agent review plan | process plan | 需要用户允许实际 spawn agents |
| next implementation list | planning guide | 不是代码承诺 |

## 11. Approximation Hierarchy

| 层级 | 应有说法 | 禁止说法 |
| --- | --- | --- |
| course-derived | 由讲义推导得到 | 已生产实现 |
| teaching helper | 可检验 fixed point | 完整模型 |
| toy code | 趋势 sanity | 事件拟合 |
| partial code | 子问题实现 | 全流程 solver |
| benchmark-output | 同 convention 对照 | 物理证明 |
| event interpretation | candidate / consistency / tension | 唯一起源 |

Formula ID：`AG-SUMMARY-APPROX-HIERARCHY-001`。

## 12. 从推导到代码的实现约定

本页不新增 production code。后续任何实现都必须更新：

```text
theory/grb-afterglow/formula-index.md
theory/grb-afterglow/14-course-roadmap-and-formula-audit.md
agents/memory/*
agents/task-ledger.md
PROJECT_MEMORY.md
```

Formula ID：`AG-SUMMARY-SYNC-REQUIREMENT-001`。

## 13. Benchmark Boundary

本章允许使用外部包做 benchmark，但必须保留三层文字：

1. 课程推导是什么；
2. 本地代码实现了什么近似；
3. 外部包对照只说明什么 convention 下的一致性。

Formula ID：`AG-SUMMARY-BENCHMARK-BOUNDARY-001`。

## 14. 不声称

- 不声称本章已经完成 full GRB afterglow inference。
- 不声称任何单页诊断能唯一解释事件。
- 不声称 theory-only Formula ID 有代码实现；已有 partial-code 的 Formula ID 也只代表相应子问题。
- 不声称 benchmark-output 是观测事实。
- 不声称 validation commands 覆盖未实现的 cascade、full acceleration solver、geometry 或 inference solver。
- 不声称 GRB 221009A 或其他事件已有唯一机制结论。

## 15. 参考文件

- `theory/grb-afterglow/index.md`
- `theory/grb-afterglow/formula-index.md`
- `14-course-roadmap-and-formula-audit.md`
- `15-notation-frames-and-convention-registry.md`
- `agents/prompts/grb-theory-codex-prompt.md`
