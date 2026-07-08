
def entrelacer(liste_a, liste_b):
    liste_ab = []
    for i in list(zip(liste_a, liste_b)):
        liste_ab.extend(list(i))
    if len(liste_a) > len(liste_b):
        n = len(liste_b)
        liste_ab.extend(liste_a[n:])
    elif len(liste_b) > len(liste_a):
        n = len(liste_a)
        liste_ab.extend(liste_b[n:])
    return liste_ab
       

print(entrelacer([1, 2, 3, 4], ["a", "b", "c"]))

# [1, 'a', 2, 'b', 3, 'c', 4]