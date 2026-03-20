# BMC 命令搜索系统迁移计划

## 一、当前状态

### 已完成
- [x] 模型：bge-m3 (BAAI/bge-m3)
- [x] 向量库：ChromaDB (cosine 距离)
- [x] 搜索优化：构建时自动注入中英同义词
- [x] API 服务：HTTP + MCP 协议

### 当前数据规模
| 接口 | 命令数 | 状态 |
|------|--------|------|
| CLI | 231 | ✅ 已构建 |
| REDFISH | 457 | ✅ 本次构建 |
| IPMI | 329 | ⏳ 待构建 |
| SNMP | 45 | ⏳ 待构建 |

---

## 二、迁移计划

### 阶段 1：内网环境部署（本阶段）

#### 1.1 模型部署
```bash
# NPU 服务器上安装 vLLM
pip install vllm

# 启动 bge-m3 服务
vllm serve BAAI/bge-m3 --port 8000 --dtype float16
```

#### 1.2 API 服务修改
- 将 `sentence_transformers.SentenceTransformer` 本地加载改为调用 vLLM API
- 示例代码：
```python
import requests

def get_embedding(text):
    resp = requests.post(
        "http://npu-server:8000/v1/embeddings",
        json={"input": [text], "model": "bge-m3"}
    )
    return resp.json()["data"][0]["embedding"]
```

#### 1.3 启动服务
```bash
# HTTP 服务
python http_server.py

# MCP 服务
python bmc_mcp_server.py
```

---

### 阶段 2：扩展数据

#### 2.1 构建 IPMI 接口
修改 `build_vector_db.py`：
```python
for interface in ["cli", "redfish", "ipmi"]:  # 添加 ipmi
```

#### 2.2 构建 SNMP 接口
```python
for interface in ["cli", "redfish", "ipmi", "snmp"]:  # 添加 snmp
```

#### 2.3 重新构建向量库
```bash
python build_vector_db.py
```

---

### 阶段 3：性能优化（可选）

| 优化项 | 方案 | 预期收益 |
|--------|------|----------|
| 混合检索 | Qdrant + bge-m3 sparse | 关键词召回提升 |
| 重排序 | bge-reranker-v2-m3 | Top-K 排序更准 |
| 查询改写 | LLM 预处理查询 | 模糊查询优化 |

---

## 三、文件结构

```
bmc_commands_search_mcp/
├── PLAN.md                    # 本计划文档
├── build_vector_db.py         # 向量库构建脚本
├── http_server.py             # HTTP API 服务
├── bmc_mcp_server.py          # MCP 协议服务
├── download_model.py          # 模型下载脚本（国内镜像）
├── chroma_db/                 # 向量数据库（运行时生成）
├── commands/                  # BMC 命令数据
│   ├── cli/
│   ├── ipmi/
│   ├── redfish/
│   └── snmp/
└── *.pdf                      # 接口文档（中英双语）
```

---

## 四、测试用例

| 查询 | 预期接口 | 预期命令 |
|------|----------|----------|
| 查询风扇信息 | CLI | `ipmcget -d faninfo` |
| 设置风扇速度 | CLI | `ipmcset -d fanlevel` |
| 用户列表 | CLI | `ipmcget -d userlist` |
| 查询温度 | REDFISH | `/redfish/v1/Chassis.../Thermal` |
| 重启 BMC | CLI | `ipmcset -d reset` |

---

## 五、注意事项

1. **模型文件**：bge-m3 约 2GB，需提前下载到 NPU 服务器
2. **向量库**：如修改数据或模型，需删除 `chroma_db/` 目录后重建
3. **离线模式**：NPU 服务器无法访问 HuggingFace，需使用 vLLM 离线模式
