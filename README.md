# Auto-Clicker

Ultra-minimalistic auto-clicker that clicks every 30 seconds.

## One-liner install & run:

**Windows CMD:**
```cmd
curl -s https://raw.githubusercontent.com/ArturNiklewicz/auto-clicker/main/click.py | python
```

**PowerShell:**
```powershell
iwr https://raw.githubusercontent.com/ArturNiklewicz/auto-clicker/main/click.py -UseBasicParsing | % Content | python
```

**macOS/Linux:**
```bash
curl -s https://raw.githubusercontent.com/ArturNiklewicz/auto-clicker/main/click.py | python3
```

## Save and run later:

**Download and save:**

*Windows CMD:*
```cmd
curl -o click.py https://raw.githubusercontent.com/ArturNiklewicz/auto-clicker/main/click.py
```

*PowerShell:*
```powershell
iwr https://raw.githubusercontent.com/ArturNiklewicz/auto-clicker/main/click.py -OutFile click.py
```

**Then run anytime:**
```cmd
python click.py
```

## Troubleshooting:

**"No such file or directory" error:**
1. Check if file downloaded: `dir` (CMD) or `ls` (PowerShell/Linux)
2. Make sure you're in the right directory
3. Try full path: `python C:\path\to\click.py`
4. Or use: `python .\click.py` (current directory)

**"python not found" error:**
- Try `python3` instead of `python`
- Install Python from python.org

## Features:
- Cross-platform (macOS, Windows, Linux)
- Auto-installs dependencies
- Minimal 8-line script
- Press Ctrl+C to stop

⚠️ **Use responsibly** - For automation and testing purposes only.