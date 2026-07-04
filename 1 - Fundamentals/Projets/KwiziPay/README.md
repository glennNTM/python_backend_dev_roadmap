# Phase 1 — KwiziPay v0 (Fundamentals)

> Fil rouge du roadmap : **KwiziPay**, un portefeuille *mobile money* qu'on va refaire à
> chaque phase, du niveau junior au niveau senior. Ici, la toute première version.

## 🎯 Objectif de cette phase

Construire un **gestionnaire de portefeuille mobile money en ligne de commande**, en
**Python pur** : pas de classe, pas de base de données, pas de librairie externe. Juste
les fondamentaux du langage bien utilisés.

L'idée n'est pas d'aller vite, mais de mobiliser **volontairement** chaque notion de la
Phase 1. Quand on refera KwiziPay en Phase 2 (POO), on résoudra *le même problème
autrement* — c'est ça qui ancre les concepts (active recall).

**Paradigme visé :** programmation **modulaire / impérative**.

## 🧩 Ce qu'on construit

Une application CLI qui permet de :

- Créer un compte client (nom, numéro de téléphone, solde initial)
- **Déposer** de l'argent sur un compte
- **Retirer** de l'argent (en refusant si le solde est insuffisant)
- **Transférer** de l'argent d'un compte à un autre
- Consulter le **solde** et l'**historique** des transactions d'un compte
- **Sauvegarder / recharger** l'état dans un fichier JSON entre deux exécutions

Chaque opération est validée (montant positif, compte existant, solde suffisant) et
horodatée.

## 🗂️ Structure de fichiers proposée

On crée un sous-dossier dédié au projet dans la phase :

```
1 - Fundamentals/
└── KwiziPay/
    ├── main.py            # point d'entrée : menu interactif (match/case)
    ├── operations.py      # deposer, retirer, transferer, historique
    ├── comptes.py         # création / recherche de comptes, validations
    ├── stockage.py        # lecture / écriture du fichier JSON
    ├── utils.py           # helpers (formatage montant, horodatage)
    ├── data/
    │   └── comptes.json   # état persisté (généré à l'exécution)
    └── requirements.txt   # vide ou stdlib only, pour prendre l'habitude
```

> Garder chaque module avec **une seule responsabilité** : c'est le premier réflexe
> d'architecture, et ça prépare le terrain des phases suivantes.

## ✅ Notions de la Phase 1 à couvrir (checklist)

Coche au fur et à mesure — le but est que le projet touche **tout** le programme.

- [ ] **Types** : `int` / `float` pour les montants, `str`, `bool`
- [ ] **Opérateurs** : arithmétiques, comparaison, logiques, `in` (appartenance)
- [ ] **Conditions** : `if / elif / else`, **guard clauses**
- [ ] **Boucles** : `for` / `while`, `break` / `continue` (menu qui tourne)
- [ ] **`match / case`** : routing des commandes du menu
- [ ] **Structures intégrées** : `dict` (comptes), `list` (historique), `tuple` (transaction), `set` (numéros uniques)
- [ ] **Compréhensions** : filtrer / résumer l'historique
- [ ] **Fonctions** : paramètres, valeurs de retour, `*args` / `**kwargs`, portée (LEGB)
- [ ] **Lambda** : ex. tri de l'historique par date ou montant
- [ ] **f-strings & méthodes de `str`** : affichage des relevés
- [ ] **Fichiers** : `open` / `with`, lecture / écriture
- [ ] **Gestion d'erreurs** : `try / except / finally`, `raise` (solde insuffisant, montant négatif)
- [ ] **Modules & stdlib** : `json`, `datetime`, `os` ; découpage en packages
- [ ] **PEP 8 + type hints** sur toutes les fonctions

## 🏁 Definition of Done

La phase est terminée quand :

1. Toutes les opérations (dépôt, retrait, transfert, historique) fonctionnent depuis le menu.
2. L'état **survit** à un redémarrage (persistance JSON OK).
3. Aucune opération invalide ne passe (montant négatif, solde insuffisant, compte inconnu
   lèvent une erreur claire, sans crash brutal).
4. Le code est réparti en modules, typé, et conforme à PEP 8.
5. La checklist ci-dessus est entièrement cochée.

## ▶️ Lancer le projet

```bash
cd "1 - Fundamentals/KwiziPay"
python main.py
```

## 🔭 La suite

En **Phase 2**, on reprend exactement ce cahier des charges mais en **POO** : `Compte`,
`Transaction`, `Portefeuille`, héritage, `@property`, décorateurs, context managers…
Le comportement sera identique, l'architecture changera du tout au tout.
