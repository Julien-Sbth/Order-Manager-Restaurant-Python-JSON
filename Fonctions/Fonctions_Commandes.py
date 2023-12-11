import json
import os
import csv
import random


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
                        print(f"Commande ID : {commande['id_commande']}")
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

        if os.path.exists(nom_fichier) and os.path.getsize(nom_fichier) > 0:
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
        else:
            data = []

        dernier_id = max([commande.get('id_commande', 0) for commande in data], default=0)
        nouvel_id = dernier_id + 1

        nom_fichier_plats = "./json/plats.json"
        total_plats = 0.0

        if os.path.exists(nom_fichier_plats) and os.path.getsize(nom_fichier_plats) > 0:
            with open(nom_fichier_plats, 'r') as fichier_plats:
                plats = json.load(fichier_plats)
                plats_dict = {plat['nom']: float(plat['prix'][:-2]) for plat in plats}

                for plat_commande in plats_commandes:
                    if plat_commande in plats_dict:
                        total_plats += plats_dict[plat_commande]

        nouvelle_commande = {
            "id_commande": nouvel_id,
            "client_id": client_id,
            "plats": plats_commandes,
            "facture": round(total_plats, 2)
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

    @staticmethod
    def obtenir_facture_par_commande_id(commande_id):
        nom_fichier = "./json/commandes.json"

        if os.path.exists(nom_fichier):
            with open(nom_fichier, 'r') as fichier:
                data = json.load(fichier)
                for commande in data:
                    if str(commande['id_commande']) == str(commande_id):
                        return commande.get('facture', "Aucune facture associée à cette commande.")
                return "Aucune facture associée à cette commande."
        else:
            return "Le fichier des commandes n'existe pas."
