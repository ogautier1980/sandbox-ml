@echo off
echo ==========================================
echo    ML Sandbox - Demarrage
echo ==========================================
echo.

REM Remonter au repertoire racine
cd /d "%~dp0.."

REM Creation des dossiers necessaires
if not exist "notebooks" mkdir notebooks
if not exist "data" mkdir data
if not exist "models" mkdir models
if not exist "src" mkdir src
if not exist "logs" mkdir logs
if not exist "mlruns" mkdir mlruns

echo [1/2] Construction de l'image Docker...
docker-compose build

echo.
echo [2/2] Demarrage du container...
docker-compose up -d ml-sandbox

echo.
echo ==========================================
echo    ML Sandbox demarre avec succes!
echo ==========================================
echo.
echo Jupyter Lab: http://localhost:8888
echo.
echo Pour arreter: docker-compose down
echo ==========================================
pause
