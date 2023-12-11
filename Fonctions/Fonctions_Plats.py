import json
import os
from collections import Counter
import random


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
        while True:
            prix = input("Veuillez entrer le prix de votre plat : ")
            try:
                prix = float(prix)
                break
            except ValueError:
                print("Veuillez entrer un nombre pour le prix.")

        prix_str = f"{prix:.3f} €"
        categorie = input("Veuillez entrer la catégorie de votre plat : ")
        nom_fichier = "./json/plats.json"

        if os.path.exists(nom_fichier) and os.path.getsize(nom_fichier) > 0:
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
        else:
            data = []

        dernier_id = max([int(plat.get("id", 0)) for plat in data], default=0)
        nouvel_id = str(dernier_id + 1)

        nouveau_plat = {
            "id": nouvel_id,
            "nom": nom,
            "description": description,
            "prix": prix_str,
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
                        if str(plat["id"]) == str(plat_id):
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
                        print(f"Commande ID : {commande['id_commande']}")
                        print(f"Client ID : {commande['client_id']}")
                        print(f"Plats commandés : {commande['plats']}")
                        commande_trouvee = True

                if not commande_trouvee:
                    print(f"Aucune commande trouvée pour le client avec l'ID {client_id}.")
        else:
            print(f"Le fichier des commandes {nom_fichier} n'existe pas.")

    @staticmethod
    def plats_populaires(nb_plats=5):
        nom_fichier_commandes = "./json/commandes.json"
        nom_fichier_plats = "./json/plats.json"

        if os.path.exists(nom_fichier_commandes) and os.path.exists(nom_fichier_plats):
            with open(nom_fichier_commandes, 'r') as fichier_commandes, open(nom_fichier_plats, 'r') as fichier_plats:
                commandes = json.load(fichier_commandes)
                plats = json.load(fichier_plats)

                plats_commandes = [plat_id for commande in commandes for plat_id in commande.get('plats', [])]
                compteur_plats = Counter(plats_commandes)

                plats_populaires_ids = [plat_id for plat_id, count in compteur_plats.most_common(nb_plats)]
                details_plats_populaires = [plat for plat in plats if plat['nom'] in plats_populaires_ids]

                random.shuffle(details_plats_populaires)

                plats_aleatoires = random.sample(details_plats_populaires, min(len(details_plats_populaires), nb_plats))

                return plats_aleatoires
        else:
            print("Les fichiers de commandes ou de plats n'existent pas.")
