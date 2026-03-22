# 🔍 逆向工程实验记录

> "理解一个系统的最好方式是拆解它"

---

## 📚 学习目标

- 理解可执行文件结构
- 学习调试器使用
- 掌握脱壳技术
- 应用于 Hive 的"蜂房应用"设计

---

## 🛠️ 工具清单

### Linux
| 工具 | 用途 | 安装 |
|------|------|------|
| **Ghidra** | 反编译 | `sudo pacman -S ghidra` |
| **radare2** | 逆向分析 | `sudo pacman -S radare2` |
| **GDB** | 调试 | `sudo pacman -S gdb` |
| **strace** | 系统调用追踪 | `sudo pacman -S strace` |
| **ltrace** | 库调用追踪 | `sudo pacman -S ltrace` |

### Windows (虚拟机)
| 工具 | 用途 |
|------|------|
| **x64dbg** | 调试器 |
| **OllyDbg** | 老派调试器 |
| **PE-bear** | PE 文件查看 |
| **Detect It Easy** | 壳检测 |
| **Scyller** | 脱壳辅助 |

---

## 🧪 实验 1: UPX 加壳与脱壳

### 步骤

```bash
# 1. 准备一个简单程序
echo 'print("Hello from Hive!")' > test.py

# 2. 打包成可执行文件
pip install pyinstaller
pyinstaller --onefile test.py

# 3. 查看原始大小
ls -lh dist/test

# 4. 用 UPX 加壳
upx dist/test -o dist/test_packed

# 5. 比较大小
ls -lh dist/test dist/test_packed

# 6. 脱壳
upx -d dist/test_packed -o dist/test_unpacked

# 7. 验证
./dist/test_unpacked
```

### 观察

```
原始文件：~7MB (Python 运行时)
UPX 压缩后：~2MB
脱壳后：~7MB

压缩率：~70%
```

---

## 🧪 实验 2: 用 Ghidra 分析简单程序

### 步骤

```bash
# 1. 写一个 C 程序
cat > simple.c << 'EOF'
#include <stdio.h>

int main() {
    printf("Hive CLI v0.1\n");
    return 0;
}
EOF

# 2. 编译
gcc -o simple simple.c

# 3. 用 Ghidra 打开
# ghidraRun
# 创建项目 → 导入 simple → 分析

# 4. 查看反编译结果
# 找到 main 函数
# 看反编译的 C 代码
```

### 预期输出

```c
undefined8 main(void)
{
  int iVar1;
  
  puts("Hive CLI v0.1");
  iVar1 = 0;
  return (ulong)(iVar1 != 0);
}
```

---

## 🧪 实验 3: 动态追踪 Hive CLI

```bash
# 1. 用 strace 追踪系统调用
strace -o trace.log python3 src/hive.py create-cell test

# 2. 查看日志
cat trace.log | head -50

# 3. 关注:
# - open/openat (文件操作)
# - read/write (数据读写)
# - stat (文件信息)
```

### 可以看到

```
openat(AT_FDCWD, "cells/test.json", O_WRONLY|O_CREAT|O_TRUNC, 0666)
write(3, "{\"id\": \"test\", ...}", 100)
close(3)
```

**这就是 Hive 创建蜂房的过程！**

---

## 🧪 实验 4: 分析 Python 字节码

```bash
# 1. 编译 Python 文件为字节码
python3 -m py_compile src/hive.py

# 2. 查看字节码
python3 -m dis src/hive.py

# 3. 或者用 uncompyle6 反编译
pip install uncompyle6
uncompyle6 src/hive.pyc
```

### 可以看到

```python
# 字节码
  0 LOAD_GLOBAL              0 (print)
  2 LOAD_CONST               1 ('✅ 创建蜂房：{name}')
  4 LOAD_FAST                0 (name)
  6 FORMAT_VALUE             0
  8 CALL_FUNCTION            2
 10 POP_TOP
```

**理解 Python 代码是如何执行的！**

---

## 🎯 对 Hive 的启发

### 1. 蜂房应用沙箱

```
从逆向工程学到:
- 程序可以被分析
- 代码可以被修改
- 数据可以被提取

应用到 Hive:
- 蜂房应用需要沙箱隔离
- 防止恶意应用
- 限制资源访问
```

### 2. 协议安全

```
从逆向工程学到:
- 协议可以被抓包分析
- 消息可以被伪造
- 加密可以被破解

应用到 Hive:
- HTP 协议需要认证
- 敏感数据需要加密
- 验证消息来源
```

### 3. 可调试性

```
从逆向工程学到:
- 调试信息很有用
- 日志帮助定位问题
- 符号表让分析更容易

应用到 Hive:
- 详细的日志系统
- 工作流执行追踪
- 错误信息友好
```

---

## 📖 学习资源

### 书籍
- 《逆向工程核心原理》
- 《加密与解密》
- 《Reversing: Secrets of Reverse engineering》

### 网站
- crackmes.one — 逆向练习题目
- pwn.college — 安全学习
- liveoverflow.com — 视频教程

### CTF
- CTFtime.org — 比赛信息
- pwnable.kr — 练习平台

---

## ⚠️ 法律提醒

```
合法用途:
✅ 学习逆向技术
✅ 分析自己的程序
✅ 安全研究
✅ CTF 比赛

非法用途:
❌ 破解商业软件
❌ 绕过许可证
❌ 侵犯版权

原则:
"学习开锁，但不去偷东西"
```

---

*最后更新：2026-03-22*
*作者：vergiss*
