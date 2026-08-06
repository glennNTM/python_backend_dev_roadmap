class KwiziPayError(Exception):
    """Gestion des erreurs de KwiziPay"""

class CompteInexistantError(KwiziPayError):
    """"Compte inexistant"""

class SoldeInsuffisantError(KwiziPayError):
    pass

class MontantInvalideError(KwiziPayError):
    pass