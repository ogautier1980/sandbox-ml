# Cours de Sécurité Informatique - Niveau Universitaire

![Completion](https://img.shields.io/badge/Completion-0%25-red)
![Notebooks](https://img.shields.io/badge/Notebooks-0%2F20-blue)
![PDFs](https://img.shields.io/badge/PDFs-0%2F5-blue)
![LaTeX](https://img.shields.io/badge/LaTeX-XeLaTeX-orange)

Cours complet de sécurité informatique couvrant la cryptographie, les protocoles d'authentification, la sécurité réseau, le machine learning en sécurité, et la sécurité logicielle.

**Statut** : 🚧 **En construction** (Structure créée)

---

## 🎯 Objectifs du Cours

À la fin de ce cours, les étudiants seront capables de :

1. **Comprendre l'émergence de la cryptographie moderne**
   - Évolution des chiffres classiques aux systèmes modernes
   - Passage de la sécurité parfaite à la sécurité computationnelle

2. **Construire et attaquer des protocoles d'authentification**
   - Conception de protocoles sécurisés
   - Cryptanalyse de protocoles basés sur mots de passe
   - Attaques pratiques (dictionary, brute-force, rainbow tables)

3. **Maîtriser les concepts de sécurité réseau**
   - DoS et défense contre DDoS
   - Analyse critique des firewalls et IDS/IPS
   - Misconceptions courantes dans l'industrie

4. **Utiliser le Machine Learning en contexte sécuritaire**
   - Applications du ML en cybersécurité
   - Adversarial Machine Learning
   - Ce qui peut mal tourner

5. **Exploiter les vulnérabilités logicielles**
   - Comprendre les problèmes de memory safety
   - Exploitation de buffer overflow sur systèmes 32 bits
   - Stack-based vulnerabilities

---

## 📚 Structure du Cours

### Partie 1 - Cryptographie à Clé Secrète (Fondations)

| Chapitre | Titre | Contenu | Durée |
|----------|-------|---------|-------|
| **01** | Introduction & Perfect Security | Notions fondamentales, One-Time Pad, théorème de Shannon | 4-6h |
| **02** | Computational Ciphers | Stream ciphers, block ciphers (AES), modes opératoires, CPA-Security | 6-8h |
| **03** | Collision-Resistant Hashing | Fonctions de hachage, MAC, HMAC, authenticated encryption (AEAD) | 4-6h |

**Durée Partie 1** : 14-20 heures

---

### Partie 2 - Protocoles d'Authentification

| Chapitre | Titre | Contenu | Durée |
|----------|-------|---------|-------|
| **04** | Building Authentication Protocols | Challenge-response, zero-knowledge proofs, Diffie-Hellman authentifié | 6-8h |
| **05** | Password-Based Protocols | PAKE, SRP, cryptanalyse de mots de passe, rainbow tables, salting | 6-8h |

**Durée Partie 2** : 12-16 heures

---

### Partie 3 - Sécurité Réseau

| Chapitre | Titre | Contenu | Durée |
|----------|-------|---------|-------|
| **06** | DoS & DDoS Attacks | Amplification, reflection, botnet, défenses (rate limiting, CDN) | 4-6h |
| **07** | Firewalls & IDS/IPS | Architectures, limitations, bypass techniques, analyse critique | 4-6h |

**Durée Partie 3** : 8-12 heures

---

### Partie 4 - Machine Learning & Security

| Chapitre | Titre | Contenu | Durée |
|----------|-------|---------|-------|
| **08** | ML for Security | Détection d'intrusion, analyse de malware, spam filtering, anomaly detection | 6-8h |
| **09** | Adversarial ML | Adversarial examples, model poisoning, evasion attacks, defenses | 6-8h |

**Durée Partie 4** : 12-16 heures

---

### Partie 5 - Sécurité Logicielle

| Chapitre | Titre | Contenu | Durée |
|----------|-------|---------|-------|
| **10** | Memory Safety Issues | Stack layout, buffer overflow, stack canaries, ASLR, NX bit | 8-10h |
| **11** | Exploitation (32-bit) | Stack smashing, shellcode, ROP, exploitation pratique sur x86 | 10-12h |

**Durée Partie 5** : 18-22 heures

---

**Durée totale** : 64-86 heures (cours complet intensif)

---

## 📖 Contenu Détaillé

### Chapitre 1 : Introduction & Perfect Security (4-6h)

**Théorie** :
- Évolution historique : César, Vigenère, Enigma, One-Time Pad
- Principes de Kerckhoffs
- Perfect Security (définition de Shannon)
- Preuve de sécurité parfaite de OTP
- Limitations pratiques (taille des clés, gestion)

**Notebooks** :
- `01_demo_otp.ipynb` - Implémentation One-Time Pad
- `01_histoire_crypto.ipynb` - Évolution des chiffres classiques
- `01_exercices.ipynb` - Exercices perfect security

**Références** : Serious Cryptography (Ch 1-2), Joy of Cryptography (Ch 1-2)

---

### Chapitre 2 : Computational Ciphers (6-8h)

**Théorie** :
- Computational Security vs Perfect Security
- Stream Ciphers : PRG, ChaCha20, nonce management
- Block Ciphers : AES (structure, rounds, modes)
- Modes opératoires : ECB (insecure), CBC, CTR, GCM
- CPA-Security

**Notebooks** :
- `02_demo_stream_cipher.ipynb` - ChaCha20
- `02_demo_aes_modes.ipynb` - Comparaison modes AES
- `02_demo_cpa_attack.ipynb` - Attaque CPA sur ECB
- `02_exercices.ipynb` - Exercices pratiques

**Références** : Serious Cryptography (Ch 3-5), Joy of Cryptography (Ch 3-6)

---

### Chapitre 3 : Collision-Resistant Hashing (4-6h)

**Théorie** :
- Propriétés des fonctions de hachage
- Paradoxe des anniversaires (birthday attack)
- SHA-2, SHA-3 (Keccak)
- MAC : HMAC-SHA256, CBC-MAC
- Authenticated Encryption (AES-GCM, ChaCha20-Poly1305)

**Notebooks** :
- `03_demo_hash_collisions.ipynb` - Birthday attack
- `03_demo_mac.ipynb` - HMAC
- `03_demo_aead.ipynb` - AES-GCM, malléabilité
- `03_exercices.ipynb` - Exercices

**Références** : Serious Cryptography (Ch 6-7), Joy of Cryptography (Ch 11-12)

---

### Chapitre 4 : Building Authentication Protocols (6-8h)

**Théorie** :
- Authentification vs identification
- Challenge-Response protocols
- Mutual authentication
- Diffie-Hellman authentifié (Authenticated Key Exchange)
- Man-in-the-Middle attacks
- Zero-Knowledge Proofs (introduction)
- Timestamps vs nonces

**Notebooks** :
- `04_demo_challenge_response.ipynb` - Protocole simple
- `04_demo_mitm.ipynb` - Attaque Man-in-the-Middle
- `04_demo_authenticated_dh.ipynb` - DH avec authentification
- `04_exercices.ipynb` - Construction de protocoles

**Références** : Boneh & Shoup (Ch 21), Katz & Lindell (Ch 10-11)

---

### Chapitre 5 : Password-Based Protocols (6-8h)

**Théorie** :
- Password storage : hashing vs encryption
- Salting et pepper
- Key derivation functions (PBKDF2, Argon2, bcrypt, scrypt)
- PAKE (Password Authenticated Key Exchange)
- SRP (Secure Remote Password)
- Cryptanalyse :
  - Dictionary attacks
  - Brute-force attacks
  - Rainbow tables
  - GPU cracking (hashcat)

**Notebooks** :
- `05_demo_password_hashing.ipynb` - bcrypt, Argon2
- `05_demo_rainbow_tables.ipynb` - Génération et utilisation
- `05_demo_hashcat.ipynb` - GPU password cracking
- `05_demo_pake.ipynb` - Implémentation PAKE simple
- `05_exercices.ipynb` - Exercices cryptanalyse

**Références** : Serious Cryptography (Ch 14), articles sur PAKE/SRP

---

### Chapitre 6 : DoS & DDoS Attacks (4-6h)

**Théorie** :
- Types de DoS :
  - Bandwidth exhaustion
  - Resource exhaustion
  - Application-layer attacks
- Techniques DDoS :
  - Amplification attacks (DNS, NTP, memcached)
  - Reflection attacks
  - Botnets (Mirai, etc.)
- Défenses :
  - Rate limiting
  - Traffic filtering (BCP38)
  - CDN (Cloudflare, Akamai)
  - Scrubbing centers
  - Anycast

**Notebooks** :
- `06_demo_syn_flood.ipynb` - Simulation SYN flood
- `06_demo_dns_amplification.ipynb` - Calcul facteur amplification
- `06_demo_rate_limiting.ipynb` - Implémentation token bucket
- `06_exercices.ipynb` - Analyse de traces DDoS

**Références** : Articles académiques, rapports d'incidents (Cloudflare, Arbor Networks)

---

### Chapitre 7 : Firewalls & IDS/IPS (4-6h)

**Théorie** :
- Types de firewalls :
  - Packet filtering
  - Stateful inspection
  - Application-layer (proxy)
  - Next-Generation Firewalls (NGFW)
- IDS vs IPS :
  - Signature-based
  - Anomaly-based
  - Limitations
- Bypass techniques :
  - Fragmentation
  - Tunneling
  - Polymorphic malware
- **Misconceptions courantes** :
  - "Firewall = sécurité totale"
  - "IPS bloque tout"
  - Defense in depth necessity

**Notebooks** :
- `07_demo_firewall_rules.ipynb` - iptables, nftables
- `07_demo_snort.ipynb` - IDS Snort, règles personnalisées
- `07_demo_evasion.ipynb` - Techniques d'évasion
- `07_exercices.ipynb` - Configuration et analyse

**Références** : Documentation Snort, Suricata, articles industriels

---

### Chapitre 8 : ML for Security (6-8h)

**Théorie** :
- Applications :
  - Spam filtering (Naive Bayes, SVM)
  - Malware detection (Random Forest, CNN)
  - Intrusion detection (anomaly detection)
  - Phishing detection
  - Network traffic analysis
- Feature engineering pour sécurité
- Problèmes :
  - Imbalanced datasets
  - Concept drift
  - False positives vs false negatives

**Notebooks** :
- `08_demo_spam_filter.ipynb` - Classification emails
- `08_demo_malware_detection.ipynb` - PE headers, opcode sequences
- `08_demo_anomaly_detection.ipynb` - Isolation Forest, One-Class SVM
- `08_demo_phishing.ipynb` - URL feature extraction
- `08_exercices.ipynb` - Projets pratiques

**Références** : Articles de recherche, datasets (KDD Cup, CICIDS)

---

### Chapitre 9 : Adversarial ML (6-8h)

**Théorie** :
- Adversarial examples :
  - FGSM, PGD, C&W attacks
  - Transferability
  - Black-box vs white-box
- Model poisoning :
  - Data poisoning
  - Backdoor attacks
- Evasion attacks :
  - Malware mutation
  - Adversarial perturbations
- Defenses :
  - Adversarial training
  - Defensive distillation
  - Detection methods
  - Certified robustness

**Notebooks** :
- `09_demo_fgsm.ipynb` - Fast Gradient Sign Method
- `09_demo_pgd.ipynb` - Projected Gradient Descent
- `09_demo_poisoning.ipynb` - Data poisoning attack
- `09_demo_defenses.ipynb` - Adversarial training
- `09_exercices.ipynb` - Robustness evaluation

**Références** : Articles fondamentaux (Goodfellow, Carlini & Wagner, Madry)

---

### Chapitre 10 : Memory Safety Issues (8-10h)

**Théorie** :
- Memory layout :
  - Stack (frames, saved registers, return address)
  - Heap
  - Data segments (.data, .bss)
  - Code segment (.text)
- Buffer overflow :
  - Stack-based
  - Heap-based
  - Off-by-one errors
- Défenses :
  - Stack canaries (SSP)
  - ASLR (Address Space Layout Randomization)
  - DEP/NX (Data Execution Prevention)
  - RELRO
  - PIE (Position Independent Executable)

**Notebooks** :
- `10_demo_stack_layout.ipynb` - Visualisation stack frames
- `10_demo_buffer_overflow.ipynb` - Overflow simple (sandbox)
- `10_demo_canaries.ipynb` - Bypass stack canaries
- `10_demo_aslr.ipynb` - Information leaks
- `10_exercices.ipynb` - Analyse de vulnérabilités

**Références** : Smashing The Stack For Fun And Profit (Aleph One), modern exploit papers

---

### Chapitre 11 : Exploitation (32-bit) (10-12h)

**Théorie** :
- x86 assembly basics (AT&T vs Intel syntax)
- Stack smashing :
  - Overwriting return address
  - Shellcode injection
  - NOP sleds
- Return-Oriented Programming (ROP) :
  - Gadgets
  - ROP chains
  - Bypassing DEP
- Exploitation pratique :
  - Tools (gdb, pwntools, ROPgadget)
  - Techniques de debugging
  - Exploit development process
- Format string vulnerabilities
- Integer overflow

**Notebooks** :
- `11_demo_shellcode.ipynb` - Écriture de shellcode x86
- `11_demo_stack_smashing.ipynb` - Exploitation simple
- `11_demo_rop.ipynb` - ROP chain construction
- `11_demo_format_string.ipynb` - Format string exploitation
- `11_exercices.ipynb` - Challenges CTF-style

**Références** : Hacking: The Art of Exploitation, Modern Binary Exploitation (RPISEC)

---

## 🎯 Objectifs Pédagogiques par Partie

### Partie 1 : Cryptographie
- Comprendre la transition perfect → computational security
- Maîtriser les primitives modernes (AES-GCM, ChaCha20-Poly1305)
- Analyser la sécurité de constructions cryptographiques

### Partie 2 : Authentification
- Concevoir des protocoles sécurisés
- Identifier et exploiter les faiblesses
- Comprendre la cryptanalyse de mots de passe

### Partie 3 : Réseau
- Analyser et mitiger les attaques DoS/DDoS
- Évaluer critiquement les solutions de sécurité réseau
- Comprendre les limitations des firewalls/IDS

### Partie 4 : ML & Sécurité
- Appliquer le ML aux problèmes de cybersécurité
- Comprendre les risques de l'adversarial ML
- Développer des modèles robustes

### Partie 5 : Software Security
- Identifier les vulnérabilités de memory safety
- Exploiter des buffer overflows (environnement contrôlé)
- Comprendre les mécanismes de défense modernes

---

## 📋 Prérequis

- **Mathématiques** : Algèbre de base, probabilités élémentaires
- **Programmation** : Python (niveau intermédiaire), notions de C
- **Systèmes** : Compréhension basique de Linux, ligne de commande
- **Réseaux** : Modèle OSI/TCP-IP, protocoles courants (HTTP, DNS, etc.)
- **Optionnel** : Assembly x86 (pour Partie 5)

---

## 🚀 Démarrage Rapide

### Option 1 : Docker (Recommandé)

Le cours utilise l'environnement Docker du projet sandbox-ml avec extensions sécurité :

```bash
# Démarrer l'environnement
docker-compose up -d

# Accéder à Jupyter Lab
http://localhost:8888

# Compiler les PDFs (quand disponibles)
docker exec ml-sandbox bash /workspace/scripts/compile_security_pdfs.sh
```

### Option 2 : Google Colab

Les notebooks seront compatibles Google Colab (sauf exploitation binaire).

### Bibliothèques & Outils Utilisés

**Python** :
- `cryptography` (PyCA) : Primitives cryptographiques
- `hashlib`, `hmac` : Hashing
- `bcrypt`, `argon2` : Password hashing
- `scapy` : Manipulation de paquets réseau
- `scikit-learn`, `tensorflow` : Machine Learning
- `pwntools` : Exploitation binaire

**Outils système** :
- `gdb`, `radare2` : Debugging/reverse engineering
- `nmap`, `wireshark` : Analyse réseau
- `snort`, `suricata` : IDS/IPS
- `hashcat`, `john` : Password cracking

---

## 📚 Ressources

### Livres

**Introduction** :
- **Serious Cryptography** - Jean-Philippe Aumasson (2017)
  - Excellent pour débuter, très pratique
  - Couvre cryptographie moderne avec exemples concrets

**Avancé** :
- **The Joy of Cryptography** - Mike Rosulek (2021)
  - Gratuit : https://joyofcryptography.com/
  - Approche rigoureuse avec preuves formelles

- **A Graduate Course in Applied Cryptography** - Dan Boneh & Victor Shoup
  - Gratuit : https://toc.cryptobook.us/
  - Référence académique complète

- **Introduction to Modern Cryptography** - Katz & Lindell (3rd ed)
  - Complémentaire à Boneh & Shoup
  - Approche formelle et théorique

**Exploitation** :
- **Hacking: The Art of Exploitation** - Jon Erickson (2nd ed)
- **The Shellcoder's Handbook** - Koziol et al.
- **Modern Binary Exploitation** - RPISEC (cours gratuit)

**Sécurité Réseau** :
- **Network Security Essentials** - William Stallings
- **Firewalls and Internet Security** - Cheswick, Bellovin, Rubin

### Articles & Papers

- **Adversarial ML** :
  - Goodfellow et al., "Explaining and Harnessing Adversarial Examples" (2014)
  - Carlini & Wagner, "Towards Evaluating the Robustness of Neural Networks" (2017)

- **Exploitation** :
  - Aleph One, "Smashing The Stack For Fun And Profit" (1996)
  - Solar Designer, "Getting around non-executable stack" (1997)

### Cours en Ligne

- **Cryptography I & II** - Dan Boneh (Stanford/Coursera)
- **Software Security** - University of Maryland (Coursera)
- **Computer Security** - UC Berkeley CS161

---

## ⚠️ Avertissements Importants

### Éthique & Légalité

**TOUTES** les techniques d'exploitation enseignées dans ce cours sont à des fins **ÉDUCATIVES UNIQUEMENT**.

**INTERDIT** :
- ❌ Exploiter des systèmes sans autorisation explicite
- ❌ Attaquer des infrastructures (DoS/DDoS)
- ❌ Craquer des mots de passe de comptes réels
- ❌ Déployer du malware
- ❌ Violer des lois sur la cybercriminalité

**AUTORISÉ** :
- ✅ Environnements sandbox (Docker, VM isolées)
- ✅ CTF (Capture The Flag) compétitions
- ✅ Bug bounty programs (avec autorisation)
- ✅ Pentesting avec contrat légal
- ✅ Labs éducatifs (HackTheBox, TryHackMe, etc.)

**Lois applicables** :
- Computer Fraud and Abuse Act (CFAA) - USA
- Computer Misuse Act - UK
- Code pénal (art. 323-1 à 323-7) - France
- Directive NIS2 - UE

---

## 🏗️ Structure des Fichiers

```
cours-securite/
├── README.md                           # Ce fichier
├── 01_perfect_security/
│   ├── 01_introduction.tex            # Théorie LaTeX
│   ├── 01_introduction.pdf            # PDF compilé
│   ├── 01_demo_otp.ipynb
│   ├── 01_histoire_crypto.ipynb
│   └── 01_exercices.ipynb
├── 02_computational_ciphers/
│   ├── 02_computational_ciphers.tex
│   ├── 02_computational_ciphers.pdf
│   ├── 02_demo_stream_cipher.ipynb
│   ├── 02_demo_aes_modes.ipynb
│   ├── 02_demo_cpa_attack.ipynb
│   └── 02_exercices.ipynb
├── 03_hashing/
│   ├── 03_hashing.tex
│   ├── 03_hashing.pdf
│   ├── 03_demo_hash_collisions.ipynb
│   ├── 03_demo_mac.ipynb
│   ├── 03_demo_aead.ipynb
│   └── 03_exercices.ipynb
├── 04_authentication_protocols/
│   ├── 04_authentication.tex
│   ├── 04_authentication.pdf
│   ├── 04_demo_challenge_response.ipynb
│   ├── 04_demo_mitm.ipynb
│   ├── 04_demo_authenticated_dh.ipynb
│   └── 04_exercices.ipynb
├── 05_password_protocols/
│   ├── 05_passwords.tex
│   ├── 05_passwords.pdf
│   ├── 05_demo_password_hashing.ipynb
│   ├── 05_demo_rainbow_tables.ipynb
│   ├── 05_demo_hashcat.ipynb
│   ├── 05_demo_pake.ipynb
│   └── 05_exercices.ipynb
├── 06_dos_ddos/
│   ├── 06_dos_ddos.tex
│   ├── 06_dos_ddos.pdf
│   ├── 06_demo_syn_flood.ipynb
│   ├── 06_demo_dns_amplification.ipynb
│   ├── 06_demo_rate_limiting.ipynb
│   └── 06_exercices.ipynb
├── 07_firewalls_ids/
│   ├── 07_firewalls_ids.tex
│   ├── 07_firewalls_ids.pdf
│   ├── 07_demo_firewall_rules.ipynb
│   ├── 07_demo_snort.ipynb
│   ├── 07_demo_evasion.ipynb
│   └── 07_exercices.ipynb
├── 08_ml_security/
│   ├── 08_ml_security.tex
│   ├── 08_ml_security.pdf
│   ├── 08_demo_spam_filter.ipynb
│   ├── 08_demo_malware_detection.ipynb
│   ├── 08_demo_anomaly_detection.ipynb
│   ├── 08_demo_phishing.ipynb
│   └── 08_exercices.ipynb
├── 09_adversarial_ml/
│   ├── 09_adversarial_ml.tex
│   ├── 09_adversarial_ml.pdf
│   ├── 09_demo_fgsm.ipynb
│   ├── 09_demo_pgd.ipynb
│   ├── 09_demo_poisoning.ipynb
│   ├── 09_demo_defenses.ipynb
│   └── 09_exercices.ipynb
├── 10_memory_safety/
│   ├── 10_memory_safety.tex
│   ├── 10_memory_safety.pdf
│   ├── 10_demo_stack_layout.ipynb
│   ├── 10_demo_buffer_overflow.ipynb
│   ├── 10_demo_canaries.ipynb
│   ├── 10_demo_aslr.ipynb
│   └── 10_exercices.ipynb
└── 11_exploitation/
    ├── 11_exploitation.tex
    ├── 11_exploitation.pdf
    ├── 11_demo_shellcode.ipynb
    ├── 11_demo_stack_smashing.ipynb
    ├── 11_demo_rop.ipynb
    ├── 11_demo_format_string.ipynb
    └── 11_exercices.ipynb
```

---

## 📈 Statut de Complétion

| Composant | Statut | Détails |
|-----------|--------|---------|
| **Notebooks** | 🚧 0% | 0/55 notebooks |
| **LaTeX Chapitre 1** | 🚧 0% | À créer |
| **LaTeX Chapitre 2** | 🚧 0% | À créer |
| **LaTeX Chapitre 3** | 🚧 0% | À créer |
| **LaTeX Chapitre 4** | 🚧 0% | À créer |
| **LaTeX Chapitre 5** | 🚧 0% | À créer |
| **LaTeX Chapitre 6** | 🚧 0% | À créer |
| **LaTeX Chapitre 7** | 🚧 0% | À créer |
| **LaTeX Chapitre 8** | 🚧 0% | À créer |
| **LaTeX Chapitre 9** | 🚧 0% | À créer |
| **LaTeX Chapitre 10** | 🚧 0% | À créer |
| **LaTeX Chapitre 11** | 🚧 0% | À créer |
| **PDFs** | 🚧 0% | 0/11 PDFs |
| **Total** | 🚧 **0%** | **Structure créée** |

---

## 🌟 Points d'Excellence Prévus

1. **Approche Hands-On** : Tous les concepts avec implémentations pratiques
2. **Attaques Réelles** : Démonstrations d'exploits historiques (PS3, Heartbleed, etc.)
3. **Standards Modernes** : Argon2, ChaCha20-Poly1305, TLS 1.3
4. **Analyse Critique** : Discussion des misconceptions industrielles
5. **Éthique** : Emphasis sur responsible disclosure et légalité
6. **CTF Ready** : Exercices style Capture The Flag

---

## 🎓 Évaluation

Chaque chapitre contiendra :
- **Exercices théoriques** : Preuves, analyse de protocoles
- **Labs pratiques** : Implémentations, attaques simulées
- **Projets** :
  - Projet 1 : Protocole d'authentification complet
  - Projet 2 : Système de détection d'intrusion ML
  - Projet 3 : Exploitation CTF challenge
  - Projet final : Audit de sécurité complet (protocole + réseau + code)

---

## 🔗 Liens Utiles

### Platforms d'Entraînement
- **HackTheBox** : https://www.hackthebox.com/
- **TryHackMe** : https://tryhackme.com/
- **picoCTF** : https://picoctf.org/
- **OverTheWire** : https://overthewire.org/wargames/

### Datasets
- **KDD Cup 99** : Intrusion detection
- **CICIDS2017** : Network traffic
- **Malware datasets** : VirusShare, MalShare
- **MNIST Adversarial** : Adversarial ML

### Outils Open Source
- **Metasploit** : Exploitation framework
- **Burp Suite** : Web application testing
- **Ghidra** : Reverse engineering (NSA)
- **Wireshark** : Network protocol analyzer

---

*Dernière mise à jour : 2026-01-12*
*Statut : Structure créée, contenu en cours de développement*
