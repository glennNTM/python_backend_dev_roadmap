class CompteBancaire:
    def __init__(self, nom: str, solde: int):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant: int):
        if montant <= 0:
            raise ValueError("Le montant doit etre positif.")
        
        self.solde += montant
        return self.solde
        
    def retirer(self, montant: int):
        if montant <= 0:
            raise ValueError("Le solde est insuffisant pour effectuer cette transaction.")
        elif montant > self.solde:
            raise ValueError("Le solde est insuffisant pour retirer ce montant.")
        
        self.solde -= montant
        return self.solde
    
    def afficher_solde(self):
        return self.solde

acc_glenn = CompteBancaire("Glenn", 50000000)
print(acc_glenn.retirer(100000))
print(acc_glenn.deposer(1))
print(acc_glenn.afficher_solde())