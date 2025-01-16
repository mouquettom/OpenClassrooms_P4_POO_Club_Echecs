from models import Joueur, Match, Tournoi
from views import TournoiView
from serialization import Serialization
from random import shuffle

class TournoiController:
    def __init__(self, tournoi=None):
        self.tournoi = tournoi

    def creer_tournoi(self):
        nom, lieu, date_debut, date_fin = TournoiView.demander_info_tournoi()

        confirmation = ""
        while confirmation not in ["y", "n"]:
            confirmation = input("\nConfirmez-vous la création de ce tournoi (y/n) ? ")
        if confirmation == "y":
            self.tournoi = Tournoi(nom, lieu, date_debut, date_fin)
            Serialization.sauvegarder_donnees(self.tournoi)
            print(f"Le Tournoi '{self.tournoi.nom}' a bien été créé.")
        else:
            print("Saisie annulée.")


    def ajouter_joueurs(self):
        if self.tournoi is None:
            print("Aucun tournoi chargé. Veuillez charger ou créer un tournoi avant d'ajouter des joueurs.")
            return

        while True:
            choix = input("\nSouhaitez-vous ajouter un joueur (y/n) ? ").strip().lower()
            if choix == "n":
                break
            elif choix == "y":
                # Récupérer les identifiants déjà utilisés
                identifiants_utilises = [joueur.id for joueur in self.tournoi.joueurs]

                # Demander un identifiant unique
                id = TournoiView.demander_identifiant(
                    "\nVeuillez entrer un identifiant unique (deux lettres suivies de cinq chiffres, ex: AB12345) : ",
                    identifiants_utilises)

                # Demander les autres informations
                prenom, nom, genre, date_naissance = TournoiView.demander_info_joueur()

                confirmation = input("\nConfirmez-vous l'ajout de ce nouveau joueur (y/n) ? ").strip().lower()
                if confirmation == "y":
                    joueur = Joueur(id, prenom, nom, genre, date_naissance)
                    self.tournoi.ajouter_joueur(joueur)
                    print(f"\n{joueur.prenom} a bien été ajouté à la liste des joueurs du tournoi.")
                    Serialization.sauvegarder_donnees(self.tournoi)
                    print(f"Le tournoi '{self.tournoi.nom}' a été mis à jour et sauvegardé.")
                else:
                    print("Ajout annulé.")
            else:
                print("Veuillez entrer 'y' pour oui ou 'n' pour non.")

    def jouer_tournoi(self):
        if self.tournoi is None:
            print("Aucun tournoi chargé. Veuillez charger ou créer un tournoi.")
            return

        while True:
            if not self.tournoi.joueurs:
                print("Veuillez d'abord ajouter des joueurs avant de lancer le tournoi.")
                break

            shuffle(self.tournoi.joueurs)

            print(f"\nDébut du tournoi : {self.tournoi.nom}")

            nb_tours = ""
            while not nb_tours.isdigit():
                nb_tours = input("\nVeuillez indiquer le nombre de tours : ")

            nb_tours = int(nb_tours)
            for numero_tour in range(1, nb_tours + 1):
                print(f"\nTour {numero_tour} :")
                paires = self.tournoi.generer_paires()

                for joueur1, joueur2 in paires:
                    # Simuler les résultats du match
                    match = Match(f"Match {len(self.tournoi.matchs) + 1}", [joueur1, joueur2])
                    TournoiView.afficher_match(f"Match {len(self.tournoi.matchs) + 1}", joueur1, joueur2)
                    match.jouer_match()
                    TournoiView.afficher_joueurs(match.joueurs)
                    self.tournoi.matchs.append(match)

                    # Ajouter les paires du tour au tournoi
                    self.tournoi.tours.append(paires)

            # Sauvegarder après le tournoi
            Serialization.sauvegarder_donnees(self.tournoi)
            break


    def charger_tournoi(self, tournois):
        tournoi = Serialization.charger_donnees()
        if tournoi:
            self.tournoi = tournoi
            print(f"Tournoi '{self.tournoi.nom}' chargé avec succès.")
        else:
            print("Aucun tournoi chargé.")

        # Si aucun tournoi n'est chargé, permettre la sélection d'un tournoi existant
        if not tournois:
            print("Aucun tournoi disponible.")
            return

        print("Sélectionnez un tournoi :")
        for i, tournoi in enumerate(tournois, start=1):
            print(f"{i}. {tournoi.nom}")

        try:
            choix = int(input("Votre choix : ")) - 1
            self.tournoi = tournois[choix]
            print(f"Le tournoi '{self.tournoi.nom}' est maintenant actif.")
        except (ValueError, IndexError):
            print("Choix invalide.")

    def afficher_classement(self):
        if self.tournoi is None:
            print("Aucun tournoi chargé. Veuillez charger ou créer un tournoi.")
            return
        self.tournoi.joueurs.sort(key=lambda joueur: getattr(joueur, 'points', 0), reverse=True)
        TournoiView.afficher_classement(self.tournoi.joueurs)

    def rapport_joueurs(self):
        TournoiView.afficher_liste_joueurs_par_ordre_alphabetique(self.tournoi.joueurs)

    def rapport_tournois(self):
        TournoiView.afficher_rapport_tournois()

    def rapport_details_tournoi(self):
        TournoiView.afficher_details_tournoi(self.tournoi)