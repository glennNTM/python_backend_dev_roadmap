from config import setup_logging, DATA_FILE

import json, logging


logger = logging.getLogger(__name__)  

def deposer():
    print("Vous voulez faire un depot")

def consulter_solde():
    print("Vous-voulez consulter un solde")
    
def retirer():
    print("Vous voulez faire un retrait")


def transferer():
    print("Vous voulez faire un transfert")

def historique():
    print("Vous voulez consulter votre historique")

def creer_un_compte(comptes: dict, nom: str, solde: float):
    pass


def charger_les_donnees() -> dict:
    try:
        with open(DATA_FILE, "r", encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        logger.error("Fichier JSON corrompu")
        return {}


