# Cours de Cryptographie - Résumé de Révision pour l'Examen

**Basé sur** : The Joy of Cryptography (Rosulek)
**Date** : 2026-01-12
**Durée du cours** : 38-48 heures (5 chapitres)

---

## 📋 Table des Matières

1. [Chapitre 1 : Introduction & Sécurité Parfaite](#chapitre-1--introduction--sécurité-parfaite)
2. [Chapitre 2 : Cryptographie Symétrique](#chapitre-2--cryptographie-symétrique)
3. [Chapitre 3 : Intégrité des Messages](#chapitre-3--intégrité-des-messages)
4. [Chapitre 4 : Cryptographie à Clé Publique](#chapitre-4--cryptographie-à-clé-publique)
5. [Chapitre 5 : Communication Anonyme](#chapitre-5--communication-anonyme)
6. [Formules Essentielles](#formules-essentielles)
7. [Attaques à Connaître](#attaques-à-connaître)
8. [Bonnes Pratiques](#bonnes-pratiques)

---

# Chapitre 1 : Introduction & Sécurité Parfaite

## Concepts Fondamentaux

### Définitions de Base

| Terme | Définition |
|-------|------------|
| **Plaintext** | Message original $m \in \mathcal{M}$ |
| **Ciphertext** | Message chiffré $c \in \mathcal{C}$ |
| **Key Space** | Ensemble des clés $\mathcal{K}$ |
| **Encryption** | $\text{Enc} : \mathcal{K} \times \mathcal{M} \to \mathcal{C}$ |
| **Decryption** | $\text{Dec} : \mathcal{K} \times \mathcal{C} \to \mathcal{M}$ |

### Principes de Kerckhoffs

> **"La sécurité d'un système cryptographique ne doit reposer que sur le secret de la clé, et non sur celui de l'algorithme."**

**Conséquences** :
- Algorithmes publics (auditables)
- Seule la clé doit rester secrète
- Permet l'analyse académique et l'amélioration

## Sécurité Parfaite (Perfect Security)

### Définition de Shannon (1949)

Un schéma de chiffrement a la **sécurité parfaite** si pour tout $m_0, m_1 \in \mathcal{M}$ et tout $c \in \mathcal{C}$ :

$$\Pr[C = c \mid M = m_0] = \Pr[C = c \mid M = m_1]$$

**Interprétation** : L'observation du ciphertext ne donne **AUCUNE** information sur le plaintext.

### One-Time Pad (OTP)

**Construction** :
- **Enc**$(k, m) = m \oplus k$
- **Dec**$(k, c) = c \oplus k$
- **Key space** : $\mathcal{K} = \{0,1\}^n$ (clé aussi longue que le message)

**Propriétés** :
- ✅ **Sécurité parfaite** (prouvée)
- ✅ **Extrêmement rapide** (opération XOR)
- ❌ **Clé aussi longue que le message**
- ❌ **Clé à usage unique** (one-time only!)

### Théorème de Shannon

> **Si un schéma de chiffrement a la sécurité parfaite, alors $|\mathcal{K}| \geq |\mathcal{M}|$**

**Conséquence** : La sécurité parfaite nécessite des clés au moins aussi longues que les messages.

### Attaque Two-Time Pad

**Problème** : Réutiliser la même clé $k$ pour deux messages $m_1, m_2$ :

$$c_1 = m_1 \oplus k$$
$$c_2 = m_2 \oplus k$$
$$c_1 \oplus c_2 = m_1 \oplus m_2$$

**Conséquence** : L'adversaire obtient le XOR des deux messages, permettant des attaques statistiques.

**Cas réel** : Projet VENONA (1940s) - déchiffrement de messages soviétiques ayant réutilisé des clés OTP.

---

# Chapitre 2 : Cryptographie Symétrique

## Computational Security

### Transition : Perfect Security → Computational Security

| Perfect Security | Computational Security |
|------------------|------------------------|
| Sécurité inconditionnelle | Sécurité contre adversaires polynomiaux |
| Clés très longues ($\geq$ message) | Clés courtes (128-256 bits) |
| Coût : gestion des clés | Coût : hypothèses mathématiques |

### Hypothèse de Difficulté

**Principe** : Certains problèmes sont "difficiles" (pas de solution efficace connue)
- Exemples : Factorisation, Logarithme Discret

## Pseudorandom Generators (PRG)

### Définition

$$\text{PRG} : \{0,1\}^\lambda \to \{0,1\}^{n}$$
où $n \gg \lambda$ (expansion)

**Propriété clé** : La sortie est **indistinguable** d'une chaîne vraiment aléatoire pour un adversaire polynomial.

### Exemples de PRG

| PRG | Sécurité | Usage |
|-----|----------|-------|
| **LCG** (Linear Congruential) | ❌ **Dangereux** | JAMAIS en crypto |
| **BBS** (Blum-Blum-Shub) | ✅ Prouvable (factorisation) | Théorique |
| **ChaCha20** | ✅ Excellent | TLS 1.3, WireGuard |
| **AES-CTR** | ✅ Excellent | Standard |
| **DRBG** (NIST) | ✅ Standard | Génération aléatoire |

### Stream Ciphers

**Construction** : $\text{Enc}_k(m) = m \oplus \text{PRG}(k)$

**Exemples** :
- **ChaCha20** : 256 bits de clé, 96 bits de nonce, 32 bits de compteur
- **AES-CTR** : AES utilisé comme PRG

**Gestion des nonces** :
1. **Compteur** : Incrémentation (simple, déterministe)
2. **Aléatoire** : 96 bits aléatoires (nécessite RNG cryptographique)
3. **Dérivation** : À partir de métadonnées (contexte)

⚠️ **CRITIQUE** : Ne JAMAIS réutiliser (nonce, clé) → Two-Time Pad attack!

## Block Ciphers

### Pseudorandom Permutation (PRP)

**Définition** : $E_k : \{0,1\}^n \to \{0,1\}^n$ est une permutation pseudoaléatoire si elle est indistinguable d'une permutation vraiment aléatoire.

**Jeu PRP-IND** :
- Adversaire reçoit soit $E_k$ (PRP), soit $\pi$ (permutation aléatoire)
- Il peut faire des requêtes et doit deviner lequel

### AES (Advanced Encryption Standard)

**Paramètres** :
- Taille de bloc : **128 bits**
- Tailles de clé : **128, 192, 256 bits**
- Nombre de rounds : **10, 12, 14** (selon taille de clé)

**Structure** : Substitution-Permutation Network (SPN)

**Opérations par round** :
1. **SubBytes** : S-box (substitution non-linéaire)
   - Inversion dans $\text{GF}(2^8)$ + transformation affine
2. **ShiftRows** : Permutation des lignes
3. **MixColumns** : Matrice MDS dans $\text{GF}(2^8)$
4. **AddRoundKey** : XOR avec sous-clé de round

**Propriétés** :
- ✅ Standard mondial (NIST 2001)
- ✅ Accélération matérielle (AES-NI)
- ✅ Pas de faiblesses cryptographiques connues (clé 128+ bits)

### Modes Opératoires

#### ECB (Electronic Codebook)

```
c_i = E_k(m_i)
```

❌ **JAMAIS utiliser ECB !**
- Déterministe (mêmes blocs → mêmes ciphertexts)
- Révèle les patterns dans les données
- Vulnérable aux attaques CPA

#### CBC (Cipher Block Chaining)

```
c_0 = IV (aléatoire)
c_i = E_k(c_{i-1} ⊕ m_i)
```

**Propriétés** :
- ✅ Sécurité CPA (si IV aléatoire et imprévisible)
- ❌ Séquentiel (pas de parallélisation du chiffrement)
- ✅ Déchiffrement parallélisable
- ⚠️ IV prévisible → vulnérable

#### CTR (Counter Mode)

```
c_i = E_k(nonce || counter_i) ⊕ m_i
```

**Propriétés** :
- ✅ Sécurité CPA (si nonce jamais réutilisé)
- ✅ **Parallélisable** (chiffrement et déchiffrement)
- ✅ Accès aléatoire (peut déchiffrer bloc i sans déchiffrer 1..i-1)
- ✅ Pas de padding nécessaire
- ⚠️ **Recommandé** pour la plupart des usages

#### OFB (Output Feedback)

```
s_0 = IV
s_i = E_k(s_{i-1})
c_i = s_i ⊕ m_i
```

**Propriétés** :
- ✅ Stream cipher mode
- ❌ Risque de cycle (si on revient à un état précédent)
- ❌ Moins utilisé que CTR

### Sécurité CPA (Chosen Plaintext Attack)

**Définition** : Un schéma est CPA-secure si un adversaire ayant accès à un oracle de chiffrement ne peut pas distinguer les chiffrements de deux messages de son choix.

**Jeu IND-CPA** :
1. Adversaire choisit $m_0, m_1$
2. Challenger tire $b \in \{0,1\}$ et retourne $c = \text{Enc}_k(m_b)$
3. Adversaire devine $b'$
4. Gagne si $b = b'$

**Résultats** :
- ECB : ❌ **PAS CPA-secure**
- CBC (IV aléatoire) : ✅ **CPA-secure**
- CTR : ✅ **CPA-secure**

---

# Chapitre 3 : Intégrité des Messages

## Message Authentication Codes (MAC)

### Définition

Un MAC est une triple $(\text{Gen}, \text{Mac}, \text{Vrfy})$ :
- **Gen**$(1^\lambda) \to k$
- **Mac**$(k, m) \to t$ (tag)
- **Vrfy**$(k, m, t) \to \{0,1\}$

### Sécurité : UF-CMA (Unforgeability under Chosen Message Attack)

**Jeu** :
1. Adversaire peut demander tags pour messages de son choix : $t_i = \text{Mac}_k(m_i)$
2. Adversaire produit $(m^*, t^*)$ avec $m^* \notin \{m_1, \ldots, m_q\}$
3. Gagne si $\text{Vrfy}_k(m^*, t^*) = 1$

**Sécurité** : $\Pr[\text{Adversaire gagne}] \leq \epsilon$ (négligeable)

## Constructions de MAC

### CBC-MAC

**Algorithme** :
```
t_0 = 0^n
for i = 1 to ℓ:
    t_i = E_k(t_{i-1} ⊕ m_i)
return t_ℓ
```

⚠️ **DANGER** : CBC-MAC basique est **INSÉCURISÉ** pour messages de longueur variable !

**Attaque** : Si $t = \text{CBC-MAC}_k(m)$ pour $m$ de 1 bloc, alors $\text{CBC-MAC}_k(m \| (m \oplus t)) = t$

**Solutions** :
- **CMAC** (NIST SP 800-38B) : Deux sous-clés $k_1, k_2$ pour traiter le dernier bloc
- **Encoder la longueur** : Préfixer par $\ell$

### HMAC (Hash-based MAC)

**Construction** :
$$\text{HMAC}_k(m) = H((k \oplus \text{opad}) \| H((k \oplus \text{ipad}) \| m))$$

où :
- $\text{opad} = 0x5c5c\ldots5c$ (64 octets)
- $\text{ipad} = 0x3636\ldots36$ (64 octets)

**Propriétés** :
- ✅ **Standard** (RFC 2104)
- ✅ Sécurité prouvée (si $H$ résistant aux collisions)
- ✅ Utilisé partout (TLS, SSH, IPsec, JWT)
- ✅ Pas de timing attacks (si implémenté correctement)

## Fonctions de Hachage

### Propriétés de Sécurité

1. **Pre-image resistance** : Étant donné $y$, difficile de trouver $x$ tel que $H(x) = y$
2. **Second pre-image resistance** : Étant donné $x$, difficile de trouver $x' \neq x$ tel que $H(x) = H(x')$
3. **Collision resistance** : Difficile de trouver $x, x'$ tels que $H(x) = H(x')$

### Paradoxe des Anniversaires

**Théorème** : Pour une fonction de hachage à $n$ bits, trouver une collision nécessite $\approx 2^{n/2}$ évaluations (pas $2^n$).

**Exemple** : SHA-256 (256 bits) → sécurité $2^{128}$ contre collisions.

**Application** : 23 personnes → 50% de chance que deux aient le même anniversaire.

### Construction Merkle-Damgård

**Principe** : Construire $H : \{0,1\}^* \to \{0,1\}^n$ à partir de $h : \{0,1\}^n \times \{0,1\}^b \to \{0,1\}^n$ (fonction de compression).

**Algorithme** :
1. **Padding** : $m' = m \| 1 \| 0^k \| \langle |m| \rangle_{64}$
2. **Découpage** : $m' = m_1 \| m_2 \| \cdots \| m_t$
3. **Itération** :
   ```
   H_0 = IV
   for i = 1 to t:
       H_i = h(H_{i-1}, m_i)
   return H_t
   ```

**Théorème** : Si $h$ est résistant aux collisions, alors $H$ l'est aussi.

**Davies-Meyer** (utilisé dans SHA-256) :
$$h(H_{i-1}, m_i) = E_{m_i}(H_{i-1}) \oplus H_{i-1}$$

⚠️ **Limitation** : **Length extension attack** - Si on connaît $H(m)$, on peut calculer $H(m \| \text{suffix})$ sans connaître $m$ !

**Conséquence** : $H(k \| m)$ n'est PAS un MAC sécurisé.

### Fonctions de Hachage Modernes

| Fonction | Sortie | Sécurité | Statut |
|----------|--------|----------|--------|
| **MD5** | 128 bits | ❌ Cassé | Obsolète |
| **SHA-1** | 160 bits | ❌ Cassé (2017) | Obsolète |
| **SHA-256** | 256 bits | ✅ Sécurisé | Recommandé |
| **SHA-3** | Variable | ✅ Sécurisé | Standard 2015 |
| **BLAKE3** | 256 bits | ✅ Très rapide | Moderne |

## Authenticated Encryption (AEAD)

### Problème : Chiffrement Sans Intégrité

**Attaque de malléabilité sur CTR** :
```
c = m ⊕ PRG(k)
c' = c ⊕ Δ  →  m' = m ⊕ Δ
```

Adversaire peut modifier le ciphertext de manière contrôlée !

### Solutions : Combiner Chiffrement et MAC

| Composition | Sécurité | Exemple |
|-------------|----------|---------|
| **Encrypt-and-MAC** | ❌ Peut révéler infos | SSH (ancien) |
| **MAC-then-Encrypt** | ⚠️ Risqué (padding oracle) | TLS 1.0 |
| **Encrypt-then-MAC** | ✅ **Toujours sécurisé** | IPsec |

### AEAD : Authenticated Encryption with Associated Data

**Interface** :
- **Enc**$(k, \text{nonce}, m, \text{ad}) \to c, t$
- **Dec**$(k, \text{nonce}, c, t, \text{ad}) \to m$ ou $\perp$

où :
- $m$ : message (chiffré)
- $\text{ad}$ : données associées (authentifiées mais non chiffrées)
- $t$ : tag d'authentification

### AES-GCM (Galois/Counter Mode)

**Construction** :
- **Chiffrement** : Mode CTR avec AES
- **Authentification** : GHASH (multiplication polynomiale dans $\text{GF}(2^{128})$)

**Propriétés** :
- ✅ **Standard** (NIST SP 800-38D)
- ✅ **Très rapide** (accélération matérielle CLMUL)
- ✅ Parallélisable
- ✅ Utilisé partout (TLS 1.3, WireGuard, HTTPS)
- ⚠️ **Nonce 96 bits** : Ne JAMAIS réutiliser !

### ChaCha20-Poly1305

**Construction** :
- **Chiffrement** : ChaCha20 stream cipher
- **Authentification** : Poly1305 MAC

**Propriétés** :
- ✅ Plus rapide qu'AES-GCM sans accélération matérielle
- ✅ Résistant aux timing attacks
- ✅ Utilisé dans TLS 1.3, WireGuard, Google QUIC
- ✅ **Recommandé** pour mobile et IoT

### Autres Schémas AEAD

**AES-CCM** :
- Composition MAC-then-Encrypt (CBC-MAC + CTR)
- Utilisé dans WPA2, Bluetooth LE, Zigbee
- ⚠️ Deux passes (plus lent que GCM)

**AES-OCB** :
- Une seule passe (optimal)
- ✅ Très rapide et prouvé sécurisé
- ❌ Historique de brevets → adoption limitée

**ASCON** :
- Vainqueur CAESAR competition (lightweight)
- Basé sur construction éponge (comme SHA-3)
- ✅ Standardisé NIST 2023
- ✅ Idéal pour IoT et systèmes embarqués

---

# Chapitre 4 : Cryptographie à Clé Publique

## Problèmes Mathématiques Difficiles

### Logarithme Discret (DLP)

**Problème** : Étant donné $g, g^a$, trouver $a$.

**Groupes sécurisés** :
- $\mathbb{Z}_p^*$ avec $p$ premier de 2048-4096 bits
- Courbes elliptiques (256 bits suffisent)

### Computational Diffie-Hellman (CDH)

**Problème** : Étant donné $g, g^a, g^b$, calculer $g^{ab}$.

**Relation** : Si on résout DLP, on résout CDH.

### Decisional Diffie-Hellman (DDH)

**Problème** : Distinguer $(g, g^a, g^b, g^{ab})$ de $(g, g^a, g^b, g^c)$ où $c$ aléatoire.

**Relations** :
$$\text{DLP} \Rightarrow \text{CDH} \Rightarrow \text{DDH}$$

⚠️ **DDH est facile dans $\mathbb{Z}_p^*$ entier** (via symbole de Legendre) !

**Solution** : Travailler dans sous-groupe d'ordre premier $q$ de $\mathbb{Z}_p^*$.

## Diffie-Hellman Key Exchange

**Protocole** :
1. **Alice** : Choisit $a$, envoie $g^a$
2. **Bob** : Choisit $b$, envoie $g^b$
3. **Clé partagée** : $k = g^{ab}$ (Alice calcule $(g^b)^a$, Bob calcule $(g^a)^b$)

**Sécurité passive** : CDH suffit

⚠️ **Vulnérable à Man-in-the-Middle** !

**Solutions** :
- Authenticated DH (certificats, signatures)
- Station-to-Station Protocol

## Chiffrement ElGamal

**Gen**$(1^\lambda)$ :
- Choisir $x \in \mathbb{Z}_q$
- $pk = g^x$, $sk = x$

**Enc**$(pk, m)$ :
- Choisir $y \in \mathbb{Z}_q$
- $c_1 = g^y$, $c_2 = m \cdot (pk)^y = m \cdot g^{xy}$
- Retourner $(c_1, c_2)$

**Dec**$(sk, (c_1, c_2))$ :
- $m = c_2 / (c_1^{sk}) = c_2 / (g^y)^x$

**Propriétés** :
- ✅ CPA-secure (sous hypothèse DDH)
- ✅ Homomorphisme multiplicatif
- ❌ Expansion 2× (ciphertext = 2 éléments du groupe)
- ⚠️ Malleable (adversaire peut modifier $m$ en $m'$)

## RSA

### Génération de Clés

**Gen**$(1^\lambda)$ :
1. Choisir deux grands premiers $p, q$ (1024 bits chacun pour RSA-2048)
2. $n = p \cdot q$
3. $\phi(n) = (p-1)(q-1)$
4. Choisir $e$ tel que $\gcd(e, \phi(n)) = 1$ (souvent $e = 65537$)
5. Calculer $d = e^{-1} \bmod \phi(n)$
6. $pk = (n, e)$, $sk = (n, d)$

### RSA Textbook (INSÉCURISÉ !)

**Enc**$(pk, m) = m^e \bmod n$

**Dec**$(sk, c) = c^d \bmod n$

❌ **Déterministe** → PAS CPA-secure !
❌ **Homomorphisme multiplicatif** → malleable

### RSA-OAEP (Sécurisé)

**OAEP-Encode**$(m)$ :
1. Choisir $r \xleftarrow{\$} \{0,1\}^{k_0}$
2. $s = (m \| 0^{k_1}) \oplus G(r)$
3. $t = r \oplus H(s)$
4. Retourner $s \| t$

**Enc**$(pk, m)$ :
1. $\hat{m} = \text{OAEP-Encode}(m)$
2. $c = (\hat{m})^e \bmod n$

**Propriétés** :
- ✅ CPA-secure (modèle oracle aléatoire)
- ✅ Standard PKCS#1 v2.2 (RFC 8017)
- ⚠️ Taille message limitée (~190 octets pour RSA-2048)

### Chiffrement Hybride

**Pratique courante** :
1. Générer clé AES aléatoire $k_{\text{AES}}$
2. $c_{\text{sym}} = \text{AES-GCM}_{k_{\text{AES}}}(m)$
3. $c_{\text{key}} = \text{RSA-OAEP}(pk, k_{\text{AES}})$
4. Transmettre $(c_{\text{key}}, c_{\text{sym}})$

## Signatures Numériques

### Définition

Un schéma de signature est une triple $(\text{Gen}, \text{Sign}, \text{Vrfy})$ :
- **Gen**$(1^\lambda) \to (pk, sk)$
- **Sign**$(sk, m) \to \sigma$
- **Vrfy**$(pk, m, \sigma) \to \{0,1\}$

**Sécurité** : UF-CMA (Unforgeability under Chosen Message Attack)

### RSA Signatures

**Sign**$(sk, m)$ : $\sigma = H(m)^d \bmod n$

**Vrfy**$(pk, m, \sigma)$ : Vérifier $\sigma^e \stackrel{?}{=} H(m) \pmod{n}$

**Standard moderne** : RSA-PSS (Probabilistic Signature Scheme)

### DSA (Digital Signature Algorithm)

**Paramètres** :
- $p$ : premier (2048-3072 bits)
- $q$ : premier divisant $p-1$ (256 bits)
- $g$ : générateur d'ordre $q$ dans $\mathbb{Z}_p^*$

**Sign**$(sk, m)$ :
1. Choisir $k \xleftarrow{\$} \mathbb{Z}_q^*$ (**unique et aléatoire !**)
2. $r = (g^k \bmod p) \bmod q$
3. $s = k^{-1} \cdot (H(m) + x \cdot r) \bmod q$
4. Retourner $(r, s)$

**Vrfy**$(pk, m, (r, s))$ :
1. $w = s^{-1} \bmod q$
2. $u_1 = H(m) \cdot w \bmod q$, $u_2 = r \cdot w \bmod q$
3. $v = (g^{u_1} \cdot y^{u_2} \bmod p) \bmod q$
4. Accepter si $v = r$

⚠️ **CRITIQUE : Nonce Reuse Attack !**

Si deux signatures utilisent le même $k$ :
- $r_1 = r_2$
- De $s_1 - s_2 = k^{-1}(H(m_1) - H(m_2))$, on retrouve $k$
- De $s_1 = k^{-1}(H(m_1) + xr_1)$, on retrouve $x$ (clé secrète) !

**Cas réels** :
- PlayStation 3 (2010) : Hack complet via nonce constant
- Android Bitcoin wallets (2013) : Vol de Bitcoins

### ECDSA (Elliptic Curve DSA)

**Variante de DSA** sur courbes elliptiques :
- Même algorithme mais opérations sur courbe
- Clés plus courtes : 256 bits (ECDSA) ≈ 3072 bits (DSA)
- Plus rapide

**Courbes standard** :
- **NIST P-256, P-384, P-521** : Standards FIPS (TLS)
- **secp256k1** : Bitcoin, Ethereum

### EdDSA (Ed25519)

**Moderne et recommandé** :
- ✅ Très rapide (~10× plus rapide que RSA)
- ✅ Résistant aux side-channels
- ✅ Pas de nonce aléatoire (dérivé du message + clé)
- ✅ Clés 256 bits
- ✅ Utilisé dans SSH, Signal, Tor

---

# Chapitre 5 : Communication Anonyme

## Définitions d'Anonymat

### Types d'Anonymat

| Type | Définition |
|------|------------|
| **Sender anonymity** | Impossible d'identifier l'émetteur |
| **Receiver anonymity** | Impossible d'identifier le destinataire |
| **Unlinkability** | Impossible de relier deux messages du même émetteur |

### Adversaires

**Modèles de menace** :
1. **Passive** : Observe le trafic réseau
2. **Active** : Peut modifier/injecter/supprimer des paquets
3. **Global** : Observe tout le réseau
4. **Local** : Observe seulement certains liens

## Mixnets (Chaum 1981)

### Mix de Chaum

**Principe** : Serveurs intermédiaires qui mélangent les messages.

**Protocole** (3 mixes) :
1. Alice chiffre pour Mix 3 : $E_3(m, \text{dest})$
2. Alice chiffre pour Mix 2 : $E_2(E_3(m, \text{dest}), \text{Mix3})$
3. Alice chiffre pour Mix 1 : $E_1(E_2(E_3(m, \text{dest}), \text{Mix3}), \text{Mix2})$
4. Envoie à Mix 1

**Chaque Mix** :
- Déchiffre sa couche
- Attend d'accumuler $N$ messages (batch)
- Mélange aléatoirement
- Envoie au prochain hop

**Propriétés** :
- ✅ Anonymat si **au moins 1 mix honnête**
- ✅ Unlinkability (si batches suffisamment grands)
- ❌ **Haute latence** (attente du batch)

### Attaques sur Mixnets

**Flushing attack** :
- Adversaire injecte beaucoup de messages
- Force le mix à vider son batch
- Peut lier entrées/sorties

**(n-1) attack** :
- Adversaire contrôle tous les messages sauf 1 dans un batch
- Identifie le message cible facilement

**Tagging attack** :
- Adversaire modifie un ciphertext
- Observe quel message sort modifié

## Onion Routing / Tor

### Principe

**Différence avec mixnets** :
- Pas de batching (faible latence)
- Circuit persistant (plusieurs messages)
- Chiffrement en couches (oignon)

### Protocole Tor Simplifié

**Établissement de circuit (3 relais)** :
1. Alice → Guard : Négociation clé DH → $k_1$
2. Alice → Middle (via Guard) : Négociation clé DH → $k_2$
3. Alice → Exit (via Guard, Middle) : Négociation clé DH → $k_3$

**Envoi de message** :
1. Alice construit oignon : $E_{k_1}(E_{k_2}(E_{k_3}(m)))$
2. Guard déchiffre couche 1, envoie à Middle
3. Middle déchiffre couche 2, envoie à Exit
4. Exit déchiffre couche 3, envoie $m$ au destinataire

### Architecture Tor

**Composants** :
- **Directory Authorities** : Liste des relais disponibles (consensus)
- **Guard nodes** : Premier relais (stable, évite attaques temporelles)
- **Middle relays** : Relais intermédiaires
- **Exit nodes** : Dernier relais (sortie vers Internet)
- **Hidden services** (.onion) : Serveurs anonymes

**Propriétés** :
- ✅ Faible latence (~2-3× connexion directe)
- ✅ ~7000 relais, ~2 millions d'utilisateurs
- ⚠️ Exit node voit trafic en clair (sauf HTTPS)
- ⚠️ Vulnérable si adversaire global (traffic correlation)

### Attaques sur Tor

**Traffic correlation** :
- Adversaire observe entrée et sortie du circuit
- Corrélation temporelle des paquets
- Peut identifier utilisateur

**Website fingerprinting** :
- Analyser taille/timing des paquets
- Identifier site web visité (même avec HTTPS + Tor)
- Précision ~90% en laboratoire

**Sybil attack** :
- Adversaire lance beaucoup de relais malveillants
- Augmente probabilité d'être dans le circuit

**Défenses** :
- Choisir circuits aléatoirement (résistance Sybil)
- Padding/dummy traffic (contre fingerprinting)
- Éviter JavaScript (contre de-anonymisation)

### Hidden Services (.onion)

**Principe** : Serveur accessible uniquement via Tor

**Protocole** :
1. Service choisit introduction points et rendezvous points
2. Service publie descripteur dans DHT Tor
3. Client cherche descripteur, contacte introduction point
4. Rendez-vous établi avec circuit à double sens

**Propriétés** :
- ✅ Serveur anonyme (adresse .onion non localisable)
- ✅ Pas besoin de certificat SSL
- ❌ Plus lent (6 hops au total)

## Alternatives

### I2P (Invisible Internet Project)

- Réseau overlay complet (pas seulement proxy comme Tor)
- Tous les participants sont relais
- Optimisé pour hidden services

### Mixminion

- Mix protocol moderne
- Support réponses anonymes
- Haute latence (email anonyme)

### Private Information Retrieval (PIR)

- Requêter base de données sans révéler requête
- Coût computationnel élevé
- Applications : DNS privé, recherche de certificats

---

# Formules Essentielles

## Algèbre Modulaire

$$a \equiv b \pmod{n} \iff n \mid (a - b)$$

**Inverse modulaire** : $a \cdot a^{-1} \equiv 1 \pmod{n}$

**Théorème d'Euler** : Si $\gcd(a,n) = 1$, alors $a^{\phi(n)} \equiv 1 \pmod{n}$

**Petit théorème de Fermat** : Si $p$ premier, $a^{p-1} \equiv 1 \pmod{p}$

## Probabilités

**Indépendance** : $\Pr[A \cap B] = \Pr[A] \cdot \Pr[B]$

**Probabilité conditionnelle** : $\Pr[A \mid B] = \frac{\Pr[A \cap B]}{\Pr[B]}$

**Loi des probabilités totales** : $\Pr[A] = \sum_i \Pr[A \mid B_i] \cdot \Pr[B_i]$

## Sécurité

**Avantage** : $\text{Adv}(\mathcal{A}) = \left| \Pr[\mathcal{A} \text{ gagne}] - \frac{1}{2} \right|$

**Négligeable** : $\epsilon(\lambda) = o(1/\lambda^c)$ pour tout $c > 0$

---

# Attaques à Connaître

## Attaques Cryptographiques

| Attaque | Cible | Description | Mitigation |
|---------|-------|-------------|------------|
| **Two-Time Pad** | OTP, Stream cipher | Réutilisation nonce/clé | Nonce unique |
| **Birthday attack** | Hash | Trouver collision en $2^{n/2}$ | Hash ≥256 bits |
| **Length extension** | Merkle-Damgård | $H(m) \Rightarrow H(m \| \text{suffix})$ | HMAC, SHA-3 |
| **Padding oracle** | CBC + MAC | Devine padding via erreurs | Encrypt-then-MAC |
| **Nonce reuse (DSA)** | DSA/ECDSA | Récupère clé secrète | Nonce dérivé |
| **Chosen ciphertext** | RSA textbook, ElGamal | Malléabilité | OAEP, AEAD |
| **Man-in-the-Middle** | DH | Intercepte échange | Authenticated DH |
| **Small exponent** | RSA | $e=3$ + petit $m$ | OAEP padding |

## Attaques Réseau (Anonymat)

| Attaque | Cible | Description | Mitigation |
|---------|-------|-------------|------------|
| **Traffic correlation** | Tor | Corrélation temporelle entrée/sortie | Padding, cover traffic |
| **Website fingerprinting** | Tor | Identifie site via taille/timing | Padding, multiplexing |
| **(n-1) attack** | Mixnet | Contrôle tous messages sauf 1 | Batches grands, réputation |
| **Tagging attack** | Mixnet | Modifie message pour tracer | Authentification |
| **Sybil attack** | P2P, Tor | Lance beaucoup de nœuds | Sélection aléatoire, réputation |

---

# Bonnes Pratiques

## ✅ À FAIRE

### Clés et Nonces
- ✅ Générer clés avec RNG cryptographique (`secrets`, `/dev/urandom`)
- ✅ Clés ≥ 128 bits (symétrique), ≥ 2048 bits (RSA), ≥ 256 bits (ECC)
- ✅ Nonce/IV unique pour chaque message
- ✅ Renouveler clés régulièrement

### Primitives
- ✅ **Chiffrement** : AES-256-GCM, ChaCha20-Poly1305
- ✅ **Hash** : SHA-256, SHA-3, BLAKE3
- ✅ **MAC** : HMAC-SHA256
- ✅ **Signatures** : Ed25519, RSA-PSS-2048+, ECDSA-P256
- ✅ **Échange de clés** : ECDH-X25519, DH-2048+

### Composition
- ✅ **AEAD obligatoire** (GCM, Poly1305, CCM)
- ✅ Si composition manuelle : **Encrypt-then-MAC**
- ✅ Chiffrement hybride pour messages longs (RSA-OAEP + AES-GCM)

### Développement
- ✅ Utiliser bibliothèques auditées (OpenSSL, libsodium, PyCA/cryptography)
- ✅ Constant-time comparisons (MACs, passwords)
- ✅ Effacer clés en mémoire après usage
- ✅ Suivre standards NIST, ANSSI, IETF RFCs

## ❌ À ÉVITER ABSOLUMENT

### Algorithmes Cassés
- ❌ MD5, SHA-1 (collisions trouvées)
- ❌ DES, 3DES (clés trop courtes)
- ❌ RC4 (biais statistiques)
- ❌ RSA < 2048 bits

### Modes et Constructions Dangereux
- ❌ **ECB mode** (révèle patterns)
- ❌ Chiffrement sans authentification
- ❌ RSA textbook (pas de padding)
- ❌ CBC-MAC pour longueurs variables
- ❌ $H(k \| m)$ comme MAC (length extension)

### Erreurs Courantes
- ❌ Réutiliser nonce/IV
- ❌ Nonce/IV prévisible
- ❌ Clés dérivées de passwords faibles
- ❌ Comparer MACs/hashes avec `==` (timing attack)
- ❌ Implémenter sa propre crypto
- ❌ Générer aléatoire avec `random.random()` (pas crypto)

### Gestion des Erreurs
- ❌ Messages d'erreur différents (padding oracle)
- ❌ Timing différent selon erreur
- ❌ Décrypter avant de vérifier MAC

---

# Résumé par Niveau de Sécurité

## Sécurité Parfaite (Théorique)
- **One-Time Pad** : Seul chiffrement prouvé parfaitement sécurisé
- Clé aussi longue que message, usage unique
- Utilisé : Ligne rouge Moscou-Washington (guerre froide)

## Sécurité Computationnelle (Pratique)

### Symétrique
- **Chiffrement** : AES-256-GCM (standard), ChaCha20-Poly1305 (mobile)
- **Hash** : SHA-256 (standard), BLAKE3 (moderne)
- **MAC** : HMAC-SHA256

### Asymétrique
- **Échange clés** : ECDH-X25519 (recommandé), DH-3072
- **Chiffrement** : RSA-OAEP-2048+, ECIES
- **Signatures** : Ed25519 (recommandé), RSA-PSS-2048+, ECDSA-P256

### Composition
- **AEAD** : AES-GCM, ChaCha20-Poly1305, AES-CCM, ASCON (IoT)
- **Hybride** : RSA-OAEP + AES-GCM

## Anonymat (Propriétés Différentes)
- **Faible latence** : Tor (navigation web)
- **Haute latence** : Mixnets (email anonyme)
- **Hidden services** : .onion (serveurs anonymes)

---

# Checklist Avant l'Examen

## Concepts Théoriques
- [ ] Définir sécurité parfaite (Shannon)
- [ ] Théorème de Shannon ($|\mathcal{K}| \geq |\mathcal{M}|$)
- [ ] Distinguer PRG, PRF, PRP
- [ ] Jeux de sécurité : IND-CPA, UF-CMA, CDH, DDH
- [ ] Paradoxe des anniversaires ($2^{n/2}$)
- [ ] Construction Merkle-Damgård + théorème

## Attaques
- [ ] Two-Time Pad (réutilisation nonce)
- [ ] Birthday attack sur hash
- [ ] Length extension (Merkle-Damgård)
- [ ] Padding oracle (CBC + MAC-then-Encrypt)
- [ ] Nonce reuse (DSA/ECDSA → clé secrète !)
- [ ] Man-in-the-Middle (DH)
- [ ] Traffic correlation (Tor)

## Protocoles
- [ ] One-Time Pad : Enc, Dec, propriétés
- [ ] Modes AES : ECB ❌, CBC ✅, CTR ✅ (différences)
- [ ] HMAC : Construction, pourquoi sécurisé
- [ ] AES-GCM : Composants (CTR + GHASH)
- [ ] Diffie-Hellman : Protocole, sécurité (CDH), MITM
- [ ] RSA : Gen, Enc/Dec, pourquoi OAEP
- [ ] DSA : Sign, Vrfy, attaque nonce reuse
- [ ] Tor : Circuit, onion layers, hidden services

## Comparaisons
- [ ] Perfect vs Computational Security
- [ ] Stream cipher vs Block cipher
- [ ] MAC vs Hash vs Signature
- [ ] Symétrique vs Asymétrique (performances, usage)
- [ ] Encrypt-and-MAC vs MAC-then-Encrypt vs Encrypt-then-MAC
- [ ] Mixnets vs Tor (latence, anonymat)
- [ ] RSA vs ECC (tailles de clés, performance)

## Standards et Recommandations
- [ ] Algorithmes recommandés 2026
- [ ] Tailles de clés minimales (AES: 128, RSA: 2048, ECC: 256)
- [ ] Quand utiliser AEAD (toujours !)
- [ ] Composition sécurisée (Encrypt-then-MAC)
- [ ] Bibliothèques à utiliser (libsodium, PyCA)

---

# Conseils pour l'Examen

## Stratégie de Révision

1. **Revoir les notebooks** : Comprendre les implémentations
2. **Refaire les exercices** : Sans regarder les solutions
3. **Dessiner les schémas** : Modes AES, circuits Tor, constructions
4. **Mémoriser les attaques** : Conditions, impacts, mitigations
5. **Lister les standards** : Algorithmes recommandés par composant

## Pièges Courants

⚠️ **Ne pas confondre** :
- Hash ≠ MAC ≠ Signature
- Perfect security ≠ Computational security
- CDH ≠ DDH (DDH plus fort)
- Encrypt-and-MAC ≠ Encrypt-then-MAC
- RSA textbook ≠ RSA-OAEP

⚠️ **Toujours vérifier** :
- Nonce unique ?
- Authentification avant déchiffrement ?
- Clés suffisamment longues ?
- Algorithme non obsolète ?

## Questions Fréquentes

**"Pourquoi ne pas utiliser ECB ?"**
→ Déterministe, révèle patterns, pas CPA-secure

**"Pourquoi HMAC et pas juste H(k||m) ?"**
→ Length extension attack sur Merkle-Damgård

**"Pourquoi Encrypt-then-MAC ?"**
→ Seule composition toujours sécurisée, évite padding oracle

**"Pourquoi RSA-OAEP et pas RSA textbook ?"**
→ Textbook déterministe et malleable, pas CPA-secure

**"Comment éviter nonce reuse en DSA ?"**
→ Nonce dérivé déterministiquement (RFC 6979) ou Ed25519

**"Tor garantit-il l'anonymat ?"**
→ Contre adversaire local oui, contre adversaire global non (traffic correlation)

---

**Bonne chance pour l'examen !** 🎓

*N'oubliez pas : La sécurité repose sur le secret des clés, pas des algorithmes (Kerckhoffs).*
