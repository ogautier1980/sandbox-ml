#!/bin/bash

echo "🔐 Compilation des PDFs du cours de Cryptographie"
echo "================================================="
echo ""

cd /workspace/cours-crypto || exit 1

for chapter_dir in 01_introduction 02_symmetric_crypto 03_message_integrity 04_public_key_crypto 05_anonymous_communication; do
    if [ -d "$chapter_dir" ]; then
        cd "$chapter_dir"
        tex_file=$(ls *.tex 2>/dev/null | head -1)
        if [ -n "$tex_file" ]; then
            echo "📄 Compilation de $tex_file..."
            xelatex -interaction=nonstopmode "$tex_file" > /tmp/xelatex_${chapter_dir}_1.log 2>&1
            xelatex -interaction=nonstopmode "$tex_file" > /tmp/xelatex_${chapter_dir}_2.log 2>&1
            pdf_file="${tex_file%.tex}.pdf"
            if [ -f "$pdf_file" ]; then
                echo "   ✅ $pdf_file créé"
            else
                echo "   ❌ Erreur lors de la compilation de $pdf_file"
                echo "   Voir /tmp/xelatex_${chapter_dir}_2.log pour les détails"
            fi
        fi
        cd ..
    fi
done

echo ""
echo "================================================="
echo "✨ Compilation terminée !"
echo ""
echo "📊 PDFs créés :"
find . -name '*.pdf' -type f | sort
