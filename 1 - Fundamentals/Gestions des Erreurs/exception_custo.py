import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filemode="a", filename="app.log")

class SoldeInssufisantError(Exception):
    """Raise when sold is not enough to do the transaction"""
    pass
    # def __init__(self, message: str, value) -> None:
    #     super().__init__(message)
        
    #     self.message = message
    #     self.value = value

    # def __str__(self) -> str:
    #     return f"{self.message} (Value: {self.value})"
    
def retirer(solde: float, montant: float) -> float | None:
    try:
        if montant <= 0:
            raise ValueError(f"La valeur du montant {montant} n'est pas correcte")
        if solde < montant:
            raise SoldeInssufisantError(f"Votre solde {solde} est insuffisant.")
    except ValueError as e:
        logging.error(e)
        return None

    except SoldeInssufisantError as e:
        logging.warning(e)
        return None
    else:
        logging.info(f"Montant retire: {montant} / Nouveau solde: {solde - montant}")
        return solde - montant 
    finally:
        logging.info("Tentative de transaction finie")
    
print(retirer(1000.0, -25000.0))
print(retirer(100.0, 25000.0))
print(retirer(100000.0, 25000.0))