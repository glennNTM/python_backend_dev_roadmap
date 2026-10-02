# KwiziPay v0

Gestionnaire de portefeuille Mobile Money en ligne de commande. Projet fil rouge de la Phase 1 (Python Fundamentals) : bibliothèque standard uniquement, sans classe, sans base de données, sans framework.

## Fonctionnalités

Un menu interactif propose sept options :

1. Créer un compte avec un solde initial (0 accepté, négatif refusé).
2. Consulter le solde d'un compte.
3. Déposer de l'argent sur un compte.
4. Retirer de l'argent d'un compte.
5. Transférer de l'argent d'un compte à un autre.
6. Consulter l'historique, pour tous les comptes ou pour un compte précis, du plus récent au plus ancien.
7. Quitter (sauvegarde puis sortie).

Une saisie vide au nom d'un compte annule l'opération et ramène au menu. Un choix hors menu affiche un message d'option invalide. Ctrl+C et Ctrl+D (EOF) sauvegardent l'état et quittent proprement.

## Règles métier

- Un compte n'est créé que par l'option 1 et son nom doit être unique.
- Un montant d'opération (dépôt, retrait, transfert) doit être strictement positif.
- Un retrait ou un transfert ne peut pas dépasser le solde. Le message de refus indique le solde disponible.
- Un compte ne peut pas se transférer de l'argent à lui-même.
- Un transfert valide tout avant de modifier quoi que ce soit : en cas de refus, aucun solde ne change.

## Structure du projet

- `main.py` : point d'entrée, boucle du menu, saisies, affichages, capture des exceptions et journalisation des refus.
- `operations.py` : logique métier (comptes, dépôt, retrait, transfert, historique, chargement et sauvegarde JSON). Aucun `input` ni `print`.
- `exceptions.py` : hiérarchie d'exceptions, avec `KwiziPayError` comme classe de base (`CompteInexistantError`, `CompteDejaExistantError`, `SoldeInsuffisantError`, `MontantInvalideError`, `OperationInvalideError`).
- `config.py` : chemins (`DATA_FILE`, `LOG_FILE`) calculés avec `pathlib`, création du dossier `data/`, fonction `setup_logging()`.
- `data/comptes.json` : état persisté (créé automatiquement).
- `kwizipay.log` : journal (créé automatiquement).

## Données et persistance

Le fichier JSON contient un seul document :

```
{"comptes": {nom: solde}, "historique": [[operation, compte_1, compte_2, montant, date_iso], ...]}
```

Les fonctions métier modifient `comptes` et `historique` en place. L'état est sauvegardé après chaque opération réussie et à la sortie. Au chargement, un fichier absent, au JSON invalide, mal encodé ou à la structure inattendue (clés manquantes, mauvais types) donne un état vide au lieu d'un plantage. Les transactions sont des tuples en mémoire et redeviennent des listes après rechargement, ce qui n'a pas d'impact sur le code.

## Journalisation

`setup_logging()` configure un fichier `kwizipay.log` (niveau DEBUG, horodatage, niveau, message). Chaque module obtient son logger avec `logging.getLogger(__name__)`.

- INFO : opérations réussies, sortie clavier.
- WARNING : refus métier, choix de menu invalide.
- ERROR : fichier JSON corrompu, erreur de conversion d'un montant.

## Lancement

```bash
python main.py
```

Python 3.10 ou plus est requis (`match / case`).

## Limites connues de la v0

- Un seul utilisateur, pas d'authentification, pas de concurrence.
- Montants en `float` (pas de `Decimal`), donc pas adapté à une vraie comptabilité.
- Un fichier corrompu n'est pas sauvegardé en `.bak` avant d'être écrasé par l'état vide.
- Les erreurs d'écriture du fichier (`OSError`) ne sont pas capturées.
- Les options 1 et 3 ne capturent pas `ValueError` : un montant non numérique y fait planter l'application (les options 4 et 5 le gèrent).
- Si le JSON est valide mais de structure inattendue, `charger_les_donnees()` ne retourne rien et le démarrage échoue.
- Aucun test automatisé : la validation s'est faite par tests manuels.

