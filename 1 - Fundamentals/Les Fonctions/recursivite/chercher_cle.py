


def chercher_cle(donnees: dict, cle_cherchee):
    for cle in donnees.items():
        if cle == cle_cherchee:
            return cle
        elif isinstance(cle, dict):
            chercher_cle(cle, cle_cherchee)
        elif isinstance(cle, list):
            for i in cle:
                if i == cle_cherchee:
                    return i
        else:
            pass