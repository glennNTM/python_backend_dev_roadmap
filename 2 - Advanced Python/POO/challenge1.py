class Rectangle:
    def __init__(self, longueur: int, largeur: int):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self) -> int:
        return self.longueur * self.largeur

    def perimetre(self) -> int:
        return (self.longueur + self.largeur) * 2

a = Rectangle(12, 10)

print(a.aire(), a.perimetre())
