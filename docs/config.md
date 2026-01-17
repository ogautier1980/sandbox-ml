# Guide de Configuration - ML Sandbox

Guide pas à pas pour installer et configurer l'environnement ML Sandbox sur un nouveau PC.

---

## Prérequis

| Logiciel | Téléchargement | Vérification |
|----------|----------------|--------------|
| **Docker Desktop** | [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/) | `docker --version` |
| **VS Code** | [code.visualstudio.com](https://code.visualstudio.com/) | `code --version` |
| **Git** | [git-scm.com](https://git-scm.com/) | `git --version` |

---

## Méthode 1 : VS Code Dev Container (Recommandée)

### Étape 1 : Installer l'extension Dev Containers

1. Ouvrir VS Code
2. Extensions (`Ctrl+Shift+X`) → Rechercher **"Dev Containers"** (Microsoft) → Installer

### Étape 2 : Cloner le repository

```bash
git clone https://github.com/ogautier1980/sandbox-ml.git
cd sandbox-ml
code .
```

### Étape 3 : Ouvrir dans le container

1. VS Code détecte `.devcontainer/devcontainer.json`
2. Cliquer sur **"Reopen in Container"** (notification en bas à droite)
3. Ou : `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"

### Étape 4 : Attendre le build

Premier lancement : **10-20 minutes** (téléchargement image, installation packages)

### Étape 5 : Accéder à Jupyter Lab

→ **http://localhost:8888** (sans mot de passe)

---

## Méthode 2 : Docker Compose

```bash
git clone https://github.com/ogautier1980/sandbox-ml.git
cd sandbox-ml

# Windows
docs\start.bat

# Linux/macOS
chmod +x docs/start.sh && ./docs/start.sh

# Ou directement
docker-compose up -d --build
```

---

## Services disponibles

| Service | Port | URL |
|---------|------|-----|
| Jupyter Lab | 8888 | http://localhost:8888 |
| TensorBoard | 6006 | http://localhost:6006 |
| MLflow | 5000 | http://localhost:5000 |

---

## Commandes utiles

```bash
# Démarrer / Arrêter
docker-compose up -d
docker-compose down

# Logs
docker-compose logs -f ml-sandbox

# Shell dans container
docker exec -it ml-sandbox bash

# Reconstruire
docker-compose build --no-cache && docker-compose up -d

# Services optionnels
docker-compose --profile tensorboard up -d
docker-compose --profile mlflow up -d
```

---

## Vérification de l'installation

```python
import torch, tensorflow as tf, sklearn, pandas as pd, numpy as np
print(f"PyTorch: {torch.__version__}")
print(f"TensorFlow: {tf.__version__}")
print(f"CUDA: {torch.cuda.is_available()}")
```

```bash
tesseract --version
libreoffice --version
pandoc --version
```

---

## Résolution de problèmes

### Mémoire insuffisante
Docker Desktop → Settings → Resources → Memory : **8 GB minimum**

### Port déjà utilisé
Modifier dans `docker-compose.yml` : `"8889:8888"`

### Permissions Linux/macOS
```bash
sudo chown -R $USER:$USER notebooks/ data/ models/ src/
```

---

## Ressources

- [tools.md](tools.md) - Documentation des outils
- [guide-ml-sandbox.pdf](guide-ml-sandbox.pdf) - Guide PDF complet
