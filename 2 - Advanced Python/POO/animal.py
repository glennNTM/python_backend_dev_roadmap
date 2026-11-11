class Animal():
    def __init__(self, nom: str):
        self.nom = nom

    def crier(self):
        return "Woooooo!"

class Chien(Animal):
    def crier(self):
        return "Ouaf"

class Chat(Animal):
    def crier(self):
        return "Miaou"

class Mouton(Animal):
    def crier(self):
        return "Beeee"

class Poisson(Animal):
    pass


serpent = Animal("Serpent")
chien = Chien("Oscar")
chat = Chat("Garfield")
mouton = Mouton("Moumou")
poisson = Poisson("Nemo")


animaux = [serpent, chat, chien, mouton, poisson]

for animal in animaux:
    print(animal.crier())