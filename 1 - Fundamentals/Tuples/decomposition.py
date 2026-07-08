# Écris une fonction qui prend un tuple de coordonnées (x, y) et retourne la distance de ce point à l'origine (0, 0).

def decomposition(coordonnees: tuple[int, int]) -> float | None:
    if len(coordonnees) != 2:        
        return None
    x, y = coordonnees
    return (x**2 + y**2) ** 0.5

print(decomposition(()))
print(decomposition((8, 10)))

