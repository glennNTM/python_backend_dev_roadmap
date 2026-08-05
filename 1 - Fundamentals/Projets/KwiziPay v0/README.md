# KwiziPay v0 — Gestionnaire de portefeuille Mobile Money (CLI)

> Projet fil rouge de la **Phase 1 : Python Fundamentals**.
> Un gestionnaire de portefeuille *mobile money* en ligne de commande, **sans classe ni base de données**, écrit dans un paradigme modulaire et impératif.
> L'objectif est de consolider l'intégralité des fondamentaux Python sur un cas concret inspiré du contexte fintech africain.

---

## Objectif pédagogique

Ce projet croise et met en pratique toutes les notions de la phase 1 : types natifs, structures de données, fonctions, gestion des fichiers, gestion des erreurs et logging. Aucune bibliothèque externe lourde, aucun framework : uniquement la bibliothèque standard, pour bien maîtriser le langage avant d'ajouter des couches d'abstraction.

---

## Fonctionnalités

Un menu interactif en ligne de commande permet à l'utilisateur de gérer des comptes et d'effectuer des opérations financières simples.

Les opérations prises en charge sont le dépôt sur un compte, le retrait d'un compte, le transfert entre deux comptes, et la consultation de l'historique des transactions. À chaque lancement, l'application charge l'état des comptes depuis un fichier de persistance, et à chaque opération réussie, elle met à jour cet état et journalise la transaction.

---

## Concepts Python mis en œuvre

**Types et structures de données.** Les comptes sont stockés dans un dictionnaire associant un nom de compte à son solde. L'historique des transactions est une liste de tuples, chaque tuple capturant une opération (type, montant, comptes concernés, horodatage). Le choix du tuple pour une transaction reflète sa nature : un enregistrement figé, de taille fixe, aux champs de natures différentes.

**Fonctions.** La logique est découpée en fonctions à responsabilité unique : `deposer()`, `retirer()`, `transferer()`, `historique()`, plus des fonctions utilitaires de validation et de formatage. Les fonctions sont pures autant que possible (elles retournent des valeurs plutôt que de muter un état global), et chaque fonction est annotée avec des type hints.

**Structures de contrôle.** Le routage du menu s'appuie sur `match / case` pour diriger chaque choix utilisateur vers l'opération correspondante. Les validations utilisent des guard clauses pour rejeter tôt les entrées invalides.

**Gestion des erreurs.** Les cas d'échec métier (solde insuffisant, montant négatif ou nul, compte inexistant) sont gérés par des exceptions, dont une exception personnalisée `SoldeInsuffisantError` héritant d'`Exception`. Les blocs `try / except / else / finally` encadrent les opérations risquées, avec une capture différenciée selon le type d'erreur.

**Logging.** Le module `logging` remplace tout `print` de diagnostic. Les événements sont journalisés avec des niveaux de gravité appropriés : `info` pour les opérations réussies, `warning` pour les refus métier normaux (solde insuffisant), `error` pour les erreurs de saisie ou de programmation. Le fichier de log est résolu de façon portable pour se situer au même niveau que le script, via `pathlib` et `__file__`.

**Gestion des fichiers et persistance.** L'état des comptes est persisté au format JSON via le module `json`, lu et écrit à travers un context manager `with open(...)`, avec encodage UTF-8 explicite. Le chargement gère proprement l'absence de fichier au premier lancement (`FileNotFoundError`) et un fichier corrompu ou vide (`json.JSONDecodeError`), en retournant un état par défaut plutôt que de planter. Le module `datetime` horodate les transactions.

---

## Structure du projet

Le code est organisé en modules à responsabilités séparées :

- `main.py` : point d'entrée, boucle du menu interactif, routage des commandes.
- `operations.py` : les fonctions métier (dépôt, retrait, transfert, historique).
- `utils.py` : fonctions transverses (validation, formatage, persistance JSON, configuration du logging).
- `exceptions.py` : les exceptions personnalisées du domaine (par exemple `SoldeInsuffisantError`).
- `requirements.txt` : les dépendances (minimales à ce stade, la bibliothèque standard suffisant pour l'essentiel).

---

## Règles métier

Un dépôt exige un montant strictement positif. Un retrait exige un montant strictement positif qui ne dépasse pas le solde disponible, sous peine de `SoldeInsuffisantError`. Un transfert combine un retrait sur le compte source et un dépôt sur le compte destination, et échoue intégralement si l'une des deux étapes est invalide. Toute opération sur un compte inexistant est rejetée.

---

## Bonnes pratiques appliquées

Séparation systématique du calcul et de l'affichage. Type hints sur toutes les signatures. Guard clauses pour valider les entrées en amont. Exceptions explicites plutôt que retours silencieux. Logging structuré plutôt que `print`. Chemins de fichiers portables via `pathlib`. Aucune donnée sensible journalisée en clair (les identifiants et soldes complets sont masqués ou arrondis dans les logs, réflexe de confidentialité propre au contexte fintech).

---

## Lancement

Depuis le dossier du projet, exécuter le point d'entrée :

```bash
python main.py
```

Au premier lancement, le fichier de persistance est créé automatiquement s'il n'existe pas. Les lancements suivants restaurent l'état précédent des comptes.

---

## Limites assumées de la v0

Cette version n'a volontairement ni classes, ni base de données, ni interface graphique, ni concurrence. C'est un choix pédagogique : maîtriser le paradigme impératif et modulaire avant d'introduire la POO (v1) et les couches plus avancées. Les évolutions prévues (refonte orientée objet, validation Pydantic, persistance en base, API web, concurrence) constituent les jalons des phases suivantes de la roadmap.

---

## Positionnement dans la roadmap

KwiziPay v0 clôt la Phase 1. La Phase 2 (Advanced Python) reprendra exactement le même problème métier en le réécrivant en orienté objet, pour éprouver le contraste entre les deux paradigmes sur un cas identique.