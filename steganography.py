"""
Stéganographie LSB — Ayoub LADAME
But : cacher et révéler un message secret dans une image (usage éducatif)
Bibliothèque : Pillow
Installation : pip install Pillow
"""

from PIL import Image
import sys
import os

# ── Constantes ────────────────────────────────────────────────────────────────
DELIMITER = "###END###"  # marqueur de fin du message caché


# ════════════════════════════════════════════════════════════════════════════
# ENCODER — cacher un message dans une image
# ════════════════════════════════════════════════════════════════════════════
def encode(image_path: str, message: str, output_path: str):
    """Cache un message secret dans une image via la technique LSB."""

    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())

    # Ajouter le délimiteur au message
    full_message = message + DELIMITER

    # Convertir le message en binaire
    binary_message = ''.join(format(ord(c), '08b') for c in full_message)

    # Vérifier si l'image est assez grande
    max_bits = len(pixels) * 3
    if len(binary_message) > max_bits:
        print(f"[!] Erreur : l'image est trop petite pour ce message.")
        print(f"    Capacité max : {max_bits // 8} caractères")
        return

    # Modifier les bits LSB des pixels
    new_pixels = []
    bit_index = 0

    for pixel in pixels:
        r, g, b = pixel
        new_rgb = []

        for channel in [r, g, b]:
            if bit_index < len(binary_message):
                # Remplacer le bit le moins significatif
                new_channel = (channel & ~1) | int(binary_message[bit_index])
                bit_index += 1
            else:
                new_channel = channel
            new_rgb.append(new_channel)

        new_pixels.append(tuple(new_rgb))

    # Sauvegarder l'image modifiée
    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)
    print(f"[✓] Message caché avec succès dans : {output_path}")
    print(f"[i] Taille du message : {len(message)} caractères")


# ════════════════════════════════════════════════════════════════════════════
# DECODER — révéler le message caché
# ════════════════════════════════════════════════════════════════════════════
def decode(image_path: str):
    """Révèle le message secret caché dans une image."""

    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())

    # Extraire les bits LSB de chaque canal
    bits = []
    for pixel in pixels:
        for channel in pixel:
            bits.append(channel & 1)

    # Reconvertir les bits en caractères
    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(''.join(map(str, byte)), 2))
        message += char

        # Arrêter quand on trouve le délimiteur
        if message.endswith(DELIMITER):
            message = message[:-len(DELIMITER)]
            print(f"[✓] Message révélé : {message}")
            return message

    print("[!] Aucun message trouvé dans cette image.")
    return None


# ════════════════════════════════════════════════════════════════════════════
# MENU PRINCIPAL
# ════════════════════════════════════════════════════════════════════════════
def menu():
    print("=" * 45)
    print("   Stéganographie LSB — Ayoub LADAME")
    print("=" * 45)
    print("1. Cacher un message dans une image")
    print("2. Révéler un message caché")
    print("3. Quitter")
    print("=" * 45)

    choix = input("Votre choix : ").strip()

    if choix == "1":
        image_path  = input("Chemin de l'image source (ex: image.png) : ").strip()
        message     = input("Message à cacher : ").strip()
        output_path = input("Nom de l'image de sortie (ex: output.png) : ").strip()

        if not os.path.exists(image_path):
            print(f"[!] Image introuvable : {image_path}")
        else:
            encode(image_path, message, output_path)

    elif choix == "2":
        image_path = input("Chemin de l'image à analyser : ").strip()

        if not os.path.exists(image_path):
            print(f"[!] Image introuvable : {image_path}")
        else:
            decode(image_path)

    elif choix == "3":
        print("Au revoir !")
        sys.exit(0)

    else:
        print("[!] Choix invalide.")


# ── Lancement ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    while True:
        menu()
        print()