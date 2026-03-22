# 🧬 Hive

**知识细胞系统 —— 一个有生命的知识操作系统**

> "从化学反应的角度去构想一个细胞"

---

## 🌱 构想

Hive 不是一个笔记应用，不是一个知识库。

**Hive 是一个能生长、能学习、能进化的"第二大脑"。**

### 核心类比

| 细胞结构 | Hive 蜂房 | 功能 |
|----------|----------|------|
| 细胞膜 | 协议接口 | 控制进出 |
| 细胞器 | 蜂房应用 | 执行特定功能 |
| 细胞核 | 核心知识库 | 存储核心规则 |
| 信号分子 | 协议消息 | 细胞间通信 |

---

## 🎯 目标

- **蜂房（Cell）** — 独立的知识处理单元
- **协议（Protocol）** — 蜂房间通信的语言
- **工作流（Workflow）** — 知识流动的代谢通路
- **自生长** — 系统能根据你的使用模式进化

---

## 📁 项目结构

```
hive/
├── src/              # 源代码
│   └── hive.py       # CLI 主程序
├── cells/            # 蜂房定义
│   ├── examples/     # 示例蜂房
│   │   ├── japanese.json
│   │   ├── medical.json
│   │   └── music.json
│   └── *.json        # 用户创建的蜂房
├── protocol/         # 协议规范
│   └── HTP-v1.md     # Hive 传输协议 v1
├── workflows/        # 工作流定义
│   └── jp-med-translate.yaml
├── docs/             # 文档
│   ├── vision.md          # 愿景文档
│   ├── cell-analogy.md    # 细胞类比
│   └── music-theory.md    # 音乐理论
├── experiments/      # 实验记录
│   └── reverse-engineering.md
├── scripts/          # 辅助脚本
│   └── demo.sh       # 演示脚本
└── README.md         # 本文件
```

---

## 🚀 状态

**阶段 0：种子（Seed）** ✅

- [x] 项目创建
- [x] CLI 基础功能
- [x] 协议 v1 文档
- [x] 示例蜂房
- [x] 工作流定义
- [x] 文档体系

**阶段 1：发芽（Sprout）** 🌱

- [ ] Web 界面原型
- [ ] 工作流引擎实现
- [ ] 蜂房应用沙箱
- [ ] 本地部署脚本

---

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/vergission-1/hive.git
cd hive

# 运行演示
bash scripts/demo.sh

# 或者手动使用
python3 src/hive.py help
python3 src/hive.py create-cell my-cell
python3 src/hive.py list-cells
```

---

## 📚 文档

| 文档 | 说明 |
|------|------|
| [愿景文档](docs/vision.md) | Hive 的长期愿景和哲学 |
| [细胞类比](docs/cell-analogy.md) | 从生物学借鉴的设计原则 |
| [协议规范](protocol/HTP-v1.md) | 蜂房间通信协议 |
| [音乐理论](docs/music-theory.md) | 游戏音乐创作指南 |
| [逆向工程](experiments/reverse-engineering.md) | 逆向工程学习记录 |

---

## 🧪 哲学

> "这不是图书馆，这是生命。"

Hive 的设计灵感来自细胞生物学：
- 蜂房 = 细胞
- 协议 = 信号分子
- 工作流 = 代谢通路
- 应用 = 细胞器

知识在这里是活的，会生长、会进化、会与你共鸣。

---

## 📜 License

MIT — 知识应该自由流动
