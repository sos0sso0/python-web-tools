#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Excel文件合并工具
将多个Excel文件合并成一个文件

功能说明：
- 合并多个Excel文件到一个文件中
- 支持选择合并方式（按行合并、按列合并等）
- 自动创建输出目录
- 所有处理在本地完成，不上传任何数据
"""

import os
import sys
from pathlib import Path

# 输出目录配置
OUTPUT_DIR = r"D:\pyOutput"


def ensure_output_directory():
    """确保输出目录存在"""
    output_path = Path(OUTPUT_DIR)
    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ 已创建输出目录: {OUTPUT_DIR}")
    else:
        print(f"✓ 输出目录已存在: {OUTPUT_DIR}")


def select_excel_files():
    """
    让用户选择要合并的Excel文件
    
    返回:
        list: 选择的文件路径列表
    """
    print("\n" + "="*50)
    print("Excel文件合并工具")
    print("="*50)
    print("\n请输入要合并的Excel文件路径（每行一个，输入空行结束）：")
    
    files = []
    while True:
        file_path = input("> ").strip()
        if not file_path:
            break
        if os.path.exists(file_path):
            files.append(file_path)
            print(f"  ✓ 已添加: {os.path.basename(file_path)}")
        else:
            print(f"  ✗ 文件不存在: {file_path}")
    
    return files


def merge_excel_files(file_list):
    """
    合并Excel文件的主要功能
    
    参数:
        file_list (list): 要合并的Excel文件路径列表
    
    返回:
        str: 输出文件的路径
    """
    # TODO: 在此处实现Excel文件合并的具体逻辑
    # 当前为占位符，实际功能待后续补充
    
    print("\n开始合并Excel文件...")
    print(f"共选择了 {len(file_list)} 个文件")
    
    # 示例输出文件名
    output_file = os.path.join(OUTPUT_DIR, "merged_result.xlsx")
    
    print(f"\n合并功能正在开发中...")
    print(f"预期输出文件: {output_file}")
    
    return output_file


def main():
    """主函数"""
    try:
        # 确保输出目录存在
        ensure_output_directory()
        
        # 选择要合并的文件
        selected_files = select_excel_files()
        
        if not selected_files:
            print("\n⚠ 未选择任何文件，程序退出。")
            return
        
        if len(selected_files) < 2:
            print("\n⚠ 至少需要选择2个文件才能进行合并。")
            return
        
        # 合并文件
        output_path = merge_excel_files(selected_files)
        
        print("\n" + "="*50)
        print("✓ 处理完成！")
        print(f"输出文件将保存在: {output_path}")
        print("="*50)
        
    except KeyboardInterrupt:
        print("\n\n⚠ 用户中断操作")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ 发生错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
