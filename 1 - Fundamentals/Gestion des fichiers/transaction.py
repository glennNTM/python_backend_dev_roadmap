def enregistrer_transaction(chemin: str, texte: str):
    with open(chemin, "a", encoding='utf-8') as f:
        f.write(texte)

def lire_transaction(chemin: str):
    if not chemin:
        print("Le fichier n'existe pas.")
        return []
    else:
        with open(chemin, "r", encoding='utf-8') as f:
            return f.readlines()
  
enregistrer_transaction(r"C:\Users\Glenn\fichier.txt","\nTransaction faite a 23h 58."*10)
lire_transaction(r"C:\Users\Glenn\fichier")