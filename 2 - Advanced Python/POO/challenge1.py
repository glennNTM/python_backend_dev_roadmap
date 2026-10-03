class Rectangle:
    def __init__(self, longueur: int, largeur: int):
        self.longueur = longueur
        self.largeur = largeur

        def aire(self):
            print(f"L'aire du rectangle est de {self.longueur * self.largeur}")

        def perimetre(self):
            print(f"Le perimetre du rectangle est de {(self.longueur + self.largeur) * 2}")

a = Rectangle(12, 10)
a.aire()
a.perimetre()