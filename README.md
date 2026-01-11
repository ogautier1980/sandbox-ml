# ML Sandbox

Container Docker pour le Machine Learning en Python.

## Démarrage rapide

### Prérequis
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [VS Code](https://code.visualstudio.com/) + extension "Dev Containers"

### Installation

```bash
git clone https://github.com/ogautier1980/sandbox-ml.git
cd sandbox-ml
```

**VS Code (recommandé)** : Ouvrir le dossier → "Reopen in Container"

**Docker Compose** : `docker-compose up -d --build`

### Accès
- **Jupyter Lab** : http://localhost:8888

## Contenu

| Catégorie | Outils |
|-----------|--------|
| ML/DL | PyTorch, TensorFlow, scikit-learn, XGBoost, LightGBM |
| Data | NumPy, Pandas, Polars, SciPy |
| Viz | Matplotlib, Seaborn, Plotly |
| NLP | Transformers, spaCy, LangChain |
| Docs | LaTeX, LibreOffice, Pandoc, OCR (Tesseract) |
| Web | FastAPI, Streamlit, Gradio |

## Documentation

| Document | Description |
|----------|-------------|
| [docs/config.md](docs/config.md) | Guide d'installation détaillé |
| [docs/tools.md](docs/tools.md) | Documentation de tous les outils |
| [docs/guide-ml-sandbox.tex](docs/guide-ml-sandbox.tex) | Source LaTeX du guide PDF |

## Structure

```
sandbox-ml/
├── cours/          # Cours complet ML (14 chapitres + annexes)
├── docs/           # Documentation
├── notebooks/      # Vos notebooks (créé au démarrage)
├── src/            # Code source
├── data/           # Datasets (gitignored)
├── models/         # Modèles (gitignored)
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Commandes utiles

```bash
docker-compose up -d          # Démarrer
docker-compose down           # Arrêter
docker exec -it ml-sandbox bash  # Shell
docker-compose build --no-cache  # Reconstruire
```
