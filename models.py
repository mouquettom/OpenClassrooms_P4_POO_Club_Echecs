class Joueur:

    def __init__(self, id, prenom, nom, genre, date_naissance):
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.genre = genre
        self.date_naissance = date_naissance
        self.points = 0.0

    def vainqueur_match(self):
        self.points += 1

    def match_nul(self):
        self.points += 0.5

    def __repr__(self):
        return f"{self.prenom} {self.nom} [{self.points} pts]"


class Match:

    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs

    def jouer_match(self):
        print(f"1. {self.joueurs[0].prenom} {self.joueurs[0].nom} gagne.")
        print(f"2. {self.joueurs[1].prenom} {self.joueurs[1].nom} gagne.")
        print("3. Match nul.")

        while True:
            choix = input("\nChoisissez une option : ")

            if choix == "1":
                self.joueurs[0].vainqueur_match()
                print(f"\n{self.joueurs[0].prenom} remporte le match.")
                break
            elif choix == "2":
                self.joueurs[1].vainqueur_match()
                print(f"\n{self.joueurs[1].prenom} remporte le match.")
                break
            elif choix == "3":
                for joueur in self.joueurs:
                    joueur.match_nul()
                print("\nMatch nul. Chaque joueur remporte 0.5 points.")
                break
            else:
                print("Choix invalide.")
                continue


class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, nombre_tours=4):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.joueurs = []
        self.matchs = []
        self.tours = []
        self.historique_matchs = set()  # Ajout pour suivre les matchs joués

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def ajouter_match(self, match):
        self.matchs.append(match)

    def generer_paires(self):
        self.joueurs.sort(key=lambda joueur: (-joueur.points, joueur.nom))

        paires = []
        joueurs_non_paires = self.joueurs[:]

        while joueurs_non_paires:
            joueur1 = joueurs_non_paires.pop(0)

            # Trouver un joueur avec qui joueur1 n'a pas encore joué
            for joueur2 in joueurs_non_paires:
                if (joueur1.id, joueur2.id) not in self.historique_matchs and (joueur2.id, joueur1.id) not in self.historique_matchs:
                    paires.append((joueur1, joueur2))
                    joueurs_non_paires.remove(joueur2)
                    # Ajouter le match à l'historique
                    self.historique_matchs.add((joueur1.id, joueur2.id))
                    break
            else:
                # Si aucun joueur valide n'est trouvé, appairer avec le suivant disponible
                if joueurs_non_paires:
                    joueur2 = joueurs_non_paires.pop(0)
                    paires.append((joueur1, joueur2))
                    self.historique_matchs.add((joueur1.id, joueur2.id))

        return paires