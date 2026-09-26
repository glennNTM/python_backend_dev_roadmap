import json

from operations import deposer, retirer, transferer, charger_historique, creer_un_compte, consulter_solde, charger_les_donnees, sauvegarder
from config import DATA_FILE



menu = """

    [1]: Créer un compte.
    [2]: Consulter un solde.
    [3]: Dépôt.
    [4]: Retrait.
    [5]: Transfert.
    [6]: Historique.
    [7]: Quitter.

    """

comptes, historique = charger_les_donnees()
print("Bienvenue dans KwiziPay, vote gestionnaire de portefeuille Mobile Money (CLI). Quelle operation voulez-vous faire? : ")


while True:
    try:
        choix = (input(menu))
        if choix in ['1', '2', '3', '4', '5', '6', '7']:
            match choix:
                case '1':
                    compte_nom = input("Entrez le nom du compte que vous-voulez creer: ")
                    if not compte_nom:
                        print("Vous n'avez pas entrer de nom, loperation va etre annuler.")
                        break
                    else:
                        solde_initial = float(input("Entrez votre solde initial: "))

                        with open(DATA_FILE, "a", encoding='utf-8') as f:
                            json.dump((compte_nom, solde_initial), f, indent=4)

                        print(f"Le compte {compte_nom} a ete cree avec un solde {solde_initial}")

                    creer_un_compte(comptes, compte_nom, solde_initial)
                case '2':
                    compte_a_consulter = input("Entrez le nom du compte que vous souhaitez consulter: ")
                    if not compte_a_consulter:
                        print("Vous n'avez pas entrer de nom, l'operation va etre annuler.")
                        continue
                    elif compte_a_consulter not in comptes:
                        print("Ce compte n'existe pas.")
                    else:
                        solde = consulter_solde(comptes, compte_a_consulter)
                        print(f"Le solde du compte {compte_a_consulter} est de {solde} XAF")
                case '3':
                    deposer()
                case '4':
                    retirer()
                case '5':
                    transferer()
                case '6':
                    charger_historique()
                case '7':
                    sauvegarder(comptes, historique)
                    print("Sauvegarde faite.")
                    break
    except KeyboardInterrupt:
        sauvegarder(comptes, historique)
        break
