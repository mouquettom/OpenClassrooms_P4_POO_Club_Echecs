from datetime import datetime
import re
import os

class TournoiView:

    @staticmethod
    def afficher_joueurs(joueurs):
        for joueur in joueurs:
            print(f" - {joueur.prenom} {joueur.nom} [{joueur.points} pts]")

    @staticmethod
    def afficher_match(match, joueur1, joueur2):
        print(f"\n{match} : {joueur1.nom} (Score: {joueur1.points}) vs {joueur2.nom} (Score: {joueur2.points})")

    @staticmethod
    def afficher_classement(joueurs):
        print("\nClassement final :\n")
        for index, joueur in enumerate(joueurs, start=1):
            print(f"{index}. {joueur}")

    @staticmethod
    def demander_date_valide(message):
        while True:
            date = input(message)
            try:
                date_obj = datetime.strptime(date, "%d/%m/%Y")
                return date_obj
            except ValueError:
                print("Date invalide. Veuillez entrer une date au format jj/mm/aaaa.")

    @staticmethod
    def demander_genre_valide(message):
        choix_genre = ""
        while choix_genre not in ["h", "f"]:
            choix_genre = input(message).lower()
            if choix_genre not in ["h", "f"]:
                print("Veuillez entrer 'h' pour homme ou 'f' pour femme.")
        return choix_genre

    @staticmethod
    def demander_identifiant(message, identifiants_utilises):
        """
        Demande un identifiant unique à l'utilisateur, vérifie qu'il respecte le format
        et qu'il n'est pas déjà utilisé.
        """
        while True:
            identifiant = input(message).strip()

            # Vérifier le format de l'identifiant
            if not re.match(r"^[A-Z]{2}\d{5}$", identifiant):
                print(
                    "Erreur : L'identifiant doit contenir deux lettres majuscules suivies de cinq chiffres (ex: AB12345).")
                continue

            # Vérifier si l'identifiant est déjà utilisé
            if identifiant in identifiants_utilises:
                print("Erreur : Cet identifiant est déjà utilisé. Veuillez en saisir un autre.")
                continue
            else:
                print(f"Identifiant '{identifiant}' ajouté avec succès.")

            # Retourner l'identifiant valide et unique
            return identifiant

    @staticmethod
    def demander_info_tournoi():
        nom = input("\nLe nom du Tournoi : ")
        lieu = input("Le lieu du Tournoi : ")
        date_debut = TournoiView.demander_date_valide("La date de début (jj/mm/aaaa) : ")
        date_fin = TournoiView.demander_date_valide("La date de fin (jj/mm/aaaa) : ")
        return nom, lieu, date_debut, date_fin

    @staticmethod
    def demander_info_joueur():
        prenom = input("\nQuel est le prénom du joueur : ")
        nom = input("Quel est le nom de famille du joueur : ")
        genre = TournoiView.demander_genre_valide("Quel est le genre du joueur (h/f) : ")
        date_naissance = TournoiView.demander_date_valide("Quelle est la date de naissance du joueur (jj/mm/aaaa) : ")
        return prenom, nom, genre, date_naissance

    @staticmethod
    def liste_joueurs_par_ordre_alphabetique(joueurs):
        print("\nListe des joueurs (ordre alphabétique) :")
        for joueur in joueurs:
            print(f"- {joueur.nom} {joueur.prenom}")

    @staticmethod
    def afficher_rapport_tournois(dossier="data"):
        # Vérifier si le dossier existe
        if not os.path.exists(dossier):
            print(f"Le dossier '{dossier}' n'existe pas.")
            return None

        # Récupérer les fichiers JSON dans le dossier
        fichiers = [f for f in os.listdir(dossier) if f.endswith(".json")]
        if not fichiers:
            print("Aucun fichier de tournoi disponible.")
            return None

        # Afficher la liste des noms de tournois (sans extension)
        print("\nLa liste de tous les tournois :\n")
        noms_tournois = [os.path.splitext(f)[0] for f in fichiers]
        for i, nom in enumerate(noms_tournois):
            print(f"{i + 1}. {nom}")

        # Retourner la liste des noms de tournois
        return noms_tournois

    @staticmethod
    def afficher_details_tournoi(tournoi):
        print(f"\nDétail du tournoi en cours : {tournoi.nom} ({tournoi.lieu}) - {tournoi.date_debut} / {tournoi.date_fin}")

    @staticmethod
    def afficher_liste_joueurs_par_ordre_alphabetique(joueurs):
        print(f"\nLa liste des joueurs (par ordre alphabétique) :\n")
        joueurs.sort(key=lambda joueur: joueur.nom)
        for i, joueur in enumerate(joueurs):
            print(f"{i + 1}. {joueur.nom} {joueur.prenom} ({joueur.id})")