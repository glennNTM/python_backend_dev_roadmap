# Écris une fonction decouper(liste, taille) qui découpe une liste en sous-listes de longueur taille. 
# La dernière sous-liste peut être plus courte si le nombre d'éléments n'est pas divisible par taille.

def decouper(liste: list, taille: int):
    liste_decouper = list()
    for i in range(0, len(liste), taille):
        liste_decouper.append(liste[i : i + taille])
    return liste_decouper

print(decouper([1, 2, 3, 4, 5, 6, 7, 8], 3))