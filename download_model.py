#!/usr/bin/env python3
"""使用国内镜像下载 bge-m3 模型"""
import os
import sys

# 使用国内镜像
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# 确保不是离线模式
for key in ['HF_DATASETS_OFFLINE', 'TRANSFORMERS_OFFLINE', 'HF_OFFLINE']:
    if key in os.environ:
        del os.environ[key]

from huggingface_hub import snapshot_download

print("使用国内镜像下载 bge-m3 模型...")
print("模型大小约 2GB，请耐心等待...")

try:
    model_dir = snapshot_download(
        repo_id="BAAI/bge-m3",
        force_download=True,
    )
    print(f"\n模型下载完成！")
    print(f"模型路径: {model_dir}")
except Exception as e:
    print(f"下载失败: {e}")
    print("\n如果还是失败，可以尝试其他镜像:")
    print("1. https://mirror.ghproxy.com/https://huggingface.co/BAAI/bge-m3")
    print("2. 手动下载: https://huggingface.co/BAAI/bge-m3/tree/main")
