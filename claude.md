# CLAUDE.md - Projet Sandbox-ML

**Mémoire permanente pour les sessions Claude**

| Info | Valeur |
|------|--------|
| Repository | [github.com/ogautier1980/sandbox-ml](https://github.com/ogautier1980/sandbox-ml) |
| Version | 0.2 |
| Mise à jour | 2026-01-11 |

---

## Structure du Projet

```
sandbox-ml/
├── Dockerfile              # Image Python 3.11 + ML + outils
├── docker-compose.yml      # Services (Jupyter, TensorBoard, MLflow)
├── requirements.txt        # ~100 packages Python
├── README.md               # Documentation rapide
├── claude.md               # Ce fichier
├── .gitignore
├── .vscode/                # Config VS Code
├── .devcontainer/          # Dev Container
├── docs/                   # Documentation complète
│   ├── config.md           # Guide d'installation
│   ├── tools.md            # Guide des outils (~2000 lignes)
│   ├── guide-ml-sandbox.tex  # Source LaTeX du guide PDF
│   ├── guide-ml-sandbox.pdf  # Guide complet (config + tools)
│   ├── build-pdf.bat/sh   # Scripts de compilation PDF
│   ├── start.bat
│   └── start.sh
├── notebooks/              # Notebooks Jupyter (monté dans container)
├── data/                   # Données (monté dans container)
├── models/                 # Modèles ML (monté dans container)
├── src/                    # Code source (monté dans container)
└── TPs/                    # Travaux pratiques ML (monté dans container)
```

---

## Container Docker

| Composant | Contenu |
|-----------|---------|
| **Base** | Python 3.11-slim |
| **ML/DL** | PyTorch, TensorFlow, scikit-learn, XGBoost, LightGBM, CatBoost |
| **Data** | NumPy, Pandas, Polars, SciPy, PyArrow |
| **Viz** | Matplotlib, Seaborn, Plotly, Bokeh, Altair |
| **NLP** | Transformers, spaCy, NLTK, LangChain |
| **Docs** | LaTeX, Pandoc, pypdf, python-docx, LibreOffice |
| **OCR** | Tesseract (FR/EN), pytesseract, EasyOCR |
| **Media** | OpenCV, Pillow, ImageMagick, FFmpeg, sox |
| **Web** | FastAPI, Flask, Streamlit, Gradio |

### Ports

| Port | Service |
|------|---------|
| 8888 | Jupyter Lab |
| 6006 | TensorBoard |
| 5000 | MLflow |

---

## Règles de Maintenance

### Interdictions
- Fichiers temporaires à la racine → utiliser `/tmp/`
- Duplication de documentation
- Plus de 6 fichiers à la racine (hors dotfiles)

### Bonnes Pratiques
- Documentation complète → `docs/`
- Notebooks et code → `TPs/`, `notebooks/`, `src/`
- Mettre à jour ce fichier après chaque session

---

## Commandes Utiles

```bash
# Démarrage (construction + lancement)
docker-compose up -d --build

# Démarrage rapide (sans reconstruction)
docker-compose up -d

# Shell interactif
docker exec -it ml-sandbox bash

# Reconstruire complètement
docker-compose build --no-cache && docker-compose up -d

# Arrêter les containers
docker-compose down

# Compiler le PDF depuis le container
docker exec ml-sandbox bash -c "cd /workspace/docs && xelatex -interaction=nonstopmode guide-ml-sandbox.tex && xelatex -interaction=nonstopmode guide-ml-sandbox.tex"

# Voir les logs
docker-compose logs -f ml-sandbox

# Accès Jupyter Lab
# http://localhost:8888
```

---

## Points Techniques Importants

### Docker
- **Image base** : `python:3.11-slim` (Debian Trixie)
- **Correction importante** : Utiliser `libgl1` au lieu de `libgl1-mesa-glx` (obsolète dans Trixie)
- **Volumes montés** : docs/, TPs/, notebooks/, data/, models/, src/
- **Polices LaTeX** : Installer `lmodern` et `texlive-fonts-extra` pour compilation PDF

### Génération PDF
- Utiliser `xelatex` (2 passes) au lieu de `latexmk` pour compatibilité
- Commande complète : `xelatex -interaction=nonstopmode file.tex` (x2)
- Le PDF généré fait ~110 KB pour 18 pages

---

## Historique

### 2026-01-11 - Finalisation et génération PDF
- Correction Dockerfile : `libgl1-mesa-glx` → `libgl1`
- Ajout volumes docs/ et TPs/ dans docker-compose.yml
- Installation polices LaTeX supplémentaires dans container
- Génération réussie du guide PDF (guide-ml-sandbox.pdf)
- Amélioration de claude.md avec infos techniques

### 2026-01-10 - Création et configuration initiale
- Structure Docker complète pour ML
- ~100 packages Python configurés
- Outils système : LaTeX, LibreOffice, Tesseract OCR, FFmpeg, ImageMagick
- Documentation : config.md, tools.md, guide LaTeX
- Configuration VS Code + Dev Container
- Réorganisation : documentation déplacée vers `docs/`
