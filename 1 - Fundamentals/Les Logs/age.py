import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def verifier_age(age: int) -> int | None:
    logging.debug(f'{age}')
    if age <= 0 or age >= 120:
        logging.warning("La valeur de l'age est suspecte")
        return None
    else:
        logging.info("La valeur de l'age est normale.")
        return age
    

verifier_age(10)