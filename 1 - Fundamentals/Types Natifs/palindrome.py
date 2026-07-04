#  Fonction qui vérifie si une chaîne est un palindrome (se lit pareil à l'endroit et à l'envers)
# On utilise les methodes lower() et replace() pour gerer la casse et les espaces


def est_palindrome(mot: str) -> bool:
    return mot.lower().replace(" ", "") == mot[::-1].lower().replace(" ", "")

print(est_palindrome("Radar")) # True

