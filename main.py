from controllers import TournoiController
from serialization import Serialization

if __name__ == "__main__":
    print("\n*** TOURNOI INTERNATIONAL D'ECHECS ***")

    def menu_principal():
        controller = TournoiController()
        tournois = []  # Liste pour stocker tous les tournois

        while True:
            print("\nMenu principal :\n")
            print("1. Créer un tournoi")
            print("2. Ajouter des joueurs")
            print("3. Jouer le tournoi")
            print("4. Afficher classement")
            print("5. Voir rapports")
            print("6. Charger un tournoi existant")
            print("7. Sauvegarder")
            print("8. Quitter")

            choix = input("\nChoisissez une option : ")
            if not choix.isdigit() or int(choix) not in range(1, 9):
                print("\nOption invalide. Veuillez entrer un chiffre entre 1 et 8.")
                continue

            if choix == "1":
                controller.creer_tournoi()
                tournois.append(controller.tournoi)
            elif choix == "2":
                if controller.tournoi:
                    controller.ajouter_joueurs()
                else:
                    print("\nAucun tournoi n'a été créé. Veuillez d'abord créer un tournoi.")
            elif choix == "3":
                if controller.tournoi:
                    controller.jouer_tournoi()
                else:
                    print("\nAucun tournoi n'a été créé. Veuillez d'abord créer un tournoi.")
            elif choix == "4":
                if controller.tournoi:
                    controller.afficher_classement()
                else:
                    print("\nAucun tournoi n'a été créé. Veuillez d'abord créer un tournoi.")
            elif choix == "5":
                if controller.tournoi:
                    print("\nRapports disponibles :")
                    print("\n1. Liste de tous les joueurs (ordre alphabétique)")
                    print("2. Liste de tous les tournois")
                    print("3. Détail du tournoi en cours")
                    print("4. Annuler")

                    sous_choix = input("\nChoisissez une option : ")
                    if sous_choix == "1":
                        controller.rapport_joueurs()
                    elif sous_choix == "2":
                        controller.rapport_tournois()
                    elif sous_choix == "3":
                        controller.rapport_details_tournoi()
                    elif sous_choix == "4":
                        continue
                    else:
                        print("Option invalide.")
                else:
                    print("\nAucun tournoi n'a été créé. Veuillez d'abord créer un tournoi.")
            elif choix == "6":
                tournoi_charge = Serialization.charger_donnees()
                if tournoi_charge:
                    controller.tournoi = tournoi_charge
                    tournois.append(controller.tournoi)
                    print(f"\nLe tournoi '{controller.tournoi.nom}' a été chargé avec succès.")
                else:
                    print("Échec du chargement du tournoi.")
            elif choix == "7":  # Sauvegarder
                if not tournois:
                    print("\nAucun tournoi à sauvegarder.")
                else:
                    Serialization.sauvegarder_donnees(controller.tournoi)
                    print("Données sauvegardées avec succès.")
            elif choix == "8":
                print("\nAu revoir !")
                break


    menu_principal()