class KwiwiPayError(Exception):
    """Gestion des erreurs de KwiziPay"""

class CompteInexistantError(KwiwiPayError):
    pass

class SoldeInsuffisantError(KwiwiPayError):
    pass

class MontantInvalideError(KwiwiPayError):
    pass



