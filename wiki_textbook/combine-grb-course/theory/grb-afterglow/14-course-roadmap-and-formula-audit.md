# 14 课程路线图与公式审计

状态：v0.1 课程总控页。本页不是新的物理机制，而是给 01-13 页建立学习路线、Formula ID 审计表、代码映射状态和下一批实现优先级。它的目标是防止课程越写越散，也防止代码层把 theory-only 边界误读成已实现功能。

核心原则：课程的完整性不等于代码的完整性；代码验证通过也不等于物理解释完成。每个 Formula ID 都应能回答四个问题：从哪页推导来，解析状态是什么，当前代码是否实现，能支持什么 claim。

## 1. 物理图像

当前 afterglow 课程主线已经从基础动力学延伸到事件解释：

```text
01 external shock dynamics
  -> 02 synchrotron breaks and closure
  -> 03 reverse shock
  -> 04 jet / structured jet / EATS
  -> 05 injection / density degeneracy
  -> 06 NR transition / radio calorimetry
  -> 07 two-component decomposition
  -> 08 polarization / VLBI
  -> 09 fitting workflow
  -> 10 SSC / TeV
  -> 11 acceleration / maximum energy
  -> 12 cascade / neutrino / propagation
  -> 13 event interpretation chain
```

Formula ID：`AG-ROADMAP-COURSE-SPINE-001`。

这条 spine 的设计逻辑是：先写可推导的局域物理，再写几何和多成分，再写高能过程，最后写解释纪律。它不是按照某个事件或某个软件包组织的。

## 2. 学习路线

建议读法分三条：

| Route | Pages | Goal |
| --- | --- | --- |
| standard afterglow core | 01 -> 02 -> 09 -> 13 | 能读懂 closure、breaks、basic reports |
| geometry and components | 03 -> 04 -> 07 -> 08 -> 13 | 能区分 reverse shock、jet、structured jet、polarization/VLBI |
| high-energy extension | 10 -> 11 -> 12 -> 13 | 能审计 SSC、KN、opacity、hadronic/cascade/neutrino claims |

Formula ID：`AG-ROADMAP-LEARNING-ROUTES-001`。

如果只想快速检查一个事件报告，先读 09 和 13；如果要判断 TeV 机制，至少要联读 10、11、12 和 13；如果要判断几何，至少要联读 04、08 和 13。

## 3. 一般审计表达式

对每个 Formula ID，定义审计记录：

$$
\mathcal{A}_{\rm ID}
=
\{
{\rm page},
{\rm quantity},
{\rm derivation\ status},
{\rm code\ layer},
{\rm validation},
{\rm claim\ boundary}
\}.
$$

Formula ID：`AG-ROADMAP-FORMULA-AUDIT-001`。

其中 code layer 只允许有限集合：

$$
{\rm code\ layer}
\in
\{
{\rm theory\ only},
{\rm teaching\ helper},
{\rm toy\ code},
{\rm partial\ code},
{\rm production\ helper},
{\rm benchmark\ output},
{\rm future\ helper}
\}.
$$

Formula ID：`AG-ROADMAP-CODE-LAYER-TAXONOMY-001`。

这不是形式主义。它决定一句话能不能写成：

```text
derived in course
implemented in local code
validated against fixed points
benchmarked against external package
used for event interpretation
```

这五件事必须分开。

## 4. Page-level status matrix

| Page | Main role | Current status | Code relation |
| --- | --- | --- | --- |
| 01 | BM / external shock dynamics | course-derived core | dynamics helpers partially code-backed |
| 02 | synchrotron breaks / closure | course-derived core | synchrotron helpers and closure checks partially code-backed |
| 03 | reverse shock | scale derivation | toy code-backed, not full hydro |
| 04 | jet / structured jet / EATS | geometry derivation | angular/EATS toy helpers |
| 05 | injection / density degeneracy | theory extension | mostly theory-only |
| 06 | NR / radio calorimetry | theory extension | theory-only / teaching |
| 07 | two-component jet | diagnostic extension | theory-only |
| 08 | polarization / VLBI | diagnostic extension | theory-only |
| 09 | fitting workflow | reporting discipline | event scripts / diagnostics, not fitter |
| 10 | SSC / TeV | high-energy leptonic extension | toy SSC / opacity / benchmark-related helpers |
| 11 | acceleration / maximum energy | acceleration boundary | source-agnostic screening helpers exist; full solver missing |
| 12 | cascade / neutrino / propagation | high-energy boundary | theory-only / partial hadronic scale helpers |
| 13 | event interpretation chain | claim discipline | report workflow, not inference engine |

Formula ID：`AG-ROADMAP-PAGE-STATUS-MATRIX-001`。

## 5. Formula ID status classes

当前 Formula IDs 可分成六类 practical classes：

| Class | Meaning | Examples |
| --- | --- | --- |
| core dynamics | blast-wave and shock quantities | `AG-DYN-*`, `FS-DYN-*` |
| radiation core | synchrotron, SSC, opacity kernels | `SYN-*`, `AG-SSC-*`, `AG-TEV-*` |
| geometry diagnostics | jet, EATS, polarization, VLBI | `SJ-*`, `EATS-*`, `POL-*`, `VLBI-*` |
| extension diagnostics | injection, density, two-component, fitting | `EI-*`, `DENS-*`, `TCJ-*`, `FIT-*` |
| high-energy boundary | acceleration, cascade, neutrino | `AG-ACC-*`, `AG-CASCADE-*`, `AG-NU-*` |
| interpretation discipline | claim/report/checklist logic | `AG-INTERP-*`, `AG-ROADMAP-*` |

Formula ID：`AG-ROADMAP-ID-CLASS-001`。

这个分类用于课程维护，不是 physics hierarchy，也不应暗示某个机制比另一个机制“更真实”。

## 6. Code-backed 与 theory-only 边界

最重要的审计区别是：

$$
{\rm derived}
\ne
{\rm implemented}
\ne
{\rm validated}
\ne
{\rm event\ inferred}.
$$

Formula ID：`AG-ROADMAP-DERIVED-IMPLEMENTED-VALIDATED-001`。

当前 broad status：

| Status | Representative content | Safe claim |
| --- | --- | --- |
| code-backed fixed point | BM dynamics helpers, synchrotron characteristic quantities, selected gamma-gamma/SSC helpers | implementation follows stated convention |
| toy / teaching code | reverse shock scales, EATS weights, SSC feedback, energy partition | useful sanity layer |
| benchmark-output | selected `naima` / `agnpy` / EBL-style comparisons | same-convention numerical parity |
| partial-code | source-agnostic acceleration screening, selected cooling / opacity / hadronic scale helpers | subproblem implemented, not full event solver |
| theory-only | injection/density extensions, radio calorimetry, polarization/VLBI, two-component geometry, full cascade/neutrino | course derivation or boundary only |
| missing production solver | full hydrodynamics, full structured-jet light curve, full SSC transfer, afterglow maximum-energy solver, full cascade, neutrino event rate | must not claim implemented |

Formula ID：`AG-ROADMAP-IMPLEMENTATION-BOUNDARY-001`。

## 7. 下一批 helper 优先级

最安全的下一批 code helpers 是 closed expressions 且 blast radius 低的部分：

| Priority | Helper | Formula IDs | Why safe |
| --- | --- | --- | --- |
| done | `larmor_radius_cm` | `AG-ACC-LARMOR-001` | source-agnostic helper exists |
| done | `bohm_acceleration_time_s` | `AG-ACC-TACC-001` | source-agnostic helper exists |
| done | `hillas_max_energy_ev` | `AG-ACC-HILLAS-001` | source-agnostic helper exists |
| done | `electron_synchrotron_loss_limited_gamma_max` | `AG-ACC-SYN-LIMIT-GAMMA-001` | source-agnostic helper exists |
| P2 | `pion_muon_cooling_break_gamma` | `AG-CASCADE-SECONDARY-COOL-DECAY-001` | closed regime boundary |
| P2 | `neutrino_flavor_mix` | `AG-NU-FLAVOR-MIXING-001` | linear mixing helper |
| P2 | `closure_residual_report_row` | `AG-INTERP-CLOSURE-GATE-001` | reporting helper |
| P3 | `secondary_emissivity_integral` | `AG-CASCADE-SECONDARY-EMISSIVITY-001` | needs kernel interface design |
| P3 | `maximum_energy_timescale_competition` | `AG-ACC-COMPETITION-001` | needs channel registry |

Formula ID：`AG-ROADMAP-HELPER-PRIORITY-001`。

不建议立刻实现：

- full \(p\gamma\) secondary spectra;
- Bethe-Heitler pair injection spectrum;
- full EM cascade solver;
- neutrino detector event-rate predictor;
- full MCMC afterglow inference pipeline.

这些需要成熟 kernels、external model choices 或 statistical architecture。过早实现会让代码近似反向决定理论起点。

## 8. Validation map

当前本课程层的 recurring validation commands：

```text
python tools\build_afterglow_html.py
python -m reproduce.grb.validation.check_radiation_dynamics_v2
python -m reproduce.grb.validation.check_unified_spectrum_api
python E:\combine\reproduce\grb\validation_lab\check_trace_manifest.py
python E:\combine\reproduce\grb\validation_lab\check_radiation_acceleration_v1.py
```

做更宽的 release-style checks 时，若本地环境具备可选依赖，也运行 validation-lab suite：

```text
python E:\combine\reproduce\grb\validation_lab\run_validation_suite.py --local-only
```

event-specific report checks、production-suite checks、Formula ID diff checks 与 HTML link smoke checks 只有在 workspace 中确认命令名后，才应加入这张表。

Formula ID：`AG-ROADMAP-VALIDATION-MAP-001`。

这些命令验证已有代码和追踪一致性。它们不把 theory-only pages 验证成 numerical solvers。一个 theory-only page 的“完成”指它具备：

| Requirement | Meaning |
| --- | --- |
| physical picture | what process is being modeled |
| variables / frame | what quantities and reference frame are used |
| general expression | non-delta, non-toy starting point |
| detailed derivation | no hidden "after integration" leap |
| exact analytic status | closed / semi-analytic / numerical boundary |
| approximation hierarchy | where delta / toy formulas belong |
| code convention | how local code differs |
| benchmark boundary | what external packages can and cannot prove |
| must-not-claim | explicit overclaim blockers |

Formula ID：`AG-ROADMAP-THEORY-COMPLETENESS-001`。

## 9. 如何阅读 Formula IDs

Formula ID 不自动等于 function name。它可以是：

| Formula ID type | Example | Implementation expectation |
| --- | --- | --- |
| course-derived equation | `AG-DYN-BM-ENERGY-001` | may have helper |
| diagnostic definition | `FIT-CLOSURE-RESID-001` | may be report-only |
| formal integral | `AG-CASCADE-SECONDARY-EMISSIVITY-001` | needs mature kernel before code |
| approximation hierarchy | `AG-INTERP-APPROX-HIERARCHY-001` | no direct function required |
| benchmark boundary | package parity IDs | external comparison only |
| future helper | `AG-ACC-COMPETITION-001` | design required |

Formula ID：`AG-ROADMAP-FORMULA-ID-READING-001`。

实现时优先使用能表明层级的命名：

```text
*_scale
*_toy
*_teaching
*_fixed_point
*_production
*_benchmark
```

这样 downstream code 更不容易把 sanity helper 误当成 production solver。

## 10. 当前完成度评估

若“完成”指 formal lecture-note boundary，而不是 full numerical inference product，那么本课程已经足以作为第一版 afterglow theory module：

| Dimension | Status |
| --- | --- |
| dynamics spine | formal derivation covered; helpers partial-code |
| synchrotron / closure | formal derivation covered; helpers partial-code |
| reverse shock / jet / geometry | derivation and diagnostic boundary covered |
| injection / density / component degeneracy | theory-only boundary covered |
| radio calorimetry / polarization / VLBI | diagnostic boundary covered |
| SSC / TeV / KN / opacity | formal kernel boundary plus toy/code-boundary covered |
| acceleration / maximum energy | closed-limit derivations plus source-agnostic screening helpers covered |
| cascade / neutrino | formal boundary covered, not solver |
| event interpretation discipline | reporting and claim boundary covered |
| implementation audit | this page establishes it |

Formula ID：`AG-ROADMAP-COMPLETION-ASSESSMENT-001`。

剩余缺口不是失败，而是诚实边界：

- no full hydrodynamic afterglow solver in local code;
- no full structured-jet / EATS light-curve solver;
- no full SSC radiative transfer;
- no maximum-energy timescale registry;
- no \(p\gamma\) / BH / photodisintegration spectrum;
- no EM cascade solver;
- no neutrino event-rate pipeline;
- no full Bayesian event inference.

## 11. 精确解析状态

| Audit object | Status | Comment |
| --- | --- | --- |
| roadmap spine | closed list | changes when pages are added |
| page status matrix | audit table | manually maintained |
| code-layer taxonomy | closed convention | should be reused by future pages |
| helper priority | planning guide | can change with implementation needs |
| validation map | procedural | validates code consistency, not all theory claims |
| completion assessment | qualitative audit | not a proof of scientific completeness |

## 12. 近似层级

| Maintenance layer | What it tracks | Failure mode if skipped |
| --- | --- | --- |
| page index | reading order | users cannot find course path |
| Formula ID index | traceability | formulas become orphan text |
| code-layer label | implementation status | toy helpers become accidental production |
| validation map | regression commands | pages drift from code |
| memory ledger | cross-agent continuity | future work repeats or overclaims |
| report checklist | event discipline | candidate mechanisms become conclusions |

Formula ID：`AG-ROADMAP-MAINTENANCE-HIERARCHY-001`。

## 13. 从推导到代码的实现约定

本页不要求新增 production code。它要求未来 code changes 同步更新：

```text
theory/grb-afterglow/formula-index.md
agents/memory/literature-course-agent.md
agents/memory/derivation-agent.md
agents/memory/verification-agent.md
agents/task-ledger.md
PROJECT_MEMORY.md
```

Formula ID：`AG-ROADMAP-MEMORY-SYNC-001`。

如果未来 helper 实现了某个 Formula ID，formula-index row 必须从 `theory-only` / `future helper` 改为精确 helper path 和 validation command。若 helper 只实现特例，boundary column 必须说明省略了什么。

## 14. Benchmark boundary

本页把所有 external packages 都当作 benchmark 或 mature-method references：

- `afterglowpy` / `VegasAfterglow`: afterglow light-curve benchmark, not course derivation.
- `naima` / `agnpy`: radiation SED parity, not event proof.
- `ebltable`: EBL attenuation table, not built-in propagation truth.
- SOPHIA / AM3 / NeuCosmA / CRPropa / ELMAG: future high-energy process benchmarks, not local solvers.

Benchmark-output belongs in formula-index rows and event reports only when the convention and input parameters are stated.

## 15. 不声称

- 不声称 01-14 页等于完整 GRB afterglow inference system。
- 不声称所有 Formula IDs 都有代码实现。
- 不声称 validation commands validate theory-only cascade, acceleration, geometry or fitting claims.
- 不声称 external packages decide the theory starting point.
- 不声称 roadmap status is a scientific conclusion about any event.

## 16. 参考文件

- `theory/grb-afterglow/index.md`
- `theory/grb-afterglow/formula-index.md`
- `agents/prompts/grb-theory-codex-prompt.md`
- `agents/split-workflows/theory-codex-workflow.md`
- `agents/split-workflows/cross-interface-protocol.md`
- `PROJECT_MEMORY.md`
