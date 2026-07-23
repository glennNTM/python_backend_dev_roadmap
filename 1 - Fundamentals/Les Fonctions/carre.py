
liste_de_nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def carre(num_list: list[int]) -> list[int]:
    new_list = []
    for i in num_list:
        new_list.append(i ** 2)

    return new_list

# Fonction standard avec une boucle
print(carre(liste_de_nombre))

# Comprehension de liste
print([x ** 2 for x in liste_de_nombre])

# Fonction lambda
print(list(map(lambda x: x ** 2, liste_de_nombre)))