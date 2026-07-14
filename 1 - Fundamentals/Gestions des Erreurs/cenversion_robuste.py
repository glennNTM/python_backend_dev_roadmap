# Fonction qui convertit une chaine en entier

def convertir_en_entier(valeur: str) -> int | None:
    try:
        resultat = int(valeur)
    except ValueError:
        print(f"{valeur} doit etre un entier.")
        return None
    else:
        print("Conversion reussie")
        return resultat

    finally:
        print("Tentative de conversion terminée")
        
print(convertir_en_entier("42"))
print(convertir_en_entier("abc"))