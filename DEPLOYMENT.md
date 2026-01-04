# 部署指南 / Deployment Guide

## 项目架构 / Project Architecture

本项目包含两个不同的Python代码库，用于不同的目的：

This project contains two different Python codebases for different purposes:

### 1. 网页界面代码 / Web Interface Code
- **位置 / Location**: `/web/data_processing.py`
- **用途 / Purpose**: 在浏览器中通过PyScript/Pyodide运行
- **特点 / Features**: 
  - 在浏览器中运行，无需安装Python
  - 使用异步文件读取
  - 直接触发浏览器下载
  - 所有处理在客户端完成

### 2. 本地脚本代码 / Local Script Code
- **位置 / Location**: `/src/excel_merge.py`, `/src/business_analysis.py`
- **用途 / Purpose**: 供用户下载后在本地运行
- **特点 / Features**:
  - 需要本地安装Python环境
  - 使用命令行交互
  - 保存文件到本地磁盘
  - 适合需要离线处理大量数据的场景

## 如何更新在线界面 / How to Update the Online Interface

### 方法1: 更新网页界面的Python代码 / Method 1: Update Web Interface Python Code

如果你想修改在线界面的功能：

If you want to modify the functionality of the online interface:

1. **编辑文件 / Edit the file**: `/web/data_processing.py`
   - 这个文件包含了在浏览器中运行的Python代码
   - This file contains the Python code that runs in the browser

2. **测试更改 / Test your changes**: 
   ```bash
   # 在本地测试，启动一个简单的HTTP服务器
   # Test locally by starting a simple HTTP server
   python -m http.server 8000
   # 然后在浏览器中访问 / Then visit in browser:
   # http://localhost:8000
   ```

3. **提交更改 / Commit changes**:
   ```bash
   git add web/data_processing.py
   git commit -m "Update web interface functionality"
   ```

4. **推送到main分支 / Push to main branch**:
   ```bash
   git push origin main
   ```

5. **自动部署 / Automatic deployment**:
   - GitHub Actions会自动检测到main分支的更改
   - GitHub Actions will automatically detect changes to main branch
   - 工作流会自动部署到GitHub Pages
   - The workflow will automatically deploy to GitHub Pages
   - 通常在1-2分钟内完成
   - Usually completes within 1-2 minutes

6. **验证 / Verify**:
   - 访问: https://sos0sso0.github.io/python-web-tools/
   - Visit: https://sos0sso0.github.io/python-web-tools/
   - 清除浏览器缓存以确保看到最新版本
   - Clear browser cache to ensure you see the latest version

### 方法2: 更新HTML或CSS / Method 2: Update HTML or CSS

修改网页的界面或样式：

To modify the web interface or styling:

1. **编辑文件 / Edit**: `index.html`
2. **按照方法1的步骤3-6进行 / Follow steps 3-6 from Method 1**

### 方法3: 更新本地脚本 / Method 3: Update Local Scripts

如果你只是更新供用户下载的本地Python脚本：

If you're only updating the local Python scripts for download:

1. **编辑文件 / Edit**: `/src/excel_merge.py` or `/src/business_analysis.py`
2. **提交并推送 / Commit and push**:
   ```bash
   git add src/
   git commit -m "Update local scripts"
   git push origin main
   ```

**注意 / Note**: 更新`/src`目录中的文件**不会**自动更新网页界面的功能，因为网页使用的是`/web/data_processing.py`中的代码。

Updating files in `/src` directory **will NOT** automatically update the web interface functionality, as the web uses code from `/web/data_processing.py`.

## GitHub Actions工作流 / GitHub Actions Workflow

部署由`.github/workflows/static.yml`自动处理：

Deployment is automatically handled by `.github/workflows/static.yml`:

- **触发条件 / Trigger**: 推送到main分支时 / When pushing to main branch
- **操作 / Actions**:
  1. 检出代码 / Checkout code
  2. 配置GitHub Pages / Setup GitHub Pages
  3. 上传全部仓库内容 / Upload entire repository
  4. 部署到GitHub Pages / Deploy to GitHub Pages

## 故障排查 / Troubleshooting

### 更改没有显示？/ Changes not showing?

1. **检查工作流状态 / Check workflow status**:
   - 访问: https://github.com/sos0sso0/python-web-tools/actions
   - Visit: https://github.com/sos0sso0/python-web-tools/actions
   - 确认部署是否成功 / Confirm deployment succeeded

2. **清除浏览器缓存 / Clear browser cache**:
   - Chrome: Ctrl+Shift+Delete (Windows/Linux) or Cmd+Shift+Delete (Mac)
   - 或使用无痕模式测试 / Or test in incognito mode

3. **等待几分钟 / Wait a few minutes**:
   - GitHub Pages可能需要1-5分钟来传播更改
   - GitHub Pages may take 1-5 minutes to propagate changes

### 网页功能不工作？/ Web functionality not working?

1. **检查浏览器控制台 / Check browser console** (F12)
   - 查看Python或JavaScript错误
   - Look for Python or JavaScript errors

2. **验证文件路径 / Verify file paths**:
   - 确保`/web/data_processing.py`存在
   - Ensure `/web/data_processing.py` exists
   - 检查`index.html`中的引用路径
   - Check reference path in `index.html`

## 开发工作流建议 / Recommended Development Workflow

1. **创建功能分支 / Create feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **进行更改和测试 / Make changes and test locally**:
   ```bash
   python -m http.server 8000
   # Test at http://localhost:8000
   ```

3. **提交更改 / Commit changes**:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

4. **推送并创建Pull Request / Push and create Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **合并到main后自动部署 / Auto-deploy after merging to main**

## 文件对应关系 / File Mapping

| 功能 / Function | 网页版本 / Web Version | 本地版本 / Local Version |
|----------------|----------------------|------------------------|
| Excel文件合并 / Excel Merge | `/web/data_processing.py` → `process_excel_merge()` | `/src/excel_merge.py` |
| 经营分析 / Business Analysis | `/web/data_processing.py` → `process_business_analysis()` | `/src/business_analysis.py` |

## 联系方式 / Contact

如有问题或建议，请通过GitHub Issues联系我们。

For questions or suggestions, please contact us through GitHub Issues.
