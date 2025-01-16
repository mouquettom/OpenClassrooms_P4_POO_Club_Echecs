import os
import json
from models import Joueur, Match, Tournoi
from datetime import datetime

class Serialization:

    @staticmethod
    def sauvegarder_donnees(tournoi, dossier="data"):
        if not os.path.exists(dossier):
            os.makedirs(dossier)

        # Déterminer le fichier de sauvegarde
        if hasattr(tournoi, 'source_fichier') and tournoi.source_fichier:
            fichier = tournoi.source_fichier
        else:
            fichier = os.path.join(dossier, f"{tournoi.nom.replace(' ', '_')}.json")

        tournoi_data = {
            "nom": tournoi.nom,
            "lieu": tournoi.lieu,
            "date_debut": tournoi.date_debut.strftime("%d/%m/%Y"),
            "date_fin": tournoi.date_fin.strftime("%d/%m/%Y"),
            "joueurs": [
                {
                    "id": joueur.id,
                    "prenom": joueur.prenom,
                    "nom": joueur.nom,
                    "genre": joueur.genre,
                    "date_naissance": joueur.date_naissance.strftime("%d/%m/%Y"),
                    "points": joueur.points,
                }
                for joueur in tournoi.joueurs
            ],
            "matchs": [
                {
                    "nom": match.nom,
                    "joueurs": [
                        {"prenom": joueur.prenom, "nom": joueur.nom}
                        for joueur in match.joueurs
                    ],
                }
                for match in tournoi.matchs
            ],
        }

        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(tournoi_data, f, indent=4)
        print(f"\nTournoi '{tournoi.nom}' sauvegardé dans : {fichier}")


    @staticmethod
    def charger_donnees(dossier="data"):
        if not os.path.exists(dossier):
            print("Aucun dossier 'data' trouvé.")
            return None

        fichiers = [f for f in os.listdir(dossier) if f.endswith(".json")]
        noms_tournois = [os.path.splitext(f)[0] for f in fichiers]
        if not fichiers:
            print("Aucun fichier de tournoi trouvé.")
            return None

        print("\nSélectionnez un tournoi à charger :\n")
        for i, nom in enumerate(noms_tournois):
            print(f"{i + 1}. {nom}")
        print(f"{len(noms_tournois) + 1}. Annuler")

        choix = input("\nVotre choix : ")
        try:
            index = int(choix) - 1
            if index == len(fichiers):  # Dernière option : Annuler
                print("\nChargement annulé.")
                return None
            fichier_selectionne = fichiers[index]
        except (ValueError, IndexError):
            print("Choix invalide.")
            return None

        chemin_fichier = os.path.join(dossier, fichier_selectionne)
        try:
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                tournoi_data = json.load(f)
        except FileNotFoundError:
            print(f"Fichier non trouvé : {chemin_fichier}")
            return None
        except json.JSONDecodeError:
            print(f"Fichier corrompu ou mal formé : {chemin_fichier}")
            return None

        # Reconstruire l'objet Tournoi
        tournoi = Tournoi(
            nom=tournoi_data["nom"],
            lieu=tournoi_data["lieu"],
            date_debut=datetime.strptime(tournoi_data["date_debut"], "%d/%m/%Y"),
            date_fin=datetime.strptime(tournoi_data["date_fin"], "%d/%m/%Y"),
        )

        # Ajouter les joueurs
        for joueur_data in tournoi_data["joueurs"]:
            joueur = Joueur(
                id=joueur_data["id"],
                prenom=joueur_data["prenom"],
                nom=joueur_data["nom"],
                genre=joueur_data["genre"],
                date_naissance=datetime.strptime(joueur_data["date_naissance"], "%d/%m/%Y"),
            )
            joueur.points = joueur_data["points"]
            tournoi.ajouter_joueur(joueur)

        # Ajouter les matchs
        for match_data in tournoi_data["matchs"]:
            joueurs_match = [
                next(
                    joueur for joueur in tournoi.joueurs
                    if joueur.prenom == joueur_data["prenom"] and joueur.nom == joueur_data["nom"]
                )
                for joueur_data in match_data["joueurs"]
            ]
            match = Match(match_data["nom"], joueurs_match)
            tournoi.ajouter_match(match)

        return tournoi