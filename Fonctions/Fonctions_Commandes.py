import json
import os
import csv


class Commandes:
    @staticmethod
    def obtenir_commandes():
        nom_fichier = "./json/commandes.json"

        if os.path.exists(nom_fichier):
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
                return data
        else:
            return []

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

    @staticmethod
    def creer_commande(client_id, plats_commandes):
        nom_fichier = "./json/commandes.json"

        if os.path.exists(nom_fichier):
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
        else:
            data = []

        dernier_id = max([commande.get('id', 0) for commande in data], default=0)
        nouvel_id = dernier_id + 1

        nouvelle_commande = {
            "id": nouvel_id,
            "client_id": client_id,
            "plats": plats_commandes
        }

        data.append(nouvelle_commande)

        with open(nom_fichier, 'w') as fichier:
            json.dump(data, fichier, indent=4)

        print(f"La commande pour le client avec l'ID {client_id} a été enregistrée.")

    @classmethod
    def exporter_commandes(cls):
        nom_fichier_json = "./json/commandes.json"
        nom_fichier_csv = "./export/donnees.csv"

        if os.path.exists(nom_fichier_json):
            with open(nom_fichier_json, 'r') as fichier_json:
                data = json.load(fichier_json)
        else:
            data = []

        with open(nom_fichier_csv, 'w', newline='', encoding='utf-8') as fichier_csv:
            writer = csv.writer(fichier_csv)
            if data:
                writer.writerow(
                    data[0].keys())
                for ligne in data:
                    writer.writerow(ligne.values())

        print(f"Les données ont été exportées vers '{nom_fichier_csv}'.")