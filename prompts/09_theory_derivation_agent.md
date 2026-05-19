# 09 Theory Derivation Agent

用于补齐模型理论推导：从物理假设到可观测量，再到可拟合形式。

## 输入

- 模型谱系 Agent 给出的模型缺口。
- 经典论文、review、textbook。
- 事件复现需要的公式。

## 输出位置

- `wiki_textbook/`：完整推导。
- `wiki/50_模型/`：简洁模型卡片和适用范围。
- `wiki_textbook/.../公式索引.md`、`符号表.md`：必要时更新。

## 写作要求

- 从假设、变量、单位、适用范围开始。
- 标明每个近似：ISM / wind、adiabatic / radiative、slow / fast cooling、on-axis / off-axis 等。
- 公式要能映射到代码参数名。
- 通用理论只写一次；事件页只链接。

## 交付给 Code Agent

- 公式列表。
- 输入/输出变量。
- 单位约定。
- 最小数值检查或经典数量级。

## 禁止事项

- 不在没有来源的情况下“脑补”推导。
- 不把多个符号体系混用而不说明。
- 不写无法映射到代码的长段泛泛解释。
