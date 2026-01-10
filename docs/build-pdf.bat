@echo off
REM Script pour compiler le guide PDF via Docker
REM Exécuter depuis Windows : docs\build-pdf.bat

echo Compilation du guide ML Sandbox via Docker...
echo ==============================================

docker exec ml-sandbox bash -c "cd /workspace/docs && latexmk -xelatex -interaction=nonstopmode guide-ml-sandbox.tex && latexmk -c guide-ml-sandbox.tex"

if exist "docs\guide-ml-sandbox.pdf" (
    echo.
    echo [OK] PDF cree avec succes : docs\guide-ml-sandbox.pdf
) else (
    echo.
    echo [ERREUR] La compilation a echoue.
    echo Assurez-vous que le container ml-sandbox est en cours d'execution.
)

pause
