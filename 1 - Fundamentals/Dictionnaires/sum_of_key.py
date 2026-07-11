# Dans cet exercice, vous devez additionner toutes les valeurs du dictionnaire ensemble.

# Votre script doit donc retourner le nombre entier 8700 dans la variable resultat.

employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}

resultat = 0

# for i in employes:
#    resultat += employes[i]

# for _ in employes:
    #resultat += value
resultat = sum(employes.values())

print (resultat)