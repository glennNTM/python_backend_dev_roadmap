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

    def retirer(self, montant: int):
        minimum_solde = 5000
        solde_simule = self._solde - montant
        if solde_simule < minimum_solde:
            raise ValueError("Le solde de votre compte epargne ne peut aler sous 5000. Vous n'eavez pas assez de sous.")
        return super().retirer(montant)

    def appliquer_interets(self):
        # 1. Calcul du montant des interets
        montant = self._solde * self.taux
        self.deposer(montant)

        return self._solde
    

valid_account = CompteBancaire("Glenn", 100)
print(valid_account.solde, valid_account._nom)

valid_account = CompteBancaire("Baba", 10000)
me = CompteEpargne("Glenn", 100000, 0.03)
me.appliquer_interets()
print(me.solde)

me.retirer(10000)
me.retirer(5000)
me.retirer(500000)

print(me.solde)

