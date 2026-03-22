# 🧬 HTP v1 — Hive Transfer Protocol

**蜂房间通信协议规范**

---

## 📦 消息格式

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│  魔法数     │   版本     │   类型      │   长度      │
│  4 bytes   │  1 byte    │  1 byte    │  4 bytes   │
├─────────────┴─────────────┴─────────────┴─────────────┤
│                    Payload                            │
│                    (变长)                              │
└───────────────────────────────────────────────────────┘
```

### 魔法数
```
0x48 0x49 0x56 0x45  =  "HIVE"
```

### 消息类型
| 代码 | 类型 | 说明 |
|------|------|------|
| 0x01 | HELLO | 蜂房握手 |
| 0x02 | REQUEST | 知识请求 |
| 0x03 | RESPONSE | 知识响应 |
| 0x04 | EVENT | 事件通知 |
| 0x05 | WORKFLOW | 工作流触发 |
| 0xFF | ERROR | 错误 |

---

## 📝 JSON Payload 示例

### HELLO 消息
```json
{
  "type": "HELLO",
  "source": "cell-japanese-001",
  "target": "cell-medical-001",
  "timestamp": 1711087200,
  "capabilities": ["translate", "tokenize", "grammar"]
}
```

### REQUEST 消息
```json
{
  "type": "REQUEST",
  "source": "cell-workflow-001",
  "target": "cell-japanese-001",
  "action": "tokenize",
  "data": {
    "text": "病原生物学の用語",
    "options": {
      "output": "detailed",
      "include_reading": true
    }
  },
  "trace_id": "workflow-123"
}
```

### RESPONSE 消息
```json
{
  "type": "RESPONSE",
  "source": "cell-japanese-001",
  "target": "cell-workflow-001",
  "status": "success",
  "data": {
    "tokens": [
      {"text": "病原", "reading": "びょうげん", "pos": "noun"},
      {"text": "生物学", "reading": "せいぶつがく", "pos": "noun"},
      {"text": "の", "reading": "の", "pos": "particle"},
      {"text": "用語", "reading": "ようご", "pos": "noun"}
    ]
  },
  "trace_id": "workflow-123"
}
```

---

## 🔄 通信流程

```
┌──────────────┐                    ┌──────────────┐
│   Sender     │                    │   Receiver   │
│    Cell      │                    │    Cell      │
└──────┬───────┘                    └──────┬───────┘
       │                                   │
       │  ─ ─ ─ ─ ─ HELLO ─ ─ ─ ─ ─ ─ ─ →  │
       │                                   │
       │  ← ─ ─ ─ ─ HELLO_ACK ─ ─ ─ ─ ─ ─  │
       │                                   │
       │  ─ ─ ─ ─ ─ REQUEST ─ ─ ─ ─ ─ ─ →  │
       │                                   │
       │         (处理中...)                │
       │                                   │
       │  ← ─ ─ ─ ─ RESPONSE ─ ─ ─ ─ ─ ─   │
       │                                   │
       │  ─ ─ ─ ─ ─ ACK ─ ─ ─ ─ ─ ─ ─ ─ →  │
       │                                   │
```

---

## 🧪 错误码

| 代码 | 说明 |
|------|------|
| 0x00 | OK |
| 0x01 | CELL_NOT_FOUND |
| 0x02 | ACTION_NOT_SUPPORTED |
| 0x03 | INVALID_PAYLOAD |
| 0x04 | TIMEOUT |
| 0x05 | INTERNAL_ERROR |

---

## 📚 设计哲学

> "像细胞信号传导一样简单，像代谢通路一样可靠"

- **轻量** — 最小开销
- **可扩展** — 新类型容易添加
- **可追踪** — 每个消息有 trace_id
- **容错** — 明确的错误处理
