# J'utilise EAFP

def division_securisee(a: int, b: int)-> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("La division par 0 n'est pas possible. b doit etre different de zero")
        return None

    except TypeError:
        print(f"{a} et {b} doivent etre des entiers")
        return None


print(division_securisee("gfkmrm", 77))