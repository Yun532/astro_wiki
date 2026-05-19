# GRB 知识库扩展框架：观测数据、模型推导与复现

日期：2026-05-19

## 背景定位

现有 `astro_wiki_cn` 作为主知识库继续保留，不推翻、不替代。它已有简洁、准确、可链接的中文天文知识库结构，包括 `wiki/`、`wiki_textbook/`、`raw/`、`site/`、知识图谱和元信息页面。

现有 `astro-daily` 只作为补充材料来源：它可以提供每日论文线索、已有摘要、图表提取结果和初步解读，但不能作为知识库主线。主线由用户指定的源、事件、源类、模型或论文集合驱动。

本轮优先方向从 microquasar / SS 433 调整为 GRB。原因是用户当前更关注 GRB，且 `astro_wiki_cn` 已有 GRB 221009A、GRB 030329、GRB 080319B 和 `wiki_textbook/grb-afterglow` 的基础。

## 两个必须满足的核心需求

### 1. 可查、可取用的观测数据和数据文件

当用户想研究一个 GRB 源或事件时，需要能直接找到：

- 原始数据来源：论文、GCN、仪器数据产品、公开数据库、作者表格、supplementary material。
- 处理后数据：光变曲线、SED、spectra、观测日志、拟合点、上限、误差、单位转换后的表格。
- 图像和图表：论文图、caption、provenance、对应数据、科学用途、是否适合复用。
- 数据文件索引：本地路径、外部 URL、格式、单位、时间零点、能段、仪器、处理脚本、使用 caveat。
- 可复现处理链：如果数据来自论文图像或 PDF，需要说明是 source extraction、table extraction、digitization 还是 manual transcription。

目标不是只写“这篇文章用了多波段数据”，而是让未来真正能取数据做图、拟合或比较。

### 2. 可查、完整、可学习的模型理论推导

当用户想使用某个模型，例如 GRB afterglow 的 forward-shock 模型时，需要能从以下链条查下去：

1. 最基础的物理假设。
2. 经典模型来源论文或 review。
3. 动力学方程和辐射机制。
4. 从理论量到观测量的转换。
5. 光变曲线、SED、closure relations、break、jet geometry 的推导。
6. 某篇具体文章采用了哪个模型版本。
7. 该文章相对基础模型改了什么。
8. 拟合了哪些参数，使用了哪些数据，哪些结果是模型推断而不是观测事实。
9. 如果可行，提供 Python / notebook 复现，从 toy model 到论文级拟合近似。

模型推导可以放在 `wiki_textbook/`，也可以在模型页面中用折叠块给出，但原则是：通用理论只写一次，具体论文页面链接到理论源头；文章特有改动和拟合结果写在事件/模型比较页。

## 推荐知识结构

### 简洁主干继续放在 `wiki/`

`wiki/` 保持“准确、简洁、可查”的风格，不写成过长教材。

示例：

```text
wiki/
  20_天体源/
    grb/
      index.md
      grb-221009a/
        index.md
        观测总结.md
        多波段数据.md
        光变曲线.md
        能谱演化.md
        图像索引.md
        数据文件索引.md
        模型解释.md
        模型比较.md
        复现入口.md
        相关文献.md
        未解决问题.md
```

### 理论推导放在 `wiki_textbook/`

`wiki_textbook/` 负责从基础到模型的完整推导链。

示例：

```text
wiki_textbook/
  grb-afterglow/
    index.md
    01-相对论运动学与观测时间.md
    02-观测量与参考系变换.md
    03-fireball模型.md
    04-external-shock动力学.md
    05-synchrotron余辉谱.md
    06-light-curve-closure-relations.md
    07-jet-break与beaming修正.md
    08-energy-injection与refreshed-shock.md
    09-structured-jet与viewing-angle.md
    10-two-component-jet.md
    14-SSC与TeV-afterglow.md
    复现索引.md
```

### 模型变体放在 `wiki/50_模型/`

用于记录每个模型变体相对基础模型改了什么。

```text
wiki/
  50_模型/
    grb模型/
      standard-forward-shock.md
      wind-like-medium-afterglow.md
      structured-jet.md
      two-component-jet.md
      reverse-shock.md
      ssc-tev-afterglow.md
      extra-radio-component.md
```

### 复现代码放在新目录

建议新增：

```text
reproduce/
  grb/
    grb-221009a/
      README.md
      data/
      notebooks/
      scripts/
      outputs/
```

`wiki/` 页面只链接复现入口和结果摘要，代码和数据处理细节放 `reproduce/`。

## 代码跟随模型谱系整理

用户提出一个重要补充：如果模型推导是完整的，代码也应该跟随模型推导逐层构建，而不是按论文临时堆脚本。这是可行且值得长期维护的方向。

核心原则：理论怎么分层，代码也怎么分层；通用辐射机制、动力学、拟合工具独立成模块，具体模型组合这些模块，具体事件只负责数据读取、参数设置、复现图和比较结果。

推荐结构：

```text
reproduce/
  grb/
    core/
      constants.py
      cosmology.py
      units.py
      radiation/
        synchrotron.py
        inverse_compton.py
        ssc.py
        gamma_gamma_absorption.py
      dynamics/
        blastwave.py
        external_medium.py
        jet_geometry.py
      fitting/
        likelihood.py
        priors.py
        lightcurve.py
        sed.py

    models/
      forward_shock/
        analytic_scalings.py
        lightcurve.py
        sed.py
      reverse_shock/
      structured_jet/
      two_component_jet/
      ssc_tev_afterglow/

    events/
      grb_221009a/
        data/
        notebooks/
        fit_forward_shock.py
        fit_broken_powerlaw.py
        compare_models.py
        README.md

    validation/
      synchrotron_check.md
      forward_shock_scaling_check.md
      grb_221009a_lightcurve_check.md
```

### 代码层级职责

#### `core/radiation/`

放独立辐射机制函数，不绑定某篇论文或某个 GRB 事件。

示例：

- synchrotron emissivity / characteristic frequencies。
- inverse Compton。
- SSC。
- gamma-gamma absorption。
- pion decay / hadronic emission，后续可加。

#### `core/dynamics/`

放通用动力学。

示例：

- Blandford-McKee blast wave。
- deceleration radius / deceleration time。
- ISM / wind / general `k` density profile。
- observer time。
- jet opening angle / beaming correction。

#### `core/fitting/`

放通用拟合工具。

示例：

- likelihood。
- chi-square。
- upper limit handling。
- priors。
- broken power-law light curve。
- SED fitting helpers。

#### `models/`

放具体物理模型。模型模块组合 `core/radiation/`、`core/dynamics/` 和 `core/fitting/`。

示例：

- `forward_shock/`
- `reverse_shock/`
- `structured_jet/`
- `two_component_jet/`
- `ssc_tev_afterglow/`

#### `events/`

放具体事件复现，不写通用物理。

示例：

- GRB 221009A 数据读取。
- 论文参数配置。
- 复现 light curve。
- 复现 SED。
- 比较不同模型残差。

### 理论页与代码页互链

每个理论章节应链接对应代码。

示例：

```text
wiki_textbook/grb-afterglow/05-synchrotron余辉谱.md
→ reproduce/grb/core/radiation/synchrotron.py

wiki_textbook/grb-afterglow/04-external-shock动力学.md
→ reproduce/grb/core/dynamics/blastwave.py

wiki_textbook/grb-afterglow/06-light-curve-closure-relations.md
→ reproduce/grb/models/forward_shock/lightcurve.py
```

每个代码文件也应在 docstring 中反向标注理论页面和参考文献。

示例：

```python
"""
Implements synchrotron characteristic frequencies used in GRB afterglow models.

Theory page:
  wiki_textbook/grb-afterglow/05-synchrotron余辉谱.md

References:
  Sari, Piran & Narayan 1998
  Granot & Sari 2002
"""
```

### 验证机制

用户可以人工帮助验证，因此复现代码应有显式验证记录。

每个模块至少记录：

- 公式是否和 textbook 一致。
- 单位是否正确。
- 极限情况是否正确。
- 是否能复现经典论文中的数量级。
- 是否能复现某篇事件论文的图或拟合参数。
- 人工验收状态。

建议每个验证文件使用：

```text
验证对象：
对应理论页：
对应代码：
参考文献：
自动测试：
人工检查：
已知差异：
下一步：
```

### 代码实现策略

每个模型按以下顺序推进：

1. 理论页：从假设推到公式。
2. 代码模块：实现公式。
3. 测试文件：验证 scaling、单位和边界情况。
4. 事件 notebook：应用到具体 GRB。
5. 人工验证记录：由用户或维护者确认结果。

目标不是一次写成完整专业软件，而是逐步形成一个可读、可查、可验证、可扩展的个人 GRB afterglow 建模库。

## 辐射机制库与未来 Python 软件包

用户进一步明确：代码复现层应优先系统整理各种辐射机制，不只服务某一个事件或某一篇 afterglow 论文。后续应逐步覆盖轻子、强子、热辐射和吸收/传播效应，并保证每个代码模块与理论推导页一致。

### 优先覆盖的辐射机制

#### Leptonic mechanisms

- Synchrotron radiation。
- Synchrotron self-absorption。
- Inverse Compton。
- Synchrotron self-Compton。
- Klein-Nishina correction。
- Electron cooling。

#### Hadronic mechanisms

- Proton synchrotron。
- `pγ` interaction。
- `pp` interaction。
- `π0 -> γγ` gamma-ray emission。
- Charged pion / muon decay neutrino channel，后续可作为多信使扩展。
- Hadronic cascade，后续按需要加入。

#### Thermal / plasma mechanisms

- Thermal bremsstrahlung。
- Non-thermal bremsstrahlung。
- Blackbody / photospheric component。
- Pair production / pair opacity。

#### Propagation and attenuation

- `γγ` absorption。
- EBL absorption。
- Internal opacity。
- Cosmological redshift / luminosity distance conversion。

### 推荐包结构

后续可将 `reproduce/grb` 整理成一个轻量 Python package，例如 `astro_repro` 或 `grbmodel`。建议先用清晰源码结构，不急于发布。

```text
reproduce/
  pyproject.toml                  # 后续包化时再加入
  grbmodel/
    __init__.py
    constants.py
    units.py
    cosmology.py
    radiation/
      __init__.py
      synchrotron.py
      inverse_compton.py
      ssc.py
      bremsstrahlung.py
      hadronic_pp.py
      hadronic_pgamma.py
      gamma_gamma.py
      ebl.py
    particles/
      electron_distribution.py
      proton_distribution.py
      cooling.py
    dynamics/
      blastwave.py
      external_medium.py
      jet_geometry.py
    models/
      forward_shock.py
      reverse_shock.py
      structured_jet.py
      hadronic_afterglow.py
    fitting/
      likelihood.py
      priors.py
      lightcurve.py
      sed.py
    plotting/
      lightcurve.py
      sed.py
      corner.py
    cpp/
      README.md
      # optional C++ kernels
    bindings/
      README.md
      # pybind11 / nanobind bindings if needed
```

当前已经创建的 `reproduce/grb/core/` 和 `reproduce/grb/models/` 可以视为软件包化前的原型目录。等接口稳定后，再迁移或软链接到正式 package layout。

### Python 与 C++ 分工

默认优先 Python 实现，因为它适合推导验证、可读性、画图和快速迭代。

当出现以下需求时，可以引入 C++ kernel：

- 需要大量能量网格积分。
- 需要角向 structured jet 数值积分。
- 需要粒子 cascade 或时间依赖输运。
- 需要 MCMC / nested sampling 中反复调用 expensive spectrum 函数。
- Python / NumPy 实现已成为明确瓶颈。

推荐分工：

| 层级 | 语言 | 原则 |
| --- | --- | --- |
| 公式原型 | Python | 与理论页逐行对应，便于人工检查。 |
| 画图与 notebook | Python | matplotlib / scipy / astropy 等生态优先。 |
| 快速拟合工具 | Python + NumPy/SciPy | 先保证正确性。 |
| 重积分 / cascade / structured jet kernel | C++ | 仅在瓶颈明确后加入。 |
| Python binding | pybind11 / nanobind | C++ 结果必须有 Python wrapper 和测试。 |

C++ 不应成为黑箱。每个 C++ kernel 必须有对应 Python reference implementation，哪怕较慢，用于验证。

### 理论-代码一致性要求

每个 radiation module 必须有对应理论页或理论段落。

最低要求：

1. 理论页写清楚假设、变量、单位、适用范围。
2. 代码 docstring 指向理论页和参考文献。
3. 函数参数名尽量和理论页符号一致。
4. 单位统一说明，优先 cgs 或明确 astropy units 层。
5. 每个公式实现有一个最小数值检查。
6. 每个复杂模块有一个 Python reference implementation。
7. C++ kernel 必须和 Python reference 在测试点上对齐。
8. 事件复现不能直接调用未验证模块生成科学结论。

### 验证层级

| 验证层级 | 目标 | 示例 |
| --- | --- | --- |
| Formula check | 单个公式数量级正确 | synchrotron `ν_m`, `ν_c`, `Fν,max`。 |
| Limit check | 极限行为正确 | Thomson limit、KN suppression、高低频谱斜率。 |
| Literature check | 能复现经典论文数量级 | Sari et al. 1998 afterglow scalings。 |
| Event check | 能复现某个事件的图或参数趋势 | GRB 221009A broken power-law / radio SED。 |
| Human check | 用户人工验收 | 记录差异、疑问和是否可信。 |

### 与知识库页面的关系

页面和代码互链：

- `wiki_textbook/`：完整理论推导。
- `wiki/50_模型/辐射模型/`：简洁模型卡片和适用范围。
- `reproduce/grbmodel/radiation/` 或 `reproduce/grb/core/radiation/`：代码实现。
- `reproduce/grb/validation/`：验证记录。
- 事件页 `复现入口.md`：只链接稳定入口，不塞代码细节。

### 图片与网页资产

用户提到网页里现在可能已经有一些图片。后续图像 Agent 需要先检查现有站点或 wiki 资产目录，避免重复提取。若网页已有图片，应优先登记它们的来源和路径，再判断是否需要从 raw/source 包补更高质量版本。

## 页面职责

### `观测总结.md`

记录经过整理的观测事实，不写模型推断。

包括：

- trigger、redshift、距离、定位、时间线。
- 各波段探测事实。
- 关键数值：fluence、peak flux、光变斜率、break time、谱指数、能段、时间范围。
- 仪器 caveat。
- 每条重要 claim 对应来源。

### `多波段数据.md`

按波段和仪器组织数据集。

包括：

- radio / mm
- optical / UV
- X-ray
- MeV / GeV / TeV
- GCN / follow-up photometry
- 数据来源、时间范围、单位、是否公开、是否已本地保存。

### `光变曲线.md`

专门整理 light curve 数据和可拟合结构。

包括：

- 时间零点。
- 时间单位。
- flux / magnitude / count rate 的定义。
- power-law decay index。
- break / bump / plateau。
- 上限和误差处理。
- 对应数据文件。

### `图像索引.md`

每个 figure 必须记录：

- figure id。
- 来源论文。
- 本地图片路径。
- caption。
- provenance：arXiv source / PDF crop / journal page / digitized。
- 科学用途。
- 对应页面。
- 是否可以作为核心图。
- 是否有对应数据文件。

### `数据文件索引.md`

这是新重点页面。

每个数据文件记录：

- 文件名 / 本地路径。
- 外部 URL。
- 来源论文或仪器。
- 数据类型：light curve / SED / spectrum / image / table / model grid。
- 列定义。
- 单位。
- 时间零点。
- 能段。
- 处理状态：raw / cleaned / digitized / model-ready。
- 生成脚本。
- caveat。

### `模型解释.md`

事件级模型解释，只写“哪些论文如何解释该事件”。

原则：

- 观测事实和模型解释分开。
- 拟合参数标注为 model-inferred。
- 每篇文章的模型假设单独列出。
- 通用公式链接到 textbook，不在这里重复长推导。

### `模型比较.md`

横向比较不同文章模型。

建议表格字段：

```text
模型 / 代表论文 / 使用数据 / 基础理论来源 / 相对基础模型的改动 / 关键假设 / 拟合参数 / 能解释什么 / 解释不了什么 / caveat
```

### `复现入口.md`

链接可运行复现材料。

包括：

- toy model。
- light curve fitting。
- SED fitting。
- structured jet 或 SSC 近似。
- 使用的数据文件。
- 输出图。
- 与论文结果的差异。

## 模型推导组织方法

以 afterglow forward-shock 为例，整理链条如下：

1. 基本假设：相对论 ejecta、外部介质、绝热/辐射损失、球对称或 jet geometry。
2. 相对论运动学：arrival time、Doppler factor、beaming。
3. 动力学：Blandford-McKee scaling、deceleration time、ISM / wind density profile。
4. 微物理参数：`epsilon_e`、`epsilon_B`、`p`、`n` 或 `A_*`。
5. 同步辐射：`nu_m`、`nu_c`、`F_nu,max`。
6. 谱段：不同 cooling regime 下的 spectral slopes。
7. 光变：从 `F_nu(t)` 推出 temporal decay index。
8. closure relation：连接 spectral index 与 temporal index。
9. jet break：opening angle、beaming correction、post-break slope。
10. 模型拟合：输入数据、似然、参数、退化、残差。
11. 文章变体：某篇论文使用或改进了上述哪个环节。
12. 编程复现：先实现 scaling toy model，再实现拟合。

## Agent 设计

这些 agent 是工作分工，不一定每次都同时启动。每个 agent 都必须写入或更新明确页面，不做泛泛总结。

### 1. 文献索引 Agent

任务：

- 读取用户给定论文或文献列表。
- 建立文献卡片。
- 判断它更新哪些对象、波段、模型、数据页。
- 提取核心 claim、公式、图表、数据表、模型来源。

输出：

- `相关文献.md`
- `wiki/90_元信息/literature-index.md`
- 待更新页面清单。

### 2. 观测数据 Agent

任务：

- 从论文、supplement、GCN、公开数据库中抽取观测数据。
- 区分 raw、processed、digitized、model-ready 数据。
- 整理单位、时间零点、能段、仪器响应或 calibration caveat。

输出：

- `多波段数据.md`
- `光变曲线.md`
- `能谱演化.md`
- `数据文件索引.md`
- `reproduce/.../data/`

### 3. 图像与图表 Agent

任务：

- 提取或登记 figure。
- 保留 caption 和 provenance。
- 判断 figure 的科学用途。
- 建立 figure 与数据文件、模型页面的链接。

输出：

- `图像索引.md`
- figure assets。
- figure reading notes。

### 4. 模型谱系 Agent

任务：

- 识别论文使用了哪个基础模型。
- 追溯模型来源，例如某篇文章采用了 xxx model，需要找到 xxx 的原始模型或 review。
- 记录模型变体和改进。

输出：

- `模型解释.md`
- `模型比较.md`
- `wiki/50_模型/grb模型/*.md`
- 需要补充的 textbook 章节清单。

### 5. 理论推导 Agent

任务：

- 从基础假设开始补齐模型推导。
- 把通用公式写入 `wiki_textbook/`。
- 把文章特有变体写入模型页或折叠块。
- 标注符号、单位、适用范围、常见误区。

输出：

- `wiki_textbook/grb-afterglow/*.md`
- `wiki_textbook/grb-afterglow/公式索引.md`
- `wiki_textbook/grb-afterglow/符号表.md`

### 6. 编程复现 Agent

任务：

- 根据理论推导实现最小 toy model。
- 根据数据文件实现 light curve 或 SED 拟合。
- 保存代码、notebook、输出图和差异说明。

输出：

- `reproduce/grb/<event>/scripts/`
- `reproduce/grb/<event>/notebooks/`
- `reproduce/grb/<event>/outputs/`
- `复现入口.md`

### 7. 模型比较 Agent

任务：

- 横向比较同一事件的不同模型。
- 对照不同论文的假设、数据、参数和失败点。
- 不强行合并为单一结论。

输出：

- `模型比较.md`
- `wiki/40_综合比较/模型比较/*.md`

### 8. 质检与知识图谱 Agent

任务：

- 检查链接、frontmatter、来源、TODO、orphan pages。
- 检查观测事实和模型解释是否混写。
- 更新 open questions、contradictions、stale claims。
- 更新 graph。

输出：

- `wiki/90_元信息/open-questions.md`
- `wiki/90_元信息/contradictions.md`
- `wiki/90_元信息/stale-claims.md`
- `knowledge_graph.json`
- lint report。

## Agent 增强规划

为了覆盖“图像、数据、模型、公式、代码、验证”全链条，后续正式运行时建议把 agent 进一步细分为 10 个角色。当前 8-agent 设计足够启动，但要稳定完成 GRB 221009A 这类复杂事件，需要更细的分工。

### 1. 文献索引 Agent

负责论文和文献集合的拆解。

输出：

- 文献卡片。
- source-to-page 更新计划。
- claim / table / figure / model / formula 清单。

### 2. 图像提取 Agent

负责从 source package、PDF 或既有工具输出中得到 figure assets。

优先级：

1. 复用当前已有的图片提取工具和其输出目录。
2. 优先使用 arXiv source package 中的原始 figure 文件。
3. 只有在 source 包不可用或图像难以对应时，才使用 PDF page-render crop。
4. 不直接覆盖已有图片资产；如果同一 figure 已存在，先比对 provenance、分辨率和来源，再决定是否新增 variant 或更新索引。

输出：

- figure 文件。
- figure provenance。
- 与论文 source 的对应关系。

### 3. 图像说明 / 读图 Agent

负责把 figure 变成可查知识，而不是只保存图片。

输出：

- `图像索引.md` 条目。
- caption 中文说明。
- 图像科学用途。
- 对应数据文件。
- 对应模型或观测页面。
- 是否适合作为 core figure。

### 4. 数据抽取 Agent

负责从论文 LaTeX 表格、supplement、source package、公开数据库或 figure digitization 中抽出数据。

输出：

- raw extracted table。
- extraction log。
- digitization provenance。
- 缺失数据清单。

### 5. 数据清洗 / 单位 Agent

负责把抽出的数据变成可拟合数据。

输出：

- model-ready CSV / JSON。
- 列定义。
- 单位、时间零点、能段、redshift/source-frame 转换说明。
- upper limit / non-detection 处理说明。

### 6. 模型谱系 Agent

负责追溯某篇文章采用了哪个模型、源头模型是谁、相对基础模型改了什么。

输出：

- 模型谱系表。
- 基础模型链接。
- 文章特定改动。
- model-inferred 参数清单。

### 7. 公式推导 Agent

负责从基础假设到可观测量、再到拟合形式的推导链。

输出：

- `wiki_textbook/` 章节补充。
- 符号表和公式索引更新建议。
- 与代码模块的映射。

### 8. 代码实现 Agent

负责根据公式推导实现代码模块。

输出：

- `reproduce/grb/core/` 通用函数。
- `reproduce/grb/models/` 模型实现。
- `reproduce/grb/events/` 事件脚本 / notebook。
- docstring 中标注理论页和参考文献。

### 9. 复现验证 Agent

负责检查代码是否真的复现了理论或论文数量级。

输出：

- 自动测试。
- 输出图。
- 与论文图 / 表 / 参数的差异。
- 人工验证记录。
- 用户可检查的简表。

### 10. 知识库质检 Agent

负责检查知识库一致性。

输出：

- 观测事实 / 模型解释混写检查。
- 缺来源检查。
- 链接检查。
- open questions / contradictions / stale claims 更新建议。
- graph / lint 生成流程建议。

## 图片 Agent 与现有图片提取工具的关系

图片 agent 不应该替代或绕开现有图片提取工具，而应该作为调度和索引层。

### 不冲突原则

1. **现有工具优先**：如果用户已有 `paper_figure_extractor` 或其他稳定工具，图片 agent 先调用或读取该工具输出，不实现一套平行且命名不同的抽图流程。
2. **raw 不改写**：`raw/arxiv/...` 中的 PDF、source tar、metadata 不改动。
3. **资产目录分离**：提取后的图片放到明确的派生资产目录，例如事件页 `assets/figures/` 或站点/public 专用目录，避免混进 raw。
4. **provenance 必填**：每张图必须记录来自 arXiv source、journal page、PDF crop、还是 digitization。
5. **不覆盖已有文件**：若目标图已存在，先比较来源和质量；必要时用后缀保存 variant，例如 `Fig04-arxiv-source.pdf`、`Fig04-pdf-crop.png`。
6. **索引是权威入口**：最终由 `图像索引.md` 说明哪张图是 core、important、reference-only 或 deprecated。

### 推荐流程

```text
source package / PDF
        ↓
现有图片提取工具
        ↓
图像提取 Agent 检查输出、重命名、记录 provenance
        ↓
图像说明 / 读图 Agent 写入图像索引
        ↓
数据抽取 Agent 判断是否需要从图中 digitize 数据
```

这样图片 agent 和现有工具是上下游关系，不是竞争关系。

## 工作流程

### 阶段 0：确认主题

用户指定：

- 一个 GRB 事件，例如 GRB 221009A。
- 一个模型，例如 forward-shock afterglow。
- 一篇或一组论文。
- 一个具体目标，例如整理 TeV afterglow 数据并复现 light curve break。

### 阶段 1：建立或检查骨架

先检查现有页面，不重写已有简洁内容。

若缺失，则新增：

- `数据文件索引.md`
- `模型比较.md`
- `复现入口.md`
- 必要的模型变体页。

### 阶段 2：文献拆解

每篇论文拆成：

- 观测事实。
- 数据产品。
- 图表。
- 模型假设。
- 公式或模型来源。
- 拟合结果。
- caveat。
- open questions。

### 阶段 3：观测数据归档

优先建立可复用数据资产：

- 光变曲线表。
- SED 表。
- spectra。
- figure assets。
- 数据 provenance。

### 阶段 4：模型谱系追溯

如果论文说采用某个模型或改进某个模型，就向前追溯：

- 原始模型论文。
- review 或 textbook。
- 基础公式。
- 模型变体。
- 文章改动。

### 阶段 5：理论推导补全

把通用推导写到 `wiki_textbook/`。

要求：

- 从假设到方程。
- 从方程到可观测量。
- 从可观测量到拟合形式。
- 每个符号有定义。
- 每个近似有适用范围。

### 阶段 6：编程复现

先做低风险 toy model：

- power-law light curve。
- broken power-law。
- synchrotron spectrum。
- closure relation check。

再逐步做：

- forward-shock light curve。
- SED fitting。
- SSC TeV component。
- structured jet 简化模型。

### 阶段 7：比较与质检

整理不同论文模型之间的关系：

- 哪些共享基础理论。
- 哪些是参数化差异。
- 哪些是真正物理改进。
- 哪些观测能区分模型。
- 哪些问题仍未解决。

## 第一阶段建议样板

建议以 GRB 221009A 为样板，因为现有知识库已有基础，且它天然覆盖用户关心的所有要素：

- prompt energetics。
- multiwavelength afterglow。
- TeV afterglow。
- radio excess。
- structured jet。
- forward shock。
- SSC / TeV 辐射。
- 多篇论文给出不同解释。

第一阶段最小目标：

1. 增强 `grb-221009a/数据文件索引.md`。
2. 增强 `grb-221009a/模型比较.md`。
3. 增强 `grb-221009a/复现入口.md`。
4. 把 LHAASO、Laskar、O'Connor 三条模型解释和数据产品对齐。
5. 在 `wiki_textbook/grb-afterglow/` 中补齐 forward shock 到 light curve fitting 的推导路线。
6. 建立一个最小 Python 复现：broken power-law light curve 或 synchrotron afterglow scaling。

## 不做什么

- 不推翻 `astro_wiki_cn` 原有结构。
- 不让 `astro-daily` 成为主线。
- 不把日报整篇搬进知识库。
- 不把模型推断写成观测事实。
- 不在没有 provenance 的情况下保存数据或图片。
- 不把不同论文模型强行合并成一个最终答案。

## 成功标准

对一个 GRB 事件，例如 GRB 221009A：

1. 用户能从事件入口快速看到已有观测、数据、模型、复现入口。
2. 用户能在数据文件索引中找到可用于画图或拟合的数据文件。
3. 用户能知道每个数据文件来自哪里、单位是什么、时间零点是什么、有什么 caveat。
4. 用户能从模型解释页跳到对应的基础理论推导。
5. 用户能从基础假设一路读到光变或 SED 拟合形式。
6. 用户能看到不同论文模型解释之间的比较。
7. 用户能运行或扩展最小复现代码。
