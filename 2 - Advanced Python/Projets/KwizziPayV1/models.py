from exceptions import MontantInvalideError, SoldeInsuffisantError


class Compte():
    def __init__(self, nom: str, solde: int = 0):
        self._nom = nom

        if solde < 0:
            raise MontantInvalideError("Le solde initial doit etre positif.")
        self._solde = solde


    def __str__(self):
        return f"Compte de {self._nom}: {self._solde} XAF."

    def __repr__(self):
        return f"Compte('{self._nom}', {self._solde})"

    @property
    def nom(self):
        return self._nom
    
    @property
    def solde(self):
        return self._solde

    @staticmethod
    def est_montant_valide(montant: int):
        if type(montant) == bool:
            raise MontantInvalideError("Le type du montant n'est pas valide. Le montant doit etre un entier positif.")
        elif montant <= 0:
            raise MontantInvalideError("Le type du montant n'est pas valide. Le montant doit etre un entier positif.")
        elif not isinstance(montant, int):
            raise MontantInvalideError("Le type du montant n'est pas valide. Le montant doit etre un entier positif.")
            
        
        

    def deposer(self, montant):
        self.est_montant_valide(montant)

        self._solde += montant
        return self._solde
        

    def retirer(self, montant: int):
        self.est_montant_valide(montant)

        if montant > self._solde:
            raise SoldeInsuffisantError("L'operation ne peut pas etre effectuer. Le solde est inferieur au montant a retirer.")
        
        self._solde -= montant
        return self._solde
    

class Transaction():
    pass

class Portefeuille():
    pass

