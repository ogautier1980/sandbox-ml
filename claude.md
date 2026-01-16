# CLAUDE.md - Projet Sandbox-ML

**Mémoire permanente pour les sessions Claude**

| Info | Valeur |
|------|--------|
| Repository | [github.com/ogautier1980/sandbox-ml](https://github.com/ogautier1980/sandbox-ml) |
| Version | 1.2 |
| Mise à jour | 2026-01-14 |

---

## Vue d'Ensemble

Environnement Docker complet pour Machine Learning avec cours universitaire intégré.

**Cours** :
- **Machine Learning** : 14 chapitres + annexes (100% complété) - 78-96h de formation

---

## Structure Projet

Voir [STRUCTURE.md](STRUCTURE.md) pour détails complets.

```
sandbox-ml/
├── README.md, STRUCTURE.md, CLAUDE.md
├── docker-compose.yml, Dockerfile, requirements.txt
├── docs/                    # config.md, tools.md, guide PDF
├── cours/                   # 14 chapitres ML + annexes
├── scripts/                 # compile_all_pdfs.sh, verify_notebook_refs.sh
└── notebooks/data/models/src/
```

---

## Container Docker

**Base** : Python 3.11-slim (Debian Trixie)

| Stack | Packages |
|-------|----------|
| **ML/DL** | PyTorch, TensorFlow, scikit-learn, XGBoost, LightGBM, CatBoost |
| **Data** | NumPy, Pandas, Polars, SciPy, PyArrow |
| **Viz** | Matplotlib, Seaborn, Plotly, Bokeh, Altair |
| **NLP** | Transformers, spaCy, NLTK, LangChain |
| **Docs** | LaTeX, Pandoc, pypdf, python-docx, LibreOffice |
| **OCR** | Tesseract (FR/EN), pytesseract, EasyOCR |
| **Media** | OpenCV, Pillow, ImageMagick, FFmpeg |
| **Web** | FastAPI, Flask, Streamlit, Gradio |

**Ports** : 8888 (Jupyter), 6006 (TensorBoard), 5000 (MLflow)

---

## Cours Machine Learning

**Statut** : 14/14 chapitres (16 PDFs, 45 notebooks Colab Ready, 15 quiz/225 QCM)

| Partie | Chapitres | Contenu |
|--------|-----------|---------|
| **Fondations** | 00-02 | Introduction, Mathématiques, Métriques |
| **ML Classique** | 03-05 | Régression, Classification, Non-Supervisé |
| **Deep Learning** | 06-08 | MLP, CNN, RNN/Transformers (BERT, GPT, RAG) |
| **Paradigmes** | 09-10 | Reinforcement Learning, Algorithmes Génétiques |
| **Applications** | 11-13 | Séries Temporelles, Vision, Recommandation |
| **Production** | 14 | MLOps, Déploiement, Best Practices |

**Features** :
- Formation Python intégrée (`00_prerequis_python.ipynb`)
- Google Colab Ready avec installation auto
- Quiz auto-évaluation (15 QCM/chapitre)
- Notebooks RAG/LLM (Sentence-BERT, FAISS, Reranking)
- Annexes : Cheat sheets, Hardware/Cloud, Carrières ML

---

## Commandes Essentielles

### Docker
```bash
docker-compose up -d --build  # Démarrage complet
docker-compose up -d          # Démarrage rapide
docker exec -it ml-sandbox bash
docker-compose down
```

### Compilation PDFs
```bash
docker exec ml-sandbox bash /workspace/scripts/compile_all_pdfs.sh
docker exec ml-sandbox bash -c "cd /workspace/cours/XX_chapitre && xelatex -interaction=nonstopmode XX_*.tex"
```

**Services** : http://localhost:8888 (Jupyter), :6006 (TensorBoard), :5000 (MLflow)

---

## Points Techniques Clés

### Docker
- Image : `python:3.11-slim` (Debian Trixie)
- Correction : `libgl1` (pas `libgl1-mesa-glx` obsolète)
- Volumes : docs/, cours/, scripts/, notebooks/, data/, models/, src/
- LaTeX : packages `lmodern`, `texlive-latex-extra`, `texlive-science`

### Génération PDF
- Commande : `xelatex -interaction=nonstopmode file.tex` (2 passes pour TOC)
- **IMPORTANT** : XeLaTeX + UTF-8 nativement → NE PAS utiliser `\usepackage[T1]{fontenc}` (cause accents manquants)
- Utiliser : `\usepackage[utf8]{inputenc}` + `\usepackage[french]{babel}` uniquement

### Scripts
- Path detection automatique
- Format : LF (Unix) obligatoire pour bash
- Wildcard support : `verify_notebook_refs.sh` gère `XX_demo_*.ipynb`

---

## Règles de Maintenance

**Standards** :
- Encodage UTF-8, fins de ligne LF (`.editorconfig`)
- Indentation : 4 espaces (Python, LaTeX), 2 espaces (JSON, YAML)

**Organisation** :
- Documentation → `docs/`
- Cours ML → `cours/`
- Scripts → `scripts/`
- Fichiers obsolètes → `archive/` (archiver, ne pas supprimer)
- Pas de fichiers temporaires à la racine → `/tmp/`

**Racine autorisée** :
- Docs : README.md, STRUCTURE.md, CLAUDE.md
- Config : .editorconfig, .gitignore, docker-compose.yml, Dockerfile, requirements.txt
- IDE : .vscode/, .devcontainer/

---

## Scripts Utilitaires

| Script | Description |
|--------|-------------|
| `compile_all_pdfs.sh` | Compile tous les PDFs cours |
| `verify_notebook_refs.sh` | Vérifie références notebooks dans .tex |

**Archivés** (tâches complétées) :
- `make_colab_ready.py` : 45 notebooks traités
- `fix_tex_refs.py` : 14 fichiers corrigés
- `fix_notebook_refs.py` : Obsolète (remplacé)

---

## Documentation

| Fichier | Contenu |
|---------|---------|
| `README.md` | Vue d'ensemble, démarrage rapide |
| `STRUCTURE.md` | Organisation complète |
| `docs/config.md` | Installation technique |
| `docs/tools.md` | Documentation exhaustive outils |
| `cours/README.md` | Guide cours ML |

---

## Historique

**2026-01-14** - Simplification projet
- Suppression cours-crypto/ et cours-securite/
- Focus exclusif sur Machine Learning
- Mise à jour documentation

**2026-01-12** - Clean-up & Optimisation
- Suppression fichiers LaTeX auxiliaires - 60 fichiers
- Optimisation CLAUDE.md (305→215 lignes, -30%)

**2026-01-11** - Pack Prioritaire ML
- Formation Python intégrée (`00_prerequis_python.ipynb`)
- 15 quiz (225 QCM) + 45 notebooks Colab Ready
- Annexes étendues (Cheat Sheets, Hardware/Cloud, Carrières)

**2026-01-11** - Finalisation Cours ML
- 14 chapitres (16 PDFs, ~1300 lignes/chapitre)
- Réorganisation pédagogique 6 parties logiques

**2026-01-10** - Création Projet
- Structure Docker complète (~100 packages)
- Documentation : config.md, tools.md, guide PDF
- VS Code + Dev Container

---

*Dernière mise à jour : 2026-01-14*
