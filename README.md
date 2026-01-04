# 基于Python的数据处理模型

Python-based Data Processing Tools - 在线访问、本地运行的数据处理工具集

## 📋 项目简介

这是一个基于Python的数据处理工具集，提供了多种数据处理功能。用户可以通过GitHub Pages访问网页界面，下载Python脚本到本地运行，确保数据安全不外传。

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

**重要说明：** 所有数据处理都在您的本地计算机上完成，**不会上传任何文件到服务器**。Python脚本直接在您的电脑上读取和处理文件，确保您的数据完全安全。

## 🚀 快速开始

### 环境要求

- Python 3.6 或更高版本
- pip (Python包管理器)

### 安装依赖

```bash
pip install pandas openpyxl matplotlib
```

### 使用步骤

1. **访问网页**：打开 [在线界面](https://sos0sso0.github.io/python-web-tools/)
2. **选择功能**：在菜单中选择需要的功能（Excel文件合并 或 经营分析）
3. **下载脚本**：点击下载按钮，将Python脚本保存到您的电脑
4. **运行脚本**：在命令行中运行脚本
   ```bash
   python excel_merge.py
   # 或
   python business_analysis.py
   ```
5. **按照提示操作**：根据程序提示选择要处理的文件
6. **查看结果**：处理结果默认保存在 `D:\pyOutput` 目录

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

当前版本的Python脚本为基础框架，具体的数据处理逻辑（如Excel合并算法、分析算法等）将在后续版本中补充完善。

### 待开发功能

- [ ] Excel文件合并的具体实现
- [ ] 经营分析的具体算法
- [ ] 更多的数据处理功能
- [ ] 图表可视化增强

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 📮 联系方式

如有问题或建议，请通过GitHub Issues联系我们。