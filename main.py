from Fonctions.Connexion import Connexion
from Fonctions.inscription import Inscription
from Fonctions.Fonctions_Plats import Plats
from Fonctions.Fonctions_Commandes import Commandes

while True:
    choix_connexion = input("Souhaitez-vous vous connecter (c) ou vous inscrire (i) ? (c/i/q pour quitter) : ")

    while choix_connexion.lower() not in ["c", "i"]:
        print("Choix invalide. Veuillez entrer 'c' pour connexion ou 'i' pour inscription.")
        choix_connexion = input("Veuillez choisir 'c' pour connexion ou 'i' pour inscription : ")

    if choix_connexion.lower() == "c":
        prenom = input("Entrez votre Prénom : ")
        mot_de_passe = input("Entrez votre Mot de passe : ")

        connexion = Connexion(prenom, mot_de_passe)
        connexion.connecter()

    elif choix_connexion.lower() == "i":

        prenom = input("Veuillez entrer votre prénom : ")
        nom = input("Veuillez entrer votre nom : ")

        while True:
            numero_telephone = input("Veuillez entrer votre numéro de téléphone : ")
            if numero_telephone.isdigit():
                break
            else:
                print("Le numéro de téléphone doit contenir uniquement des chiffres. Veuillez réessayer.")
        mot_de_passe = input("Veuillez entrer votre mot de passe : ")
        inscription = Inscription(prenom, nom, numero_telephone, mot_de_passe)

    elif choix_connexion.lower() == "q":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez choisir c pour vous connecter, i pour vous inscrire ou q pour quitter.")

    while True:
        print("1 Pour écrire un plat")
        print("2 Pour voir le dernier plat")
        print("3 Pour modifier un plat")
        print("4 Pour supprimer un plat")
        print("5 Pour visualiser les plats populaires")
        print("6 Pour afficher les commandes d'un client")
        print("7 Pour modifier les informations d'un client")
        print("8 Pour supprimer un client")
        print("9 Pour crée une commande pour un client")
        print("10 Pour afficher la commande d'un client")
        print("11 Pour exporter les commandes")
        print("12 Pour voir la facture d'un client")
        print("13 Pour enregistrer un nouveau client")
        print("14 Voir vos recommandations basé sur vos préférences")
        choix = input("Entrez votre choix (ou 'q' pour quitter) : ")

        if choix == "1":
            Plats.ecrire_plat()
        elif choix == "2":
            Plats.afficher_message_par_id()
        elif choix == "3":
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
        elif choix == "4":
            plat_a_supprimer = input("Entrez l'ID du plat à supprimer : ")
            Plats.supprimer_plat(plat_a_supprimer)
        elif choix == "5":
            plats_populaires = Plats.plats_populaires()
            if plats_populaires:
                print("Plats populaires :")
                for plat in plats_populaires:
                    print(
                        f"Nom: {plat["nom"]}, Description: {plat["description"]}, Prix: {plat["prix"]}, Categorie: {plat["categorie"]}")
            else:
                print("Aucun plat populaire trouvé.")
        elif choix == "6":
            client_id = input("Veuillez entrer l'ID du client pour afficher ses commandes : ")
            Plats.afficher_commande_par_client_id(client_id)
        elif choix == "7":
            identifiant_a_modifier = input("Entrez l'identifiant du client à modifier : ")
            nouveau_prenom = input("Entrez le nouveau prenom : ")
            nouveau_nom = input("Entrez le nouveau nom : ")
            nouveau_numero_telephone = input("Entrez le nouveau numéro de téléphone : ")
            nouveau_mot_de_passe = input("Entrez le nouveau mot de passe : ")
            Connexion.modifier_infos_client(identifiant_a_modifier, nouveau_numero_telephone, nouveau_nom,
                                            nouveau_prenom, nouveau_mot_de_passe)
        elif choix == "8":
            identifiant_a_supprimer = input("Entrez l'identifiant du client à supprimer : ")
            Connexion.supprimer_client(identifiant_a_supprimer)

        if choix == "9":
            client_id = input("Veuillez entrer l'ID du client pour lequel vous souhaitez créer une commande : ")
            plats_commandes = input("Entrez la liste des noms des plats commandés (séparés par des virgules) : ").split(
                ',')
            Commandes.creer_commande(client_id, plats_commandes)

        elif choix == "10":
            client_id = input("Veuillez entrer l'ID du client pour afficher sa commande : ")
            Commandes.afficher_commande_par_client_id(client_id)
        elif choix == "11":
            Commandes.exporter_commandes()
        elif choix == "12":
            commande_id = input("Veuillez entrer l'ID de la commande pour voir la facture : ")
            facture_associee = Commandes.obtenir_facture_par_commande_id(commande_id)
            print(facture_associee)

        elif choix == "13":
            prenom = input("Veuillez entrer votre prénom : ")
            nom = input("Veuillez entrer votre nom : ")
            numero_telephone = input("Veuillez entrer votre numéro de téléphone : ")
            mot_de_passe = input("Veuillez entrer votre mot de passe : ")

            inscription = Inscription(prenom, nom, numero_telephone, mot_de_passe)

        elif choix == "14":
            client_id = input("Veuillez entrer l'ID du client pour obtenir des recommandations : ")
            Commandes.Recommendation(client_id)

        elif choix.lower() == "q":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ou q pour quitter.")
