#!/usr/bin/env python3
"""
Script pour corriger les références aux notebooks dans les fichiers .tex
suite à la renumération des chapitres 11-14.
"""

import re
from pathlib import Path

# Mappings de corrections
CORRECTIONS = {
    '11_series_temporelles/11_series_temporelles.tex': [
        (r'% Chapitre 12 - Séries Temporelles', r'% Chapitre 11 - Séries Temporelles'),
        (r'Chapitre 12 - Séries Temporelles et Forecasting', r'Chapitre 11 - Séries Temporelles et Forecasting'),
        (r'Chapitre 12}', r'Chapitre 11}'),
        (r'12_demo_', r'11_demo_'),
        (r'12_exercices\.ipynb', r'11_exercices.ipynb'),
    ],
    '12_vision_avancee/12_vision_avancee.tex': [
        (r'% Chapitre 13 - Vision', r'% Chapitre 12 - Vision'),
        (r'Chapitre 13 - Vision par Ordinateur Avancée', r'Chapitre 12 - Vision par Ordinateur Avancée'),
        (r'Chapitre 13}', r'Chapitre 12}'),
        (r'13_demo_', r'12_demo_'),
    ],
    '13_systemes_recommandation/13_systemes_recommandation.tex': [
        (r'% Chapitre 14 - Systèmes', r'% Chapitre 13 - Systèmes'),
        (r'Chapitre 14 - Systèmes de Recommandation', r'Chapitre 13 - Systèmes de Recommandation'),
        (r'Chapitre 14}', r'Chapitre 13}'),
        (r'14_demo_', r'13_demo_'),
        (r'14_exercices\.ipynb', r'13_exercices.ipynb'),
        (r'Chapitres 01, 06, 11 \(Fondamentaux Math, Réseaux de Neurones, Best Practices\)',
         r'Chapitres 01, 06, 14 (Fondamentaux Math, Réseaux de Neurones, Best Practices)'),
        (r'\\textbf\{Chapitre 15\} : Natural Language Processing',
         r'\\textbf{Chapitre 14} : Best Practices ML et Déploiement'),
        (r'\\textbf\{Chapitre 16\} : Computer Vision Avancée.*?\\item',
         r'\\item', re.DOTALL),
    ],
    '14_best_practices/14_best_practices.tex': [
        (r'Chapitre 11 - Best Practices', r'Chapitre 14 - Best Practices'),
        (r'Chapitre 11}', r'Chapitre 14}'),
        (r'11_demo_', r'14_demo_'),
        (r'11_demo_monitoring', r'14_demo_monitoring'),
    ],
}

def fix_file(filepath: Path):
    """Applique les corrections à un fichier."""
    relative_path = str(filepath.relative_to(Path.cwd()))

    if relative_path not in CORRECTIONS:
        return False

    print(f"Correction de {relative_path}...")

    try:
        content = filepath.read_text(encoding='utf-8')
        original_content = content

        for pattern, replacement, *flags in CORRECTIONS[relative_path]:
            flag = flags[0] if flags else 0
            content = re.sub(pattern, replacement, content, flags=flag)

        if content != original_content:
            filepath.write_text(content, encoding='utf-8')
            print(f"  ✓ Fichier modifié")
            return True
        else:
            print(f"  - Aucune modification nécessaire")
            return False

    except Exception as e:
        print(f"  ✗ Erreur: {e}")
        return False

def main():
    """Point d'entrée principal."""
    base_dir = Path.cwd()
    print(f"Répertoire de travail: {base_dir}\n")

    modified_count = 0

    for relative_path in CORRECTIONS.keys():
        filepath = base_dir / relative_path
        if filepath.exists():
            if fix_file(filepath):
                modified_count += 1
        else:
            print(f"ATTENTION: Fichier introuvable: {filepath}")

    print(f"\n{'='*60}")
    print(f"Résumé: {modified_count} fichier(s) modifié(s)")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
