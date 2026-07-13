# fonction a_des_doublons(liste) qui retourne True si la liste contient au moins un élément en double, False sinon.

def a_des_doublons(liste: list) -> bool:
    if not liste:
        return False
    return len(liste) != len(set(liste))
       

print(a_des_doublons([0, False]))