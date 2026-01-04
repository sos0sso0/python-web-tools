#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
Excel文件合并工具
将多个Excel文件合并成一个文件

功能说明：
- 合并多个Excel文件到一个文件中
- 支持Excel (. xlsx, .xls) 和 CSV 文件
- 可选择是否在第一列插入来源文件名
- 支持输出为CSV或Excel格式
- 自动创建输出目录
- 所有处理在本地完成，不上传任何数据
"""

import os
import pandas as pd
from datetime import datetime

# 输出目录配置
# Windows: D:\pyOutput
# macOS: ~/Documents/pyOutput 或 /Users/YourName/pyOutput
# Linux: ~/pyOutput 或 /home/YourName/pyOutput
OUTPUT_DIR = r"D:\pyOutput"  # 请根据您的操作系统修改此路径


def ensure_output_directory():
    """确保输出目录存在"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"✓ 已创建输出目录:  {OUTPUT_DIR}")
    else:
        print(f"✓ 输出目录已存在: {OUTPUT_DIR}")


def select_excel_files():
    """
    让用户选择要合并的Excel/CSV文件
    
    返回:
        list: 选择的文件路径列表
    """
    print("\n" + "="*50)
    print("Excel/CSV文件合并工具")
    print("="*50)
    print("\n请输入要合并的Excel/CSV文件路径（每行一个，输入空行结束）：")
    print("支持的格式:  .xlsx, .xls, . csv")
    
    files = []
    while True:
        file_path = input("> ").strip()
        if not file_path:
            break
        
        # 移除可能的引号
        file_path = file_path.strip('"').strip("'")
        
        if os.path.exists(file_path):
            # 检查文件格式
            file_ext = os.path. splitext(file_path)[1].lower()
            if file_ext in ['.xlsx', '.xls', '.csv']:
                files.append(file_path)
                print(f"  ✓ 已添加: {os.path.basename(file_path)}")
            else:
                print(f"  ✗ 不支持的文件格式: {file_path}")
        else:
            print(f"  ✗ 文件不存在: {file_path}")
    
    return files


def merge_excel_files(file_list):
    """
    合并Excel/CSV文件的主要功能
    
    参数:
        file_list (list): 要合并的Excel/CSV文件路径列表
    
    返回: 
        str: 输出文件的路径
    """
    print("\n" + "="*50)
    print("开始合并文件...")
    print(f"共选择了 {len(file_list)} 个文件")
    print("="*50)
    
    # 询问用户是否插入来源文件名
    while True:
        insert_source = input('\n是否在第一列插入来源文件名？(1→是 / 2→否): ').strip()
        if insert_source in ['1', '2']: 
            break
        print("  ✗ 请输入 1 或 2")
    
    # 询问输出格式
    while True: 
        result_format = input('输出文件格式：(1→csv / 2→xlsx): ').strip()
        if result_format in ['1', '2']:
            break
        print("  ✗ 请输入 1 或 2")
    
    # 读取并合并所有文件
    print("\n正在读取文件...")
    data_list = []
    
    for file_path in file_list: 
        try:
            print(f"  读取:  {os.path.basename(file_path)}")
            
            # 根据文件扩展名选择读取方式
            file_ext = os. path.splitext(file_path)[1].lower()
            
            if file_ext in ['. xlsx', '.xls']: 
                # 读取Excel文件的第一个sheet
                data = pd.read_excel(file_path, sheet_name=0)
            else:  # . csv
                data = pd.read_csv(file_path, encoding='utf-8')
            
            # 如果需要，插入来源文件名
            if insert_source == '1':
                data.insert(loc=0, column='source', value=os.path.basename(file_path))
            
            data_list.append(data)
            print(f"    ✓ 成功读取 {len(data)} 行数据")
            
        except Exception as e:
            print(f"    ✗ 读取失败: {str(e)}")
            continue
    
    if not data_list: 
        raise Exception("没有成功读取任何文件")
    
    # 合并所有数据
    print("\n正在合并数据...")
    df = pd.concat(data_list, ignore_index=True, sort=False)
    
    # 生成输出文件名（带时间戳）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if result_format == '1':
        output_file = os.path.join(OUTPUT_DIR, f"merged_result_{timestamp}.csv")
        df.to_csv(output_file, encoding='utf_8_sig', index=False)
    else:
        output_file = os. path.join(OUTPUT_DIR, f"merged_result_{timestamp}. xlsx")
        df.to_excel(output_file, index=False)
    
    print(f"\n✓ 合并完成！")
    print(f"  合并后：{df.shape[0]} 行 × {df.shape[1]} 列")
    
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
        print(f"输出文件已保存:  {output_path}")
        print("="*50)
        
    except KeyboardInterrupt: 
        print("\n\n⚠ 用户中断操作")
    except Exception as e:
        print(f"\n✗ 发生错误: {str(e)}")


if __name__ == "__main__":
    main()
