# 基于Python的数据处理模型

Python-based Data Processing Tools - 在线访问、浏览器运行的数据处理工具集

## 📋 项目简介

这是一个基于Python的数据处理工具集，提供了多种数据处理功能。用户可以通过GitHub Pages访问网页界面，**直接在浏览器中运行Python代码处理数据**，无需下载任何文件或安装Python环境，确保数据安全不外传。

本项目使用 **PyScript/Pyodide** 技术，在浏览器中运行Python代码，所有数据处理都在您的浏览器本地完成。

## 🌐 在线访问

访问我们的在线界面：[https://sos0sso0.github.io/python-web-tools/](https://sos0sso0.github.io/python-web-tools/)

## ✨ 功能特点

### 1. Excel文件合并
- 将多个Excel文件合并成一个文件
- 支持多种合并方式
- 自动处理数据格式

### 2. 经营分析
- 销售数据分析
- 财务数据分析
- 综合经营分析
- 自动生成报表和图表

## 🔒 数据安全

**重要说明：** 所有数据处理都在您的浏览器中完成，**不会上传任何文件到服务器**。Python代码通过PyScript/Pyodide在浏览器中运行，直接读取和处理您上传的文件，确保您的数据完全安全。

## 🚀 快速开始

### 使用方法（推荐）

1. **访问网页**：打开 [在线界面](https://sos0sso0.github.io/python-web-tools/)
2. **选择功能**：在菜单中选择需要的功能（Excel文件合并 或 经营分析）
3. **上传文件**：点击"选择文件"按钮，选择需要处理的Excel文件
4. **开始处理**：点击"开始合并"或"开始分析"按钮
5. **等待完成**：首次使用时需要加载Python环境（约几秒钟），之后处理速度较快
6. **下载结果**：处理完成后，结果文件会自动下载到您的电脑

**注意：** 
- 首次使用时，PyScript会自动下载Python环境和所需库（pandas、openpyxl等），可能需要等待几秒到几十秒
- 之后使用时，环境会被浏览器缓存，加载速度会更快
- 所有处理都在浏览器中完成，完全离线工作，无需安装Python

### 传统方法（需要本地Python环境）

如果您希望下载Python脚本到本地运行：

#### 环境要求

- Python 3.6 或更高版本
- pip (Python包管理器)

#### 安装依赖

```bash
pip install pandas openpyxl matplotlib
```

#### 使用步骤

1. **下载脚本**：从 `src/` 目录下载所需的Python脚本
2. **运行脚本**：在命令行中运行脚本
   ```bash
   python excel_merge.py
   # 或
   python business_analysis.py
   ```
3. **按照提示操作**：根据程序提示选择要处理的文件
4. **查看结果**：处理结果默认保存在 `D:\pyOutput` 目录

## 📁 项目结构

```
python-web-tools/
├── index.html              # 主网页界面
├── src/                    # Python脚本目录
│   ├── excel_merge.py      # Excel文件合并工具
│   └── business_analysis.py # 经营分析工具
├── docs/                   # 文档目录
└── README.md               # 项目说明
```

## 📝 开发说明

### 技术栈

- **前端**: HTML5, CSS3, JavaScript
- **Python运行环境**: PyScript 2024.1.1 + Pyodide
- **Python库**: pandas, openpyxl (通过Pyodide自动加载)
- **部署**: GitHub Pages

### 工作原理

本项目使用PyScript和Pyodide技术，在浏览器中运行真正的Python代码：

1. **PyScript**: 提供在HTML中嵌入Python代码的能力
2. **Pyodide**: WebAssembly版本的Python解释器，可以在浏览器中运行
3. **浏览器APIs**: 使用File API读取用户上传的文件，使用Blob API触发文件下载
4. **完全客户端**: 所有处理都在浏览器中完成，无需服务器

### 当前版本功能

- ✅ 在浏览器中运行Python代码
- ✅ Excel文件合并（支持多文件按行合并）
- ✅ 经营分析基础功能（数据统计、多表分析）
- ✅ 文件上传和下载
- ✅ 加载状态提示

### 待开发功能

- [ ] Excel文件合并的更多合并方式（按列、按条件等）
- [ ] 经营分析的高级算法和可视化图表
- [ ] 更多的数据处理功能
- [ ] 性能优化（处理大文件）
- [ ] 进度条显示

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 📮 联系方式

如有问题或建议，请通过GitHub Issues联系我们。