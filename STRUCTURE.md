# Structure du Projet Sandbox-ML

Ce document décrit l'organisation complète du projet ML Sandbox.

---

## 📁 Vue d'Ensemble

```
sandbox-ml/
├── 📄 Fichiers de configuration
├── 📚 Documentation (docs/)
├── 🎓 Cours ML complet (cours/)
├── 🔧 Scripts utilitaires (scripts/)
├── 💻 Code et notebooks (src/, notebooks/)
└── 📊 Données et modèles (data/, models/)
```

---

## 📄 Racine du Projet

### Fichiers de Configuration

| Fichier | Description |
|---------|-------------|
| `README.md` | Documentation principale du projet |
| `claude.md` | Mémoire permanente pour les sessions Claude (historique complet) |
| `STRUCTURE.md` | Ce fichier - organisation du projet |
| `docker-compose.yml` | Configuration Docker Compose (services ML) |
| `Dockerfile` | Image Docker (Python 3.11 + ML/DL + outils) |
| `requirements.txt` | ~100 packages Python (ML, DL, visualisation, MLOps) |
| `.gitignore` | Fichiers à ignorer par Git |
| `.editorconfig` | Configuration éditeur (fins de ligne, indentation) |

### Répertoires de Données

| Répertoire | Contenu | Monté dans Docker |
|------------|---------|-------------------|
| `notebooks/` | Vos notebooks Jupyter personnels | ✅ `/workspace/notebooks` |
| `data/` | Datasets pour vos expérimentations | ✅ `/workspace/data` |
| `models/` | Modèles ML sauvegardés | ✅ `/workspace/models` |
| `src/` | Code source Python de vos projets | ✅ `/workspace/src` |

---

## 📚 Documentation (`docs/`)

Contient toute la documentation technique du projet.

```
docs/
├── config.md                          # Guide d'installation et configuration
├── tools.md                           # Guide des outils (~2000 lignes)
├── guide-ml-sandbox.tex               # Source LaTeX du guide complet
├── guide-ml-sandbox.pdf               # Guide PDF compilé
├── build-pdf.sh / build-pdf.bat      # Scripts de compilation PDF
├── start.sh / start.bat              # Scripts de démarrage rapide
└── archive/                          # 📦 Fichiers obsolètes archivés
    ├── CORRECTIONS_EFFECTUEES.md
    └── CORRECTIONS_NOTEBOOKS_REFS.md
```

### Fichiers Clés

- **config.md** : Installation Docker, configuration environnement, premiers pas
- **tools.md** : Documentation complète de tous les outils (PyTorch, TensorFlow, scikit-learn, MLflow, etc.)
- **guide-ml-sandbox.pdf** : Version PDF combinant config + tools

---

## 🎓 Cours Machine Learning (`cours/`)

Cours complet de Machine Learning avec 14 chapitres + annexes.

### Structure Générale

```
cours/
├── README.md                          # Documentation du cours
├── AMELIORATIONS_2026-01-11.md       # Changelog des améliorations récentes
├── _template_chapitre.tex            # Template LaTeX pour nouveaux chapitres
│
├── 00_introduction/                   # Ch 00 : Introduction au ML
├── 01_fondamentaux_mathematiques/     # Ch 01 : Algèbre, Proba, Optim
├── 02_metriques_evaluation/           # Ch 02 : Métriques classification/régression
├── 03_regression/                     # Ch 03 : Régression linéaire, Ridge, Lasso
├── 04_classification_supervisee/      # Ch 04 : KNN, Arbres, Boosting, SVM
├── 05_apprentissage_non_supervise/    # Ch 05 : Clustering, PCA, Détection anomalies
├── 06_reseaux_neurones_fondamentaux/  # Ch 06 : Perceptron, MLP, Backprop
├── 07_deep_learning_cnn/              # Ch 07 : CNN, LeNet, ResNet, Transfer Learning
├── 08_deep_learning_rnn/              # Ch 08 : RNN, LSTM, Transformers, BERT, GPT
├── 09_reinforcement_learning/         # Ch 09 : Q-Learning, DQN, Policy Gradient
├── 10_algorithmes_genetiques/         # Ch 10 : Algorithmes génétiques, optimisation
├── 11_series_temporelles/             # Ch 11 : ARIMA, Prophet, LSTM forecasting
├── 12_vision_avancee/                 # Ch 12 : YOLO, Segmentation, ViT, CLIP
├── 13_systemes_recommandation/        # Ch 13 : Collaborative Filtering, NCF
├── 14_best_practices/                 # Ch 14 : MLOps, Déploiement, FastAPI, MLflow
└── annexes/                           # Aide-mémoire, Glossaire, Ressources
```

### Contenu d'un Chapitre Type

```
XX_nom_chapitre/
├── XX_nom_chapitre.tex               # PDF théorique (LaTeX)
├── XX_nom_chapitre.pdf               # PDF compilé
├── XX_demo_*.ipynb                   # Notebooks de démonstration (1-3)
├── XX_exercices.ipynb                # Exercices pratiques (solutions intégrées)
└── XX_quiz.ipynb                     # Quiz d'auto-évaluation (15 questions QCM)
```

### Organisation Pédagogique

Le cours est organisé en **6 parties** :

| Partie | Chapitres | Contenu |
|--------|-----------|---------|
| **1. Fondations** | Ch 00-02 | Introduction, Mathématiques, Métriques |
| **2. ML Classique** | Ch 03-05 | Régression, Classification, Non-Supervisé |
| **3. Deep Learning** | Ch 06-08 | MLP, CNN, RNN/Transformers |
| **4. Paradigmes Alternatifs** | Ch 09-10 | Reinforcement Learning, Algorithmes Génétiques |
| **5. Applications Avancées DL** | Ch 11-13 | Séries Temporelles, Vision, Recommandation |
| **6. Production** | Ch 14 | MLOps, Déploiement, Best Practices |

### Statistiques

- **14 chapitres** + Annexes
- **~16 PDFs LaTeX** (~1.8 MB total)
- **45 notebooks de démonstration** (Colab Ready)
- **15 quiz** (225 questions QCM)
- **Durée totale** : 78-96 heures

### Features Clés

✅ **Formation Python intégrée** : Notebook `00_prerequis_python.ipynb` pour débutants
✅ **Google Colab Ready** : Tous les notebooks utilisables sans installation locale
✅ **Quiz d'auto-évaluation** : 15 questions QCM par chapitre avec auto-correction
✅ **Notebooks RAG/LLM** : Techniques avancées (Sentence-BERT, FAISS, Reranking)
✅ **Annexes étendues** : Cheat sheets, Guide hardware/cloud, Carrières ML, Stack complète

---

## 🔧 Scripts Utilitaires (`scripts/`)

Tous les scripts d'automatisation et de maintenance du cours.

```
scripts/
├── README.md                         # Documentation complète des scripts
├── compile_all_pdfs.sh              # Compile tous les PDFs du cours (16 fichiers)
├── verify_notebook_refs.sh          # Vérifie les références aux notebooks dans .tex
├── make_colab_ready.py              # Rend les notebooks Colab Ready automatiquement
├── fix_tex_refs.py                  # Corrige les références obsolètes dans .tex
└── archive/                         # 📦 Scripts obsolètes
    └── fix_notebook_refs.py
```

### Usage des Scripts

Tous les scripts peuvent être exécutés depuis le container Docker ou en local.

**Exemple** :
```bash
# Compiler tous les PDFs
docker exec ml-sandbox bash /workspace/scripts/compile_all_pdfs.sh

# Vérifier les références
docker exec ml-sandbox bash /workspace/scripts/verify_notebook_refs.sh

# Rendre Colab Ready
docker exec ml-sandbox python /workspace/scripts/make_colab_ready.py
```

Voir [scripts/README.md](scripts/README.md) pour plus de détails.

---

## 🐳 Configuration Docker

### Services

Le projet utilise Docker Compose avec 3 services :

| Service | Port | Description |
|---------|------|-------------|
| `ml-sandbox` | 8888, 6006, 5000 | Container principal (Jupyter Lab, TensorBoard, MLflow) |
| `tensorboard` | 6007 | TensorBoard standalone (profil optionnel) |
| `mlflow` | 5001 | MLflow standalone (profil optionnel) |

### Volumes Montés

| Local | Container | Contenu |
|-------|-----------|---------|
| `./notebooks` | `/workspace/notebooks` | Vos notebooks |
| `./data` | `/workspace/data` | Datasets |
| `./models` | `/workspace/models` | Modèles ML |
| `./src` | `/workspace/src` | Code source |
| `./docs` | `/workspace/docs` | Documentation |
| `./cours` | `/workspace/cours` | Cours ML |
| `./scripts` | `/workspace/scripts` | Scripts utilitaires |

### Image Docker

**Base** : `python:3.11-slim` (Debian Trixie)

**Packages installés** :
- **ML/DL** : PyTorch, TensorFlow, scikit-learn, XGBoost, LightGBM, CatBoost
- **Data** : NumPy, Pandas, Polars, SciPy, PyArrow
- **Viz** : Matplotlib, Seaborn, Plotly, Bokeh, Altair
- **NLP** : Transformers, spaCy, NLTK, LangChain
- **Vision** : OpenCV, Pillow, ImageMagick
- **MLOps** : MLflow, DVC, FastAPI, Streamlit, Gradio
- **Docs** : LaTeX, Pandoc, LibreOffice
- **OCR** : Tesseract (FR/EN), EasyOCR

---

## 📊 Workflows Typiques

### Démarrer le Projet

```bash
# Démarrage complet (construction + lancement)
docker-compose up -d --build

# Démarrage rapide (sans reconstruction)
docker-compose up -d

# Accès Jupyter Lab
# http://localhost:8888
```

### Travailler sur le Cours

```bash
# Modifier un chapitre (éditer le .tex)
# Compiler le PDF
docker exec ml-sandbox bash -c "cd /workspace/cours/XX_chapitre && xelatex -interaction=nonstopmode XX_*.tex"

# Ou compiler tous les PDFs
docker exec ml-sandbox bash /workspace/scripts/compile_all_pdfs.sh

# Vérifier les références
docker exec ml-sandbox bash /workspace/scripts/verify_notebook_refs.sh
```

### Créer un Nouveau Notebook

```bash
# 1. Créer le notebook dans cours/XX_chapitre/
# 2. Le rendre Colab Ready
docker exec ml-sandbox python /workspace/scripts/make_colab_ready.py

# 3. Référencer dans le .tex
# 4. Recompiler le PDF
```

---

## 📝 Conventions et Standards

### Nommage des Fichiers

#### Chapitres du Cours
- **PDFs** : `XX_nom_chapitre.tex` / `.pdf` (XX = numéro 00-14)
- **Notebooks démo** : `XX_demo_nom_descriptif.ipynb`
- **Exercices** : `XX_exercices.ipynb` (solutions intégrées)
- **Quiz** : `XX_quiz.ipynb`

#### Scripts
- **Bash** : `nom_descriptif.sh` (snake_case)
- **Python** : `nom_descriptif.py` (snake_case)

### Fins de Ligne

**Standard** : LF (Unix) pour tous les fichiers texte

Configurer avec `.editorconfig` :
```ini
[*]
end_of_line = lf
insert_final_newline = true
```

### Encodage

**Standard** : UTF-8 pour tous les fichiers

---

## 🔍 Maintenance

### Vérifications Régulières

```bash
# Vérifier les références aux notebooks
bash scripts/verify_notebook_refs.sh

# Vérifier les notebooks Colab Ready
grep -r 'Open In Colab' cours/**/*.ipynb | wc -l
# Devrait retourner 45

# Compiler tous les PDFs
bash scripts/compile_all_pdfs.sh
```

### Archivage

Les fichiers obsolètes ne sont **pas supprimés** mais **archivés** :

- **Scripts obsolètes** → `scripts/archive/`
- **Docs obsolètes** → `docs/archive/`

Cela permet de garder un historique et de pouvoir revenir en arrière si nécessaire.

---

## 📚 Documentation Complète

| Fichier | Contenu |
|---------|---------|
| `README.md` | Vue d'ensemble et démarrage rapide |
| `STRUCTURE.md` | Ce fichier - organisation complète |
| `claude.md` | Historique détaillé des développements |
| `docs/config.md` | Guide d'installation technique |
| `docs/tools.md` | Documentation exhaustive des outils (~2000 lignes) |
| `cours/README.md` | Guide du cours ML |
| `cours/AMELIORATIONS_2026-01-11.md` | Dernières améliorations (Python, Quiz, Colab) |
| `scripts/README.md` | Documentation des scripts utilitaires |

---

## 🎯 Philosophie du Projet

### Organisation

- **Séparation claire** : Contenu (cours/) vs Outils (scripts/) vs Configuration (racine)
- **Documentation exhaustive** : Chaque répertoire a son README.md
- **Standards cohérents** : Nommage, encodage, fins de ligne
- **Archivage** : Pas de suppression, on archive

### Maintenance

- **Scripts automatisés** : Compilation, vérification, transformation
- **Validation continue** : Scripts de vérification pour détecter les erreurs
- **Historique complet** : claude.md documente tous les changements
- **Reproductibilité** : Docker pour environnement identique partout

### Pédagogie

- **Progression logique** : 6 parties, des fondamentaux à la production
- **Accessibilité** : Formation Python intégrée, Colab Ready
- **Validation** : Quiz d'auto-évaluation à chaque chapitre
- **Pratique** : 45+ notebooks de démonstration

---

## 🔗 Liens Rapides

- **GitHub** : [github.com/ogautier1980/sandbox-ml](https://github.com/ogautier1980/sandbox-ml)
- **Jupyter Lab** : [http://localhost:8888](http://localhost:8888)
- **TensorBoard** : [http://localhost:6006](http://localhost:6006)
- **MLflow** : [http://localhost:5000](http://localhost:5000)

---

## 📊 Statistiques Projet

```
📚 Chapitres               : 14 + Annexes
📄 PDFs LaTeX             : 16 (~1.8 MB)
📓 Notebooks (cours)      : 45 (Colab Ready)
📝 Quiz                   : 15 (225 questions)
🔧 Scripts utilitaires    : 4 actifs + 1 archivé
📋 Documentation          : 9 fichiers principaux
🐳 Services Docker        : 3
🎓 Durée cours estimée    : 78-96 heures
```

---

*Dernière mise à jour : 2026-01-11*
