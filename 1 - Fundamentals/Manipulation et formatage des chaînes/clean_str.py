# fonction qui prend une phrase potentiellement mal formatée (espaces multiples en trop au début, à la fin, ou entre les mots) et retourne la phrase nettoyée : sans espaces superflus aux extrémités, avec un seul espace entre chaque mot, et avec la première lettre de chaque mot en majuscule.

def clean_str(phrase: str) -> str:
    clean_phrase = phrase.split(" ")
    clean_phrase=  " ".join(clean_phrase).title()

    return  clean_phrase
print(clean_str(" bonjour le monde "))