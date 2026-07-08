# Écris une fonction qui prend une liste de nombres et retourne un tuple (minimum, maximum, moyenne). 
# Guard clause obligatoire : si la liste est vide, tu ne peux calculer ni min, ni max, ni moyenne (division par zéro)

def statistiques(liste: list[int]) -> tuple[int, int, float] | None:
    if not liste:
        return None
    liste_ordonne = sorted(liste)
    minimum = liste_ordonne[0]
    maximum = liste_ordonne[-1]
    moyenne = sum(liste_ordonne) / len(liste_ordonne)
    return (minimum, maximum, moyenne)


print(statistiques([4, 6, 1, 8, 2, 9, 3]))