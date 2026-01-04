# Web Python Code

This directory contains Python code that runs in the browser via PyScript/Pyodide.

## Files

- `data_processing.py` - Main Python logic for web-based data processing
  - Excel file merging functionality
  - Business data analysis functionality
  - Browser file upload/download handlers

## How It Works

This Python code is loaded by `index.html` using PyScript. When users interact with the web interface:

1. User uploads files through the browser
2. Python code runs in the browser using Pyodide (WebAssembly Python)
3. Data processing happens entirely client-side (no server upload)
4. Results are downloaded directly to user's browser

## Updating Web Functionality

To add or modify features in the online interface:

1. Edit `data_processing.py`
2. Test locally by serving the repository:
   ```bash
   python -m http.server 8000
   ```
3. Commit and push to `main` branch
4. GitHub Actions will automatically deploy to GitHub Pages

See [DEPLOYMENT.md](../DEPLOYMENT.md) for detailed instructions.

## Key Differences from `/src` Scripts

| Feature | Web Version (`/web`) | Local Scripts (`/src`) |
|---------|---------------------|----------------------|
| Execution | Browser (PyScript/Pyodide) | Local Python interpreter |
| File Access | Browser File API | Direct filesystem access |
| Output | Browser download | Save to disk |
| User Input | Web form | Command-line prompts |
| Dependencies | Auto-loaded by PyScript | Must be installed via pip |

## Adding New Dependencies

If you need additional Python packages:

1. Update the `config` attribute in `index.html`:
   ```html
   <script type="py" src="./web/data_processing.py" 
           config='{"packages": ["pandas", "openpyxl", "NEW_PACKAGE"]}'></script>
   ```

2. Verify the package is available in Pyodide:
   - Check: https://pyodide.org/en/stable/usage/packages-in-pyodide.html

## Debugging

Open browser developer console (F12) to see:
- Python execution logs (`console.log` calls)
- Python errors and stack traces
- JavaScript errors

Use `console.log()` in Python code for debugging:
```python
from js import console
console.log("Debug message")
```
