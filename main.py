import json
import os


class Clients:
    compteur_clients = 0

    @classmethod
    def charger_compteur(cls):
        try:
            with open("compteur.json", 'r') as fichier:
                cls.compteur_clients = json.load(fichier)['compteur']
        except FileNotFoundError:
            cls.compteur_clients = 0

    def enregistrer_compteur(self):
        with open("compteur.json", 'w') as fichier:
            json.dump({'compteur': self.compteur_clients}, fichier)

    @classmethod
    def trouver_dernier_identifiant(cls):
        if not os.path.exists("clients.json"):
            return 0

        with open("clients.json", 'r') as fichier:
            clients_existant = json.load(fichier)

        liste_identifiants = [client['identifiant'] for client in clients_existant]

        if not liste_identifiants:
            return 0
        else:
            return max(liste_identifiants)


class Connexion(Clients):
    def __init__(self, prenom, mot_de_passe):
        self.prenom = prenom
        self.mot_de_passe = mot_de_passe

    def connecter(self):
        clients = self.obtenir_clients()
        for client in clients:
            if 'mot_de_passe' in client and client['prenom'] == self.prenom and client['mot_de_passe'] == self.mot_de_passe:
                print(f"Connecté en tant que client {self.prenom}.")
                return
        print("Connexion échouée. Veuillez vérifier vos informations.")



    @staticmethod
    def obtenir_clients():
        if not os.path.exists("clients.json"):
            return []
        else:
            with open("clients.json", 'r') as fichier:
                return json.load(fichier)


class Inscription(Clients):
    def __init__(self, prenom, nom, numero_telephone, mot_de_passe):
        self.prenom = prenom
        self.nom = nom
        self.numero_telephone = numero_telephone
        self.mot_de_passe = mot_de_passe
        self.identifiant = None
        self.charger_compteur()
        self.attribuer_identifiant()

    def attribuer_identifiant(self):
        dernier_identifiant = self.trouver_dernier_identifiant()

        dernier_identifiant = int(dernier_identifiant)

        self.identifiant = str(dernier_identifiant + 1)

        self.enregistrer_compteur()

        data = {
            "identifiant": self.identifiant,
            "prenom": self.prenom,
            "nom": self.nom,
            "numero_telephone": self.numero_telephone,
            "mot_de_passe": self.mot_de_passe
        }

        if not os.path.exists("clients.json"):
            clients_existant = []
        else:
            with open("clients.json", 'r') as fichier:
                clients_existant = json.load(fichier)

        clients_existant.append(data)

        with open("clients.json", 'w') as fichier:
            json.dump(clients_existant, fichier, indent=4)

        print(f"Le client {self.identifiant} a été ajouté à clients.json.")


def ecrire_message():
    message = input("Veuillez entrer votre plat : ")
    nom_fichier = "plats.json"

    data = {"message": message}

    with open(nom_fichier, 'w') as fichier:
        json.dump(data, fichier)

    print(f"Le message '{message}' a été sauvegardé dans {nom_fichier}.")


def afficher_dernier_message():
    nom_fichier = "plats.json"

    try:
        with open(nom_fichier, 'r') as fichier:
            data = json.load(fichier)
            message = data.get("message")
            if message:
                print(f"Le dernier message dans {nom_fichier} est : {message}")
            else:
                print(f"Aucun message trouvé dans {nom_fichier}.")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas.")


while True:
    choix_connexion = input("Souhaitez-vous vous connecter (C) ou vous inscrire (I) ? (C/I/q pour quitter) : ")

    if choix_connexion.lower() == "c":
        prenom = input("Entrez votre Prénom : ")
        mot_de_passe = input("Entrez votre Mot de passe : ")

        connexion = Connexion(prenom, mot_de_passe)
        connexion.connecter()

        connexion.connecter()
    elif choix_connexion.lower() == "i":
        prenom = input("Veuillez entrer votre prénom : ")
        nom = input("Veuillez entrer votre nom : ")
        numero_telephone = input("Veuillez entrer votre numéro de téléphone : ")
        mot_de_passe = input("Veuillez entrer votre mot de passe : ")

        inscription = Inscription(prenom, nom, numero_telephone, mot_de_passe)
    elif choix_connexion.lower() == "q":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez choisir C pour vous connecter, I pour vous inscrire ou q pour quitter.")

    while True:
        choix = input(
            "Que souhaitez-vous faire ? (1 pour écrire un message, 2 pour voir le dernier message, 3 pour afficher les clients, q pour quitter) : ")

        if choix == "1":
            ecrire_message()
        elif choix == "2":
            afficher_dernier_message()
        elif choix == "3":
            input("")
        elif choix.lower() == "q":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir 1, 2, 3, 4 ou q pour quitter.")