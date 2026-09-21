from operations import deposer, retirer, transferer, charger_historique, creer_un_compte, consulter_solde, charger_les_donnees, sauvegarder
from exception import MontantInvalideError, CompteDejaExistantError


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
                        continue
                    else:
                        solde_initial = float(input("Entrez votre solde initial: "))
                        if not solde_initial:
                            raise MontantInvalideError("Le ontant du solde initial est invalide. Entrez une valeur correcte.")
                        continue
                    try:
                        creer_un_compte(comptes, compte_nom, solde_initial)
                    except CompteDejaExistantError:
                        print("Ce compte exsite deja.")

                case '2':
                    consulter_solde()
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
