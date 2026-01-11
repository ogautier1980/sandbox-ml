# Cours de Cryptographie - Niveau Universitaire

Cours complet de cryptographie basé sur [The Joy of Cryptography](https://toc.cryptobook.us/) de Mike Rosulek.

## 📚 Structure du Cours

### Partie 1 - Cryptographie à Clé Secrète

| Chapitre | Titre | Contenu | Durée |
|----------|-------|---------|-------|
| **01** | Introduction & Perfect Security | Notions fondamentales, chiffres, sécurité parfaite (One-Time Pad), définitions formelles | 6-8h |
| **02** | Chiffrements Symétriques | Stream ciphers, block ciphers (DES, AES), modes opératoires, CPA-Security | 8-10h |
| **03** | Intégrité des Messages | MAC, fonctions de hachage résistantes aux collisions, HMAC, authenticated encryption (AES-GCM) | 6-8h |

### Partie 2 - Cryptographie à Clé Publique

| Chapitre | Titre | Contenu | Durée |
|----------|-------|---------|-------|
| **04** | Cryptographie Asymétrique | Fonctions à sens unique, Diffie-Hellman, chiffrement à clé publique, ElGamal, RSA | 8-10h |
| **05** | Communication Anonyme | Protocoles d'anonymat, mixnets, Tor, communication privée | 4-6h |

**Durée totale** : 32-42 heures

---

## 📖 Contenu Détaillé

### Chapitre 1 : Introduction & Perfect Security (6-8h)

**Théorie** :
- Notions fondamentales : plaintext, ciphertext, key space
- Principes de Kerckhoffs
- Perfect Security (Shannon)
- One-Time Pad : preuve de sécurité parfaite
- Limitations : taille des clés, impossibilité de réutilisation

**Notebooks** :
- `01_demo_otp.ipynb` - Implémentation One-Time Pad
- `01_demo_xor_properties.ipynb` - Propriétés du XOR
- `01_exercices.ipynb` - Exercices sur perfect security

**Références** : Cryptobook Chapters 1-2

---

### Chapitre 2 : Chiffrements Symétriques (8-10h)

**Théorie** :
- Computational Security vs Perfect Security
- Pseudorandom Generators (PRG)
- Stream Ciphers : construction à partir de PRG
- Block Ciphers : abstraction, permutations pseudoaléatoires
- DES, Triple-DES, AES (structure, rounds)
- Modes opératoires : ECB, CBC, CTR, OFB
- Semantic Security
- CPA (Chosen Plaintext Attack) Security
- Preuves de sécurité

**Notebooks** :
- `02_demo_stream_cipher.ipynb` - Stream cipher avec ChaCha20
- `02_demo_aes_modes.ipynb` - Modes AES (ECB vs CBC vs CTR)
- `02_demo_cpa_attack.ipynb` - Démonstration attaque CPA sur ECB
- `02_exercices.ipynb` - Exercices block ciphers

**Références** : Cryptobook Chapters 3-6

---

### Chapitre 3 : Intégrité des Messages (6-8h)

**Théorie** :
- Message Authentication Codes (MAC)
- Définitions de sécurité pour MAC
- Collision-Resistant Hash Functions
- Constructions : CBC-MAC, HMAC
- Paradoxe des anniversaires
- Merkle-Damgård construction
- SHA-2, SHA-3
- Authenticated Encryption with Associated Data (AEAD)
- Encrypt-then-MAC, MAC-then-Encrypt
- AES-GCM, ChaCha20-Poly1305

**Notebooks** :
- `03_demo_mac.ipynb` - HMAC-SHA256
- `03_demo_hash_collisions.ipynb` - Paradoxe des anniversaires
- `03_demo_aead.ipynb` - AES-GCM authenticated encryption
- `03_exercices.ipynb` - Exercices MAC et hachage

**Références** : Cryptobook Chapters 11-12

---

### Chapitre 4 : Cryptographie Asymétrique (8-10h)

**Théorie** :
- Fonctions à sens unique avec trappe (trapdoor)
- Groupes cycliques, logarithme discret
- Diffie-Hellman Key Exchange
- Preuve de sécurité passive
- Attaque Man-in-the-Middle
- Public Key Encryption : définitions
- Sécurité CPA pour chiffrement asymétrique
- Chiffrement ElGamal
- RSA : construction, padding (OAEP)
- Signatures numériques : définitions
- DSA, RSA signatures, EdDSA

**Notebooks** :
- `04_demo_diffie_hellman.ipynb` - Échange de clés DH
- `04_demo_elgamal.ipynb` - Chiffrement ElGamal
- `04_demo_rsa.ipynb` - RSA (chiffrement + signatures)
- `04_demo_ecdsa.ipynb` - Courbes elliptiques et ECDSA
- `04_exercices.ipynb` - Exercices cryptographie asymétrique

**Références** : Cryptobook Chapters 13-15

---

### Chapitre 5 : Communication Anonyme (4-6h)

**Théorie** :
- Définitions d'anonymat
- Mixnets : Chaum's mix
- Onion Routing
- Architecture Tor
- Traffic analysis
- Metadata protection
- Anonymous credentials
- Private Information Retrieval (PIR)

**Notebooks** :
- `05_demo_onion_routing.ipynb` - Simulation onion routing
- `05_demo_mixnet.ipynb` - Implémentation d'un mixnet simple
- `05_exercices.ipynb` - Exercices sur l'anonymat

**Références** : Cryptobook Chapter 10 + Papers on Tor

---

## 🎯 Objectifs Pédagogiques

À la fin du cours, les étudiants seront capables de :

1. **Comprendre les fondements théoriques** : Définitions formelles de sécurité, preuves de sécurité
2. **Distinguer les primitives** : Quand utiliser chiffrement symétrique vs asymétrique, MAC vs signatures
3. **Analyser des protocoles** : Identifier les vulnérabilités, comprendre les attaques
4. **Implémenter correctement** : Utiliser les bibliothèques crypto sans erreurs communes
5. **Concevoir des systèmes sécurisés** : Combiner primitives pour des applications réelles

---

## 📋 Prérequis

- **Mathématiques** : Algèbre linéaire, probabilités de base, arithmétique modulaire
- **Programmation** : Python niveau intermédiaire
- **Théorie** : Notions de complexité algorithmique (P, NP)

---

## 🔧 Installation

Le cours utilise l'environnement Docker du projet sandbox-ml :

```bash
# Démarrer l'environnement
docker-compose up -d

# Accéder à Jupyter
http://localhost:8888

# Bibliothèques Python utilisées
- cryptography (PyCA)
- pycryptodome
- hashlib, hmac (stdlib)
- sympy (math)
```

---

## 📚 Ressources

- **Livre principal** : [The Joy of Cryptography](https://toc.cryptobook.us/) - Mike Rosulek (2021)
- **Références complémentaires** :
  - *Introduction to Modern Cryptography* - Katz & Lindell
  - *Cryptography Engineering* - Ferguson, Schneier, Kohno
  - *Applied Cryptography* - Bruce Schneier
- **Cours en ligne** :
  - Cryptography I & II (Dan Boneh, Stanford/Coursera)
  - Applied Cryptography (Udacity)

---

## ⚠️ Avertissements Importants

**NE JAMAIS** en production :
- Implémenter sa propre cryptographie
- Réutiliser des nonces/IV
- Utiliser ECB mode
- Chiffrer sans authentification
- Utiliser MD5, SHA-1, DES, RC4

**TOUJOURS** :
- Utiliser des bibliothèques auditées (OpenSSL, libsodium, PyCA/cryptography)
- Suivre les recommandations NIST, ANSSI
- Authentifier avant de déchiffrer
- Utiliser des générateurs aléatoires cryptographiques (os.urandom, secrets)
- Appliquer le principe du moindre privilège

---

## 📝 Évaluation

Chaque chapitre contient :
- **Exercices théoriques** : Preuves, analyse de sécurité
- **Exercices pratiques** : Implémentations, attaques simulées
- **Projets** :
  - Projet 1 : Implémentation d'un chat chiffré (AES-GCM)
  - Projet 2 : Attaque padding oracle sur CBC
  - Projet 3 : Protocole d'échange de clés authentifié
  - Projet final : Mini-application avec cryptographie complète

---

## 🏗️ Structure des Fichiers

```
cours-crypto/
├── README.md                           # Ce fichier
├── 01_introduction/
│   ├── 01_introduction.tex            # Théorie LaTeX
│   ├── 01_introduction.pdf            # PDF compilé
│   ├── 01_demo_otp.ipynb             # One-Time Pad
│   ├── 01_demo_xor_properties.ipynb  # XOR
│   └── 01_exercices.ipynb            # Exercices
├── 02_symmetric_crypto/
│   ├── 02_symmetric_crypto.tex
│   ├── 02_symmetric_crypto.pdf
│   ├── 02_demo_stream_cipher.ipynb
│   ├── 02_demo_aes_modes.ipynb
│   ├── 02_demo_cpa_attack.ipynb
│   └── 02_exercices.ipynb
├── 03_message_integrity/
│   ├── 03_message_integrity.tex
│   ├── 03_message_integrity.pdf
│   ├── 03_demo_mac.ipynb
│   ├── 03_demo_hash_collisions.ipynb
│   ├── 03_demo_aead.ipynb
│   └── 03_exercices.ipynb
├── 04_public_key_crypto/
│   ├── 04_public_key_crypto.tex
│   ├── 04_public_key_crypto.pdf
│   ├── 04_demo_diffie_hellman.ipynb
│   ├── 04_demo_elgamal.ipynb
│   ├── 04_demo_rsa.ipynb
│   ├── 04_demo_ecdsa.ipynb
│   └── 04_exercices.ipynb
└── 05_anonymous_communication/
    ├── 05_anonymous_communication.tex
    ├── 05_anonymous_communication.pdf
    ├── 05_demo_onion_routing.ipynb
    ├── 05_demo_mixnet.ipynb
    └── 05_exercices.ipynb
```

---

*Dernière mise à jour : 2026-01-11*
