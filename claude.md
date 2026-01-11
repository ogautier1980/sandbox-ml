# CLAUDE.md - Projet Sandbox-ML

**Mémoire permanente pour les sessions Claude**

| Info | Valeur |
|------|--------|
| Repository | [github.com/ogautier1980/sandbox-ml](https://github.com/ogautier1980/sandbox-ml) |
| Version | 1.0 |
| Mise à jour | 2026-01-11 |

---

## Vue d'Ensemble du Projet

Environnement Docker complet pour Machine Learning avec cours intégré de 14 chapitres + annexes.

**Statut** : Cours 100% finalisé (PDFs théoriques + notebooks pratiques)

---

## Structure du Projet

Voir [STRUCTURE.md](STRUCTURE.md) pour la documentation complète de l'organisation.

```
sandbox-ml/
├── README.md               # Documentation rapide
├── claude.md               # Ce fichier (mémoire Claude)
├── STRUCTURE.md            # Documentation complète du projet
├── docker-compose.yml      # Services Docker
├── Dockerfile              # Image Python 3.11 + ML
├── requirements.txt        # ~100 packages Python
├── .editorconfig          # Standards de formatage
│
├── docs/                   # Documentation technique
│   ├── config.md          # Guide d'installation
│   ├── tools.md           # Guide des outils (~2000 lignes)
│   ├── guide-ml-sandbox.pdf  # Guide PDF complet
│   └── archive/           # Fichiers obsolètes
│
├── cours/                  # Cours ML (14 chapitres + annexes)
│   ├── README.md          # Documentation du cours
│   ├── 00_introduction/   # PDFs + notebooks
│   ├── ...                # Chapitres 01-13
│   └── annexes/           # Annexes complètes
│
├── scripts/                # Scripts utilitaires
│   ├── README.md          # Documentation des scripts
│   ├── compile_all_pdfs.sh     # Compilation PDFs
│   ├── verify_notebook_refs.sh # Vérification références
│   └── archive/           # Scripts obsolètes
│
└── notebooks/data/models/src/  # Répertoires de travail
```

---

## Container Docker

| Composant | Contenu |
|-----------|---------|
| **Base** | Python 3.11-slim (Debian Trixie) |
| **ML/DL** | PyTorch, TensorFlow, scikit-learn, XGBoost, LightGBM, CatBoost |
| **Data** | NumPy, Pandas, Polars, SciPy, PyArrow |
| **Viz** | Matplotlib, Seaborn, Plotly, Bokeh, Altair |
| **NLP** | Transformers, spaCy, NLTK, LangChain |
| **Docs** | LaTeX, Pandoc, pypdf, python-docx, LibreOffice |
| **OCR** | Tesseract (FR/EN), pytesseract, EasyOCR |
| **Media** | OpenCV, Pillow, ImageMagick, FFmpeg |
| **Web** | FastAPI, Flask, Streamlit, Gradio |

### Ports

| Port | Service |
|------|---------|
| 8888 | Jupyter Lab |
| 6006 | TensorBoard |
| 5000 | MLflow |

---

## Cours Machine Learning

### Vue d'Ensemble

**Statut** : 14/14 chapitres + Annexes (100% complété)
- **14 chapitres** (~16 PDFs LaTeX)
- **45 notebooks** de démonstration (Colab Ready)
- **15 quiz** d'auto-évaluation (225 questions QCM)
- **Durée totale** : 78-96 heures

### Organisation Pédagogique (6 Parties)

| Partie | Chapitres | Contenu | Durée |
|--------|-----------|---------|-------|
| **1. Fondations** | 00-02 | Introduction, Mathématiques, Métriques | 10-13h |
| **2. ML Classique** | 03-05 | Régression, Classification, Non-Supervisé | 12-15h |
| **3. Deep Learning** | 06-08 | MLP, CNN, RNN/Transformers | 18-22h |
| **4. Paradigmes Alternatifs** | 09-10 | Reinforcement Learning, AG | 8-10h |
| **5. Applications Avancées DL** | 11-13 | Séries Temporelles, Vision, Recommandation | 15-18h |
| **6. Production** | 14 | MLOps, Déploiement, Best Practices | 5-6h |

### Détail des Chapitres

**Partie 1 - Fondations**
- Ch 00 : Introduction au ML (formation Python intégrée)
- Ch 01 : Fondamentaux Mathématiques (algèbre, proba, optim)
- Ch 02 : Métriques d'Évaluation (classification, régression)

**Partie 2 - ML Classique**
- Ch 03 : Régression (linéaire, Ridge, Lasso, diagnostic)
- Ch 04 : Classification Supervisée (KNN, Arbres, Boosting, SVM)
- Ch 05 : Apprentissage Non-Supervisé (Clustering, PCA, détection anomalies)

**Partie 3 - Deep Learning**
- Ch 06 : Réseaux de Neurones Fondamentaux (Perceptron, MLP, Backprop)
- Ch 07 : Deep Learning - CNN (LeNet, ResNet, Transfer Learning)
- Ch 08 : Deep Learning - RNN (LSTM, Transformers, BERT, GPT, RAG)

**Partie 4 - Paradigmes Alternatifs**
- Ch 09 : Reinforcement Learning (Q-Learning, DQN, Policy Gradient)
- Ch 10 : Algorithmes Génétiques (optimisation évolutionnaire)

**Partie 5 - Applications Avancées DL**
- Ch 11 : Séries Temporelles (ARIMA, Prophet, LSTM forecasting)
- Ch 12 : Vision Avancée (YOLO, Segmentation, ViT, CLIP)
- Ch 13 : Systèmes de Recommandation (CF, Matrix Factorization, NCF)

**Partie 6 - Production**
- Ch 14 : Best Practices & MLOps (Pipeline, FastAPI, MLflow)

### Features Clés

✅ **Formation Python intégrée** : Notebook `00_prerequis_python.ipynb` pour débutants
✅ **Google Colab Ready** : Tous les notebooks utilisables sans installation locale
✅ **Quiz d'auto-évaluation** : 15 questions QCM par chapitre avec auto-correction
✅ **Notebooks RAG/LLM** : Techniques avancées (Sentence-BERT, FAISS, Reranking)
✅ **Annexes étendues** : Cheat sheets, Guide hardware/cloud, Carrières ML, Stack complète

---

## Scripts Utilitaires

| Script | Description | Usage |
|--------|-------------|-------|
| `compile_all_pdfs.sh` | Compile tous les PDFs (16 fichiers) | Génération documentation |
| `verify_notebook_refs.sh` | Vérifie références notebooks dans .tex | Validation cohérence |

**Scripts archivés** (tâches complétées) :
- `make_colab_ready.py` - Notebooks Colab Ready (45 notebooks traités)
- `fix_tex_refs.py` - Corrections références LaTeX (14 fichiers corrigés)
- `fix_notebook_refs.py` - Obsolète (remplacé par fix_tex_refs.py)

---

## Commandes Utiles

### Docker

```bash
# Démarrage complet
docker-compose up -d --build

# Démarrage rapide
docker-compose up -d

# Shell interactif
docker exec -it ml-sandbox bash

# Arrêter les containers
docker-compose down

# Voir les logs
docker-compose logs -f ml-sandbox
```

### Compilation PDFs

```bash
# Compiler tous les PDFs du cours
docker exec ml-sandbox bash /workspace/scripts/compile_all_pdfs.sh

# Vérifier les références
docker exec ml-sandbox bash /workspace/scripts/verify_notebook_refs.sh

# Compiler un PDF spécifique
docker exec ml-sandbox bash -c "cd /workspace/cours/XX_chapitre && xelatex -interaction=nonstopmode XX_*.tex"
```

### Accès Services

- **Jupyter Lab** : http://localhost:8888
- **TensorBoard** : http://localhost:6006
- **MLflow** : http://localhost:5000

---

## Règles de Maintenance

### Standards de Fichiers

- **Encodage** : UTF-8 pour tous les fichiers
- **Fins de ligne** : LF (Unix) - configuré via `.editorconfig`
- **Indentation** : 4 espaces (Python, LaTeX), 2 espaces (JSON, YAML)

### Organisation

- **Documentation** → `docs/`
- **Cours ML** → `cours/` (14 chapitres + annexes)
- **Scripts** → `scripts/`
- **Fichiers obsolètes** → `archive/` (ne pas supprimer, archiver)
- **Pas de fichiers temporaires à la racine** → utiliser `/tmp/`

### Fichiers Autorisés à la Racine

- `README.md`, `STRUCTURE.md`, `claude.md`
- Fichiers de configuration : `.editorconfig`, `.gitignore`, `docker-compose.yml`, `Dockerfile`, `requirements.txt`
- `.vscode/`, `.devcontainer/`

---

## Points Techniques Importants

### Docker

- **Image base** : `python:3.11-slim` (Debian Trixie)
- **Correction importante** : Utiliser `libgl1` au lieu de `libgl1-mesa-glx` (obsolète)
- **Volumes montés** : docs/, cours/, scripts/, notebooks/, data/, models/, src/
- **Polices LaTeX** : Packages requis : `lmodern`, `texlive-latex-extra`, `texlive-science`

### Génération PDF

- **Commande** : `xelatex -interaction=nonstopmode file.tex` (2 passes pour TOC)
- **Script batch** : `scripts/compile_all_pdfs.sh` (compile tous les chapitres)
- **Résultat** : 16 PDFs générés (~1.8 MB total)

### Scripts

- **Path detection** : Scripts détectent automatiquement leur répertoire
- **Format** : LF (Unix) obligatoire pour bash, CRLF possible pour .bat
- **Wildcard support** : `verify_notebook_refs.sh` gère les patterns `XX_demo_*.ipynb`

---

## Historique Léger

### 2026-01-11 - Clean-up Final du Projet
- Suppression fichiers LaTeX auxiliaires (.aux, .log, .out, .toc)
- Consolidation markdown (9 fichiers → structure claire)
- Archivage scripts one-time (make_colab_ready.py, fix_tex_refs.py)
- Simplification claude.md (historique détaillé → état actuel)
- Standards de formatage (.editorconfig)

### 2026-01-11 - Pack Prioritaire (Formation + Quiz + Colab)
- Formation Python intégrée : `00_prerequis_python.ipynb` (~280 lignes)
- 15 quiz d'auto-évaluation (225 questions QCM)
- 45 notebooks Colab Ready avec installation auto des dépendances

### 2026-01-11 - Finalisation Cours ML
- 14 chapitres créés (PDFs théoriques ~1300 lignes/chapitre)
- 45 notebooks de démonstration et exercices
- Annexes étendues (Cheat Sheets, Hardware/Cloud, Carrières, Stack ML)
- Réorganisation pédagogique en 6 parties logiques

### 2026-01-10 - Création Projet Initial
- Structure Docker complète
- ~100 packages Python
- Documentation : config.md, tools.md, guide PDF
- VS Code + Dev Container

---

## Documentation Complète

| Fichier | Contenu |
|---------|---------|
| `README.md` | Vue d'ensemble et démarrage rapide |
| `STRUCTURE.md` | Organisation complète du projet |
| `claude.md` | Ce fichier (mémoire Claude) |
| `docs/config.md` | Guide d'installation technique |
| `docs/tools.md` | Documentation exhaustive des outils |
| `cours/README.md` | Guide du cours ML |
| `scripts/README.md` | Documentation des scripts |

---

*Dernière mise à jour : 2026-01-11*
