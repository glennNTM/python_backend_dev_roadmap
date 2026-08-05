a = 12
b = 8

def surface_de_carre(long: int, large: int) -> int:
    print(f"Le carre de longueur {long} et largeur {large} a une superficie de {2 * (long + large)}")

if __name__ == "__main__":
    surface_de_carre(a, b)