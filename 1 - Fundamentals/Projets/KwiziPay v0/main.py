from operations import deposer, retirer, transferer, charger_historique, creer_un_compte, consulter_solde, charger_les_donnees, sauvegarder

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
                    creer_un_compte()
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
                    print("Bye")
                    break
    except KeyboardInterrupt:
        sauvegarder(comptes, historique)
        break
