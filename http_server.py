#!/usr/bin/env python3
"""HTTP API Server for BMC Command Search - 使用 bge-m3"""
import sys
import io

# 设置UTF-8编码（Windows兼容）
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import os

# 设置离线模式
os.environ['HF_DATASETS_OFFLINE'] = '1'
os.environ['TRANSFORMERS_OFFLINE'] = '1'

from flask import Flask, request, jsonify
from flask_cors import CORS
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

app = Flask(__name__)
CORS(app)

# 使用 bge-m3 模型
MODEL_NAME = "BAAI/bge-m3"
print(f"Loading model: {MODEL_NAME}")
model = SentenceTransformer(MODEL_NAME)
print("Model loaded!")


def get_collection():
    """获取collection"""
    client = chromadb.PersistentClient(path="./chroma_db")
    return client.get_or_create_collection("bmc_commands")


@app.route('/search', methods=['GET', 'POST'])
def search():
    """搜索BMC命令"""
    if request.method == 'POST':
        data = request.get_json() or {}
        query = data.get('query', '')
        interface_type = data.get('interface_type')
        top_k = data.get('top_k', 3)
    else:
        query = request.args.get('query', '')
        interface_type = request.args.get('interface_type')
        top_k = int(request.args.get('top_k', 3))

    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    # 直接使用 query（依赖构建时的关键词注入）
    query_embedding = model.encode([query])

    # 使用Chroma原生query - 传入embedding而不是文本
    collection = get_collection()
    where_filter = {"interface_type": interface_type} if interface_type else None

    results = collection.query(
        query_embeddings=query_embedding.tolist(),  # 使用embedding
        n_results=top_k,
        where=where_filter,
        include=["documents", "metadatas", "distances"]
    )

    commands = []
    if results["documents"] and results["documents"][0]:
        for doc, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):
            # cosine距离转换为相似度
            similarity = (1 - dist) * 100
            commands.append({
                "title": meta.get("title", ""),
                "interface_type": meta.get("interface_type", ""),
                "command": meta.get("command", ""),
                "method": meta.get("method", ""),
                "url": meta.get("url", ""),
                "oid": meta.get("oid", ""),
                "netfn": meta.get("netfn", ""),
                "cmd": meta.get("cmd", ""),
                "request_body": meta.get("request_body", ""),
                "relevance": f"{similarity:.1f}%"
            })

    return jsonify({
        "query": query,
        "interface_type": interface_type,
        "results": commands
    })


@app.route('/interfaces', methods=['GET'])
def list_interfaces():
    """列出所有接口类型"""
    collection = get_collection()
    results = collection.get(include=["metadatas"])

    interfaces = {}
    for meta in results["metadatas"]:
        it = meta.get("interface_type", "Unknown")
        interfaces[it] = interfaces.get(it, 0) + 1

    return jsonify({"interfaces": interfaces})


@app.route('/health', methods=['GET'])
def health():
    """健康检查"""
    collection = get_collection()
    count = collection.count()
    return jsonify({
        "status": "ok",
        "model": MODEL_NAME,
        "commands_count": count
    })


if __name__ == '__main__':
    print("Starting BMC Command Search HTTP Server...")
    print("Endpoint: http://localhost:5000/search?query=查询风扇信息")
    app.run(host='0.0.0.0', port=5000)


def get_collection():
    """获取collection"""
    client = chromadb.PersistentClient(path="./chroma_db")
    return client.get_or_create_collection("bmc_commands")


@app.route('/search', methods=['GET', 'POST'])
def search():
    """搜索BMC命令"""
    if request.method == 'POST':
        data = request.get_json() or {}
        query = data.get('query', '')
        interface_type = data.get('interface_type')
        top_k = data.get('top_k', 3)
    else:
        query = request.args.get('query', '')
        interface_type = request.args.get('interface_type')
        top_k = int(request.args.get('top_k', 3))

    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    # 使用Chroma原生query
    collection = get_collection()
    where_filter = {"interface_type": interface_type} if interface_type else None

    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        where=where_filter,
        include=["documents", "metadatas", "distances"]
    )

    commands = []
    if results["documents"] and results["documents"][0]:
        for doc, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):
            # cosine距离转换为相似度
            similarity = (1 - dist) * 100
            commands.append({
                "title": meta.get("title", ""),
                "interface_type": meta.get("interface_type", ""),
                "command": meta.get("command", ""),
                "method": meta.get("method", ""),
                "url": meta.get("url", ""),
                "oid": meta.get("oid", ""),
                "netfn": meta.get("netfn", ""),
                "cmd": meta.get("cmd", ""),
                "request_body": meta.get("request_body", ""),
                "relevance": f"{similarity:.1f}%"
            })

    return jsonify({
        "query": query,
        "interface_type": interface_type,
        "results": commands
    })


@app.route('/interfaces', methods=['GET'])
def list_interfaces():
    """列出所有接口类型"""
    collection = get_collection()
    results = collection.get(include=["metadatas"])

    interfaces = {}
    for meta in results["metadatas"]:
        it = meta.get("interface_type", "Unknown")
        interfaces[it] = interfaces.get(it, 0) + 1

    return jsonify({"interfaces": interfaces})


@app.route('/health', methods=['GET'])
def health():
    """健康检查"""
    collection = get_collection()
    count = collection.count()
    return jsonify({
        "status": "ok",
        "model": MODEL_NAME,
        "commands_count": count
    })


if __name__ == '__main__':
    print("Starting BMC Command Search HTTP Server...")
    print("Endpoint: http://localhost:5000/search?query=查询风扇信息")
    app.run(host='0.0.0.0', port=5000, debug=True)
