#  Fonction qui prend deux chaînes et retourne l'ensemble des caractères qui apparaissent dans les deux (intersection), en ignorant la casse. 

def caractetres_uniques(string_1: str, string_2: str) -> set :
    s = set()
    if not string_1 or not string_2:
        return set()
    a = set(string_1.lower())
    b = set(string_2.lower())

    # return a & b
    return a.intersection(b)
    
print(caractetres_uniques("auiiufh", "euhfreuif"))