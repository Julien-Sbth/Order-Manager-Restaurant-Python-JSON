import json
import os


class Clients:
    compteur_clients = 0

    @classmethod
    def charger_compteur(cls):
        try:
            with open("./compteur.json", 'r') as fichier:
                cls.compteur_clients = json.load(fichier)['compteur']
        except FileNotFoundError:
            cls.compteur_clients = 0

    def enregistrer_compteur(self):
        with open("./compteur.json", 'w') as fichier:
            json.dump({'compteur': self.compteur_clients}, fichier)

    @classmethod
    def trouver_dernier_identifiant(cls):
        if not os.path.exists("./json/clients.json"):
            return 0

        with open("./json/clients.json", 'r') as fichier:
            clients_existant = json.load(fichier)

        liste_identifiants = [client['identifiant'] for client in clients_existant]

        if not liste_identifiants:
            return 0
        else:
            return max(liste_identifiants)
