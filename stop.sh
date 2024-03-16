#!/bin/bash

# Arrêter l'API Flask
pkill -f "python app.py"

# Arrêter le serveur de développement Vue.js
npm run serve -- --close
