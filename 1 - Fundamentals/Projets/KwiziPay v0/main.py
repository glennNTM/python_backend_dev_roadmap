from operations import deposer, retirer, transferer, historique

options_dispo = range(1, 5)
while True:

    choix = int(input("""

    Bienvenue dans KwiziPay, vote gestionnaire de portefeuille Mobile Money (CLI). Quelle operation voulez-vous faire? : 

    [1] : Depot
    [2]: Retrait
    [3]: Historique
    [4]: Transfert

    """))
    while choix in [1, 2, 3, 4]:
        match choix:
            case 1:
                deposer()
            case 2:
                retirer      
            case 3:
                historique()
            case 4:
                transferer()
    else: 
        pass