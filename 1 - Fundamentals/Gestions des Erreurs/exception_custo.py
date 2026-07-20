

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
        print(e)

    except SoldeInssufisantError as e:
        print (e)
    else:
        return solde - montant 
    finally:
        print("Tentative de transaction finie")
    
print(retirer(1000.0, -25000.0))