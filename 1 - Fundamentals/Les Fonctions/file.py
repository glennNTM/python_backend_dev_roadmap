# Fonction qui calcule le montant total d'une addition en fonction d'un pourboire et d'une réduction

def calculer_montant_final(prix_base, pourcentage_pourboire, reduction):
    montant_avec_pourboire = (prix_base * pourcentage_pourboire) / 100
    montant_final = (montant_avec_pourboire * reduction) / 100
    return round(montant_final, 2)

print(calculer_montant_final(100, 15, 10))