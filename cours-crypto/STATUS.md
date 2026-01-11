# État d'Avancement : Cours de Cryptographie

**Date** : 2026-01-11
**Statut global** : Structure complète créée, 32% terminé

---

## ✅ Chapitre 1 : Introduction & Perfect Security (100%)

### Fichiers Complétés
- ✅ `01_introduction.tex` - Théorie complète (14 pages LaTeX)
- ✅ `01_demo_otp.ipynb` - Démonstration One-Time Pad
- ✅ `01_exercices.ipynb` - Exercices guidés

### Contenu
- Définitions formelles, principes de Kerckhoffs
- One-Time Pad avec preuve complète
- Théorème de Shannon
- Two-Time Pad attack, projet VENONA

**À faire** : Compiler PDF, compléter exercices

---

## ⚙️ Chapitre 2 : Chiffrements Symétriques (50%)

### Fichiers
- ⚙️ `02_symmetric_crypto.tex` - Squelette LaTeX complet
- ✅ `02_demo_aes_modes.ipynb` - ECB/CBC/CTR (complet)
- ⏳ `02_demo_stream_cipher.ipynb` - À créer
- ⏳ `02_demo_cpa_attack.ipynb` - À créer
- ⏳ `02_exercices.ipynb` - À créer

### À Compléter
**Théorie** : Preuves PRG, détails AES (S-box, GF(2^8), diagrammes TikZ)
**Notebooks** : 3 notebooks manquants

---

## ⚙️ Chapitre 3 : Intégrité des Messages (50%)

### Fichiers
- ⚙️ `03_message_integrity.tex` - Squelette complet
- ✅ `03_demo_aead.ipynb` - AES-GCM/ChaCha20-Poly1305 (complet)
- ⏳ `03_demo_mac.ipynb` - À créer
- ⏳ `03_demo_hash_collisions.ipynb` - À créer
- ⏳ `03_exercices.ipynb` - À créer

### À Compléter
**Théorie** : Merkle-Damgård, padding oracle attack
**Notebooks** : 3 notebooks manquants

---

## ⚙️ Chapitre 4 : Cryptographie à Clé Publique (40%)

### Fichiers
- ⚙️ `04_public_key_crypto.tex` - Squelette complet
- ✅ `04_demo_diffie_hellman.ipynb` - DH et ECDH (complet)
- ⏳ `04_demo_elgamal.ipynb` - À créer
- ⏳ `04_demo_rsa.ipynb` - À créer
- ⏳ `04_demo_ecdsa.ipynb` - À créer
- ⏳ `04_exercices.ipynb` - À créer

### À Compléter
**Théorie** : Preuves ElGamal/RSA-OAEP, courbes elliptiques
**Notebooks** : 4 notebooks manquants

---

## ⏳ Chapitre 5 : Communication Anonyme (30%)

### Fichiers
- ⚙️ `05_anonymous_communication.tex` - Squelette complet
- ⏳ `05_demo_onion_routing.ipynb` - À créer
- ⏳ `05_demo_mixnet.ipynb` - À créer
- ⏳ `05_exercices.ipynb` - À créer

### À Compléter
**Théorie** : Diagrammes Tor, formalisations anonymat
**Notebooks** : 3 notebooks manquants

---

## 📊 Récapitulatif

| Chapitre | LaTeX | Notebooks | %  |
|----------|-------|-----------|-----|
| Ch 1 | ✅ | 2/2 | 100% |
| Ch 2 | ⚙️ | 1/4 | 50% |
| Ch 3 | ⚙️ | 1/4 | 50% |
| Ch 4 | ⚙️ | 1/5 | 40% |
| Ch 5 | ⚙️ | 0/3 | 30% |
| **Total** | **5 fichiers .tex** | **5/18 notebooks** | **54%** |

---

## ⏱️ Estimation Complétion

- **Notebooks manquants** : 13 notebooks → ~10-12h
- **Théorie LaTeX** : Compléter preuves, diagrammes → ~10-12h
- **Compilation PDFs** : xelatex, vérifications → ~2-3h
- **TOTAL** : **~25 heures**

---

## 🚀 Prochaines Étapes

### Priorité 1 : Notebooks Démo
1. Ch 2 : stream cipher, CPA attack
2. Ch 3 : MAC, hash collisions
3. Ch 4 : ElGamal, RSA, ECDSA
4. Ch 5 : onion routing, mixnet

### Priorité 2 : Théorie LaTeX
- Preuves mathématiques complètes
- Diagrammes TikZ (AES, Tor)
- Détails algorithmes

### Priorité 3 : Exercices
- Notebooks d'exercices (5 fichiers)
- Auto-correction comme cours ML

### Priorité 4 : Finalisation
- Compilation tous PDFs
- Tests notebooks
- Intégration Colab Ready

---

*Dernière mise à jour : 2026-01-11*
