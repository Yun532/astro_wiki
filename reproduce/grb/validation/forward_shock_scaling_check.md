# Forward Shock Scaling Check

验证对象：standard adiabatic forward-shock closure relations。

对应理论页：

- `wiki_textbook/grb-afterglow/05-synchrotron余辉谱.md`
- `wiki_textbook/grb-afterglow/06-light-curve-closure-relations.md`
- `wiki_textbook/grb-afterglow/17-afterglow-fitting-workflow与参数简并.md`

对应代码：

- `reproduce/grb/models/forward_shock/analytic_scalings.py`
- `reproduce/grb/core/radiation/synchrotron.py`

自动测试：待补。

人工检查：待用户验证。

已知差异：目前只实现 sharp closure relations 和 toy synchrotron segments；尚未实现 smooth spectral breaks、self-absorption、SSC cooling 或 full normalization。

下一步：用 GRB 221009A 的 X-ray slope 和 radio/SED 数据做 first-pass closure diagnosis。