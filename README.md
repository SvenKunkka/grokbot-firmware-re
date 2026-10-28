<!-- SVENKUNKKA-README-NAV:BEGIN -->
[English overview](#project-overview-en) · [中文项目说明](#project-overview-zh) · [Maintainer on X / 维护者 X](https://x.com/Svenu1s5)
<!-- SVENKUNKKA-README-NAV:END -->

<!-- SVENKUNKKA-PROJECT-INFO:BEGIN -->

<a id="project-overview-en"></a>
## English project overview

Provides initial triage for lawfully obtained MCU firmware: size, SHA-256, block entropy, printable strings, and Cortex-M vector-table and load-address hypotheses to support further Ghidra analysis.

**Getting started:** Uses only the Python standard library. Run `python scripts/bin_triage.py firmware.bin --base 0x08000000`; see `SKILL.md` for the workflow.

**Scope:** Vector-table, base-address, and encryption or compression findings are leads requiring further verification. Analyze only firmware you are authorized to examine.

**Repository maintainer / 仓库维护者:** [SvenKunkka](https://github.com/SvenKunkka) · [X / Twitter](https://x.com/Svenu1s5)

<a id="project-overview-zh"></a>
## 中文项目说明

为合法取得的 MCU 二进制固件提供初步分诊：统计大小、SHA-256、分块熵和可打印字符串，并推测 Cortex-M 向量表及加载基址，辅助后续 Ghidra 分析。

**使用入口：** 仅需 Python 标准库；运行 `python scripts/bin_triage.py firmware.bin --base 0x08000000`，分析流程见 `SKILL.md`。

**范围说明：** 向量表、基址与加密或压缩状态属于分析线索，仍需进一步核验；仅分析有权处理的固件。

<!-- SVENKUNKKA-PROJECT-INFO:END -->

---



# grokbot-firmware-re
对**合法取得**的 MCU 固件 .bin 做初步分诊，再交给 Ghidra 深入分析。

## 优先复用的上游（深入分析）
- [mrphrazer/ghidra-headless-mcp](https://github.com/mrphrazer/ghidra-headless-mcp)：无界面 Ghidra MCP，默认只读
- [xjoker/ghidra-mcp](https://github.com/xjoker/ghidra-mcp)（Apache-2.0）
- [nightwing-us/mcpyghidra](https://github.com/nightwing-us/mcpyghidra)（Apache-2.0）

本仓库只提供 `scripts/bin_triage.py`（仅依赖 Python 标准库）：大小、SHA-256、分块熵（判断加密 / 压缩）、可打印字符串，以及 Cortex-M 向量表推测（初始 SP、复位向量，推测加载基址），方便在 Ghidra 中设置正确的内存映射。

## 用法
```bash
python scripts/bin_triage.py firmware.bin --base 0x08000000
```
仅限你有权分析的固件，遵守当地法律与许可协议。


