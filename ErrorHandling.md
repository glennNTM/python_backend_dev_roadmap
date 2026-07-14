# Gestion des erreurs en Python : EAFP vs LBYL

Deux philosophies opposées pour traiter les cas d'erreur. Python privilégie nettement la première.

---

## EAFP : Easier to Ask for Forgiveness than Permission

> « Il est plus facile de demander pardon que de demander la permission. »

On considère que l'opération va réussir, on la tente directement, et on gère l'erreur seulement si elle survient. C'est le style **idiomatique en Python**, porté par les blocs `try / except`.

```python
data = {213: 45000}

try:
    salaire_employe = data[214]
except KeyError:
    print("L'employé #214 n'existe pas")
```

On ne vérifie pas si la clé existe : on tente l'accès et on récupère le `KeyError` s'il se produit.

### Pourquoi c'est le style pythonique

- **Moins de vérifications redondantes.** Le langage lève déjà l'exception, inutile de refaire le test en amont.
- **Pas de condition de course.** Entre un `if` de vérification et l'accès réel, l'état peut changer (fichier supprimé, clé retirée par un autre thread). EAFP est atomique.
- **Performant dans le cas nominal.** Si l'erreur est rare, on ne paie pas le coût du test à chaque appel.

### Quand l'utiliser

- L'échec est l'exception, pas la règle
- Accès aux dictionnaires, attributs, fichiers, conversions de type
- Contexte concurrent ou I/O (fichiers, réseau, base de données)

---

## LBYL : Look Before You Leap

> « Regarde avant de sauter. »

On vérifie **avant** d'agir que l'opération ne provoquera pas d'erreur, généralement avec une structure conditionnelle. C'est le style dominant dans des langages comme le C.

```python
data = {213: 45000}

if 214 in data:
    print("Salaire de l'employé 214:", data[214])
else:
    print("L'employé #214 n'existe pas")
```

On teste d'abord la présence de la clé, puis on accède à la valeur seulement si le test passe.

### Avantages

- **Lisible** quand la condition est simple et le cas d'échec fréquent
- **Flux explicite** : le lecteur voit immédiatement les deux branches
- Adapté à la **validation d'entrées** en amont (formulaires, paramètres)

### Limites

- **Condition de course.** Entre la vérification et l'action, l'état peut changer. Typique avec les fichiers : `if os.path.exists(f)` puis `open(f)` peut échouer si le fichier disparaît entre les deux.
- **Vérifications redondantes.** On refait un test que Python fait déjà en interne.
- Peut devenir verbeux quand les conditions se multiplient.

### Quand l'utiliser

- Le cas d'échec est fréquent, pas exceptionnel
- Validation d'entrées utilisateur en amont du traitement
- Aucun risque de changement d'état entre le test et l'action

---

## Comparaison directe

| Critère | EAFP | LBYL |
|---|---|---|
| Approche | Tente puis rattrape | Vérifie puis agit |
| Outil | `try` / `except` | `if` / `else` |
| Condition de course | Immunisé | Vulnérable |
| Cas nominal fréquent | Rapide | Coût du test à chaque appel |
| Cas d'échec fréquent | Coût de l'exception | Plus efficace |
| Style | Pythonique | Hérité du C |

---

## Le piège classique : l'except nu

Ne jamais avaler toutes les exceptions sans distinction.

```python
# À éviter : masque les vrais bugs
try:
    salaire = data[cle]
except:
    salaire = 0
```

```python
# Correct : on cible l'exception attendue
try:
    salaire = data[cle]
except KeyError:
    salaire = 0
```

Un `except` nu attrape aussi les `KeyboardInterrupt`, les `MemoryError` et surtout les fautes de frappe dans ton propre code, qui passeront alors silencieusement.

---

## En pratique

Python fournit souvent une troisième voie qui évite le débat, comme `dict.get()` :

```python
salaire = data.get(214, "Employé inexistant")
```

Quand une méthode dédiée existe, elle est généralement préférable aux deux styles.

---

## Sources

- [EAFP, glossaire Docstring](https://www.docstring.fr/glossaire/eafp/)
- [LBYL, glossaire Docstring](https://www.docstring.fr/glossaire/lbyl/)
