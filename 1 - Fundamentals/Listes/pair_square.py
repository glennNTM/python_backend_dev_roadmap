# Fonction qui prend une liste d'entiers et retourne une nouvelle liste contenant uniquement les nombres pairs, chacun élevé au carré.

def carre_pair(liste: list[int]) -> list:
    return [item ** 2 for item in liste if item % 2 == 0]

print(carre_pair([1, 2, 3, 4, 5, 6]))