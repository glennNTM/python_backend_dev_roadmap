# Fonction qui vérifie si un nombre est un "nombre parfait" (la somme de ses diviseurs propres, hors lui-même, est égale au nombre).

"""
1. Recuperer tous les diviseurs propres du nombre(sauf lui meme). Tous les diviseurs dont le modulo sera egale a zero
2. Initialiser une variable somme a zero, et l'incrementer avec les diviseurs qu'on recupere
3. verifie si la somme et le nombre sont egaux
4. Retourner True ou False

"""

def est_parfait(nombre: int)-> bool:
    somme = 0
    if nombre <= 0: return False 
    for div in range(1, nombre):
        if nombre % div == 0:
            somme += div
    return somme == nombre

est_parfait(6)