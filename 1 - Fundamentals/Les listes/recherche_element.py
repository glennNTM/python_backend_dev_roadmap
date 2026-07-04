"""
Vous avez une liste d'éléments et devez fréquemment vérifier si un élément spécifique est présent dans cette liste.

Écrivez une fonction est_present qui prend une liste d'éléments et un élément à rechercher.

La version initiale de la fonction effectue cette vérification de manière inefficace (en O(n)).

Vous devrez modifier cette fonction pour la rendre plus efficiente (en O(1)).

"""

def est_present(liste : list, element: int | str | float | bool) -> bool:
   return element in set(liste)