# fonction qui prend deux listes (par exemple, les emails des clients du mois dernier et ceux de ce mois-ci) 
# et retourne un tuple de trois sets : les éléments présents dans les deux (clients fidèles), ceux uniquement dans la première (clients perdus), et ceux uniquement dans la seconde (nouveaux clients).

def analyse_de_client(liste_de_mail_01: list, liste_de_mail_02: list) -> tuple[set, set, set]:
    if not liste_de_mail_01 or not liste_de_mail_02:
        return (set(), set(), set())
    client_fidele = set(liste_de_mail_01) & set(liste_de_mail_02)
    client_perdu = set(liste_de_mail_01) - set(liste_de_mail_02)
    client_nouveau = set(liste_de_mail_02) - set(liste_de_mail_01)

    return (client_fidele, client_perdu, client_nouveau)

