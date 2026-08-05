# Point d'entrer de l'application



choix = int(input("""

Bienvenue dans KwiziPay, vote gestionnaire de portefeuille Mobile Money (CLI). Quelle operation voulez-vous faire? : 

[1] : Depot
[2]: Retrait
[3]: Historique
[4]: Transfert

"""))

match choix:
    case 1:
        print("Vous voulez faire un depot")
    case 2:
            print("Vous voulez faire un retrait")
    case 3:
            print("Vous voulez consulter votre historique")
    case 4:
            print("Vous voulez effectuer un transfert")