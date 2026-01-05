"""
Web-based Data Processing Tools
Python code for browser-based Excel processing using PyScript/Pyodide

This file contains the Python logic that runs in the browser via PyScript.
To update the functionality of the web interface, modify this file.
"""

import asyncio
from pyodide.ffi import create_proxy
from js import document, showSuccess, showError, Blob, URL, console, Uint8Array
import pandas as pd
from io import BytesIO
from datetime import datetime
import traceback

async def read_file_async(file):
    """异步读取文件内容 / Asynchronously read file content"""
    array_buffer = await file.arrayBuffer()
    return array_buffer.to_bytes()

def download_file(content, filename, mime_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
    """触发浏览器下载文件 / Trigger browser file download"""
    try:
        # Convert Python bytes to JavaScript Uint8Array for proper binary handling
        # Ensure content is bytes or bytearray, then convert to Uint8Array for Blob API
        if not isinstance(content, (bytes, bytearray)):
            console.error(f"Unsupported content type: {type(content)}. Expected bytes or bytearray.")
            return False
        
        # Convert to Uint8Array
        js_array = Uint8Array.new(len(content))
        js_array.assign(content)
        
        # Create blob with proper binary data
        blob = Blob.new([js_array], {"type": mime_type})
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
        console.error(traceback.format_exc())
        return False

async def process_excel_merge_vertical(files):
    """处理Excel文件纵向合并 (Vertical merge by rows)"""
    try:
        console.log(f"Processing {len(files)} files for vertical merge")
        
        # Read all files
        dfs = []
        for file in files:
            console.log(f"Reading file: {file.name}")
            content = await read_file_async(file)
            df = pd.read_excel(BytesIO(content), engine='openpyxl')
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
        console.log(f"Generated Excel file with {len(result_content)} bytes")
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"merged_vertical_{timestamp}.xlsx"
        
        # Download file
        if download_file(result_content, filename):
            showSuccess('excel-merge-vertical-status', f'✅ 纵向合并成功！文件已下载：{filename}')
        else:
            showError('excel-merge-vertical-status', '❌ 文件下载失败，请重试')
            
    except Exception as e:
        error_msg = f"❌ 纵向合并失败：{str(e)}"
        console.error(error_msg)
        console.error(f"Error details: {e.__class__.__name__}")
        console.error(traceback.format_exc())
        showError('excel-merge-vertical-status', error_msg)

async def process_excel_merge_horizontal(files):
    """处理Excel文件横向合并 (Horizontal merge by columns with first column as index)"""
    try:
        console.log(f"Processing {len(files)} files for horizontal merge")
        
        # Read all files with first column as index
        dfs = []
        for i, file in enumerate(files):
            console.log(f"Reading file: {file.name}")
            content = await read_file_async(file)
            
            # Read with first column (index 0) as index
            df = pd.read_excel(BytesIO(content), engine='openpyxl', index_col=0)
            
            # Validate that index has values
            if df.index.isnull().any():
                raise ValueError(f"文件 {file.name} 的第1列包含空值，无法作为索引列使用")
            
            # Warn about duplicate indices (but don't fail)
            if df.index.duplicated().any():
                console.warn(f'警告：文件 {file.name} 的第1列包含重复的索引值')
            
            # Add suffix to column names to avoid conflicts (except for first file)
            if i > 0:
                df = df.copy()  # Create copy to avoid modifying original
                df.columns = [f"{col}_{i+1}" for col in df.columns]
            
            dfs.append(df)
            console.log(f"Read {len(df)} rows and {len(df.columns)} columns from {file.name}")
        
        # Merge dataframes horizontally (concatenate by columns)
        # axis=1: merge by columns, matching rows with same index
        # join='outer': keep all indices from all files
        # Rows with non-matching indices will have NaN values
        merged_df = pd.concat(dfs, axis=1, join='outer')
        console.log(f"Merged result has {len(merged_df)} rows and {len(merged_df.columns)} columns")
        
        # Save to BytesIO with explicit openpyxl engine for MS Excel compatibility
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Keep the index (first column) when saving
            merged_df.to_excel(writer, sheet_name='Merged Data')
        
        # Get the content
        output.seek(0)
        result_content = output.read()
        console.log(f"Generated Excel file with {len(result_content)} bytes")
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"merged_horizontal_{timestamp}.xlsx"
        
        # Download file
        if download_file(result_content, filename):
            showSuccess('excel-merge-horizontal-status', f'✅ 横向合并成功！文件已下载：{filename}')
        else:
            showError('excel-merge-horizontal-status', '❌ 文件下载失败，请重试')
            
    except ValueError as e:
        # Handle validation errors with user-friendly messages
        error_msg = f"❌ {str(e)}"
        console.error(error_msg)
        showError('excel-merge-horizontal-status', error_msg)
    except Exception as e:
        error_msg = f"❌ 横向合并失败：{str(e)}"
        console.error(error_msg)
        console.error(f"Error details: {e.__class__.__name__}")
        console.error(traceback.format_exc())
        showError('excel-merge-horizontal-status', error_msg)

async def process_business_analysis(file, analysis_type):
    """处理经营分析"""
    try:
        console.log(f"Analyzing file: {file.name}, type: {analysis_type}")
        
        # Read file
        content = await read_file_async(file)
        df = pd.read_excel(BytesIO(content), engine='openpyxl')
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
        console.log(f"Generated analysis report with {len(result_content)} bytes")
        
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
        console.error(f"Error details: {e.__class__.__name__}")
        console.error(traceback.format_exc())
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
    'process_excel_merge_vertical': process_excel_merge_vertical,
    'process_excel_merge_horizontal': process_excel_merge_horizontal,
    'process_business_analysis': process_business_analysis
}

def get_exposed_function(name):
    """Safely get exposed Python functions"""
    if name in _exposed_functions:
        return _exposed_functions[name]
    else:
        raise ValueError(f"Function '{name}' is not exposed to JavaScript")

js.pyscript.interpreter.globals.get = get_exposed_function
