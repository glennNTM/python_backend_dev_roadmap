from models import Compte


c = Compte("Baba", 10000)
b = Compte("Mike")


c.deposer(True)
print(c, b)
