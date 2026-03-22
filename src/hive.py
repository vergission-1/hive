#!/usr/bin/env python3
"""
🧬 Hive CLI - 知识细胞系统命令行工具
"""

import json
import os
from pathlib import Path

# 蜂房存储目录
CELLS_DIR = Path(__file__).parent.parent / "cells"


def create_cell(name: str):
    """创建一个新蜂房"""
    cell_file = CELLS_DIR / f"{name}.json"
    
    if cell_file.exists():
        print(f"❌ 蜂房已存在：{name}")
        return
    
    cell = {
        "id": name,
        "name": name,
        "type": "generic",
        "data": {},
        "connections": []
    }
    
    with open(cell_file, "w", encoding="utf-8") as f:
        json.dump(cell, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 创建蜂房：{name}")


def list_cells():
    """列出所有蜂房"""
    if not CELLS_DIR.exists():
        print("📭 还没有蜂房")
        return
    
    cells = list(CELLS_DIR.glob("*.json"))
    
    if not cells:
        print("📭 还没有蜂房")
        return
    
    print("📦 蜂房列表:")
    for cell_file in cells:
        with open(cell_file, "r", encoding="utf-8") as f:
            cell = json.load(f)
        print(f"  - {cell['id']} ({cell['type']})")


def show_cell(name: str):
    """显示蜂房详情"""
    cell_file = CELLS_DIR / f"{name}.json"
    
    if not cell_file.exists():
        print(f"❌ 蜂房不存在：{name}")
        return
    
    with open(cell_file, "r", encoding="utf-8") as f:
        cell = json.load(f)
    
    print(f"🧬 蜂房：{cell['name']}")
    print(f"   类型：{cell['type']}")
    print(f"   连接：{cell['connections']}")
    print(f"   数据：{cell['data']}")


def connect_cells(from_name: str, to_name: str):
    """连接两个蜂房"""
    from_file = CELLS_DIR / f"{from_name}.json"
    to_file = CELLS_DIR / f"{to_name}.json"
    
    if not from_file.exists():
        print(f"❌ 蜂房不存在：{from_name}")
        return
    
    if not to_file.exists():
        print(f"❌ 蜂房不存在：{to_name}")
        return
    
    with open(from_file, "r", encoding="utf-8") as f:
        cell = json.load(f)
    
    if to_name not in cell["connections"]:
        cell["connections"].append(to_name)
        
        with open(from_file, "w", encoding="utf-8") as f:
            json.dump(cell, f, indent=2, ensure_ascii=False)
        
        print(f"✅ 连接：{from_name} → {to_name}")
    else:
        print(f"⚠️  已存在连接：{from_name} → {to_name}")


def help_message():
    """显示帮助信息"""
    print("""
🧬 Hive CLI - 知识细胞系统

用法:
  python hive.py <命令> [参数]

命令:
  create-cell <名称>     创建新蜂房
  list-cells             列出所有蜂房
  show-cell <名称>       显示蜂房详情
  connect <从> <到>      连接两个蜂房
  help                   显示此帮助信息

示例:
  python hive.py create-cell japanese
  python hive.py create-cell medical
  python hive.py list-cells
  python hive.py connect japanese medical
  python hive.py show-cell japanese
""")


def main():
    import sys
    
    if len(sys.argv) < 2:
        help_message()
        return
    
    command = sys.argv[1]
    
    if command == "create-cell":
        if len(sys.argv) < 3:
            print("❌ 用法：python hive.py create-cell <名称>")
            return
        create_cell(sys.argv[2])
    
    elif command == "list-cells":
        list_cells()
    
    elif command == "show-cell":
        if len(sys.argv) < 3:
            print("❌ 用法：python hive.py show-cell <名称>")
            return
        show_cell(sys.argv[2])
    
    elif command == "connect":
        if len(sys.argv) < 4:
            print("❌ 用法：python hive.py connect <从> <到>")
            return
        connect_cells(sys.argv[2], sys.argv[3])
    
    elif command == "help":
        help_message()
    
    else:
        print(f"❌ 未知命令：{command}")
        print("运行 'python hive.py help' 查看帮助")


if __name__ == "__main__":
    main()
