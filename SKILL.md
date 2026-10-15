---
name: firmware-triage
description: 拿到合法取得的 MCU 固件 bin 需要初步分析或准备 Ghidra 逆向时使用。
---
# 步骤
1. 确认固件来源合法、分析目的正当；否则停止。
2. 运行 `scripts/bin_triage.py <bin>`：看熵（是否加密）、向量表（基址、复位入口）、字符串（版本号、外设、协议线索）。
3. 用推测基址在 Ghidra（或 ghidra-headless-mcp）中加载，处理器选 ARM Cortex Little Endian。
4. 从复位向量开始梳理启动流程、外设寄存器访问，标记关键函数。
5. 报告：内存布局、关键函数、外设与协议推断、不确定项。
