# Image de base Python avec CUDA support (optionnel)
FROM python:3.11-slim

# Métadonnées
LABEL maintainer="ML Sandbox"
LABEL description="Container Docker pour le Machine Learning en Python"

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1
ENV DEBIAN_FRONTEND=noninteractive

# Répertoire de travail
WORKDIR /workspace

# Installation des dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Build tools
    build-essential \
    cmake \
    pkg-config \
    # Utilitaires de base
    curl \
    wget \
    git \
    vim \
    nano \
    htop \
    tree \
    # Compression / Archives
    zip \
    unzip \
    p7zip-full \
    tar \
    gzip \
    bzip2 \
    xz-utils \
    # LaTeX (pour génération PDF, rapports)
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-lang-french \
    latexmk \
    pandoc \
    # Traitement d'images
    imagemagick \
    graphviz \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    # PDF tools
    poppler-utils \
    ghostscript \
    # Fonts
    fonts-liberation \
    fonts-dejavu \
    # SSH/SCP (pour transferts)
    openssh-client \
    rsync \
    # OCR (reconnaissance de texte)
    tesseract-ocr \
    tesseract-ocr-fra \
    tesseract-ocr-eng \
    # LibreOffice (conversion documents)
    libreoffice-writer \
    libreoffice-calc \
    libreoffice-impress \
    libreoffice-common \
    # Comparaison de fichiers
    wdiff \
    diffutils \
    # Audio (pour transcriptions)
    sox \
    libsox-fmt-all \
    # Autres utilitaires
    jq \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/* \
    # Configurer ImageMagick pour autoriser la conversion PDF
    && sed -i 's/rights="none" pattern="PDF"/rights="read|write" pattern="PDF"/' /etc/ImageMagick-6/policy.xml || true

# Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Exposition des ports
EXPOSE 8888 6006 5000

# Commande par défaut : Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
