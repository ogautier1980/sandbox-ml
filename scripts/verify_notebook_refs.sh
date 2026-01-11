#!/bin/bash

# Script de vérification des références aux notebooks dans les fichiers .tex
# Vérifie que tous les notebooks référencés dans les .tex existent bien
# Note: Ce script doit être exécuté depuis le répertoire scripts/

# Déterminer le répertoire du cours
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COURS_DIR="$(dirname "$SCRIPT_DIR")/cours"

cd "$COURS_DIR" || { echo "❌ Erreur: répertoire cours/ non trouvé"; exit 1; }

echo "🔍 Vérification des références aux notebooks dans les fichiers .tex"
echo "📁 Répertoire cours: $COURS_DIR"
echo "===================================================================="
echo ""

ERRORS=0
WARNINGS=0

# Couleurs
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction pour extraire les références aux notebooks d'un fichier .tex
check_tex_file() {
    local tex_file="$1"
    local chapter_dir=$(dirname "$tex_file")
    local chapter_name=$(basename "$chapter_dir")

    echo -e "${BLUE}📄 Vérification: $chapter_name${NC}"

    # Chercher toutes les références aux .ipynb dans le fichier .tex
    # Format: \texttt{XX\_nom\_fichier.ipynb} où les underscores sont échappés
    local notebook_refs=$(grep -o 'texttt{[^}]*\.ipynb}' "$tex_file" 2>/dev/null | sed 's/texttt{//g' | sed 's/}//g' | sed 's/\\_/_/g' | sort -u)

    if [ -z "$notebook_refs" ]; then
        echo -e "   ${YELLOW}⚠️  Aucune référence à des notebooks trouvée${NC}"
        ((WARNINGS++))
        echo ""
        return
    fi

    local chapter_num=$(echo "$chapter_name" | grep -o '^[0-9][0-9]')
    local found_any=0
    local missing_count=0

    for notebook in $notebook_refs; do
        found_any=1

        # Ignorer les références avec wildcards (ex: 01_demo_*.ipynb)
        if [[ "$notebook" == *"*"* ]]; then
            # Vérifier qu'au moins un fichier correspondant existe
            local pattern="${notebook//\*/\*}"  # Garder le wildcard
            local matching_files=$(ls "$chapter_dir"/$pattern 2>/dev/null | wc -l)

            if [ $matching_files -gt 0 ]; then
                echo -e "   ${GREEN}✅ $notebook (${matching_files} fichier(s) correspondant(s))${NC}"
            else
                echo -e "   ${YELLOW}⚠️  WILDCARD: $notebook (aucun fichier correspondant)${NC}"
                ((WARNINGS++))
            fi
            continue
        fi

        # Chercher le notebook dans le répertoire du chapitre
        if [ -f "$chapter_dir/$notebook" ]; then
            echo -e "   ${GREEN}✅ $notebook${NC}"
        else
            echo -e "   ${RED}❌ MANQUANT: $notebook${NC}"
            ((ERRORS++))
            ((missing_count++))
        fi
    done

    if [ $missing_count -eq 0 ] && [ $found_any -eq 1 ]; then
        echo -e "   ${GREEN}✓ Tous les notebooks référencés existent${NC}"
    fi

    echo ""
}

# Parcourir tous les chapitres
for chapter_dir in [0-9][0-9]_*/; do
    if [ -d "$chapter_dir" ]; then
        tex_file="${chapter_dir}$(basename ${chapter_dir}).tex"
        if [ -f "$tex_file" ]; then
            check_tex_file "$tex_file"
        fi
    fi
done

# Vérifier les annexes
if [ -f "annexes/annexes.tex" ]; then
    check_tex_file "annexes/annexes.tex"
fi

echo "===================================================================="
echo -e "${BLUE}📊 Résumé de la vérification${NC}"
echo ""

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ Toutes les références sont correctes !${NC}"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠️  $WARNINGS avertissement(s)${NC}"
    exit 0
else
    echo -e "${RED}❌ $ERRORS notebook(s) référencé(s) mais manquant(s)${NC}"
    if [ $WARNINGS -gt 0 ]; then
        echo -e "${YELLOW}⚠️  $WARNINGS avertissement(s)${NC}"
    fi
    echo ""
    echo "💡 Conseil: Créez les notebooks manquants ou supprimez les références dans les fichiers .tex"
    exit 1
fi
