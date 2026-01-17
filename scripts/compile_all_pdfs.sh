#!/bin/bash
# Script pour compiler tous les PDFs du cours ML
# Usage: bash compile_all_pdfs.sh
# Note: Ce script doit être exécuté depuis le répertoire scripts/ ou avec le bon COURS_DIR

# Déterminer le répertoire du cours
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COURS_DIR="$(dirname "$SCRIPT_DIR")/cours"

cd "$COURS_DIR" || { echo "❌ Erreur: répertoire cours/ non trouvé"; exit 1; }

echo "🚀 Compilation des PDFs du cours Machine Learning"
echo "📁 Répertoire cours: $COURS_DIR"
echo "================================================="

# Fonction pour compiler un PDF
compile_pdf() {
    local dir=$1
    local file=$2

    if [ -f "$dir/$file" ]; then
        echo ""
        echo "📄 Compilation de $file..."
        cd "$dir"

        # Première passe
        xelatex -interaction=nonstopmode "$file" > /dev/null 2>&1

        # Deuxième passe (pour références croisées et TOC)
        xelatex -interaction=nonstopmode "$file" > /dev/null 2>&1

        if [ -f "${file%.tex}.pdf" ]; then
            echo "   ✅ ${file%.tex}.pdf créé"
        else
            echo "   ❌ Erreur lors de la compilation"
        fi

        # Nettoyage des fichiers auxiliaires
        rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz

        cd - > /dev/null
    else
        echo "   ⏭️  $file non trouvé, passage au suivant"
    fi
}

# Chapitres à compiler
chapters=(
    "00_introduction:00_introduction_ml.tex"
    "01_fondamentaux_mathematiques:01_fondamentaux_mathematiques.tex"
    "02_metriques_evaluation:02_metriques_evaluation.tex"
    "03_regression:03_regression.tex"
    "04_classification_supervisee:04_classification_supervisee.tex"
    "05_apprentissage_non_supervise:05_apprentissage_non_supervise.tex"
    "06_reseaux_neurones_fondamentaux:06_reseaux_neurones_fondamentaux.tex"
    "07_deep_learning_cnn:07_deep_learning_cnn.tex"
    "08_deep_learning_rnn:08_deep_learning_rnn.tex"
    "09_reinforcement_learning:09_reinforcement_learning.tex"
    "10_algorithmes_genetiques:10_algorithmes_genetiques.tex"
    "11_series_temporelles:11_series_temporelles.tex"
    "12_vision_avancee:12_vision_avancee.tex"
    "13_systemes_recommandation:13_systemes_recommandation.tex"
    "14_best_practices:14_best_practices.tex"
)

# Annexes
annexes=(
    "annexes:annexes.tex"
)

# Compilation des chapitres
echo ""
echo "📚 Compilation des chapitres principaux..."
for chapter in "${chapters[@]}"; do
    IFS=':' read -r dir file <<< "$chapter"
    compile_pdf "$dir" "$file"
done

# Compilation des annexes
echo ""
echo "📋 Compilation des annexes..."
for annexe in "${annexes[@]}"; do
    IFS=':' read -r dir file <<< "$annexe"
    compile_pdf "$dir" "$file"
done

echo ""
echo "================================================="
echo "✨ Compilation terminée !"
echo ""
echo "📊 Statistiques :"
pdf_count=$(find . -name "*.pdf" -type f | wc -l)
echo "   - PDFs créés : $pdf_count"
echo ""
echo "💡 Les PDFs sont dans leurs répertoires respectifs"
