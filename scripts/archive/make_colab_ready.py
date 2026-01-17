#!/usr/bin/env python3
"""
Script pour rendre les notebooks Google Colab Ready
Ajoute une cellule d'installation des dépendances au début de chaque notebook
"""

import json
import os
from pathlib import Path

# Cellule d'installation à ajouter au début
COLAB_INSTALL_CELL = {
    "cell_type": "markdown",
    "metadata": {
        "id": "colab_badge"
    },
    "source": [
        "# 🚀 Google Colab Setup\n",
        "\n",
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ogautier1980/sandbox-ml/blob/main/cours/XX_CHAPTER/XX_NOTEBOOK.ipynb)\n",
        "\n",
        "**Si vous exécutez ce notebook sur Google Colab**, exécutez la cellule suivante pour installer les dépendances."
    ]
}

COLAB_DEPS_CELL = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {
        "id": "colab_install"
    },
    "outputs": [],
    "source": [
        "# Installation des dépendances (Google Colab uniquement)\n",
        "import sys\n",
        "IN_COLAB = 'google.colab' in sys.modules\n",
        "\n",
        "if IN_COLAB:\n",
        "    print('📦 Installation des packages...')\n",
        "    \n",
        "    # Packages ML de base\n",
        "    !pip install -q numpy pandas matplotlib seaborn scikit-learn\n",
        "    \n",
        "    # Détection du chapitre et installation des dépendances spécifiques\n",
        "    notebook_name = 'NOTEBOOK_NAME'  # Sera remplacé automatiquement\n",
        "    \n",
        "    # Ch 06-08 : Deep Learning\n",
        "    if any(x in notebook_name for x in ['06_', '07_', '08_']):\n",
        "        !pip install -q torch torchvision torchaudio\n",
        "    \n",
        "    # Ch 08 : NLP\n",
        "    if '08_' in notebook_name:\n",
        "        !pip install -q transformers datasets tokenizers\n",
        "        if 'rag' in notebook_name:\n",
        "            !pip install -q sentence-transformers faiss-cpu rank-bm25\n",
        "    \n",
        "    # Ch 09 : Reinforcement Learning\n",
        "    if '09_' in notebook_name:\n",
        "        !pip install -q gymnasium[classic-control]\n",
        "    \n",
        "    # Ch 04 : Boosting\n",
        "    if '04_' in notebook_name and 'boosting' in notebook_name:\n",
        "        !pip install -q xgboost lightgbm catboost\n",
        "    \n",
        "    # Ch 05 : Clustering avancé\n",
        "    if '05_' in notebook_name:\n",
        "        !pip install -q umap-learn\n",
        "    \n",
        "    # Ch 11 : Séries temporelles\n",
        "    if '11_' in notebook_name:\n",
        "        !pip install -q statsmodels prophet\n",
        "    \n",
        "    # Ch 12 : Vision avancée\n",
        "    if '12_' in notebook_name:\n",
        "        !pip install -q ultralytics timm segmentation-models-pytorch\n",
        "    \n",
        "    # Ch 13 : Recommandation\n",
        "    if '13_' in notebook_name:\n",
        "        !pip install -q scikit-surprise implicit\n",
        "    \n",
        "    # Ch 14 : MLOps\n",
        "    if '14_' in notebook_name:\n",
        "        !pip install -q mlflow fastapi pydantic\n",
        "    \n",
        "    print('✅ Installation terminée !')\n",
        "else:\n",
        "    print('ℹ️  Environnement local détecté, les packages sont déjà installés.')"
    ]
}


def process_notebook(notebook_path):
    """Ajoute les cellules Colab au début d'un notebook"""

    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Vérifier si le notebook a déjà les cellules Colab
    if nb['cells'] and 'colab_badge' in str(nb['cells'][0].get('metadata', {})):
        print(f"  ⏭️  Déjà Colab Ready: {notebook_path.name}")
        return False

    # Créer les cellules avec le bon nom de notebook
    notebook_name = notebook_path.name
    chapter_dir = notebook_path.parent.name

    # Cellule markdown avec badge
    markdown_cell = COLAB_INSTALL_CELL.copy()
    markdown_source = markdown_cell['source'][0]
    markdown_source = markdown_source.replace('XX_CHAPTER', chapter_dir)
    markdown_source = markdown_source.replace('XX_NOTEBOOK', notebook_name)
    markdown_cell['source'] = [markdown_source] + markdown_cell['source'][1:]

    # Cellule code avec installation
    code_cell = COLAB_DEPS_CELL.copy()
    code_source = '\n'.join(code_cell['source'])
    code_source = code_source.replace('NOTEBOOK_NAME', notebook_name)
    code_cell['source'] = code_source.split('\n')

    # Insérer les cellules au début
    nb['cells'].insert(0, code_cell)
    nb['cells'].insert(0, markdown_cell)

    # Sauvegarder
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"  ✅ Ajouté Colab: {notebook_path.name}")
    return True


def main():
    """Traite tous les notebooks du cours"""

    # Déterminer le répertoire du cours
    script_dir = Path(__file__).parent
    cours_dir = script_dir.parent / 'cours'

    if not cours_dir.exists():
        print(f"❌ Erreur: répertoire cours/ non trouvé à {cours_dir}")
        return

    print(f"📁 Répertoire cours: {cours_dir}\n")

    total = 0
    modified = 0

    # Parcourir tous les répertoires de chapitres
    for chapter_dir in sorted(cours_dir.glob('[0-9][0-9]_*')):
        if not chapter_dir.is_dir():
            continue

        print(f"📚 Chapitre: {chapter_dir.name}")

        # Trouver tous les notebooks (sauf quiz)
        notebooks = list(chapter_dir.glob('*.ipynb'))
        notebooks = [nb for nb in notebooks if 'quiz' not in nb.name.lower()]

        if not notebooks:
            print("  ⚠️  Aucun notebook trouvé\n")
            continue

        for notebook_path in sorted(notebooks):
            total += 1
            if process_notebook(notebook_path):
                modified += 1

        print()

    print(f"\n{'='*60}")
    print(f"✨ Résumé:")
    print(f"   Total notebooks: {total}")
    print(f"   Modifiés: {modified}")
    print(f"   Déjà Colab Ready: {total - modified}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
