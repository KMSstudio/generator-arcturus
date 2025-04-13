@echo off
REM Stage all changes
git add .

REM Prompt for commit message
set /p msg=Commit message: 

REM Commit with the entered message
git commit -m "%msg%"

REM Get current branch name
FOR /F "tokens=*" %%b IN ('git rev-parse --abbrev-ref HEAD') DO SET branch=%%b

REM Push to current branch
git push origin %branch%

pause