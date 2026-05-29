# 🔐 Stéganographie LSB en Python

Projet réalisé par **Ayoub LADAME**

## 📌 Description

Ce projet implémente une technique simple de **stéganographie LSB (Least Significant Bit)** en Python.
Il permet de :

* 📥 **Cacher** un message secret dans une image
* 📤 **Révéler** un message caché dans une image

La méthode utilisée modifie les bits les moins significatifs des pixels RGB afin d’y stocker discrètement des données.

> ⚠️ Projet à but éducatif uniquement.

---

# 🛠 Technologies utilisées

* **Python 3**
* Bibliothèque : **Pillow**

---

# 📦 Installation

## 1. Cloner le projet

```bash
git clone https://github.com/ayoubladame458-sys/steganography-lsb.git
cd steganography-lsb
```

## 2. Installer les dépendances

```bash
pip install Pillow
```

---

# ▶️ Exécution du programme

```bash
python steganography.py
```

---

# 📋 Fonctionnalités

## 🔒 Cacher un message

Le programme :

1. Ouvre une image
2. Convertit le message en binaire
3. Modifie les bits LSB des pixels
4. Sauvegarde une nouvelle image contenant le message caché

### Exemple

```text
Message : Bonjour
Image source : image.png
Image de sortie : secret.png
```

---

## 🔓 Révéler un message

Le programme :

1. Lit les bits LSB de l’image
2. Reconstruit les caractères
3. Détecte le délimiteur spécial `###END###`
4. Affiche le message secret

---

# 🧠 Principe du LSB

LSB signifie **Least Significant Bit**.

Chaque pixel RGB contient 3 canaux :

* Rouge (R)
* Vert (G)
* Bleu (B)

Le programme modifie uniquement le dernier bit de chaque canal, ce qui rend les changements invisibles à l’œil humain.

### Exemple

Avant :

```text
10110010
```

Après insertion d’un bit :

```text
10110011
```

La différence visuelle est pratiquement impossible à remarquer.

---

# 📁 Structure du projet

```text
steganography-lsb/
│
├── steganography.py
├── README.md
├── image.png
└── output.png
```

---

# ⚙️ Fonctions principales

## `encode(image_path, message, output_path)`

Cache un message dans une image.

### Paramètres

| Paramètre     | Description     |
| ------------- | --------------- |
| `image_path`  | Image source    |
| `message`     | Message secret  |
| `output_path` | Image de sortie |

---

## `decode(image_path)`

Révèle le message caché dans une image.

### Paramètres

| Paramètre    | Description      |
| ------------ | ---------------- |
| `image_path` | Image à analyser |

---

# 🖥 Exemple d’utilisation

## Menu principal

```text
=============================================
   Stéganographie LSB — Ayoub LADAME
=============================================
1. Cacher un message dans une image
2. Révéler un message caché
3. Quitter
=============================================
```

---

# ⚠️ Limitations

* Fonctionne uniquement avec les images RGB
* Les images trop petites ne peuvent pas contenir de longs messages
* La compression d’image peut détruire les données cachées

> Il est recommandé d’utiliser des fichiers `.png`

---

# 📚 Concepts abordés

* Manipulation d’images
* Bits et représentation binaire
* Cryptographie basique
* Cybersécurité
* Python I/O

---

# 👨‍💻 Auteur

**Ayoub LADAME**
Étudiant en Génie Informatique — Cybersécurité

GitHub : https://github.com/ayoubladame458-sys

---

# 📜 Licence

Projet open-source à usage éducatif.
