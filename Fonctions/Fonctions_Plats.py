import json
import os


def ecrire_Plat():
    nom = input("Veuillez entrer un nom de votre plat : ")
    description = input("Veuillez entrer une description de votre plat : ")
    prix = input("Veuillez entrer le prix de votre plat : ")
    categorie = input("Veuillez entrer la catégorie de votre plat : ")
    nom_fichier = "./json/plats.json"

    # Charger les données existantes s'il y en a
    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'r') as fichier:
            data = json.load(fichier)
    else:
        data = []

    # Trouver le dernier ID ou initialiser à 0 s'il n'y en a pas
    dernier_id = max([plats.get('id', 0) for plats in data], default=0)

    # Nouvel ID pour le nouveau plat
    nouvel_id = dernier_id + 1

    # Créer le dictionnaire pour le nouveau plat avec l'ID
    nouveau_plat = {
        "id": nouvel_id,
        "nom": nom,
        "description": description,
        "prix": prix,
        "categorie": categorie
    }

    # Ajouter le nouveau plat à la liste des plats
    data.append(nouveau_plat)

    # Enregistrer les données mises à jour dans le fichier JSON
    with open(nom_fichier, 'w') as fichier:
        json.dump(data, fichier, indent=4)

    print(f"Les informations du plat ont été sauvegardées dans {nom_fichier}.")



def afficher_dernier_message():
    nom_fichier = "./json/plats.json"

    try:
        if os.path.exists(nom_fichier):
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
                if data:
                    dernier_plat = data[-1]  # Récupère le dernier plat de la liste
                    print(f"Le dernier plat dans {nom_fichier} est : {dernier_plat}")
                else:
                    print(f"Aucun plat trouvé dans {nom_fichier}.")
        else:
            print(f"Le fichier {nom_fichier} n'existe pas.")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas.")
