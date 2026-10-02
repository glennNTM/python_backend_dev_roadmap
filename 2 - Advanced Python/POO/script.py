class Voiture:
    def __init__(self, marque: str, modèle: str, vitesse: float):
        self.marque = marque
        self.modèle = modèle
        self.vitesse = vitesse

    def démarrer(self):
        print(f"{self.marque} {self.modèle} démarre. Elle roule a {self.vitesse}Km")

# Exemple de classe 'Voiture' avec des attributs et une méthode


voiture_1 = Voiture("Toyota", 5000, "60")

voiture_1.démarrer()

