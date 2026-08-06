from config import setup_logging, DATA_FILE

import json, logging


logger = logging.getLogger(__name__)  

def charger_les_donnees():
    logger.error("Fichier JSON corrompu")

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

def creer_un_compte(compte_nom: str):
    compte_nom = input("Entrz le nom du compte que vous-voulez creer: ")
    json.load(DATA_FILE)