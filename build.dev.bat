@echo off
echo [FREEZE] Locking current Python package versions into requirements.txt...
pip freeze > requirements.txt

echo.
echo [BUILD] Building Docker image 'arcturus'...
docker build -t arcturus .

echo.
echo [CLEANUP] Removing old container if it exists...
docker rm -f arcturus-container >nul 2>&1

echo.
echo [RUN] Starting new container 'arcturus-container' on port 8000...
docker run -d -p 8000:8000 --env-file .env --name arcturus-container arcturus

echo.
echo [DONE] Build complete. Open http://localhost:8000/docs to test.
pause