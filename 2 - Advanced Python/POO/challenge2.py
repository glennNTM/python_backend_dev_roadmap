class CompteBancaire:
    def __init__(self, nom: str, solde: int):
        self.nom = nom
        self.solde = solde

    def __str__(self):
        return f"Compte de {self.nom}: {self.solde} XAF."

    def __repr__(self):
        return f"CompteBancaire('{self.nom}', {self.solde})"

    def __eq__(self, other):
        return self.nom == other.nom


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
acc_1 = CompteBancaire("Mike", 50000)
acc_2 = CompteBancaire("Mike", 60000)

print(acc_glenn.retirer(100000))
print(acc_glenn.deposer(1))
print(acc_glenn.afficher_solde())
print(acc_glenn)

acc = [acc_glenn, acc_1, acc_2]

print(acc)
print(acc_1 == acc_2)