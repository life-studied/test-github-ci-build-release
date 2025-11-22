#!/usr/bin/env python3
import shutil
from pathlib import Path

SRC_DIR = Path(".")
RELEASE_DIR = Path("/tmp/release")  # 直接生成到系统临时目录

# 清空并创建目标目录
if RELEASE_DIR.exists():
    shutil.rmtree(RELEASE_DIR)
RELEASE_DIR.mkdir()

# 复制所有markdown文件
for md_file in SRC_DIR.rglob("*.md"):
    dest = RELEASE_DIR / md_file.relative_to(SRC_DIR)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(md_file, dest)