# fonction qui prend une chaîne et retourne le ou les caractères les plus fréquents (en ignorant la casse et les espaces). Si plusieurs caractères sont à égalité de fréquence maximale, retourne-les tous.

def cartere_frequence(caractere: str) -> list[str]:
    caractere = caractere.lower().replace(" ", "")
    
    max_freq = 0
    list_char = []
    for i in set(caractere):
        x = caractere.count(i)
        if x > max_freq:
            max_freq = x
    for j in set(caractere):
        if caractere.count(j) == max_freq:
            list_char.append(j)

    return list_char

print(cartere_frequence(" Mississippi "))