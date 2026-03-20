#!/usr/bin/env python3
"""BMC Commands Search MCP Server - bge-m3 版本"""

import sys
import io
import os

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from mcp.server.fastmcp import FastMCP
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

os.environ['HF_DATASETS_OFFLINE'] = '1'
os.environ['TRANSFORMERS_OFFLINE'] = '1'

MODEL_NAME = "BAAI/bge-m3"
model = SentenceTransformer(MODEL_NAME, device='cuda' if torch.cuda.is_available() else 'cpu')

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("bmc_commands")

mcp = FastMCP("bmc-commands-search")

@mcp.tool()
def search_bmc_command(query: str, interface_type: str = None, top_k: int = 3) -> str:
    """
    根据自然语言查询检索BMC命令（支持中文）
    """
    # 中文关键词扩展 - 增强语义匹配
    expanded = query
    if '风扇' in query or 'fan' in query.lower():
        expanded += " fan faninfo cooling fanlevel 风扇转速 散热"
    if '温度' in query or 'temperature' in query.lower():
        expanded += " temperature temp sensor 温度传感器 热"
    if '电源' in query or 'power' in query.lower():
        expanded += " power psu 电源状态"
    if '用户' in query or 'user' in query.lower():
        expanded += " user 用户列表 用户管理"
    if '版本' in query or 'version' in query.lower():
        expanded += " version versioninfo 版本信息"
    if '网络' in query or 'network' in query.lower():
        expanded += " network lan ipmi 网络配置"
    if '重启' in query or 'reset' in query.lower():
        expanded += " reset reboot 重启 关机"

    # 使用 bge-m3 生成 embedding
    query_embedding = model.encode([expanded])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k,
        where={"interface_type": interface_type} if interface_type else None,
        include=["documents", "metadatas", "distances"]
    )

    if not results['documents'][0]:
        return "未找到匹配的命令。"

    output = []
    for i, (doc, meta, dist) in enumerate(zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    ), 1):
        similarity = (1 - dist) * 100  # cosine distance -> similarity
        output.append(f"""【{i}】 相似度: {similarity:.1f}%
接口: {meta.get('interface_type', 'N/A')}
标题: {meta.get('title', 'N/A')}
命令: {meta.get('command', 'N/A')}
内容: {doc[:300]}...""")

    return "\n\n".join(output)


if __name__ == "__main__":
    print("Starting BMC Commands MCP Server (bge-m3)")
    print("Available tool: search_bmc_command")
    mcp.run()