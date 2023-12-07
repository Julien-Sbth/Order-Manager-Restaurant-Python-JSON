from Fonctions.Connexion import Connexion
from Fonctions.inscription import Inscription
from Fonctions.Fonctions_Plats import Plats

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
            "6 pour modifier un plat, 7 pour supprimer un plat, q pour quitter) : ")

        if choix == "1":
            Plats.ecrire_plat()
        elif choix == "2":
            Plats.afficher_message_par_id()
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
        elif choix.lower() == "q":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir 1, 2, 3, 4, 5, 6 pour modifier un plat, 7 pour supprimer un plat,"
                  "ou q pour quitter.")