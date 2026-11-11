from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nom: str):
            self.nom = nom
    @abstractmethod
    def crier(self):
        pass
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
   
    def crier(self):
            return "Popo"


# s = Animal("Serpent")


chien = Chien("Oscar")
chat = Chat("Garfield")
mouton = Mouton("Moumou")
poisson = Poisson("Nemo")


animaux = [ chat, chien, mouton, poisson]

for animal in animaux:
    print(animal.crier())