# Scripts Utilitaires - Cours ML

Ce répertoire contient tous les scripts d'automatisation et de maintenance du cours de Machine Learning.

---

## 📜 Scripts Actifs

### 1. `compile_all_pdfs.sh`

**Description** : Compile tous les PDFs LaTeX du cours (15 chapitres + annexes)

**Usage** :
```bash
# Depuis le container Docker
docker exec ml-sandbox bash /workspace/scripts/compile_all_pdfs.sh

# Ou directement
bash scripts/compile_all_pdfs.sh
```

**Fonctionnement** :
- Compile tous les fichiers `.tex` avec `xelatex` (2 passes)
- Génère 16 PDFs : Ch 00-14 + Annexes
- Nettoyage automatique des fichiers auxiliaires (.aux, .log, .out, .toc)
- Affiche un rapport final (succès/échecs, taille totale)

**Durée** : ~2-3 minutes

---

### 2. `verify_notebook_refs.sh`

**Description** : Vérifie que tous les notebooks référencés dans les PDFs existent réellement

**Usage** :
```bash
# Depuis le container Docker
docker exec ml-sandbox bash /workspace/scripts/verify_notebook_refs.sh

# Ou directement
bash scripts/verify_notebook_refs.sh
```

**Fonctionnement** :
- Extrait toutes les références `\texttt{XX_*.ipynb}` des fichiers `.tex`
- Gère les wildcards (`01_demo_*.ipynb`)
- Vérifie l'existence de chaque fichier notebook
- Affiche les notebooks manquants (si erreurs)
- Rapports avec couleurs (✅ vert, ❌ rouge, ⚠️ jaune)

**Durée** : ~2-3 secondes

---

## 📦 Scripts Archivés

Les scripts suivants ont été archivés car leur tâche est complétée :

### `archive/make_colab_ready.py`
- **Tâche complétée** : 45 notebooks rendus Colab Ready (100%)
- **Ne pas ré-exécuter** sauf si nouveaux notebooks ajoutés

### `archive/fix_tex_refs.py`
- **Tâche complétée** : 14 fichiers .tex corrigés (références notebooks)
- **Ne pas ré-exécuter** sauf si renumération des chapitres

### `archive/fix_notebook_refs.py`
- **Obsolète** : Remplacé par `fix_tex_refs.py`

---

## 🔧 Workflows Typiques

### Après avoir modifié des fichiers .tex
```bash
# 1. Compiler tous les PDFs
bash scripts/compile_all_pdfs.sh

# 2. Vérifier les références
bash scripts/verify_notebook_refs.sh
```

### Ajout de nouveaux notebooks
```bash
# 1. Rendre Colab Ready (utiliser script archivé si besoin)
python scripts/archive/make_colab_ready.py

# 2. Vérifier les références
bash scripts/verify_notebook_refs.sh
```

---

## 📁 Organisation

```
scripts/
├── README.md                    # Ce fichier
├── compile_all_pdfs.sh          # Compilation PDFs
├── verify_notebook_refs.sh      # Vérification références
└── archive/                     # Scripts one-time complétés
    ├── make_colab_ready.py
    ├── fix_tex_refs.py
    └── fix_notebook_refs.py
```

---

## 🔗 Voir Aussi

- [STRUCTURE.md](../STRUCTURE.md) - Organisation complète du projet
- [claude.md](../claude.md) - Mémoire permanente et historique
- [cours/README.md](../cours/README.md) - Documentation du cours ML
