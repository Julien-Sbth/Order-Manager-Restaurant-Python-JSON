import json
import os


def ecrire_Plat():
    nom = input("Veuillez entrer un nom de votre plat : ")
    description = input("Veuillez entrer une description de votre plat : ")
    prix = input("Veuillez entrer le prix de votre plat : ")
    categorie = input("Veuillez entrer la catégorie de votre plat : ")
    nom_fichier = "./json/plats.json"

    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'r') as fichier:
            data = json.load(fichier)
    else:
        data = []

    dernier_id = max([plats.get('id', 0) for plats in data], default=0)

    nouvel_id = dernier_id + 1

    nouveau_plat = {
        "id": nouvel_id,
        "nom": nom,
        "description": description,
        "prix": prix,
        "categorie": categorie
    }

    data.append(nouveau_plat)

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
