# Résumé de Révision - Sécurité Informatique

**Cours de Sécurité Informatique - Niveau Universitaire**
**Préparation Examens**

---

## Table des Matières

1. [Cryptographie Symétrique](#1-cryptographie-symétrique)
2. [Intégrité des Messages](#2-intégrité-des-messages)
3. [Protocoles d'Authentification](#3-protocoles-dauthentification)
4. [Sécurité Réseau](#4-sécurité-réseau)
5. [Sûreté Mémoire (Buffer Overflow)](#5-sûreté-mémoire-buffer-overflow)
6. [Formules et Concepts Clés](#6-formules-et-concepts-clés)

---

## 1. Cryptographie Symétrique

### 1.1 Perfect Security (One-Time Pad)

**Définition** : Un chiffrement a la **perfect security** si :
```
Pr[M = m | C = c] = Pr[M = m]  ∀ m, c
```
L'observation du chiffré ne donne AUCUNE information sur le message.

**One-Time Pad (OTP)** :
- Chiffrement : `c = m ⊕ k`
- Déchiffrement : `m = c ⊕ k`
- **Conditions** :
  - Clé aussi longue que le message : `|K| = |M|`
  - Clé **uniformément aléatoire** et **usage unique**

**Théorème de Shannon** : Si `|M| > |K|`, alors **pas de perfect security possible**.

**Limitations OTP** :
- ❌ Clé aussi longue que le message (impraticable)
- ❌ Clé à usage unique (distribution difficile)
- ✅ Sécurité inconditionnelle (même contre adversaire avec puissance infinie)

### 1.2 Sécurité Computationnelle

**Secure PRG (Pseudo-Random Generator)** :
```
PRGadv[A, G] := |Pr[A(G(s)) = 1] - Pr[A(r) = 1]|
```
où `s ←$ S` (seed), `r ←$ R` (vraiment aléatoire)

**Définition** : G est un **Secure PRG** si `PRGadv[A, G]` est **négligeable** pour tout adversaire **efficace** (polynomial-time).

**Stream Cipher** :
```
c = m ⊕ PRG(k)
```
- Étend une courte clé k en un long keystream
- Exemples : **RC4** (cassé), **ChaCha20** (moderne)

### 1.3 Block Ciphers

**AES (Advanced Encryption Standard)** :
- Taille de bloc : 128 bits
- Tailles de clés : 128, 192, 256 bits
- Structure : Substitution-Permutation Network (SPN)

**Modes d'opération** :

| Mode | Chiffrement | Parallélisable ? | IV requis ? | Sécurité |
|------|-------------|------------------|-------------|----------|
| **ECB** | `c_i = E(k, m_i)` | ✅ Oui | ❌ Non | ❌ Patterns visibles |
| **CBC** | `c_i = E(k, m_i ⊕ c_{i-1})` | ❌ Non (encrypt) / ✅ Oui (decrypt) | ✅ Oui | ⚠️ Vulnérable padding oracle |
| **CTR** | `c_i = m_i ⊕ E(k, IV + i)` | ✅ Oui | ✅ Oui (nonce) | ✅ Secure (CPA) |

**CPA Security (Chosen-Plaintext Attack)** :
- Adversaire peut choisir des messages et obtenir leurs chiffrés
- **CTR mode** est CPA-secure
- **ECB** n'est PAS CPA-secure (déterministe)

### 1.4 Attaques Classiques

**Padding Oracle Attack** :
- Cible : CBC mode avec PKCS#7 padding
- Exploit : Information leak sur la validité du padding
- Permet de déchiffrer sans la clé !

**Known-Plaintext Attack** :
- Attaquant connaît des paires `(m, c)`
- Peut parfois récupérer la clé (ex: stream cipher avec réutilisation de clé)

---

## 2. Intégrité des Messages

### 2.1 Fonctions de Hachage Cryptographiques

**Propriétés requises** :

1. **Collision Resistance** :
   ```
   Difficile de trouver m₁ ≠ m₂ tel que H(m₁) = H(m₂)
   ```

2. **Preimage Resistance** :
   ```
   Étant donné h, difficile de trouver m tel que H(m) = h
   ```

3. **Second Preimage Resistance** :
   ```
   Étant donné m₁, difficile de trouver m₂ ≠ m₁ tel que H(m₁) = H(m₂)
   ```

**Paradoxe des anniversaires** :
- Pour hash de n bits, collision probable après `√(2^n) = 2^(n/2)` essais
- SHA-256 (256 bits) : collision après ~2^128 essais

**Hash functions modernes** :
- ✅ **SHA-256** : 256 bits, secure
- ✅ **SHA-3** (Keccak) : Standard alternatif
- ❌ **MD5** : Cassé (collisions trouvées)
- ❌ **SHA-1** : Cassé (collisions pratiques depuis 2017)

### 2.2 Message Authentication Code (MAC)

**Définition** : `tag = MAC(k, m)`

**Vérification** : `Verify(k, m, tag) → {accept, reject}`

**Sécurité** : Adversaire ne peut pas forger un tag valide pour un nouveau message, même en observant des paires `(m_i, tag_i)`.

**HMAC (Hash-based MAC)** :
```
HMAC(k, m) = H((k ⊕ opad) || H((k ⊕ ipad) || m))
```
- `ipad = 0x36` répété
- `opad = 0x5C` répété
- **Standard** : HMAC-SHA256

**Encrypt-then-MAC** (recommandé) :
```
c = Enc(k1, m)
tag = MAC(k2, c)
Envoyer: (c, tag)
```

### 2.3 AEAD (Authenticated Encryption with Associated Data)

**Combine** chiffrement + authentification en une seule primitive.

**AES-GCM** (Galois/Counter Mode) :
```
(c, tag) = AES-GCM-Encrypt(k, nonce, plaintext, associated_data)
```
- **Nonce** : 96 bits, DOIT être unique
- **Associated Data** : Authentifié mais non chiffré (headers)
- ✅ Parallélisable, rapide (accélération hardware)
- ⚠️ Catastrophique si nonce réutilisé

**ChaCha20-Poly1305** :
- Alternative à AES-GCM
- Meilleure sur CPU sans AES-NI
- Utilisé par TLS 1.3

---

## 3. Protocoles d'Authentification

### 3.1 Hachage de Mots de Passe

**❌ JAMAIS faire** :
```
hash = SHA256(password)  // Vulnérable aux rainbow tables !
```

**✅ Toujours faire** :
```
salt = random(16 bytes)
hash = bcrypt(password, salt, cost=12)
```

**Salting** :
- Salt unique par utilisateur
- Rend les rainbow tables inutiles
- Stockage : `(salt, hash)`

**Password KDF (Key Derivation Functions)** :

| Algorithme | Coût | Résistance | Recommandation |
|------------|------|------------|----------------|
| SHA-256 | Très rapide | ❌ Faible | Jamais utiliser |
| PBKDF2 | Itérations (100k+) | ⚠️ Moyen | Acceptable |
| **bcrypt** | Cost (12-14) | ✅ Bon | **Recommandé** |
| **scrypt** | Mémoire + CPU | ✅ Excellent | Recommandé |
| **Argon2** | Mémoire + CPU | ✅ Meilleur | **Standard moderne** |

**Benchmark bcrypt** (cost = 12) :
- ~300ms par hash sur CPU moderne
- Ralentit considérablement les attaques brute-force
- 1 million de tentatives ≈ 3.5 jours

### 3.2 Rainbow Tables et Tables de Hellman

**Problème** : Comment casser un hash sans sel efficacement ?

**Approches naïves** :
1. **Attaque en temps** : Calculer H(w) pour chaque tentative → Très lent
2. **Table complète** : Stocker (w, H(w)) pour tous les mots → Énorme mémoire (400 GB)

**Solution : Compromis Temps-Mémoire (TMTO)**

#### Tables de Hellman (1980)

**Principe** : Chaînes de réduction avec UNE fonction R

```
p₀ --H--> h₁ --R--> p₁ --H--> h₂ --R--> p₂ --H--> ... --R--> pₜ
```

**Stockage** : Seulement `(p₀, pₜ)` pour chaque chaîne

**Paramètres** :
- `m` chaînes de longueur `t`
- Couverture : ~`0.5 × m × t` mots de passe (50% à cause des collisions)
- Espace : O(m) stockage
- Temps recherche : O(t²) opérations

**Problème : Collisions de chaînes (Merging chains)**
```
Chaîne 1: password --H--> a3f5... --R--> admin123 --H--> ...
Chaîne 2: letmein  --H--> a3f5... --R--> admin123 --H--> ...
                           ^
                      Collision ! Les chaînes fusionnent
```

→ Perte de 50% de couverture

#### Rainbow Tables (Oechslin, 2003)

**Idée clé** : Utiliser des fonctions de réduction **DIFFÉRENTES** à chaque étape

```
p₀ --H--> h₁ --R₁--> p₁ --H--> h₂ --R₂--> p₂ --H--> ... --Rₜ--> pₜ
```

**Avantage** : Élimine les collisions de chaînes !

```
Chaîne 1: password --H--> a3f5... --R₁--> admin123 --H--> b2e8... --R₂--> ...
Chaîne 2: letmein  --H--> a3f5... --R₁--> user4567  --H--> c9d3... --R₂--> ...
                           ^                 ^
                       Même hash      Différents mots (R₁ ≠ R₂)
                                     Pas de fusion !
```

**Comparaison Hellman vs Rainbow** :

| Caractéristique | Hellman | Rainbow |
|-----------------|---------|---------|
| Fonctions réduction | 1 seule (R) | t différentes (R₁...Rₜ) |
| Collisions chaînes | ✅ Oui (50%) | ❌ Non |
| Couverture (m×t) | ~0.5 × m×t | ~0.86 × m×t |
| Temps recherche | O(t²) | O(t²) |
| Efficacité | Moyenne | **2× meilleure** |

#### Exemple Concret

**Paramètres** :
- Espace : alphanumériques 8 chars = 62⁸ ≈ 2.18×10¹⁴
- Hash : MD5 (rapide)
- Chaînes : m = 10⁸ (100 millions)
- Longueur : t = 10⁶ (1 million)
- Couverture : ~8.6×10¹³ (40% de l'espace)
- **Espace disque : 1.6 GB seulement !**

#### Défense : Le salage rend Rainbow Tables inutiles

**Avec sel unique** :
```
User 1: password + sel₁ --H--> hash₁
User 2: password + sel₂ --H--> hash₂  (différent !)
```

**Impact** :
- Sel de 128 bits → 2¹²⁸ ≈ 3.4×10³⁸ sels possibles
- Espace requis : 2¹²⁸ × 1.6 GB ≈ **10³⁸ exaoctets**
- **Totalement infaisable !**

**Conclusion** : Le salage (≥128 bits) rend Rainbow Tables **complètement inefficaces**.

### 3.3 Protocoles Challenge-Response

**Objectif** : Ne JAMAIS transmettre le mot de passe sur le réseau.

**Protocole basique (HMAC)** :
```
1. Client → Server : username
2. Server → Client : challenge (nonce aléatoire)
3. Client → Server : response = HMAC(password_key, challenge)
4. Server vérifie : response == HMAC(stored_key, challenge)
```

**Avantages** :
- ✅ Mot de passe jamais transmis
- ✅ Protection contre replay attack (challenge change à chaque fois)

**SCRAM (Salted Challenge Response Authentication Mechanism)** :
- Standard RFC 5802
- **Mutual authentication** (client ET serveur s'authentifient)
- Utilise PBKDF2 pour dériver les clés
- Serveur ne stocke pas le mot de passe, mais `SaltedPassword`

### 3.3 Multi-Factor Authentication (MFA)

**Trois facteurs** :
1. **Ce que vous savez** : Mot de passe, PIN
2. **Ce que vous avez** : Token, smartphone, YubiKey
3. **Ce que vous êtes** : Biométrie (empreinte, iris)

**TOTP (Time-based One-Time Password)** RFC 6238 :
```
counter = floor(time / 30)
hash = HMAC-SHA1(secret, counter)
code = Dynamic_Truncate(hash) mod 10^6
```
- Codes à 6 chiffres
- Valides pendant 30 secondes
- Tolérance : ±1 time step (90s total)
- Compatible : Google Authenticator, Authy

**FIDO2/WebAuthn** :
- Standard moderne (passwordless)
- Utilise cryptographie à clé publique
- Clé privée dans hardware token (YubiKey, TPM)
- ✅ Résiste au phishing (validation domaine intégrée)

### 3.4 Attaques sur l'Authentification

**Credential Stuffing** :
- Utiliser identifiants volés d'un site sur d'autres sites
- Problème : Réutilisation de mots de passe

**Phishing** :
- Faux site qui vole identifiants
- Défense : MFA (TOTP, FIDO2)

**Brute Force** :
- Tester systématiquement tous les mots de passe
- Défense : Rate limiting, account lockout, CAPTCHA

**Timing Attack** :
- Mesurer le temps de vérification
- Défense : `hmac.compare_digest()` (constant-time comparison)

---

## 4. Sécurité Réseau

### 4.1 Attaques DoS/DDoS

**SYN Flood** :
```
1. Attaquant → Server : SYN (IP source forgée)
2. Server → (void) : SYN-ACK (va nulle part)
3. Server alloue ressources et attend ACK qui ne vient jamais
4. Table de connexions saturée → Denial of Service
```

**Défense : SYN Cookies** :
```
seq_num = Hash(src_ip, src_port, dst_ip, dst_port, time, secret)
```
- Ne stocke PAS l'état avant connexion complète
- Encode l'information dans le numéro de séquence
- Linux : `net.ipv4.tcp_syncookies = 1`

**Amplification Attacks** :

| Protocole | Requête | Réponse | Facteur |
|-----------|---------|---------|---------|
| DNS (ANY) | 60 B | 3000 B | **50x** |
| NTP (monlist) | 48 B | 468 B | 9.7x |
| Memcached | 15 B | 750 KB | **51,000x** |

**Principe** :
1. Attaquant envoie requête avec IP source forgée (victime)
2. Serveur envoie grosse réponse à la victime
3. 10 Mbps attaquant → 500+ Gbps vers victime !

**Défenses DDoS** :
- **Prévention** : BCP 38 filtering (anti-spoofing), rate limiting
- **Détection** : Anomaly detection (déviations >3σ), NetFlow analysis
- **Mitigation** : CDN (Cloudflare), scrubbing centers, BGP blackholing

### 4.2 Firewalls

**Types** :

1. **Packet Filtering** (stateless) :
   - Filtre IP source/dest, ports, protocole
   - Rapide mais peu intelligent

2. **Stateful Firewall** :
   - Suit l'état des connexions TCP
   - Comprend NEW vs ESTABLISHED
   - Plus sécurisé

3. **Application Layer / WAF** :
   - Inspecte contenu HTTP/HTTPS
   - Détecte SQLi, XSS
   - Exemple : ModSecurity

**Exemple iptables** (stateful) :
```bash
# Politique par défaut : DROP
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Autoriser connexions établies
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Autoriser SSH (avec rate limiting anti brute-force)
iptables -A INPUT -p tcp --dport 22 -m recent --set
iptables -A INPUT -p tcp --dport 22 -m recent --update --seconds 60 --hitcount 4 -j DROP
iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 22 -j ACCEPT

# Autoriser HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

**Principe du moindre privilège** : Tout bloquer par défaut, autoriser explicitement.

### 4.3 IDS/IPS (Intrusion Detection/Prevention Systems)

**IDS** : Détecte et alerte (passif)
**IPS** : Détecte et bloque (actif)

**Types de détection** :

1. **Signature-based** :
   - Compare trafic à base de signatures d'attaques connues
   - ✅ Rapide, précis pour attaques connues
   - ❌ Vulnérable aux zero-days

2. **Anomaly-based** :
   - Détecte déviations du comportement normal
   - ✅ Peut détecter attaques inconnues
   - ❌ Taux élevé de faux positifs

**Métriques IDS** :
- **TPR** (True Positive Rate) : Pr[Alerte | Attaque] (sensibilité, recall)
- **FPR** (False Positive Rate) : Pr[Alerte | Normal]
- **TNR** (True Negative Rate) : Pr[Pas alerte | Normal] (spécificité)
- **FNR** (False Negative Rate) : Pr[Pas alerte | Attaque]
- **PPV** (Positive Predictive Value) : Pr[Attaque | Alerte] = TP / (TP + FP)

### 4.4 Base-Rate Fallacy et IDS (Analyse Détaillée)

**Le problème** : Un IDS avec 99% de précision est-il vraiment efficace ?

#### Exemple Concret : IDS "99% précis"

**Paramètres** :
- TPR = 99% (détecte 99% des attaques)
- FPR = 1% (1% du trafic légitime déclenche alerte)
- **Base rate** : Pr[Attaque] = 0.1% (seulement 0.1% du trafic est malveillant)

**Question** : Si une alerte se déclenche, quelle est la probabilité que ce soit une vraie attaque ?

**Théorème de Bayes** :
```
Pr[Attaque | Alerte] = Pr[Alerte | Attaque] × Pr[Attaque] / Pr[Alerte]
```

où :
```
Pr[Alerte] = Pr[Alerte | Attaque] × Pr[Attaque] + Pr[Alerte | Normal] × Pr[Normal]
           = 0.99 × 0.001 + 0.01 × 0.999
           = 0.00099 + 0.00999
           = 0.01098
```

Donc :
```
Pr[Attaque | Alerte] = (0.99 × 0.001) / 0.01098
                      = 0.00099 / 0.01098
                      ≈ 0.09 = 9%
```

**Résultat choquant** : Seulement **9% des alertes sont vraies** !
→ **91% sont des faux positifs** !

#### Table de Confusion (100,000 connexions)

|  | **Attaque réelle** | **Trafic normal** | **Total** |
|--|-------------------|-------------------|-----------|
| **Alerte** | 99 (TP) | 999 (FP) | 1,098 |
| **Pas alerte** | 1 (FN) | 98,901 (TN) | 98,902 |
| **Total** | 100 | 99,900 | 100,000 |

**Calcul PPV** :
```
PPV = TP / (TP + FP) = 99 / (99 + 999) = 99/1,098 ≈ 9%
```

#### Le Phénomène de Base-Rate Fallacy

**Intuition erronée** :
> "Mon IDS a 99% de précision, donc si une alerte se déclenche, il y a 99% de chances que ce soit une attaque."

**FAUX !** Cette intuition ignore que :
- Le taux de base (base rate) des attaques est très faible (0.1%)
- Il y a BEAUCOUP PLUS de trafic légitime que malveillant
- Même 1% de FPR génère énormément de fausses alertes

**Calcul mental rapide** :
- 100,000 connexions : 100 attaques, 99,900 normales
- FP générés : 99,900 × 1% = 999 fausses alertes
- TP générés : 100 × 99% = 99 vraies alertes
- Ratio FP:TP = 999:99 ≈ 10:1 en faveur des faux positifs !

#### Impact Opérationnel

**Conséquences pratiques** :

1. **Alert Fatigue** :
   - Analystes submergés par fausses alertes
   - "Cry-wolf effect" : Alertes ignorées
   - Burnout des analystes SOC

2. **Attaques Manquées** :
   - Vraies attaques noyées dans le bruit
   - Coût triage : 1,098 alertes pour 99 vraies attaques
   - Si 5 min/alerte → 91 heures de travail !

3. **Faux Sentiment de Sécurité** :
   - "Nous avons un IDS 99%, nous sommes protégés"
   - Négligence autres mesures

#### Solutions pour Améliorer le PPV

**1. Réduire le FPR** (impact énorme !)

| FPR | Alertes totales | PPV |
|-----|-----------------|-----|
| 1% | 1,098 | **9%** |
| 0.5% | 599 | 16% |
| 0.1% | 199 | **50%** |
| 0.01% | 109 | **91%** |

→ Diviser FPR par 10 améliore PPV de 9% à 50% !

**2. Corrélation d'événements** :
- Combiner 2 IDS indépendants (FPR = 1% chacun)
- FPR combiné : 0.01 × 0.01 = 0.01%
- PPV passe à ~91% !

**3. Machine Learning et Tuning** :
- Feature engineering (géoloc, réputation IP, etc.)
- Ensemble methods
- Active learning avec feedback humain
- Anomaly scoring (score 0-100 au lieu de binaire)

**4. Context-Aware Detection** :
- Historique utilisateur/IP
- Géolocalisation anormale
- Reputation scoring (blacklists)
- Behavioral analytics

#### Métriques Importantes vs Trompeuses

**✅ Métriques importantes** :
- **PPV** (Positive Predictive Value) : Métrique opérationnelle clé
- **FPR absolu** : Nombre fausses alertes/jour
- **Alert-to-incident ratio** : Combien d'alertes pour une vraie attaque ?

**❌ Métriques trompeuses** :
- **Accuracy globale** : (TP + TN) / Total = 99%
  - Dominée par les vrais négatifs (trafic normal)
  - Ne révèle PAS le problème des 91% de FP !
- **TPR seul** : Ignore complètement les faux positifs

#### Conclusion Base-Rate Fallacy

**Points clés** :
1. Le **taux de base** (base rate) est CRUCIAL pour interpréter les alertes
2. Un IDS "précis" peut générer majoritairement des FP si base rate est faible
3. Toujours calculer **PPV** (Pr[Attaque | Alerte]), pas seulement TPR
4. **Réduire FPR** est plus important qu'augmenter TPR dans de nombreux cas
5. La **corrélation** de signaux indépendants améliore drastiquement le PPV

**Citation** :
> "A test that is 99% accurate sounds impressive, but when applied to a population where only 0.1% are positive, the majority of positive results will be false positives."

**Limitations IDS/IPS** :
- ❌ Faux positifs/négatifs inévitables
- ❌ Chiffrement (TLS) rend inspection difficile
- ❌ Performance (deep packet inspection coûteuse)
- ❌ Évasion possible (fragmentation, polymorphisme)

---

## 5. Sûreté Mémoire (Buffer Overflow)

### 5.1 Layout Mémoire (x86 32-bits)

```
Adresses Hautes (0xFFFFFFFF)
+------------------+
| Kernel Space     | (OS)
+------------------+ 0xC0000000
| Stack ↓          | Variables locales, return addresses
|                  |
|     ...          |
|                  |
| Heap ↑           | malloc(), new
+------------------+
| .bss             | Variables non initialisées
+------------------+
| .data            | Variables globales initialisées
+------------------+
| .text            | Code exécutable (read-only)
+------------------+
Adresses Basses (0x08048000)
```

### 5.2 Stack Frame

```
Adresses Hautes
+-------------------+ <-- EBP + 8
| Argument 1        |
+-------------------+ <-- EBP + 4
| Return Address    | <-- CIBLE de l'attaque !
+-------------------+ <-- EBP
| Saved EBP         |
+-------------------+ <-- EBP - 4
| Variable locale 1 |
+-------------------+
| buffer[64]        | <-- Overflow démarre ici
+-------------------+ <-- ESP
Adresses Basses
```

**Instructions clés** :
```asm
call func    ; Push return address, jump to func
ret          ; Pop return address → EIP (jump)
push ebp     ; Sauvegarde ancien EBP
mov ebp, esp ; EBP = ESP (nouveau frame)
```

### 5.3 Buffer Overflow Attack

**Code vulnérable** :
```c
void vulnerable(char *input) {
    char buffer[64];
    strcpy(buffer, input);  // Pas de vérification de taille !
}
```

**Exploitation** :

**Calcul de l'offset** :
```
Buffer at    : EBP - 72
Return addr at: EBP + 4
Offset = (EBP + 4) - (EBP - 72) = 76 bytes
```

**Payload structure** :
```
[NOP sled (100 bytes)] + [Shellcode (25 bytes)] + [Padding (51 bytes)]
+ [Fake EBP (4 bytes)] + [Return Address (4 bytes)]
```

**Shellcode** (execve("/bin/sh")) :
```asm
xor eax, eax        ; EAX = 0
push eax            ; NULL terminator
push 0x68732f2f     ; "//sh"
push 0x6e69622f     ; "/bin"
mov ebx, esp        ; EBX = ptr to "/bin//sh"
xor ecx, ecx        ; ECX = NULL (argv)
xor edx, edx        ; EDX = NULL (envp)
mov al, 0x0b        ; EAX = 11 (syscall execve)
int 0x80            ; syscall
```

**Hex** : `\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80`

**NOP Sled** :
- Préfixer shellcode de nombreux NOP (`\x90`)
- Pointer return address vers le milieu du NOP sled
- Si on atterrit sur un NOP, on "glisse" jusqu'au shellcode

### 5.4 Défenses

**Stack Canaries** :
```
Stack avec canary:
+-------------------+
| Return Address    |
+-------------------+
| Saved EBP         |
+-------------------+
| CANARY (random)   | <-- Vérifié avant return
+-------------------+
| buffer[64]        |
+-------------------+
```
- Valeur aléatoire secrète entre buffer et return address
- Vérifiée avant le return
- Si modifiée → `abort()` (stack smashing detected)
- Compilation : `gcc -fstack-protector-all`

**NX Bit (DEP - Data Execution Prevention)** :
- Marque stack et heap comme **non-exécutables**
- Shellcode injecté ne peut pas être exécuté
- Compilation : `gcc -z noexecstack`
- **Contournement** : ROP (Return-Oriented Programming)

**ASLR (Address Space Layout Randomization)** :
- Randomise adresses de : stack, heap, bibliothèques, exécutable
- Attaquant ne peut pas prédire les adresses
- Linux : `echo 2 > /proc/sys/kernel/randomize_va_space`
- **Contournement** : Information leak, brute force (32-bits)

**Return-Oriented Programming (ROP)** :
- Chaîner des "gadgets" (petits bouts de code + RET)
- Gadget : `pop eax ; ret`, `pop ebx ; ret`, `int 0x80 ; ret`
- Payload : `[addr gadget1] + [data] + [addr gadget2] + ...`
- Contourne NX (réutilise code existant)

**Compilation sécurisée** :
```bash
gcc -fstack-protector-all \    # Stack canaries
    -D_FORTIFY_SOURCE=2 \      # Runtime checks
    -fPIE -pie \               # Position Independent (ASLR)
    -Wl,-z,relro,-z,now \      # Read-only GOT/PLT
    -o secure program.c
```

**Vérifier protections** :
```bash
checksec --file=./program
# Output: Canary, NX, PIE, RELRO status
```

---

## 6. Formules et Concepts Clés

### 6.1 Cryptographie

**Perfect Security** :
```
Pr[M = m | C = c] = Pr[M = m]
```

**Shannon's Theorem** :
```
Perfect security ⇒ |K| ≥ |M|
```

**PRG Advantage** :
```
PRGadv[A, G] = |Pr[A(G(s)) = 1] - Pr[A(r) = 1]|
```
Secure PRG ⇔ `PRGadv[A, G]` négligeable pour tout A efficient.

**Birthday Paradox** :
```
Collisions probables après √(2^n) ≈ 2^(n/2) essais
Pour SHA-256 (256 bits) : ~2^128 essais
```

### 6.2 Authentification

**HMAC** :
```
HMAC(k, m) = H((k ⊕ opad) || H((k ⊕ ipad) || m))
```

**TOTP** :
```
counter = floor(time / 30)
code = HOTP(secret, counter) mod 10^6
```

**bcrypt** (approx) :
```
Temps ≈ 2^cost × base_time
cost=12 → ~300ms
```

### 6.3 Sécurité Réseau

**Amplification Factor** :
```
Factor = Response_Size / Request_Size
```

**IDS Metrics** :
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
FPR = FP / (FP + TN)
FNR = FN / (FN + TP)
```

**Bayes Theorem** :
```
Pr[A|B] = Pr[B|A] × Pr[A] / Pr[B]

où Pr[B] = Σ Pr[B|Aᵢ] × Pr[Aᵢ]
```

### 6.4 Buffer Overflow

**Offset Calculation** :
```
Offset = (Return_Address_Position) - (Buffer_Start)
Souvent: Offset = buffer_size + saved_ebp_size + autres_variables
```

**Stack Growth** : Vers le BAS (adresses décroissantes)
**Heap Growth** : Vers le HAUT (adresses croissantes)

---

## 📝 Checklist de Révision

### Cryptographie ✓
- [ ] Définition perfect security
- [ ] OTP : avantages et limitations
- [ ] Théorème de Shannon
- [ ] PRG : définition sécurité
- [ ] Stream cipher vs Block cipher
- [ ] Modes AES : ECB, CBC, CTR (différences)
- [ ] CPA security

### Intégrité ✓
- [ ] 3 propriétés hash functions
- [ ] Paradoxe des anniversaires
- [ ] SHA-256 vs MD5/SHA-1
- [ ] MAC vs HMAC
- [ ] Encrypt-then-MAC
- [ ] AEAD (AES-GCM)

### Authentification ✓
- [ ] Pourquoi PAS SHA-256(password)
- [ ] Salting : principe et utilité
- [ ] bcrypt, scrypt, Argon2 : différences
- [ ] Challenge-Response : fonctionnement
- [ ] SCRAM : caractéristiques
- [ ] TOTP : algorithme
- [ ] MFA : 3 facteurs
- [ ] FIDO2/WebAuthn

### Réseau ✓
- [ ] SYN Flood : attaque et défense (SYN cookies)
- [ ] Amplification : DNS, NTP, Memcached (facteurs)
- [ ] DoS defenses : rate limiting, CDN, scrubbing
- [ ] Firewall : stateless vs stateful
- [ ] iptables : politique par défaut, règles essentielles
- [ ] IDS vs IPS
- [ ] Signature-based vs Anomaly-based
- [ ] Base-rate fallacy (Bayes)

### Buffer Overflow ✓
- [ ] Layout mémoire : stack, heap, .text, .data, .bss
- [ ] Stack frame : structure complète
- [ ] Buffer overflow : principe
- [ ] Calcul offset
- [ ] Shellcode : structure, contraintes
- [ ] NOP sled : utilité
- [ ] Stack canaries : fonctionnement
- [ ] NX bit (DEP)
- [ ] ASLR
- [ ] ROP : principe

---

## 🎯 Conseils d'Examen

1. **QCM Vrai/Faux** :
   - Lisez bien CHAQUE mot (surtout les négations)
   - Pénalité : -0.5 par erreur → si doute, ne pas répondre

2. **Questions Ouvertes** :
   - **Dessins** : Stack frame, protocoles → TOUJOURS inclure
   - **Justifications** : Expliquer le "pourquoi", pas juste le "quoi"
   - **Calculs** : Montrer les étapes intermédiaires

3. **Code C/Buffer Overflow** :
   - Compter soigneusement les bytes
   - Penser à `strcpy()` qui copie aussi `\0`
   - Dessiner le stack avec adresses

4. **Probabilités/IDS** :
   - Appliquer Bayes méthodiquement
   - Calculer `Pr[B]` d'abord (loi des probabilités totales)

5. **Gestion du temps** :
   - QCM : 1-2 min max par question
   - Questions ouvertes : Lire TOUTES les questions d'abord
   - Faire les plus faciles en premier

---

**Bonne révision !** 🚀

*Dernière mise à jour : Janvier 2025*
