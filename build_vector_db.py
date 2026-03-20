#!/usr/bin/env python3
"""构建BMC命令向量数据库 - 使用 bge-m3"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import json
import os
import torch
from pathlib import Path

# 设置离线模式（使用本地缓存的bge-m3）
os.environ['HF_DATASETS_OFFLINE'] = '1'
os.environ['TRANSFORMERS_OFFLINE'] = '1'

from sentence_transformers import SentenceTransformer
import chromadb

# === 改动：使用 bge-m3 ===
MODEL_NAME = "BAAI/bge-m3"
print(f"Loading model: {MODEL_NAME}")
model = SentenceTransformer(MODEL_NAME)
print("Model loaded!")

def load_all_commands():
    """加载命令数据 - 当前版本只构建 CLI + REDFISH"""
    all_commands = []
    # 只构建 CLI 和 REDFISH 接口
    for interface in ["cli", "redfish"]:
        dir_path = Path("commands") / interface
        if dir_path.exists():
            for f in dir_path.glob("*.json"):
                with open(f, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    for item in data:
                        item['interface_type'] = interface.upper()
                        all_commands.append(item)
    return all_commands


def create_search_text(item):
    """自动提取关键词 + 构建双语搜索文本"""
    interface = item.get('interface_type', '未知')
    title = item.get('title', '').strip()
    desc = item.get('description', '').strip()
    cmd = item.get('command', '').strip()
    example = item.get('example', '').strip()
    name = item.get('name', '').strip()  # CLI 命令名

    # 从 command + name + title 提取关键词
    text_to_check = (cmd + ' ' + name + ' ' + title).lower()

    # 中文同义词映射（根据 title/cmd 自动注入）
    domain_map = {
        # 风扇相关
        'fan': 'fan faninfo fanlevel fanmode 风扇 散热 风扇转速 风扇速度 风扇转速级别 风扇档位',
        'cooling': 'cooling coolingdevice 散热 冷却 散热设备',
        # 温度相关
        'temperature': 'temperature temp thermal 温度 温度传感器 热 热量',
        'temp': 'temp temperature 温度 热',
        # 电源相关
        'power': 'power psu 电源 电源状态',
        # 用户相关
        'user': 'user userlist account 用户 用户列表',
        # 版本相关
        'version': 'version firmware 版本 固件 固件版本',
        # 网络相关
        'network': 'network lan ipmi 网络 网口 网卡',
        # 传感器相关
        'sensor': 'sensor sensorinfo 传感器 传感器信息',
        # 日志相关
        'log': 'log event 日志 事件',
        # 重启相关
        'reset': 'reset reboot 重启 重启系统',
    }

    english_keywords = []
    for key, synonyms in domain_map.items():
        if key in text_to_check:
            english_keywords.append(synonyms)

    # 中文操作词扩展
    action_keywords = []
    if '查询' in title or '获取' in title or 'get' in text_to_check:
        action_keywords.append('query get list show 查看 获取 查询 列出')
    if '设置' in title or '修改' in title or 'set' in text_to_check:
        action_keywords.append('set configure change update 设置 修改 配置 调整')

    rich_text = f"""
BMC命令 {interface}
命令名称：{name}
命令：{cmd}
功能标题：{title}
功能描述：{desc}
使用示例：{example}
领域关键词：{' '.join(english_keywords)}
操作关键词：{' '.join(action_keywords)}
查询表达式：查询{title} 获取{title} get {name} show {name} {name} status
    """.strip()

    return rich_text


def build_vector_db():
    print("Loading commands...")
    commands = load_all_commands()
    print(f"Total commands: {len(commands)}")

    print("\nCreating vector database...")
    client = chromadb.PersistentClient(path="./chroma_db")
    try:
        client.delete_collection("bmc_commands")
    except:
        pass

    collection = client.get_or_create_collection(
        name="bmc_commands",
        metadata={"hnsw:space": "cosine"}
    )

    ids = []
    texts = []
    metadatas = []

    for i, cmd in enumerate(commands):
        cmd_id = f"{cmd.get('interface_type', 'unknown')}_{i:04d}"
        search_text = create_search_text(cmd)

        ids.append(cmd_id)
        texts.append(search_text)

        metadata = {
            'interface_type': cmd.get('interface_type', ''),
            'title': cmd.get('title', '')[:300],
            'command': cmd.get('command', '')[:500],
        }
        # 保留其他可能的字段
        for k in ['method', 'url', 'netfn', 'cmd', 'oid', 'request_body']:
            if k in cmd:
                metadata[k] = str(cmd[k])[:500]

        metadatas.append(metadata)

    print("Generating embeddings...")
    embeddings = model.encode(
        texts,
        batch_size=32,               # 4070S 安全值，可调到64
        normalize_embeddings=True,
        show_progress_bar=True
    )

    print("Adding to database...")
    collection.add(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=texts,
        metadatas=metadatas
    )

    print(f"Vector database created: ./chroma_db  Total: {collection.count()}")
    return collection, model


if __name__ == "__main__":
    build_vector_db()
