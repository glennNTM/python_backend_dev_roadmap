# Tu as une liste de tuples (nom, solde). Trie-la par solde décroissant en utilisant sorted() avec key= et une lambda. Puis, avec max() et une lambda, trouve le compte au solde le plus élevé.

comptes = [
    ("Alice", 150000),
    ("Bob", 32000),
    ("Charlie", 890000),
    ("Diane", 5000),
    ("Emile", 47000),
]
liste_trie = sorted(comptes, key=lambda x: x[0], reverse=True)
max_comptes = max(comptes, key=lambda x: x[1])

print(liste_trie)
print(max_comptes)