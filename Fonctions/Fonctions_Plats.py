import json
import os


class Plats:
    def __init__(self):
        pass

    @staticmethod
    def obtenir_plats():
        nom_fichier = "./json/plats.json"

        if os.path.exists(nom_fichier):
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
                return data
        else:
            return []

    @staticmethod
    def ecrire_plat():
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

        dernier_id = max([plat.get('id', 0) for plat in data], default=0)
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

    @staticmethod
    def afficher_message_par_id():
        nom_fichier = "./json/plats.json"

        plat_id = input("Veuillez entrer l'ID du plat pour afficher ses informations : ")

        try:
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
                if data and isinstance(data, list):
                    plat_trouve = False
                    for plat in data:
                        if str(plat['id']) == str(plat_id):
                            nom = plat.get("nom")
                            description = plat.get("description")
                            prix = plat.get("prix")
                            categorie = plat.get("categorie")

                            if nom and description and prix and categorie:
                                print(f"Informations du plat avec l'ID {plat_id} :")
                                print(f"Nom: {nom}")
                                print(f"Description: {description}")
                                print(f"Prix: {prix}")
                                print(f"Categorie: {categorie}")
                                plat_trouve = True
                                break

                    if not plat_trouve:
                        print(f"Aucun plat avec l'ID {plat_id} trouvé.")
                else:
                    print(f"Aucune donnée valide dans {nom_fichier}.")
        except FileNotFoundError:
            print(f"Le fichier {nom_fichier} n'existe pas.")

    @staticmethod
    def modifier_plat(plat_id, nouvelle_info):
        nom_fichier = "./json/plats.json"

        if os.path.exists(nom_fichier):
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
        else:
            print("Le fichier des plats n'existe pas.")
            return

        plat_trouve = False

        for plat in data:
            if str(plat['id']) == str(plat_id):
                plat.update(nouvelle_info)
                plat_trouve = True
                break

        if plat_trouve:
            with open(nom_fichier, 'w') as fichier:
                json.dump(data, fichier, indent=4)
            print(f"Informations du plat avec l'ID {plat_id} mises à jour.")
        else:
            print(f"Aucun plat avec l'ID {plat_id} trouvé.")

    @staticmethod
    def supprimer_plat(plat_id):
        nom_fichier = "./json/plats.json"

        if os.path.exists(nom_fichier):
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
        else:
            print("Le fichier des plats n'existe pas.")
            return

        plat_trouve = False

        for idx, plat in enumerate(data):
            if str(plat['id']) == str(plat_id):
                del data[idx]
                plat_trouve = True
                break

        if plat_trouve:
            with open(nom_fichier, 'w') as fichier:
                json.dump(data, fichier, indent=4)
            print(f"Le plat avec l'ID {plat_id} a été supprimé.")
        else:
            print(f"Aucun plat avec l'ID {plat_id} trouvé.")

    @staticmethod
    def afficher_commande_par_client_id(client_id):
        nom_fichier = "./json/commandes.json"

        commande_trouvee = False

        if os.path.exists(nom_fichier):
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
                for commande in data:
                    if str(commande['client_id']) == str(client_id):
                        print(f"Commande ID : {commande['id']}")
                        print(f"Client ID : {commande['client_id']}")
                        print(f"Plats commandés : {commande['plats']}")
                        commande_trouvee = True

                if not commande_trouvee:
                    print(f"Aucune commande trouvée pour le client avec l'ID {client_id}.")
        else:
            print(f"Le fichier des commandes {nom_fichier} n'existe pas.")

