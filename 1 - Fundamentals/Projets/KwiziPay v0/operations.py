from config import DATA_FILE
from exceptions import CompteInexistantError, CompteDejaExistantError, MontantInvalideError, SoldeInsuffisantError, OperationInvalideError

from datetime import datetime
import json, logging

logger = logging.getLogger(__name__)  

def deposer(comptes: dict, nom: str, montant: float, historique: list):
     if not nom in comptes:
            logger.warning(f"Tentative de depot a echoue. Le compte {nom} n'existe pas")
            raise CompteInexistantError("Ce compte n'existe pas.")
     elif montant <= 0:
         raise MontantInvalideError("Le montant doit etre superieure a 0.")
     else:
         comptes[nom] += montant
         logger.info(f"Depot sur le compte {nom} effectue avec succes!")
         enregistrer_transaction(historique=historique, operation="depot", montant=montant, compte_1=nom)

def consulter_solde(comptes: dict, nom: str) -> float:
    if not nom in comptes:
    # On verifie si le compte est bien existant
        raise CompteInexistantError("Ce compte n'existe pas.")
    else:
        return comptes[nom]

def retirer(comptes: dict, nom: str, montant: float, historique: list):
    if not nom in comptes:
        logger.warning(f"Tentative de retrait a echoue. Le compte {nom} n'existe pas")
        raise CompteInexistantError("Ce compte n'existe pas.")

    elif montant <= 0:
        raise MontantInvalideError("Le montant doit etre superieure a 0.")
    elif comptes[nom] < montant:
        raise SoldeInsuffisantError(f"Le solde {comptes[nom]} est insuffisant pour effectuer cette operation.")
    else:
        comptes[nom] -= montant
        logger.info(f"Retrait sur le compte {nom} effectue avec succes!")
        enregistrer_transaction(historique=historique, operation="retrait", montant=montant, compte_1=nom)

def transferer(comptes: dict, compte_source: str, compte_destination: str, montant: float, historique: list):
    if not compte_source in comptes:
        logger.warning("Le transfert a echoue.")
        raise CompteInexistantError("Ce compte n'existe pas.")
    elif not compte_destination in comptes:
        logger.warning("Le transfert a echoue.")
        raise CompteInexistantError("Ce compte n'existe pas.")
    elif compte_source == compte_destination:
        logger.warning("Le transfert a echoue.")
        raise OperationInvalideError("Le transfere d'un compte vers lui-meme n'est pas possible. Cette operation ne peut pas etre efectuer.")
    elif montant <= 0:
        logger.warning("Le transfert a echoue.")
        raise MontantInvalideError(f"Le montant {montant} est invalide. Le transfert ne peut pas etre effectue.")
    elif comptes[compte_source] < montant:
        logger.warning("Le transfert a echoue.")
        raise SoldeInsuffisantError(f"Solde insufisant pour effectuer ce transfert. Solde : {comptes[compte_source]}")
    else:
        comptes[compte_source] -= montant
        comptes[compte_destination] += montant

        logger.info(f"Transfert effectue avec succes!")
        enregistrer_transaction(historique=historique, operation="transfert", montant=montant, compte_1=compte_source, compte_2=compte_destination)

def charger_historique(historique: list, compte: str = None) -> list:
    if compte:
        historique_filtre = [t for t in historique if compte == t[1] or compte == t[2]]
    else:
        historique_filtre = historique.copy()
    
    res = sorted(historique_filtre, key=lambda x: x[4], reverse=True)
    return res

def enregistrer_transaction(historique: list, operation: str, montant: float, compte_1: str, compte_2: str = None): 
    """ Construire et stocker une entree """
    transaction_date = datetime.now().isoformat()
    transaction = (operation, compte_1, compte_2, montant, transaction_date)
    historique.append(transaction)
    
def creer_un_compte(comptes: dict, nom: str, solde: float):
    if nom in comptes:
        logger.error("Erreur lors de la creation du compte.")
        raise CompteDejaExistantError("Un compte avec ce nom existe deja.")
    elif solde < 0:
        logger.warning("Erreur lors de la creation du compte.")
        raise MontantInvalideError("Le solde doit etre superieure ou egale a 0.")
    else:
        comptes[nom] = solde
        logger.info("Compte cree avec succes!")

def charger_les_donnees() -> tuple[dict, list]:
    try:
        with open(DATA_FILE, "r", encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict) and "comptes" in data and "historique" in data and isinstance(data["comptes"], dict) and isinstance(data["historique"], list):
                comptes = data["comptes"]
                historique = data["historique"]
                return (comptes, historique)
    except FileNotFoundError:
        return ({}, [])
    except json.JSONDecodeError:
        logger.error("Fichier JSON corrompu")
        return ({}, [])
    except (UnicodeDecodeError, KeyError, TypeError) as e:
        logger.error(e)
        return ({}, [])

def sauvegarder(comptes: dict, historique: list):
    data = {"comptes": comptes, "historique": historique}
    with open(DATA_FILE, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)