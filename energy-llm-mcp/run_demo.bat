@echo off
start cmd /k "ollama serve"
timeout /t 3
start cmd /k "uvicorn mcp_server:app --reload"
timeout /t 3
python llm_client.py