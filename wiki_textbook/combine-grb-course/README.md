# combine GRB course snapshot

状态：2026-05-29 同步快照。这个目录把 `E:\combine` 中正在编写的 GRB 理论课程主线同步到旧知识库仓库的独立分支，便于 GitHub diff、代码审阅和网页端查看。

## 内容

- `theory/radiation-mechanisms/`：辐射机制课程源码 Markdown。
- `theory/grb-afterglow/`：GRB afterglow 课程源码 Markdown。
- `site/public/combine-grb-course/radiation-mechanisms/`：辐射机制课程已编译 HTML。
- `site/public/combine-grb-course/grb-afterglow/`：余辉课程已编译 HTML。

## 网页入口

如果这个分支合并或部署到 GitHub Pages，静态入口为：

- `/combine-grb-course/`
- `/combine-grb-course/radiation-mechanisms/index.html`
- `/combine-grb-course/grb-afterglow/index.html`

## 同步边界

这个快照只同步课程源码和编译网页，不把 `E:\combine` 的全部实验代码、validation outputs、agent 工作区或本地临时文件写入旧知识库。课程页中的 theory-only、teaching-only、benchmark-output、production-helper 等标签仍按页面声明解释；不能因为出现在网页快照中就升级为已完成 solver。

本次同步前在 `E:\combine` 已通过：

```powershell
python tools\build_theory_html.py
python tools\build_afterglow_html.py
python -m reproduce.grb.validation.check_radiation_dynamics_v2
python -m reproduce.grb.validation.check_unified_spectrum_api
python E:\combine\reproduce\grb\validation_lab\check_trace_manifest.py
python -m reproduce.grb.validation_lab.check_radiation_acceleration_v1
python -m reproduce.grb.validation.check_radiation_mechanisms_v1
```
