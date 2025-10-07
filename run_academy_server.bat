@echo off
REM مسیر پایتون محیط مجازی
set PYTHON_EXE=C:\Users\Avaye Honar\Desktop\panel\venv\Scripts\python.exe

REM مسیر فایل run_server.py
set SERVER_SCRIPT=C:\Users\Avaye Honar\Desktop\panel\run_server.py

echo Starting Django Academy Server...
%PYTHON_EXE% %SERVER_SCRIPT%
pause
