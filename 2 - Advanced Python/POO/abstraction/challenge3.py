from abc import ABC, abstractmethod


class MoyenDePaiement(ABC):
    @abstractmethod
    def payer(self, montant):
        pass
class MobileMoney(MoyenDePaiement):
    def payer(self, montant: int):
        print(f"Paiement de {montant} XAF via mobile money en cours...")

class Especes(MoyenDePaiement):
    def payer(self, montant: int):
        print(f"Paiement de {montant} XAF en espece en cours...")

class Cheques(MoyenDePaiement):
    def payer(self, montant: int):
        print(f"Paiement de {montant} XAF par cheque en cours...")

# class Crypto(MoyenDePaiement):
#     pass

airtel_money = MobileMoney()
billet = Especes()
bgfi_check = Cheques()
# binance = Crypto()


a = [airtel_money, billet, bgfi_check]

for i in a:
    i.payer(5000)