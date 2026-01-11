# Cours Complet de Machine Learning

**Niveau** : Intermédiaire à Avancé
**Prérequis** : Bon niveau scientifique/mathématique/informatique, Python
**Durée estimée** : 70-84 heures (6 parties, 14 chapitres)

---

## 📚 Vue d'Ensemble

Ce cours offre une formation complète en Machine Learning, couvrant :
- Les fondamentaux théoriques (mathématiques, statistiques)
- Les algorithmes classiques (régression, classification, clustering)
- Le Deep Learning (CNN, RNN, Transformers)
- Les paradigmes avancés (Reinforcement Learning, Algorithmes Génétiques)
- Les bonnes pratiques de production (MLOps, déploiement)

Chaque chapitre comprend :
- **PDF théorique** (15-35 pages) - Concepts, mathématiques, algorithmes
- **Notebooks de démonstration** (1-4 par chapitre) - Code commenté et visualisations
- **Exercices pratiques** avec solutions

---

## 📖 Structure du Cours

### Partie 1 : Fondations (3 chapitres, 6-9h)

#### [Chapitre 00 - Introduction au Machine Learning](00_introduction/)
- Définitions et histoire du ML
- Types d'apprentissage (supervisé, non-supervisé, par renforcement)
- Pipeline ML et vocabulaire fondamental
- Applications et éthique

#### [Chapitre 01 - Fondamentaux Mathématiques](01_fondamentaux_mathematiques/)
- Algèbre linéaire (vecteurs, matrices, SVD)
- Statistiques et probabilités (distributions, théorème de Bayes)
- Calcul différentiel (gradient, descente de gradient)

#### [Chapitre 02 - Métriques d'Évaluation](02_metriques_evaluation/)
- Métriques de classification (accuracy, precision, recall, F1, ROC-AUC)
- Métriques de régression (MSE, RMSE, MAE, R²)
- Validation croisée (K-fold, stratified, time series split)

---

### Partie 2 : Machine Learning Classique (3 chapitres, 16-20h)

#### [Chapitre 03 - Régression](03_regression/)
- Régression linéaire (simple, multiple, polynomiale)
- Régularisation (Ridge, Lasso, Elastic Net)
- Diagnostic et analyse des résidus

#### [Chapitre 04 - Classification Supervisée](04_classification_supervisee/)
- Arbres de décision (CART, Random Forest)
- K-Nearest Neighbors (KNN)
- Support Vector Machines (SVM)
- Méthodes d'ensemble (Bagging, Boosting, XGBoost)

#### [Chapitre 05 - Apprentissage Non-Supervisé](05_apprentissage_non_supervise/)
- Clustering (K-means, DBSCAN, hierarchique)
- Réduction de dimensionnalité (PCA, t-SNE, UMAP)
- Détection d'anomalies

---

### Partie 3 : Deep Learning (3 chapitres, 18-22h)

#### [Chapitre 06 - Réseaux de Neurones Fondamentaux](06_reseaux_neurones_fondamentaux/)
- Perceptron et MLP
- Backpropagation (dérivation complète)
- Fonctions d'activation et optimiseurs
- Régularisation (dropout, batch normalization)

#### [Chapitre 07 - Deep Learning - CNN](07_deep_learning_cnn/)
- Convolution 2D et pooling
- Architectures classiques (LeNet, AlexNet, ResNet)
- Transfer learning
- Applications en vision par ordinateur

#### [Chapitre 08 - Deep Learning - RNN et Transformers](08_deep_learning_rnn/)
- RNN, LSTM, GRU
- Attention mechanism
- Transformers (BERT, GPT introduction)
- Applications NLP et séries temporelles

---

### Partie 4 : Paradigmes Alternatifs (2 chapitres, 8-10h)

#### [Chapitre 09 - Reinforcement Learning](09_reinforcement_learning/)
- MDP et équation de Bellman
- Q-Learning et SARSA
- Deep Q-Network (DQN)
- Policy Gradient et Actor-Critic
- Applications (jeux, robotique)

#### [Chapitre 10 - Algorithmes Génétiques](10_algorithmes_genetiques/)
- Inspiration évolutionnaire
- Sélection, croisement, mutation
- Optimisation de fonctions
- Applications (TSP, hyperparameter tuning)

---

### Partie 5 : Applications Avancées du Deep Learning (3 chapitres, 12-15h)

#### [Chapitre 11 - Séries Temporelles et Forecasting](11_series_temporelles/)
- Stationnarité, décomposition, autocorrélation
- Modèles classiques (ARIMA, SARIMA, Prophet)
- Deep Learning (LSTM, GRU, Attention)
- Métriques et validation temporelles
- Détection d'anomalies

#### [Chapitre 12 - Vision par Ordinateur Avancée](12_vision_avancee/)
- Object Detection (R-CNN, Fast/Faster R-CNN, YOLO)
- Semantic Segmentation (FCN, U-Net, DeepLab)
- Instance Segmentation (Mask R-CNN)
- Vision Transformers (ViT, Swin)
- Vision-Language Models (CLIP)

#### [Chapitre 13 - Systèmes de Recommandation](13_systemes_recommandation/)
- Collaborative Filtering (User-Based, Item-Based, Matrix Factorization)
- Deep Learning (NCF, Autoencoders, Two-Tower Models)
- Content-Based Filtering (TF-IDF, Embeddings)
- Systèmes Hybrides
- Métriques (RMSE, Precision@K, Recall@K, NDCG)
- Problèmes pratiques (Cold Start, Sparsity, Scalability)

---

### Partie 6 : Production et Best Practices (1 chapitre, 6-8h)

#### [Chapitre 14 - MLOps et Déploiement](14_best_practices/)
- Pipeline ML complet (EDA, feature engineering, validation)
- Hyperparameter tuning (GridSearch, Optuna)
- Interprétabilité (SHAP, LIME)
- MLOps (tracking, versioning, monitoring)
- Déploiement (API FastAPI, conteneurisation Docker)
- Scalabilité et production

---

### Annexes

- **Annexe A** : Datasets de référence (30+ datasets annotés)
- **Annexe B** : Ressources supplémentaires (livres, cours, blogs)
- **Annexe C** : Glossaire (150+ termes français/anglais)

---

## 🚀 Démarrage Rapide

### Installation

```bash
# Cloner le repository
git clone https://github.com/ogautier1980/sandbox-ml.git
cd sandbox-ml

# Démarrer l'environnement Docker
docker-compose up -d --build

# Accéder à Jupyter Lab
# http://localhost:8888
```

### Navigation

1. **Lire le PDF théorique** dans chaque chapitre
2. **Exécuter les notebooks de démonstration** dans Jupyter Lab
3. **Faire les exercices** (solutions séparées)
4. **Passer au chapitre suivant**

---

## 📊 Datasets Utilisés

- **Iris** - Classification multi-classe (ch. 00, 04, 05)
- **Diabetes** - Régression (ch. 03)
- **Breast Cancer** - Classification binaire (ch. 04)
- **MNIST** - Vision, chiffres manuscrits (ch. 05, 06, 07)
- **CIFAR-10** - Images couleur (ch. 07)
- **IMDB Reviews** - NLP, sentiment analysis (ch. 08)
- **Frozen Lake / CartPole** - Reinforcement Learning (ch. 09)
- **MovieLens** - Systèmes de recommandation (ch. 14)
- **Kaggle Competitions** - Projets réalistes (ch. 11)

---

## 🛠️ Outils et Librairies

### ML Classique
- **scikit-learn** - Algorithmes, métriques, pipelines
- **NumPy, Pandas** - Manipulation de données
- **Matplotlib, Seaborn, Plotly** - Visualisation

### Deep Learning
- **PyTorch** - Framework principal
- **torchvision** - Vision par ordinateur
- **Hugging Face Transformers** - NLP

### MLOps
- **MLflow** - Tracking expériences
- **Optuna** - Hyperparameter tuning
- **SHAP** - Interprétabilité
- **FastAPI, Streamlit** - Déploiement

---

## 📈 Progression Recommandée

### Débutant → Intermédiaire
Chapitres **00 → 05** (fondations + ML classique)

### Intermédiaire → Avancé
Chapitres **06 → 08** (Deep Learning)

### Avancé → Expert
Chapitres **09 → 11** (RL, GA, production)

---

## 🎯 Objectifs d'Apprentissage

À la fin de ce cours, vous serez capable de :

✅ Comprendre les fondements mathématiques du ML
✅ Choisir et implémenter l'algorithme adapté à un problème
✅ Évaluer rigoureusement les performances d'un modèle
✅ Construire des réseaux de neurones profonds (CNN, RNN, Transformers)
✅ Appliquer le Reinforcement Learning à des problèmes de décision
✅ Déployer des modèles en production avec MLOps
✅ Interpréter et expliquer les prédictions d'un modèle

---

## 🔗 Références Principales

- **Documentation officielle** : [scikit-learn](https://scikit-learn.org/), [PyTorch](https://pytorch.org/)
- **Livres** : Hands-On ML (Géron), Deep Learning Book (Goodfellow)
- **Cours** : Stanford CS229, fast.ai, Coursera ML Specialization

---

## 👥 Public Cible

Ce cours s'adresse à :
- Étudiants en Master/Ingénierie (informatique, mathématiques, physique)
- Data Scientists souhaitant approfondir leurs connaissances
- Développeurs voulant se spécialiser en ML/IA
- Chercheurs nécessitant des bases solides en apprentissage automatique

**Prérequis techniques** :
- Python (NumPy, Pandas)
- Mathématiques (algèbre linéaire, probabilités, dérivées)
- Statistiques de base

---

## 📝 Licence

Ce cours est destiné à un usage éducatif.

---

## 🤝 Contribution

Pour toute suggestion ou correction :
- Ouvrir une issue sur [GitHub](https://github.com/ogautier1980/sandbox-ml/issues)
- Proposer une pull request

---

**Bonne formation ! 🚀**
