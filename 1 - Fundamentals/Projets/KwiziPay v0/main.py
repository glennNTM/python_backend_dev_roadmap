from operations import deposer, retirer, transferer, charger_historique, creer_un_compte, consulter_solde, charger_les_donnees, sauvegarder
from exceptions import CompteInexistantError, MontantInvalideError, SoldeInsuffisantError, OperationInvalideError



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

                # Creer un compte
                case '1': 
                    compte_nom = input("Entrez le nom du compte que vous-voulez creer: ")
                    if not compte_nom:
                        print("Vous n'avez pas entrer de nom, l'operation va etre annuler.")
                        continue
                    try:
                        solde_initial = float(input("Entrez votre solde initial: "))

                        creer_un_compte(comptes, compte_nom, solde_initial)
                        print(f"Le compte {compte_nom} a ete cree avec un solde {solde_initial}")
                        sauvegarder(comptes, historique)

                    except CompteInexistantError as e:
                        print(e)
                    except MontantInvalideError as e:
                        print(e)
                    except ValueError as e:
                        print(e)

                # Consulter le solde d'un compte
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
                
                # Faire un depot sur un compte
                case '3':
                    try:
                        compte_recepteur = input("Sur quel compte souhaitez-vous faire un depot? : ")
                        montant_du_depot = float(input("Combien souhaitez-vous deposer? : "))
                        deposer(comptes, compte_recepteur, montant_du_depot, historique)
                        sauvegarder(comptes, historique)

                    except CompteInexistantError as e:
                        print(e)
                    except MontantInvalideError as e:
                        print(e)
                    except ValueError as e:
                        print(e)

                # Faire un retrait sur un compte
                case '4':
                    try:
                        compte_de_retrait = input("Sur quel compte souhaitez-vous retirer de l'argent? : ")
                        montant_du_retrait = float(input("Combien souhaitez-vous retirer? : "))
                        retirer(comptes, compte_de_retrait, montant_du_retrait, historique)
                        sauvegarder(comptes, historique) 
                    except CompteInexistantError as e:
                        print(e)
                    except MontantInvalideError as e:
                        print(e)
                    except OperationInvalideError as e:
                        print(e)
                    except ValueError as e:
                        print(e)

                # Faire un virement d'un compte a un autre
                case '5':
                    try:
                        donneur = input("Depuis quel compte souhaitez-vous envoyer de l'argent? : ")
                        recepteur = input("Vers quel compte souhaitez-vous envoyer de l'argent? : ")
                        montant_du_virement = float(input("Combien souhaitez-vous envoyer? :"))
                        transferer(comptes, donneur, recepteur, montant_du_virement, historique)
                        sauvegarder(comptes, historique)
                    except CompteInexistantError as e:
                        print(e)
                    except MontantInvalideError as e:
                        print(e)
                    except SoldeInsuffisantError as e:
                        print(e)
                    except ValueError as e:
                        print(e)

                
                # Consulter l'historique des transactions 
                case '6':
                    historique_de_compte = input("L'historique de quel compte voulez-vous consulter? (Laisser vide pour consulter l'historique de tous les comptes) : ")
                    t = charger_historique(historique, historique_de_compte)
                    if t:
                        print(t)
                    else:
                        print("Aucune transaction.")
                
                # Quitter
                case '7':
                    sauvegarder(comptes, historique)
                    print("Sauvegarde faite.")
                    break
        else:
            print("Choisissez parmi les options disponibles.")
    except KeyboardInterrupt:
        sauvegarder(comptes, historique)
        print("Au revoir.")
        break
