import json
from config import DATA_FILE, setup_logging


def charger_les_donnees() -> dict:
    with open(DATA_FILE, encoding="utf-8") as f:
        try:
            json.load(f)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass


#  try:
#         return a / b
#     except ZeroDivisionError:
#         logging.warning("La division par 0 n'est pas possible. b doit etre different de zero")
#         return None

#     except TypeError:
#         logging.error(f"{a} et {b} doivent etre des entiers pour faire la division")
#         return None