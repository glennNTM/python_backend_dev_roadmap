from config import setup_logging, DATA_FILE
from exceptions import CompteInexistantError, CompteDejaExistantError, MontantInvalideError, SoldeInsuffisantError

import json, logging


logger = logging.getLogger(__name__)  

def deposer(comptes: dict, nom: str, montant: float):
     if not nom in comptes:
            raise CompteInexistantError("Ce compte n'existe pas.")
     elif montant <= 0:
         raise MontantInvalideError("Le montant doit etre superieure a 0.")
     else:
         comptes[nom] += montant
         logger.info(f"Depot sur le compte {nom} effectue avec succes!")

def consulter_solde(comptes: dict, nom: str):
    if not nom in comptes:
    # On verifie si le comte est bien existant
        raise CompteInexistantError("Ce compte n'existe pas.")
    else:
        return comptes[nom]


def retirer(comptes: dict, nom: str, montant: float, ):
    if not nom in comptes:
        raise CompteInexistantError("Ce compte n'existe pas.")
    elif montant <= 0:
        raise MontantInvalideError("Le montant doit etre superieure a 0.")
    elif comptes[nom] < montant:
        raise SoldeInsuffisantError(f"Le solde {comptes[nom]} est insuffisant pour effectuer cette operation.")
    else:
        comptes[nom] -= montant
        logger.info(f"Retrait sur le compte {nom} effectue avec succes!")
   

def transferer():
    print("Vous voulez faire un transfert")

def historique():
    print("Vous voulez consulter votre historique")

def creer_un_compte(comptes: dict, nom: str, solde: float):
    if nom in comptes:
        raise CompteDejaExistantError("Un compte avec ce non existe deja.")
    elif solde < 0:
        raise MontantInvalideError("Le solde doit etre superieure ou egale a 0.")
    else:
        comptes[nom] = solde
        logger.info("Compte cree avec succes!")



def charger_les_donnees() -> dict:
    try:
        with open(DATA_FILE, "r", encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        logger.error("Fichier JSON corrompu")
        return {}


def sauvegarder(comptes: dict):
    with open(DATA_FILE, "w", encoding='utf-8') as f:
        json.dump(comptes, f, indent=2)
   