def aplatir(liste: list[int]) -> list:
    liste_aplatie = []

    for i in liste:
        if isinstance(i, list):
            liste_aplatie.extend(aplatir(i))
        else:
            liste_aplatie.append(i)

    return liste_aplatie

print(aplatir([1, [2, [3, [4]]], 5]))