# Fonction qui prend une liste de nombres et retourne une nouvelle liste où chaque nombre négatif est remplacé par 0, et chaque nombre positif est laissé tel quel

# Contrainte: utiliser une comprehension de liste


def neg_replace_by_zero_v0(liste: list[int]) -> list[int]:
    for i in range(len(liste)):
        if liste[i] < 0:
            liste[i] = 0

    return liste
print(neg_replace_by_zero_v0([-3, 5, -1, 8, 0]))

def neg_replace_by_zero_v1(liste: list[int]) -> list[int]:
    
    return [0 if i < 0 else i for i in liste]

print(neg_replace_by_zero_v1([-3, 5, -1, 8, 0]))
