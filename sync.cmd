@echo off
rem Sube el Cortex de gestion a GitHub. Se corre desde cualquier terminal:
rem   C:\Users\PC\Documents\cortex-gestion\sync.cmd
chcp 65001 >nul
cd /d "%~dp0"

git add -A
git diff --cached --quiet
if errorlevel 1 git commit -q -m "sync %date% %time:~0,5%"

git remote get-url origin >nul 2>&1
if errorlevel 1 (
  echo.
  echo  Cortex guardado en esta PC. Todavia no esta conectado a GitHub: ver pendientes.md, seccion Cortex.
  exit /b 0
)

git pull --rebase --autostash -q
if errorlevel 1 (
  echo.
  echo  No se pudo traer lo nuevo de GitHub. Mira el mensaje de arriba y pasaselo a Claude.
  exit /b 1
)

git push -q
if errorlevel 1 (
  echo.
  echo  No se pudo subir a GitHub. Mira el mensaje de arriba y pasaselo a Claude.
  exit /b 1
)

echo.
echo  Cortex sincronizado con GitHub.
