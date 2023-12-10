import json
import os
from Fonctions.clients import Clients


class Inscription(Clients):
    def __init__(self, prenom, nom, numero_telephone, mot_de_passe):
        self.prenom = prenom
        self.nom = nom
        self.numero_telephone = numero_telephone
        self.mot_de_passe = mot_de_passe
        self.identifiant = None
        self.attribuer_identifiant()

    def attribuer_identifiant(self):
        dernier_identifiant = self.trouver_dernier_identifiant()

        dernier_identifiant = int(dernier_identifiant)

        self.identifiant = str(dernier_identifiant + 1)

        data = {
            "identifiant": self.identifiant,
            "prenom": self.prenom,
            "nom": self.nom,
            "numero_telephone": self.numero_telephone,
            "mot_de_passe": self.mot_de_passe
        }

        if not os.path.exists("./json/clients.json"):
            clients_existant = []
        else:
            with open("./json/clients.json", 'r') as fichier:
                clients_existant = json.load(fichier)

        clients_existant.append(data)

        with open("./json/clients.json", 'w') as fichier:
            json.dump(clients_existant, fichier, indent=4)

        print(f"Le client {self.identifiant} a été ajouté à clients.json.")
