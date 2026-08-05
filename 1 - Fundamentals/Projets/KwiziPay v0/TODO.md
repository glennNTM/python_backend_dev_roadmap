# KwiziPay v0 — Plan de construction

Plan de travail ordonné. Chaque étape ne dépend que des précédentes : suis l'ordre, tu ne seras jamais bloqué par un module pas encore écrit.

**Règle du sens des dépendances** — à tenir du début à la fin :

```
main.py  →  operations.py  →  validations.py, stockage.py  →  exceptions.py
(I/O console)   (métier)         (règles, persistance)        (n'importe rien)
```

Une flèche ne remonte jamais. `operations.py` ne contient **aucun** `print` ni `input`.

---

## Étape 0 — Assainir la structure

- [x] Supprimer le dossier `validations/` (il contient `stockage.py`, `utils.py` et `data/` : trois choses qui ne sont pas des validations)
- [x] Remonter `data/comptes.json` à la racine du projet → `data/comptes.json`
- [x] Créer `validations.py` à la racine (fichier, pas dossier)
- [x] Créer `stockage.py` à la racine
- [x] Supprimer `utils.py` (nom fourre-tout : dans 3 semaines il contiendra 12 fonctions sans lien)
- [x] Décider du sort de `comptes.py` : le supprimer (recommandé — le dict de comptes circulera en paramètre, ça garde les fonctions pures) ou lui donner un rôle strict « manipulation du dict en mémoire », distinct de `stockage.py` = « I/O disque »
- [x] Ajouter un `.gitignore` avec `__pycache__/` et `*.log` (le `__pycache__/` actuel ne doit pas être versionné)
- [ ] Mettre `{"comptes": {}, "transactions": []}` dans `comptes.json` (un fichier vide n'est pas du JSON valide)

**Structure cible :**

```
KwiziPay v0/
├── main.py           # I/O console : boucle, menu, affichage
├── operations.py     # métier : deposer, retirer, transferer, historique
├── validations.py    # valider_montant, valider_compte
├── stockage.py       # charger_donnees / sauvegarder_donnees (JSON)
├── exceptions.py     # KwiziPayError + filles
├── config.py         # chemins pathlib + setup_logging()
├── data/
│   └── comptes.json
├── kwizipay.log      # généré, ignoré par git
├── requirements.txt
├── README.md
└── TODO.md
```

---

## Étape 1 — `exceptions.py`

Le socle : aucune dépendance, tout le monde en dépend. À écrire en premier.

- [ ] `KwiziPayError(Exception)` — classe de base, docstring explicite
- [ ] `CompteInexistantError(KwiziPayError)`
- [ ] `SoldeInsuffisantError(KwiziPayError)`
- [ ] `MontantInvalideError(KwiziPayError)`
- [ ] Donner à `SoldeInsuffisantError` un `__init__` qui stocke `solde` et `montant` en attributs, pour que le message soit informatif sans reformater à chaque `except`

**Concepts :** héritage, hiérarchie d'exceptions, `super().__init__()`.

---

## Étape 2 — `config.py`

- [ ] `BASE_DIR = Path(__file__).resolve().parent` — chemin portable, indépendant du répertoire d'où on lance le script
- [ ] `DATA_FILE = BASE_DIR / "data" / "comptes.json"`
- [ ] `LOG_FILE = BASE_DIR / "kwizipay.log"`
- [ ] `setup_logging()` : `logging.basicConfig()` avec niveau, format (horodatage + niveau + message) et `encoding="utf-8"`

**Concepts :** `pathlib`, `__file__`, module `logging`.

**Piège :** si tu écris `Path("data/comptes.json")`, le chemin est relatif au répertoire courant — lancer le script depuis un autre dossier casse tout. `__file__` règle ça définitivement.

---

## Étape 3 — `stockage.py`

- [ ] `charger_donnees() -> dict` : lit le JSON avec `with open(..., encoding="utf-8")`
- [ ] Gérer `FileNotFoundError` → retourner `{"comptes": {}, "transactions": []}` (premier lancement)
- [ ] Gérer `json.JSONDecodeError` → logger un `error`, retourner la structure par défaut (fichier vide ou corrompu)
- [ ] `sauvegarder_donnees(donnees: dict) -> None` : écrit avec `indent=2` et `ensure_ascii=False` (sinon les accents sortent en `é`)
- [ ] Créer le dossier `data/` s'il n'existe pas : `DATA_FILE.parent.mkdir(parents=True, exist_ok=True)`

**Concepts :** `json`, context manager `with`, `try/except` sur l'I/O, encodage explicite.

**Piège majeur :** ton README prévoit que les transactions soient des **tuples**. JSON ne connaît pas le tuple : à la relecture tu récupéreras des **listes**. Deux options — soit tu convertis au chargement (`[tuple(t) for t in ...]`), soit tu persistes les transactions en dictionnaires (plus lisible dans le fichier). Choisis consciemment et note ton choix.

---

## Étape 4 — `validations.py`

Les guard clauses, isolées et testables séparément.

- [ ] `valider_montant(montant: float) -> None` : lève `MontantInvalideError` si `<= 0`
- [ ] `valider_compte(comptes: dict, nom: str) -> None` : lève `CompteInexistantError` si absent
- [ ] `valider_solde(solde: float, montant: float) -> None` : lève `SoldeInsuffisantError` si insuffisant

**Concepts :** guard clauses, `raise`, type hints, fonctions à responsabilité unique.

**Convention :** ces fonctions ne retournent rien. Soit elles passent, soit elles lèvent. Ne les fais pas retourner `True`/`False` — sinon l'appelant peut oublier de tester le retour, alors qu'une exception, on ne peut pas l'ignorer.

---

## Étape 5 — `operations.py`

Le cœur métier. **Aucun `print`, aucun `input` ici.**

- [ ] `deposer(comptes: dict, nom: str, montant: float) -> float` — valide, crédite, retourne le nouveau solde
- [ ] `retirer(comptes: dict, nom: str, montant: float) -> float` — valide (dont le solde), débite, retourne le nouveau solde
- [ ] `transferer(comptes: dict, source: str, destination: str, montant: float) -> None` — **valide tout AVANT de modifier quoi que ce soit**
- [ ] `historique(transactions: list, nom: str | None = None) -> list` — retourne les transactions, filtrées par compte si `nom` est fourni
- [ ] `enregistrer_transaction(transactions: list, type_op: str, montant: float, ...) -> None` — horodatage via `datetime.now().isoformat()`
- [ ] Vérifier que source ≠ destination dans le transfert
- [ ] Type hints sur **toutes** les signatures + docstrings mentionnant les exceptions levées

**Concepts :** fonctions pures, `datetime`, composition de fonctions, atomicité.

**Piège majeur — l'atomicité du transfert.** Si tu écris `retirer(...)` puis `deposer(...)` et que le dépôt échoue (compte destination inexistant), l'argent a **disparu** : débité de la source, jamais crédité ailleurs. Valide les deux comptes et le solde *d'abord*, ne modifie qu'ensuite. C'est le vrai sujet de la ligne « échoue intégralement si l'une des deux étapes est invalide » de ton README.

---

## Étape 6 — `main.py` (réécriture)

L'état actuel a trois bugs à corriger en réécrivant :

- [ ] **Boucle infinie** ligne 16 : `while choix in [1,2,3,4]` — `choix` ne change jamais dans le corps, la boucle tourne à l'infini. C'est un `match` seul qu'il te faut, la boucle externe `while True` suffit
- [ ] **Ligne 21** : `retirer` sans parenthèses — tu évalues la fonction sans l'appeler, il ne se passe rien
- [ ] **`else: pass`** ligne 26 : c'est un `while/else` (rare et déroutant), pas le `case _:` que tu voulais

À écrire :

- [ ] `while True:` + option `[5] Quitter` avec `break` (sinon l'utilisateur ne peut sortir qu'au Ctrl+C)
- [ ] `try/except ValueError` autour de `int(input(...))` — sinon taper « a » plante l'application
- [ ] `case _:` pour tout choix hors menu
- [ ] `except KwiziPayError as e:` → message utilisateur propre + `logger.warning`
- [ ] `charger_donnees()` **une seule fois** au démarrage, `sauvegarder_donnees()` après chaque opération réussie
- [ ] Fonctions de saisie dédiées (`demander_montant()`, `demander_compte()`) qui rebouclent tant que l'entrée est invalide
- [ ] `except KeyboardInterrupt:` pour un Ctrl+C propre (sauvegarde + message d'au revoir)
- [ ] Bloc `if __name__ == "__main__":` — indispensable, ton code est actuellement au niveau module et s'exécuterait à l'import

**Concepts :** `match/case` avec `case _`, `while/break`, gestion d'erreurs en couches, `__name__`.

---

## Étape 7 — Logging

- [ ] Appeler `setup_logging()` au tout début de `main()`
- [ ] `logger = logging.getLogger(__name__)` dans chaque module (pas le logger racine)
- [ ] `info` sur chaque opération réussie
- [ ] `warning` sur chaque refus métier (solde insuffisant, montant invalide) — c'est normal, pas une erreur
- [ ] `error` sur JSON corrompu et erreurs d'I/O
- [ ] Remplacer **tous** les `print` de diagnostic ; ne garder que les `print` destinés à l'utilisateur, dans `main.py`
- [ ] Masquer les données sensibles dans les logs (ne pas journaliser les soldes complets en clair — réflexe fintech annoncé dans ton README)

---

## Étape 8 — Finitions

- [ ] `requirements.txt` (vide ou avec un commentaire : la stdlib suffit — le fichier existe pour la forme et les futures phases)
- [ ] Relire : type hints sur 100 % des signatures
- [ ] Docstrings sur toutes les fonctions publiques
- [ ] Mettre à jour la section « Structure du projet » du README : elle décrit encore `utils.py` et ne mentionne ni `stockage.py`, ni `validations.py`, ni `config.py`
- [ ] Vérifier que le README ne promet rien que le code ne fait pas

---

## Étape 9 — Tests manuels (checklist de recette)

- [ ] Premier lancement sans `comptes.json` → création automatique, pas de crash
- [ ] `comptes.json` vidé à la main → message d'erreur propre, pas de crash
- [ ] Dépôt d'un montant négatif → refusé
- [ ] Dépôt d'un montant nul → refusé
- [ ] Retrait supérieur au solde → `SoldeInsuffisantError`, solde inchangé
- [ ] Transfert vers un compte inexistant → **source non débitée** (le test qui compte)
- [ ] Transfert d'un compte vers lui-même → refusé
- [ ] Saisie « abc » au menu → redemande, pas de crash
- [ ] Choix « 99 » au menu → message d'option invalide
- [ ] Ctrl+C → sortie propre
- [ ] Redémarrage → les soldes de la session précédente sont bien restaurés
- [ ] `kwizipay.log` contient bien info / warning / error aux bons endroits

---

## Ordre de travail conseillé

Étapes 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9, sans sauter.

Après chaque étape, lance `python main.py` : même incomplet, ça doit toujours démarrer sans planter. Un module qui casse le démarrage est un module à corriger avant de passer au suivant.
