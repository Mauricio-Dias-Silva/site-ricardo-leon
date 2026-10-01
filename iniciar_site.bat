@echo off
title Site ONG Ricardo Leon Xavier - Servidor Django
cd /d "%~dp0"

echo ==========================================================
echo    ONG DE FISIOTERAPIA - RICARDO LEON XAVIER
echo    Projeto Integrador VI - UNIVESP & AuraCloud
echo ==========================================================
echo Iniciando servidor Django...
echo.

:: Localiza o Python
set PYTHON_CMD=python
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
)

:: Abre o navegador em background apos 2 segundos
start /b cmd /c "timeout /t 2 >nul & start http://127.0.0.1:8000"

:: Inicia o servidor
echo Servidor rodando em: http://127.0.0.1:8000
echo Painel de Gestao (Ricardo Leon): http://127.0.0.1:8000/admin/
echo Login: admin  ^|  Senha: admin123
echo.
echo Pressione Ctrl+C para parar o servidor.
echo ==========================================================
"%PYTHON_CMD%" manage.py runserver 127.0.0.1:8000
pause

