import json
import os


class Clients:
    @classmethod
    def trouver_dernier_identifiant(cls):
        if not os.path.exists("./json/clients.json"):
            return 0

        with open("./json/clients.json", 'r') as fichier:
            clients_existant = json.load(fichier)

        if not clients_existant:
            return 0
        else:
            derniers_clients = sorted(clients_existant, key=lambda x: x.get('identifiant', 0), reverse=True)
            dernier_identifiant = derniers_clients[0]['identifiant']
            return dernier_identifiant
