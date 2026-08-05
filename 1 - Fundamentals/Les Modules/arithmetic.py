a = 18
b = 5

def somme(num_1: int, num_2: int) -> int:
    print(f"La somme de {num_1} et {num_2} est {num_1 + num_2}")

def difference(num_1: int, num_2: int) -> int:
    print(f"La difference de {num_1} et {num_2} est {num_1 - num_2}")

def multiplication(num_1: int, num_2: int) -> int:
    print(f"La multiplication de {num_1} et {num_2} est {num_1 * num_2}")

def division(num_1: int, num_2: int) -> int:
    print(f"La division entiere de {num_1} et {num_2} est {num_1 // num_2}")

if __name__ == "__main__":
    somme(a, b)
    difference(a, b)
    multiplication(a, b)
    division(a, b)