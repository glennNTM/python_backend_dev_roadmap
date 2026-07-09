# Fonction qui prend un dictionnaire et retourne un nouveau dictionnaire où les clés et valeurs sont inversées

def inverser(d: dict) -> dict:
    if not d:
        return {}
    resultat = {}
    for cle, valeur in d.items():
        resultat[valeur] = cle
    return resultat

print(inverser({"a": 1, "b": 2}))