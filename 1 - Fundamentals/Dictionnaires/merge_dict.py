#  fonction qui fusionne deux dictionnaires dont les valeurs sont numériques. Si une clé existe dans les deux, les valeurs s'additionnent

def merge_dictionnaire(dict_1: dict, dict_2: dict)-> dict: 

    if not dict_1 and not dict_2:
        return {}
    resultat = dict_1.copy()
    for cle, valeur in dict_2.items():
        if cle in resultat:
            resultat[cle] += valeur
        else:
            resultat[cle] = valeur

    return resultat

print(merge_dictionnaire({"a": 1, "b": 2}, {"b": 3, "c": 4}))  
   

    
