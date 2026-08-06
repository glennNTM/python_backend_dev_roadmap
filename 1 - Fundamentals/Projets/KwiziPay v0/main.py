from operations import deposer, retirer, transferer, historique, creer_un_compte, consulter_solde

menu = """

    [1]: Créer un compte.
    [2]: Consulter un solde.
    [3]: Dépôt.
    [4]: Retrait.
    [5]: Transfert.
    [6]: Historique.
    [7]: Quitter.

    """

print("Bienvenue dans KwiziPay, vote gestionnaire de portefeuille Mobile Money (CLI). Quelle operation voulez-vous faire? : ")

while True:
    choix = int(input(menu))
    if choix in [1, 2, 3, 4, 5, 6, 7]:
        match choix:
            case 1:
                creer_un_compte()
            case 2:
                consulter_solde()
            case 3:
                deposer()
            case 4:
                retirer()
            case 5:
                transferer()
            case 6:
                historique()
            case 7:
                print("Bye")
                break
        
