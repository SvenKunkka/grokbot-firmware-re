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
