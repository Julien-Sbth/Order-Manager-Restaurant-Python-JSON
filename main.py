from Fonctions.Connexion import Connexion
from Fonctions.inscription import Inscription
from Fonctions.Fonctions_Plats import ecrire_Plat, afficher_dernier_message

while True:
    choix_connexion = input("Souhaitez-vous vous connecter (c) ou vous inscrire (i) ? (c/i/q pour quitter) : ")

    if choix_connexion.lower() == "c":
        prenom = input("Entrez votre Prénom : ")
        mot_de_passe = input("Entrez votre Mot de passe : ")

        connexion = Connexion(prenom, mot_de_passe)
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
        print("Choix invalide. Veuillez choisir c pour vous connecter, i pour vous inscrire ou q pour quitter.")

    while True:
        choix = input(
            "Que souhaitez-vous faire ? (1 pour écrire un plat, 2 pour voir le dernier plat, 3 pour afficher les "
            "clients, 4 pour modifier les informations d'un client, 5 pour supprimer un client q pour quitter) : ")

        if choix == "1":
            ecrire_Plat()
        elif choix == "2":
            afficher_dernier_message()
        elif choix == "3":
            input("")
        elif choix == "4":
            identifiant_a_modifier = input("Entrez l'identifiant du client à modifier : ")
            nouveau_prenom = input("Entrez le nouveau prenom : ")
            nouveau_nom = input("Entrez le nouveau nom : ")
            nouveau_numero_telephone = input("Entrez le nouveau numéro de téléphone : ")
            nouveau_mot_de_passe = input("Entrez le nouveau mot de passe : ")
            Connexion.modifier_infos_client(identifiant_a_modifier, nouveau_numero_telephone, nouveau_nom, nouveau_prenom, nouveau_mot_de_passe)
        elif choix == "5":
            identifiant_a_supprimer = input("Entrez l'identifiant du client à supprimer : ")
            Connexion.supprimer_client(identifiant_a_supprimer)
        elif choix.lower() == "q":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir 1, 2, 3, 4, 5 ou q pour quitter.")