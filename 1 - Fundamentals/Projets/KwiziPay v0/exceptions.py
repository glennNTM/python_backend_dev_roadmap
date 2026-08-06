class KwiziPayError(Exception):
    """Gestion des erreurs de KwiziPay"""

class CompteInexistantError(KwiziPayError):
    """"Compte inexistant"""

class CompteDejaExistantError(KwiziPayError):
    """""Un compte avec ce nom existe deja"""
    

class SoldeInsuffisantError(KwiziPayError):
        """""Solde insuffisant"""


class MontantInvalideError(KwiziPayError):
       """""Montant invalide"""
