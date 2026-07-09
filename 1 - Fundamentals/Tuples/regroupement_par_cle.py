# Fonction qui prend une liste de tuples (nom, département) ([("Alice", "IT"), ("Bob", "RH"), ("Charlie", "IT")]) 
# Retourne un dictionnaire regroupant les noms par département ({"IT": ["Alice", "Charlie"], "RH": ["Bob"]}). 
def regroupement(liste: list[tuple])-> dict | None:
    if not liste:
        return None
    resultat = {}

    for nom, departement in liste:
        if not departement in resultat:
            # On ajoute le nouveau departement comme cle, la liste avec le nom en valeur
            resultat[departement] = [nom]
        else:
            resultat[departement].append(nom)

    return resultat

print(regroupement([("Alice", "IT"), ("Bob", "RH"), ("Charlie", "IT")]))