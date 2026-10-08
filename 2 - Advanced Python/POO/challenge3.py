class Livre:
    def __init__(self, titre: str, auteur: str, disponible : bool = True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def __str__(self):
        if self.disponible:
            return f"{self.titre} de {self.auteur} est disponible"
        return f"{self.titre} de {self.auteur} est emprunte"
        

class Bibliotheque:
    def __init__(self):
        self.livres : list[Livre] = []
    def ajouter(self, new_livre: Livre, ):
        self.livres.append(new_livre)

    def emprunter(self, titre: str):
        for livre in self.livres:
            if titre == livre.titre:
                if livre.disponible:
                    livre.disponible = False
                    print(f"Vous avez emprunte: {livre.titre}")
                    return
                elif livre.disponible == False:
                    print("Ce livre n'est pas diponible.")
                    return
        else:
            print("Ce livre n'exsite pas.")

print(Livre)
fav_livre = Livre("L'Etranger", "Albert Camus")
mediatheque = Bibliotheque()
mediatheque.ajouter(fav_livre)
mediatheque.emprunter("L'Etranger")

print(fav_livre)