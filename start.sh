#!/bin/bash

# Lancer l'API Flask en arrière-plan
python app.py &

# Attendre un court instant pour s'assurer que l'API est démarrée
sleep 1

# Lancer l'application Vue.js
npm run serve
