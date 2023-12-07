from Fonctions.Connexion import Connexion
from Fonctions.inscription import Inscription
from Fonctions.Fonctions_Plats import Plats
from Fonctions.Fonctions_Commandes import Commandes

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
            "commandes d'un client, 4 pour modifier les informations d'un client, 5 pour supprimer un client, "
            "6 pour modifier un plat, 7 pour supprimer un plat, 8 pour crée une commande, 9 pour afficher la commande "
            "d'un client q pour quitter) : ")

        if choix == "1":
            Plats.ecrire_plat()
        elif choix == "2":
            Plats.afficher_message_par_id()
        elif choix == "3":
            client_id = input("Veuillez entrer l'ID du client pour afficher ses commandes : ")
            Plats.afficher_commande_par_client_id(client_id)
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
        elif choix == "6":
            plat_a_modifier = input("Entrez l'ID du plat à modifier : ")
            nouveau_nom = input("Entrez le nouveau nom : ")
            nouvelle_description = input("Entrez la nouvelle description : ")

            while True:
                nouveau_prix = input("Entrez le nouveau prix : ")
                try:
                    nouveau_prix = float(nouveau_prix)
                    break
                except ValueError:
                    print("Le prix doit être un nombre.")

            nouvelle_categorie = input("Entrez la nouvelle catégorie : ")

            Plats.modifier_plat(plat_a_modifier, {
                "nom": nouveau_nom,
                "description": nouvelle_description,
                "prix": nouveau_prix,
                "categorie": nouvelle_categorie
            })
        elif choix == "7":
            plat_a_supprimer = input("Entrez l'ID du plat à supprimer : ")
            Plats.supprimer_plat(plat_a_supprimer)
        elif choix == "8":
            client_id = input("Veuillez entrer l'ID du client pour lequel vous souhaitez créer une commande : ")
            plats_commandes = input("Entrez la liste des ID des plats commandés (séparés par des virgules) : ").split(
                ',')
            Commandes.creer_commande(client_id, plats_commandes)
        elif choix == "9":
            client_id = input("Veuillez entrer l'ID du client pour afficher sa commande : ")
            Commandes.afficher_commande_par_client_id(client_id)
        elif choix.lower() == "q":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir 1, 2, 3, 4, 5, 6 pour modifier un plat, 7 pour supprimer un plat,"
                  "ou q pour quitter.")