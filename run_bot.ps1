# -----------------------------
# MCP Developer Documentation Bot
# Turnkey Runner Script (Windows PowerShell)
# -----------------------------

function Write-Bot {
    param([string]$Message, [ConsoleColor]$Color = 'White')
    Write-Host "[MCP Bot] $Message" -ForegroundColor $Color
}

# 1️⃣ Install dependencies
Write-Bot "Installing dependencies..." Cyan
python -m pip install --upgrade pip
pip install -r requirements.txt

# 2️⃣ Run documentation generation
Write-Bot "Scanning repository and generating documentation..." Cyan
python run.py tests/example_repo

# 3️⃣ Run MCP conversation logging
Write-Bot "Running MCP interactive session and logging sample queries..." Cyan
python run_mcp_logging.py

# 4️⃣ Finish
Write-Bot "✅ All tasks completed successfully!" Green
Write-Bot "Check your outputs in 'sample_output/' and conversation logs in 'tests/results/'" Yellow
