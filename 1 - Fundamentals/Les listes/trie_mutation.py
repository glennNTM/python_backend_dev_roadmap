
a = [9, 5, 2, 1, 3]

def trier_muta(liste: list) -> None:
    return liste.sort()

print(a) # [9, 5, 2, 1, 3]
print(trier_muta(a)) # None
print(a) # [1, 2, 3, 5, 9]

a = [9, 5, 2, 1, 3]

def trier_pure(liste: list) -> list:
    new_liste = sorted(liste)
    return new_liste

print(a)
print(trier_pure(a)) # [1, 2, 3, 5, 9]
print(a)