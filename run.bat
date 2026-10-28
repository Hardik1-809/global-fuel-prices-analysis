@echo off
title Global Fuel Analytics - Flask Server
echo ========================================================
echo  Starting Global Fuel Analytics Web Application...
echo  Open your browser at: http://127.0.0.1:5000/
echo ========================================================
echo.
cd /d "%~dp0"
if exist venv\Scripts\python.exe (
    venv\Scripts\python.exe app.py
) else (
    python app.py
)
pause

