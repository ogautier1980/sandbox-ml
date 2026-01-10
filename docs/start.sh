#!/bin/bash

echo "=========================================="
echo "   ML Sandbox - Démarrage"
echo "=========================================="
echo ""

# Remonter au répertoire racine
cd "$(dirname "$0")/.."

# Création des dossiers nécessaires
mkdir -p notebooks data models src logs mlruns

echo "[1/2] Construction de l'image Docker..."
docker-compose build

echo ""
echo "[2/2] Démarrage du container..."
docker-compose up -d ml-sandbox

echo ""
echo "=========================================="
echo "   ML Sandbox démarré avec succès!"
echo "=========================================="
echo ""
echo "Jupyter Lab: http://localhost:8888"
echo ""
echo "Pour arrêter: docker-compose down"
echo "=========================================="
