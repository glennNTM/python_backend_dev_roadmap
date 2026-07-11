#  Fonction qui prend une liste et retourne un dictionnaire a vec le nombre d'occurence de chaque item

def ocuurence(liste: list) -> dict:
    resultat = {}
    if not liste:
          return resultat
    for i in liste:
        if i in resultat:
             resultat[i] += 1
        else:
             resultat[i] = 1
         
    return resultat

print(ocuurence([1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 8, 9]))