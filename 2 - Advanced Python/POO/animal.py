class Animal():
    def __init__(self, nom: str):
        self.nom = nom

    def crier(self):
        return "Woooooo!"

class Chien(Animal):
    def crier(self):
        return "Ouaf"


serpent = Animal("Serpent")
print(serpent.crier())

chien1 = Chien("Oscar")
print(chien1.crier())