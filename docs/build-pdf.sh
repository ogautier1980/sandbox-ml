#!/bin/bash
# Script pour compiler le guide PDF
# Exécuter depuis le container Docker : ./docs/build-pdf.sh

cd /workspace/docs

echo "Compilation du guide ML Sandbox..."
echo "=================================="

# Compilation avec latexmk (gère automatiquement les multiples passes)
latexmk -xelatex -interaction=nonstopmode guide-ml-sandbox.tex

# Vérifier le résultat
if [ -f "guide-ml-sandbox.pdf" ]; then
    echo ""
    echo "✅ PDF créé avec succès : docs/guide-ml-sandbox.pdf"
    echo "   Taille : $(du -h guide-ml-sandbox.pdf | cut -f1)"

    # Nettoyer les fichiers auxiliaires
    latexmk -c guide-ml-sandbox.tex
    echo "   Fichiers auxiliaires nettoyés."
else
    echo ""
    echo "❌ Erreur lors de la compilation."
    echo "   Consultez le fichier guide-ml-sandbox.log pour plus de détails."
fi
