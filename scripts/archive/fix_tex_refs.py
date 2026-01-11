#!/usr/bin/env python3
"""
Script pour corriger les références obsolètes aux notebooks dans les .tex
après la renumération des chapitres
"""

import re
from pathlib import Path

def fix_tex_file(tex_path):
    """Corrige les références dans un fichier .tex"""
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Corrections des références obsolètes
    # Format: XX\_demo\_ → XX_demo_
    content = re.sub(r'(\d{2})\\_demo\\_', r'\1_demo_', content)
    content = re.sub(r'(\d{2})\\_exercices', r'\1_exercices', content)
    content = re.sub(r'(\d{2})\\_demo\_\*', r'\1_demo_*', content)

    # Corrections spécifiques des chapitres renumérés
    # Ch 11 (était 12)
    content = re.sub(r'\{12_demo_\*\.ipynb\}', r'{11_demo_*.ipynb}', content)
    content = re.sub(r'\{12_exercices\.ipynb\}', r'{11_exercices.ipynb}', content)
    content = re.sub(r'\{12_demo_', r'{11_demo_', content)

    # Ch 12 (était 13)
    content = re.sub(r'\{13_demo_\*\.ipynb\}', r'{12_demo_*.ipynb}', content)
    content = re.sub(r'\{13_demo_', r'{12_demo_', content)

    # Ch 13 (était 14)
    content = re.sub(r'\{14_demo_\*\.ipynb\}', r'{13_demo_*.ipynb}', content)
    content = re.sub(r'\{14_exercices\.ipynb\}', r'{13_exercices.ipynb}', content)
    content = re.sub(r'\{14_demo_', r'{13_demo_', content)

    if content != original:
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    # Déterminer le répertoire du cours
    script_dir = Path(__file__).parent
    cours_dir = script_dir.parent / 'cours'

    if not cours_dir.exists():
        print(f"❌ Erreur: répertoire cours/ non trouvé à {cours_dir}")
        return

    print("🔧 Correction des références aux notebooks dans les .tex")
    print(f"📁 Répertoire cours: {cours_dir}")
    print("=" * 70)

    fixed_count = 0
    total_count = 0

    # Parcourir tous les fichiers .tex
    for tex_file in cours_dir.glob('**/*.tex'):
        if 'template' in tex_file.name:
            continue

        total_count += 1
        if fix_tex_file(tex_file):
            print(f"✅ Corrigé: {tex_file.relative_to(cours_dir)}")
            fixed_count += 1

    print("=" * 70)
    print(f"📊 Résumé: {fixed_count}/{total_count} fichiers corrigés")

if __name__ == '__main__':
    main()
