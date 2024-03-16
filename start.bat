@echo off

rem Lancer l'API Flask en arrière-plan
start cmd /c "python app.py"

rem Attendre un court instant pour s'assurer que l'API est démarrée
timeout /t 1 >nul

rem Lancer l'application Vue.js
npm run serve
