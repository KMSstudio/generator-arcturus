@echo off
echo [DEV] Starting FastAPI server (with reload)...
uvicorn main:app --reload
pause