# lancer la commande python renommer_fichiers.py chemin_du_dossier prefixe pour nommer les fichier prefixe1 prefixe2 etc

import os
import sys

def renommer_fichiers(dossier, prefixe):
    # Vérifier si le dossier existe
    if not os.path.exists(dossier):
        print(f"Le dossier '{dossier}' n'existe pas.")
        return

    # Obtenir la liste des fichiers dans le dossier
    fichiers = os.listdir(dossier)

    # Parcourir la liste des fichiers et les renommer
    for i, fichier in enumerate(fichiers, start=1):
        # Séparer le nom de fichier et l'extension
        nom_fichier, extension = os.path.splitext(fichier)

        # Construire le nouveau nom de fichier avec le préfixe et le numéro
        nouveau_nom = f"{prefixe}{i}{extension}"

        # Construire le chemin complet pour l'ancien et le nouveau fichier
        ancien_chemin = os.path.join(dossier, fichier)
        nouveau_chemin = os.path.join(dossier, nouveau_nom)

        # Renommer le fichier
        os.rename(ancien_chemin, nouveau_chemin)

        print(f"Renommage de '{fichier}' en '{nouveau_nom}'.")

if __name__ == "__main__":
    # Vérifier si les arguments nécessaires sont fournis
    if len(sys.argv) != 3:
        print("Usage: python script.py <dossier> <prefixe>")
        sys.exit(1)

    # Récupérer les arguments
    dossier = sys.argv[1]
    prefixe = sys.argv[2]

    # Appeler la fonction de renommage
    renommer_fichiers(dossier, prefixe)
