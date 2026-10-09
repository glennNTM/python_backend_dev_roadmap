# 

class Chanson:
    paroles = """Joyeux anniversaire,
Joyeux anniversaire,
Joyeux anniversaire {prenom},
Joyeux anniversaire."""

    @staticmethod
    def chante_pour(prenom):
        return Chanson.paroles


print(Chanson.chante_pour(prenom="Paul"))