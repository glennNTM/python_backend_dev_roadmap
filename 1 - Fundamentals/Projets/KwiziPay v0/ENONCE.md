# KwiziPay v0 — Énoncé du projet

## Contexte

Dans une grande partie de l'Afrique, l'argent circule par mobile money : un compte identifié par un nom ou un numéro, un solde, et des opérations élémentaires réalisées depuis un téléphone. KwiziPay est une simulation de ce service.

Tu dois écrire la **v0** : une application en ligne de commande, exécutée dans un terminal, utilisée par une seule personne à la fois.

---

## Mission

Construire un gestionnaire de portefeuille mobile money utilisable via un menu interactif au clavier.

L'utilisateur doit pouvoir :

- créer un compte ;
- consulter le solde d'un compte ;
- déposer de l'argent sur un compte ;
- retirer de l'argent d'un compte ;
- transférer de l'argent d'un compte vers un autre ;
- consulter l'historique des transactions ;
- quitter l'application.

L'état des comptes survit à la fermeture de l'application : au relancement, les soldes et l'historique sont ceux de la session précédente.

---

## Parcours utilisateur

Le menu se réaffiche après chaque opération, qu'elle ait réussi ou échoué. À n'importe quelle question, une saisie vide annule l'opération en cours et ramène au menu — sans quoi l'utilisateur se retrouve prisonnier d'une saisie dont il ne sait pas sortir.

**Créer un compte.** L'utilisateur donne un nom. Si ce nom est déjà pris, l'opération est refusée. Il donne ensuite un solde initial, éventuellement nul. Le compte créé est confirmé à l'écran.

**Consulter un solde.** L'utilisateur donne un nom de compte et voit le solde correspondant. C'est le premier geste d'un utilisateur de mobile money : il doit être accessible sans passer par une opération.

**Dépôt.** L'utilisateur désigne le compte à créditer, puis le montant. Le compte est crédité et le nouveau solde affiché.

**Retrait.** Même chemin que le dépôt, avec un contrôle supplémentaire sur le solde. En cas de refus, l'utilisateur apprend quel est son solde disponible, et ce solde reste strictement inchangé.

**Transfert.** L'utilisateur désigne un compte source, un compte destination et un montant. Toutes les conditions sont vérifiées **avant** la moindre modification : si l'une échoue, aucun des deux comptes ne bouge. Sinon, les deux nouveaux soldes sont affichés.

**Historique.** L'utilisateur peut cibler un compte ou demander l'ensemble. Les transactions sont présentées de la plus récente à la plus ancienne. L'absence de transaction est annoncée explicitement, pas rendue par une liste vide.

**Quitter.** L'état est sauvegardé, l'utilisateur salué, l'application sort proprement. Une interruption clavier suit exactement le même chemin.

**Choix hors menu.** Une entrée qui ne correspond à aucune option produit un message d'option invalide et un retour au menu.

---

## Règles métier

- Un montant d'opération est strictement positif.
- Deux comptes ne peuvent pas porter le même nom.
- Un retrait ne peut pas rendre un solde négatif.
- Une opération sur un compte qui n'existe pas est refusée.
- Un transfert est **atomique** : soit les deux comptes sont mis à jour, soit aucun ne l'est. Aucun cas de figure ne doit faire disparaître de l'argent.
- Un compte ne peut pas se transférer de l'argent à lui-même.
- Chaque transaction réussie est enregistrée avec sa nature, son montant, le ou les comptes concernés et sa date.

---

## Contraintes

- Python, bibliothèque standard uniquement.
- Aucune classe : paradigme impératif et modulaire. (La version orientée objet viendra en phase 2.)
- Aucune base de données, aucune interface graphique, aucun framework.
- Le code métier ne parle jamais au terminal : l'affichage et la saisie sont concentrés en un seul endroit.
- Les messages de diagnostic passent par un système de journalisation, pas par des affichages console.
- Aucune donnée sensible en clair dans les journaux.

---

## Critères d'acceptation

L'application est considérée comme terminée quand elle satisfait ces comportements :

1. Elle démarre sans erreur alors qu'aucune donnée n'a encore jamais été enregistrée.
2. Elle démarre sans erreur alors que le fichier de données a été vidé ou corrompu à la main.
3. Une saisie absurde au menu (lettre, nombre hors menu, ligne vide) ne fait jamais planter l'application.
4. Un compte n'apparaît que par l'option de création : aucune autre opération ne crée un compte au passage, une faute de frappe sur un nom produit un refus et non un nouveau compte.
5. Un montant négatif ou nul est refusé, avec un message compréhensible.
6. Un retrait supérieur au solde est refusé et laisse le solde inchangé.
7. Un transfert vers un compte inexistant laisse le compte source **intact**.
8. Une interruption clavier (Ctrl+C) sort proprement, sans perte de données.
9. Après redémarrage, l'état est identique à celui de la fin de la session précédente.
10. Le fichier de journal rend compte des opérations réussies, des refus métier et des erreurs techniques, chacun à son niveau de gravité.

---

## Livrable

Un dossier de projet exécutable par `python main.py`, dont le README décrit fidèlement ce que le code fait — ni plus, ni moins.
