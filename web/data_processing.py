"""
Web-based Data Processing Tools
Python code for browser-based Excel processing using PyScript/Pyodide

This file contains the Python logic that runs in the browser via PyScript.
To update the functionality of the web interface, modify this file.

Note: This is different from the /src scripts which are standalone CLI tools
for local download and execution.
"""

import asyncio
from pyodide.ffi import create_proxy
from js import document, showSuccess, showError, Blob, URL, console
import pandas as pd
from io import BytesIO
from datetime import datetime

async def read_file_async(file):
    """异步读取文件内容 / Asynchronously read file content"""
    array_buffer = await file.arrayBuffer()
    return array_buffer.to_bytes()

def download_file(content, filename, mime_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
    """触发浏览器下载文件 / Trigger browser file download"""
    try:
        # Create blob using proper Pyodide syntax
        from js import Object
        options = Object.fromEntries([['type', mime_type]])
        blob = Blob.new([content], options)
        url = URL.createObjectURL(blob)
        
        # Create download link
        a = document.createElement('a')
        a.href = url
        a.download = filename
        a.click()
        
        # Clean up
        URL.revokeObjectURL(url)
        return True
    except Exception as e:
        console.error(f"Download error: {str(e)}")
        return False

async def process_excel_merge(files):
    """处理Excel文件合并"""
    try:
        console.log(f"Processing {len(files)} files for merge")
        
        # Read all files
        dfs = []
        for file in files:
            console.log(f"Reading file: {file.name}")
            content = await read_file_async(file)
            df = pd.read_excel(BytesIO(content))
            dfs.append(df)
            console.log(f"Read {len(df)} rows from {file.name}")
        
        # Merge dataframes (concatenate by rows)
        merged_df = pd.concat(dfs, ignore_index=True)
        console.log(f"Merged result has {len(merged_df)} rows")
        
        # Save to BytesIO with explicit openpyxl engine for MS Excel compatibility
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            merged_df.to_excel(writer, index=False, sheet_name='Merged Data')
        
        # Get the content
        output.seek(0)
        result_content = output.read()
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"merged_excel_{timestamp}.xlsx"
        
        # Download file
        if download_file(result_content, filename):
            showSuccess('excel-merge-status', f'✅ 合并成功！文件已下载：{filename}')
        else:
            showError('excel-merge-status', '❌ 文件下载失败，请重试')
            
    except Exception as e:
        error_msg = f"❌ 合并失败：{str(e)}"
        console.error(error_msg)
        showError('excel-merge-status', error_msg)

async def process_business_analysis(file, analysis_type):
    """处理经营分析"""
    try:
        console.log(f"Analyzing file: {file.name}, type: {analysis_type}")
        
        # Read file
        content = await read_file_async(file)
        df = pd.read_excel(BytesIO(content))
        console.log(f"Read {len(df)} rows, {len(df.columns)} columns")
        
        # Perform basic analysis based on type
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Original data
            df.to_excel(writer, sheet_name='原始数据', index=False)
            
            # Basic statistics
            if len(df.select_dtypes(include=['number']).columns) > 0:
                stats_df = df.describe()
                stats_df.to_excel(writer, sheet_name='统计摘要')
            
            # Analysis type specific processing
            if analysis_type == 'sales':
                # Sales analysis placeholder
                summary_sheet = pd.DataFrame({
                    '分析项': ['总行数', '总列数', '数值列数'],
                    '结果': [len(df), len(df.columns), len(df.select_dtypes(include=['number']).columns)]
                })
                summary_sheet.to_excel(writer, sheet_name='销售分析', index=False)
                
            elif analysis_type == 'financial':
                # Financial analysis placeholder
                summary_sheet = pd.DataFrame({
                    '分析项': ['总行数', '总列数', '数值列数'],
                    '结果': [len(df), len(df.columns), len(df.select_dtypes(include=['number']).columns)]
                })
                summary_sheet.to_excel(writer, sheet_name='财务分析', index=False)
                
            else:  # comprehensive
                # Comprehensive analysis
                summary_sheet = pd.DataFrame({
                    '分析项': ['总行数', '总列数', '数值列数', '文本列数'],
                    '结果': [
                        len(df), 
                        len(df.columns), 
                        len(df.select_dtypes(include=['number']).columns),
                        len(df.select_dtypes(include=['object']).columns)
                    ]
                })
                summary_sheet.to_excel(writer, sheet_name='综合分析', index=False)
        
        # Get the content
        output.seek(0)
        result_content = output.read()
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        analysis_type_cn = {'sales': '销售', 'financial': '财务', 'comprehensive': '综合'}
        filename = f"{analysis_type_cn.get(analysis_type, '综合')}分析报告_{timestamp}.xlsx"
        
        # Download file
        if download_file(result_content, filename):
            showSuccess('business-analysis-status', f'✅ 分析完成！报告已下载：{filename}')
        else:
            showError('business-analysis-status', '❌ 报告下载失败，请重试')
            
    except Exception as e:
        error_msg = f"❌ 分析失败：{str(e)}"
        console.error(error_msg)
        showError('business-analysis-status', error_msg)

# Explicitly expose only the required functions to JavaScript
import js
if not hasattr(js, 'pyscript'):
    js.pyscript = js.Object.new()
if not hasattr(js.pyscript, 'interpreter'):
    js.pyscript.interpreter = js.Object.new()
if not hasattr(js.pyscript.interpreter, 'globals'):
    js.pyscript.interpreter.globals = js.Object.new()

# Create a safe getter that only exposes specific functions
_exposed_functions = {
    'process_excel_merge': process_excel_merge,
    'process_business_analysis': process_business_analysis
}

def get_exposed_function(name):
    """Safely get exposed Python functions"""
    if name in _exposed_functions:
        return _exposed_functions[name]
    else:
        raise ValueError(f"Function '{name}' is not exposed to JavaScript")

js.pyscript.interpreter.globals.get = get_exposed_function
