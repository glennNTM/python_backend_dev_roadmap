from dataclasses import dataclass

@dataclass
class Transaction():
    type : str
    montant : float
    compte: str
    date : str
    status: str = "validee"

    def check_montant(self):
        if self.montant <= 500.0:
            print("La transaction ne peut pas etre effectue.")
            self.status = "refusee"


t1 = Transaction(type="depot", montant=1000000.0, compte="Glenn", date=10/11/2026)
t2 = Transaction(type="depot", montant=1000000.0, compte="Glenn", date=10/11/2026)

print(t1 == t2)