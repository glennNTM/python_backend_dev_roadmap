import logging

from operations import deposer, retirer, transferer, charger_historique, creer_un_compte, consulter_solde, charger_les_donnees, sauvegarder
from exceptions import KwiziPayError
from config import setup_logging

logger = logging.getLogger(__name__)  

menu = """

    [1]: Créer un compte.
    [2]: Consulter un solde.
    [3]: Dépôt.
    [4]: Retrait.
    [5]: Transfert.
    [6]: Historique.
    [7]: Quitter.

    """

def main():
        setup_logging()

        comptes, historique = charger_les_donnees()
        print("Bienvenue dans KwiziPay, vote gestionnaire de portefeuille Mobile Money (CLI). Quelle operation voulez-vous faire? : ")


        while True:
            try:
                choix = (input(menu))
                if choix in ['1', '2', '3', '4', '5', '6', '7']:
                    match choix:

                        # Creer un compte
                        case '1': 
                            compte_nom = input("Entrez le nom du compte que vous-voulez creer: ")
                            if not compte_nom:
                                print("Vous n'avez pas entrer de nom, l'operation va etre annuler.")
                                continue
                            try:
                                solde_initial = float(input("Entrez votre solde initial: "))

                                creer_un_compte(comptes, compte_nom, solde_initial)
                                print(f"Le compte {compte_nom} a ete cree avec un solde {solde_initial} XAF")
                                sauvegarder(comptes, historique)

                            except KwiziPayError as e:
                                print(e)
                                logger.warning(e)                      

                        # Consulter le solde d'un compte
                        case '2':
                            try:
                                compte_a_consulter = input("Entrez le nom du compte que vous souhaitez consulter: ")
                                if not compte_a_consulter:
                                    print("Vous n'avez pas entrer de nom, l'operation va etre annuler.")
                                    continue
                                elif compte_a_consulter not in comptes:
                                    print("Ce compte n'existe pas.")
                                else:
                                    solde = consulter_solde(comptes, compte_a_consulter)
                                    print(f"Le solde du compte {compte_a_consulter} est de {solde} XAF")
                            except KwiziPayError as e:
                                print(e)
                                logger.warning(e)
                        
                        # Faire un depot sur un compte
                        case '3':
                            try:
                                compte_recepteur = input("Sur quel compte souhaitez-vous faire un depot? : ")
                                montant_du_depot = float(input("Combien souhaitez-vous deposer? : "))
                                deposer(comptes, compte_recepteur, montant_du_depot, historique)
                                sauvegarder(comptes, historique)

                                print(f"Le depot de {montant_du_depot} sur le compte {compte_recepteur} a ete effectue avec succes.")

                            except KwiziPayError as e:
                                print(e)
                                logger.warning(e)


                        # Faire un retrait sur un compte
                        case '4':
                            try:
                                compte_de_retrait = input("Sur quel compte souhaitez-vous retirer de l'argent? : ")
                                montant_du_retrait = float(input("Combien souhaitez-vous retirer? : "))
                                retirer(comptes, compte_de_retrait, montant_du_retrait, historique)
                                sauvegarder(comptes, historique) 

                                print(f"Le retrait de {montant_du_retrait} du compte {compte_de_retrait} a ete effectue avec succes. ")
                            except KwiziPayError as e:
                                print(e)
                                logger.warning(e)
                            except ValueError as e:
                                print(e)
                                logger.error(e)

                        # Faire un virement d'un compte a un autre
                        case '5':
                            try:
                                donneur = input("Depuis quel compte souhaitez-vous envoyer de l'argent? : ")
                                recepteur = input("Vers quel compte souhaitez-vous envoyer de l'argent? : ")
                                montant_du_virement = float(input("Combien souhaitez-vous envoyer? : "))
                                transferer(comptes, donneur, recepteur, montant_du_virement, historique)
                                sauvegarder(comptes, historique)
                                print(f"Le virement de {montant_du_virement} du compte {donneur} vers le compte {recepteur} a ete effectue avec succes.")
                            except KwiziPayError as e:
                                print(e)
                                logger.warning
                            except ValueError as e:
                                print(e)
                                logger.error(e)

                        
                        # Consulter l'historique des transactions 
                        case '6':
                            historique_de_compte = input("L'historique de quel compte voulez-vous consulter? (Laisser vide pour consulter l'historique de tous les comptes) : ")
                            t = charger_historique(historique, historique_de_compte)
                            if t:
                                for operation, compte_1, compte_2, montant, date in t:
                                    if compte_2:
                                        print(f"Transfert de {compte_1} a {compte_2}: {montant} XAF le {date}\n")
                                    else:
                                        print(f"{operation} sur {compte_1}: {montant} XAF le {date}\n")
                            else:
                                print("Aucune transaction.")
                        
                        # Quitter
                        case '7':
                            sauvegarder(comptes, historique)
                            print("Sauvegarde faite.")
                            break
                else:
                    print("Choisissez parmi les options disponibles.")
                    logger.warning(f"Choix invalide : {choix}")
            except KeyboardInterrupt:
                sauvegarder(comptes, historique)
                print("Au revoir.")
                logger.info("Sortie clavier.")
                break
            except EOFError:
                sauvegarder(comptes, historique)
                print("Au revoir.")
                logger.info("Sortie clavier.")
                break

if __name__=="__main__":
    main()