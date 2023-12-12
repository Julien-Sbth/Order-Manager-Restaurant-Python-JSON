import json
import os
from Fonctions.clients import Clients


class Connexion(Clients):
    def __init__(self, prenom, mot_de_passe):
        self.prenom = prenom
        self.mot_de_passe = mot_de_passe

    def connecter(self):
        while True:
            clients = self.obtenir_clients()
            for client in clients:
                if 'mot_de_passe' in client and client['prenom'] == self.prenom and client['mot_de_passe'] == self.mot_de_passe:
                    print(f"Connecté en tant que client {self.prenom}.")
                    return
            print("Connexion échouée. Veuillez vérifier vos informations.")
            self.prenom = input("Entrez votre prénom : ")
            self.mot_de_passe = input("Entrez votre mot de passe : ")

    @staticmethod
    def modifier_infos_client(identifiant, nouveau_prenom, nouveau_nom, nouveau_telephone, nouveau_mot_de_passe):
        clients = Connexion.obtenir_clients()

        for client in clients:
            if client['prenom'] == identifiant:
                client['prenom'] = nouveau_prenom
                client['nom'] = nouveau_nom
                client['numero_telephone'] = nouveau_telephone
                client['mot_de_passe'] = nouveau_mot_de_passe

                # Enregistrer les modifications dans le fichier JSON
                with open("./json/clients.json", 'w') as fichier:
                    json.dump(clients, fichier, indent=4)
                print(f"Informations du client {identifiant} mises à jour.")
                return

        print(f"Aucun client avec l'identifiant {identifiant} trouvé.")

    @staticmethod
    def supprimer_client(identifiant):
        clients = Connexion.obtenir_clients()

        for idx, client in enumerate(clients):
            if client['prenom'] == identifiant:
                del clients[idx]
                with open("./json/clients.json", 'w') as fichier:
                    json.dump(clients, fichier, indent=4)
                print(f"Le client {identifiant} a été supprimé.")
                return

        print(f"Aucun client avec l'identifiant {identifiant} trouvé.")

    @staticmethod
    def obtenir_clients():
        if not os.path.exists("./json/clients.json"):
            return []
        else:
            with open("./json/clients.json", 'r') as fichier:
                return json.load(fichier)
