
transactions = [
    {"montant": 5000, "type": "retrait"},
    {"montant": 25000, "type": "retrait"},
    {"montant": 12000, "type": "depot"},
    {"montant": 30000, "type": "retrait"},
    {"montant": 8000, "type": "retrait"},
]

# Filtre en utilisant la method filter
transactions_filtrees = list(filter(lambda x: x["montant"] > 10000 and x["type"] == "retrait", transactions))

# Filtre en utilsant une comprehension de liste
transactions_filtrees_v2 = [x for x in transactions if x["montant"] > 10000 and x["type"] == "retrait" ]

print(transactions_filtrees)
 
print(transactions_filtrees_v2)

# Je remarque que pour les operations ou on retourne des listes(filtre, maping, tri, etc.) c'est souvent mieux d'utiliser les comprehension de liste que une fonction lambda, ou une boucle conditionelle
# Les fonctions lambda sont bien quand la contion(expression est pas complexe) par trop verbeuse