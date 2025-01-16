# OpenClassrooms_P4_POO_Tournoi_Echecs

## Documentation
### Description

Ce programme est une application Python hors ligne pour la gestion des tournois d'échecs. Il permet d'ajouter des joueurs, de gérer des tournois, de générer des paires dynamiques basées sur les résultats des matchs, et de produire des rapports détaillés. Les données sont sauvegardées et chargées à l'aide de fichiers JSON.
### Fonctionnalités

    Gestion des joueurs : Ajout de joueurs avec nom, prénom, genre et date de naissance.
    Gestion des tournois : Création de tournois, gestion des tours et des matchs.
    Rapports : Génération de listes de joueurs, tournois, tours, et matchs.
    Interface utilisateur : Menu interactif basé sur la console.

### Prérequis

    Python 3.8 ou supérieur
    Installer les dépendances (facultatif) avec : pip install -r requirements.txt

### Utilisation

Lancez la console, placez-vous dans le dossier de votre choix et clonez le dépôt :

    git clone https://github.com/mouquettom/OpenClassrooms_P4_POO_Club_Echecs.git

Allez dans le dossier OPC_P4_Tournoi_Echecs, puis créez un nouvel environnement virtuel :

    python -m venv env.

Ensuite, activez-le.
#### Windows:

    env\scripts\activate.bat

#### Linux:

    source env/bin/activate

Vous pouvez dorénavant exécuter le programme depuis le terminal :

    python3 main.py

### Conformité PEP 8

Rapport HTML généré par flake8 disponible dans le dossier rapport_flake8.
Structure MVC

Le projet suit l'architecture MVC, qui sépare les responsabilités en trois couches : le Modèle gère les données et la logique métier, la Vue affiche les données et interagit avec l'utilisateur, et le Contrôleur fait le lien entre les deux, en traitant les actions utilisateur et en mettant à jour les données ou l'affichage en conséquence.

    models.py : Définit les classes principales (Joueur, Match, Tournoi).
    views.py : Gère les interactions utilisateur (affichage, saisie).
    controllers.py : Contient la logique métier (création d'un tournoi, ajout de joueurs).
    main.py : Point d'entrée du programme.
