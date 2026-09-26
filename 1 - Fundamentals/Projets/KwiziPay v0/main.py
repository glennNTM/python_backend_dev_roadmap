import json

from operations import deposer, retirer, transferer, charger_historique, creer_un_compte, consulter_solde, charger_les_donnees, sauvegarder
from exceptions import CompteInexistantError
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
                        print("Vous n'avez pas entrer de nom, l'operation va etre annuler.")
                        break
                    else:
                        solde_initial = float(input("Entrez votre solde initial: "))

                        with open(DATA_FILE, "a", encoding='utf-8') as f:
                            json.dump((compte_nom, solde_initial), f, indent=4)

                            creer_un_compte(comptes, compte_nom, solde_initial)
                            print(f"Le compte {compte_nom} a ete cree avec un solde {solde_initial}")

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
                    compte_recepteur = input("Sur quel compte souhaitez-vous faire un depot? : ")
                    if compte_recepteur not in comptes:
                        raise CompteInexistantError("Ce compte existe pas")
                    montant_du_depot = float(input("Combien souhaitez-vous deposer? : "))
                    with open(DATA_FILE, "a", encoding='utf-8') as f:
                        json.dump((compte_recepteur, montant_du_depot), f, indent=4)
                    deposer(comptes, compte_recepteur, montant_du_depot, historique)
                    
                case '4':
                    compte_de_retrait = input("Sur quel compte souhaitez-vous retirer de l'argent? : ")
                    if compte_de_retrait not in comptes:
                            raise CompteInexistantError("Ce compte existe pas")
                    montant_du_retrait = float(input("Combien souhaitez-vous retirer? : "))
                    with open(DATA_FILE, "a", encoding='utf-8') as f:
                        json.dump((compte_de_retrait, montant_du_retrait), f, indent=4)
                        retirer(comptes, compte_de_retrait, montant_du_retrait, historique)
                case '5':
                    donneur = input("Depuis quel compte souhaitez-vous envoyer de l'argnet? :")
                    recepteur = input("Vers quel compte souhaitez-vous envoyer de l'argent? :")
                    montant_du_virement = float(input("Combien souhaitez-vous envoyer? :"))
                    with open(DATA_FILE, "a", encoding='utf-8') as f:
                        json.dump((donneur, recepteur, montant_du_virement), f, indent=4)
                    transferer(comptes, donneur, recepteur, montant_du_virement, historique)
                case '6':
                    historique_de_compte = input("L'historique de quel compte voulez-vous consulter? (Laisser vide pour consulter l'historique de tous les comptes) : ")
                    print(charger_historique(historique, historique_de_compte))
                case '7':
                    sauvegarder(comptes, historique)
                    print("Sauvegarde faite.")
                    break
    except KeyboardInterrupt:
        sauvegarder(comptes, historique)
        break
