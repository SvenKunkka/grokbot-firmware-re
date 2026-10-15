#!/usr/bin/env python3
"""固件 .bin 分诊：哈希、熵、字符串、Cortex-M 向量表推测。只读。"""
import argparse, hashlib, math, re, struct

def entropy(b):
    if not b: return 0.0
    c = [0] * 256
    for x in b: c[x] += 1
    return -sum(n / len(b) * math.log2(n / len(b)) for n in c if n)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("bin"); ap.add_argument("--base", default=None)
    ap.add_argument("--block", type=int, default=4096); ap.add_argument("--strings", type=int, default=30)
    a = ap.parse_args(); data = open(a.bin, "rb").read()
    print(f"大小 {len(data)} 字节  SHA-256 {hashlib.sha256(data).hexdigest()}")
    ents = [entropy(data[i:i + a.block]) for i in range(0, len(data), a.block)]
    hi = sum(e > 7.5 for e in ents)
    print(f"整体熵 {entropy(data):.2f}；{hi}/{len(ents)} 个块熵>7.5（多则可能加密或压缩）")
    if len(data) >= 8:
        sp, rv = struct.unpack_from("<II", data, 0)
        print(f"向量表推测：初始 SP=0x{sp:08X}，复位向量=0x{rv:08X}（Thumb 位={rv & 1}）")
        if 0x20000000 <= sp < 0x20100000: print("  SP 落在常见 SRAM 区，像 Cortex-M 镜像")
        guess = int(a.base, 16) if a.base else (rv & 0xFFF00000)
        print(f"  推测加载基址 0x{guess:08X}（可用 --base 指定）")
    strs = re.findall(rb"[\x20-\x7e]{6,}", data)
    print(f"可打印字符串 {len(strs)} 条，前 {a.strings} 条：")
    for s in strs[:a.strings]: print("  " + s.decode())

if __name__ == "__main__":
    main()
