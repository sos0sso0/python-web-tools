# Python-based Data Processing Tools - 使用文档

## 目录
1. [系统要求](#系统要求)
2. [安装指南](#安装指南)
3. [功能说明](#功能说明)
4. [常见问题](#常见问题)

## 系统要求

- **操作系统**: Windows 10/11, macOS, Linux
- **Python版本**: Python 3.6 或更高版本
- **硬盘空间**: 至少100MB可用空间（用于安装依赖和保存输出）

## 安装指南

### 1. 安装Python

如果您还没有安装Python，请访问 [Python官网](https://www.python.org/downloads/) 下载并安装。

**Windows用户注意**: 安装时请勾选 "Add Python to PATH" 选项。

### 2. 验证Python安装

打开命令行（Windows: cmd 或 PowerShell；macOS/Linux: Terminal），输入：

```bash
python --version
```

应该显示类似 `Python 3.x.x` 的版本信息。

### 3. 安装所需依赖

下载本项目的 `requirements.txt` 文件，在命令行中切换到文件所在目录，运行：

```bash
pip install -r requirements.txt
```

或者手动安装各个包：

```bash
pip install pandas openpyxl matplotlib
```

## 功能说明

### Excel文件合并

**功能描述**：将多个Excel文件合并成一个文件。

**使用方法**：
1. 下载 `excel_merge.py` 到您的电脑
2. 在命令行中运行：`python excel_merge.py`
3. 按照提示输入要合并的Excel文件路径（每行一个）
4. 输入空行结束文件选择
5. 合并后的文件将保存在 `D:\pyOutput` 目录

**示例**：
```
请输入要合并的Excel文件路径（每行一个，输入空行结束）：
> C:\Users\YourName\Documents\data1.xlsx
  ✓ 已添加: data1.xlsx
> C:\Users\YourName\Documents\data2.xlsx
  ✓ 已添加: data2.xlsx
> 
```

### 经营分析

**功能描述**：对业务数据进行分析，生成报表和图表。

**使用方法**：
1. 下载 `business_analysis.py` 到您的电脑
2. 在命令行中运行：`python business_analysis.py`
3. 按照提示输入要分析的数据文件路径
4. 选择分析类型（销售/财务/综合）
5. 分析结果将保存在 `D:\pyOutput` 目录

**支持的分析类型**：
- 销售数据分析
- 财务数据分析
- 综合经营分析

## 常见问题

### Q: 输出目录 D:\pyOutput 不存在怎么办？
A: 程序会自动创建该目录，无需手动创建。如果您想更改输出目录，可以修改脚本中的 `OUTPUT_DIR` 变量。

### Q: 为什么要在本地运行，而不是在线处理？
A: 本地运行确保您的数据完全安全，不会上传到任何服务器。这对于包含敏感信息的业务数据尤其重要。

### Q: 我的Excel文件包含公式，会被正确处理吗？
A: 当前版本主要处理数据值。具体的公式处理功能将在后续版本中完善。

### Q: 支持哪些Excel文件格式？
A: 支持 .xlsx 和 .xls 格式的Excel文件。

### Q: 遇到错误怎么办？
A: 
1. 检查Python和依赖包是否正确安装
2. 确认文件路径是否正确
3. 检查Excel文件是否损坏或正在被其他程序打开
4. 如果问题持续，请在GitHub上提交Issue

### Q: 可以处理多大的文件？
A: 取决于您的计算机内存。建议单个Excel文件不超过100MB。

### Q: macOS/Linux用户的输出目录在哪里？
A: 您可以修改脚本中的 `OUTPUT_DIR` 变量，改为适合您系统的路径，例如：
- macOS: `~/Documents/pyOutput`
- Linux: `~/pyOutput`

## 技术支持

如有其他问题，请访问项目的GitHub页面提交Issue：
https://github.com/sos0sso0/python-web-tools/issues
