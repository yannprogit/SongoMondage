@echo off

REM Arrêter l'API Flask
taskkill /F /IM python.exe /T

REM Arrêter le serveur de développement Vue.js
taskkill /F /IM node.exe /T
