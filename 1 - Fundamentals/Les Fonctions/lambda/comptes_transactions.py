# Objectif : obtenir les comptes triés du plus grand total de transactions au plus petit.

"""""
Tu as un dictionnaire {compte: [liste de transactions]}. 
Trie les comptes selon la somme de leurs transactions, du plus grand total au plus petit, 
en utilisant sorted() sur .items() avec une lambda qui calcule cette somme. Réfléchis à ce que reçoit ta lambda (un tuple clé-valeur) et comment y accéder.

"""

comptes_transactions = {
    "Alice": [15000, 22000, 8000],
    "Bob": [5000, 3000],
    "Charlie": [90000, 45000, 30000],
    "Diane": [12000],
}

comptes_transactions_tries = sorted(comptes_transactions.items(), key= lambda x: sum(x[1]), reverse=True)

print(comptes_transactions_tries)