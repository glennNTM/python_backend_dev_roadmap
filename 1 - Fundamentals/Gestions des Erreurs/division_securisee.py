# J'utilise EAFP
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def division_securisee(a: int, b: int)-> float | None:
    logging.debug(f'{a} - {b}')
    try:
        return a / b
    except ZeroDivisionError:
        logging.warning("La division par 0 n'est pas possible. b doit etre different de zero")
        return None

    except TypeError:
        logging.error(f"{a} et {b} doivent etre des entiers pour faire la division")
        return None


print(division_securisee(100, 77))
print(division_securisee(100, 0))
print(division_securisee("100", 15))