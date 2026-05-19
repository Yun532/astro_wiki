# 10 Code Reproduction Agent

用于把理论推导和事件数据变成可运行代码。代码必须跟随模型层级组织，而不是按论文临时堆脚本。

## 代码分层

- `reproduce/grb/core/`：通用常数、单位、辐射机制、动力学、拟合工具。
- `reproduce/grb/models/`：具体模型组合，例如 forward shock、reverse shock、structured jet、SSC。
- `reproduce/grb/events/`：具体事件数据读取、脚本、输出。
- `reproduce/grb/validation/`：验证记录。

## 实现规则

- 先 Python reference implementation，只有瓶颈明确时再加 C++ kernel。
- 每个代码文件 docstring 标明 theory page 和参考文献。
- 函数参数名尽量与理论页符号一致。
- 事件脚本不能直接生成未验证的科学结论。
- 输出图和表必须写明“toy / sanity check / paper-level reproduction”的等级。

## 输出

- 通用模块、模型模块、事件脚本或 notebook。
- 输出 CSV / PNG / 验证记录。
- 与 wiki `复现入口.md` 的链接。

## 禁止事项

- 不把临时探索脚本当正式复现。
- 不引入 C++ 黑箱；C++ 必须有 Python reference 和测试点。
- 不覆盖用户数据。
