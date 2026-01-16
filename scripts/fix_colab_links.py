#!/usr/bin/env python3
"""
Script pour corriger les liens 'Open in Colab' dans les notebooks.
Remplace les placeholders XX_CHAPTER/XX_NOTEBOOK.ipynb par les vrais chemins.
"""

import json
import os
import re
from pathlib import Path

def fix_colab_link(notebook_path):
    """Corrige le lien Colab dans un notebook."""
    # Extraire le chemin relatif depuis cours/
    rel_path = notebook_path.relative_to(Path('cours'))
    chapter_dir = rel_path.parts[0]  # ex: "00_introduction"
    notebook_name = rel_path.name     # ex: "00_demo_ml_pipeline.ipynb"

    # Construire le bon chemin pour Colab
    correct_path = f"cours/{chapter_dir}/{notebook_name}"

    # Lire le notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Chercher et corriger le lien Colab
    modified = False
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            source = cell.get('source', [])
            if isinstance(source, list):
                for i, line in enumerate(source):
                    # Chercher les liens Colab avec placeholder
                    if 'colab-badge.svg' in line and 'XX_CHAPTER/XX_NOTEBOOK' in line:
                        # Remplacer par le bon chemin
                        new_line = re.sub(
                            r'cours/XX_CHAPTER/XX_NOTEBOOK\.ipynb',
                            correct_path,
                            line
                        )
                        if new_line != line:
                            source[i] = new_line
                            modified = True
                            print(f"[OK] Corrige: {notebook_path.relative_to(Path('.'))}")
                            print(f"  -> {correct_path}")

    # Sauvegarder si modifié
    if modified:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)

    return modified

def main():
    """Point d'entrée principal."""
    cours_dir = Path('cours')

    if not cours_dir.exists():
        print("Erreur: Le dossier 'cours' n'existe pas")
        return 1

    # Trouver tous les notebooks
    notebooks = list(cours_dir.glob('**/*.ipynb'))
    print(f"Trouvé {len(notebooks)} notebooks à vérifier...\n")

    fixed_count = 0
    for notebook_path in sorted(notebooks):
        if fix_colab_link(notebook_path):
            fixed_count += 1

    print(f"\n{'='*60}")
    print(f"Terminé! {fixed_count}/{len(notebooks)} notebooks corrigés.")
    print(f"{'='*60}")

    return 0

if __name__ == '__main__':
    exit(main())
