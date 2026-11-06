class CompteBancaire:
    def __init__(self, nom: str, solde: int):
        self._nom = nom
        if solde < 0:
            raise ValueError("Le montant doit etre positif.")
        self._solde = solde

    def __str__(self):
        return f"Compte de {self._nom}: {self._solde} XAF."

    def __repr__(self):
        return f"CompteBancaire('{self._nom}', {self._solde})"

    def __eq__(self, other):
        return self._nom == other._nom

    @property
    def nom(self):
        return self._nom

    @property
    def solde(self):
            return self._solde

    def deposer(self, montant: int):
        if montant <= 0:
            raise ValueError("Le montant doit etre positif.")
        
        self._solde += montant
        return self._solde


    def retirer(self, montant: int):
        if montant <= 0:
            raise ValueError("Le solde est insuffisant pour effectuer cette transaction.")
        elif montant > self._solde:
            raise ValueError("Le solde est insuffisant pour retirer ce montant.")
        
        self._solde -= montant
        return self._solde
    
    def afficher_solde(self):
        return self.solde

class CompteEpargne(CompteBancaire):
    def __init__(self, nom: str, solde: int, taux: float):
        super().__init__(nom, solde)
        self.taux = taux

    def appliquer_interets(self):
        # 1. Calcul du montant des interets
        if self.taux:
            return self._solde * self.taux

    def ajouter_interet(self, montant):
            montant = self.appliquer_interets
            if montant <= 0:
                raise ValueError("Le montant doit etre positif.")
            
            self._solde += montant
            return self._solde

valid_account = CompteBancaire("Glenn", 100)
print(valid_account.solde, valid_account._nom)
valid_account.solde = 100000
valid_account.nom = "Autre"

valid_account = CompteBancaire("Baba", -100)