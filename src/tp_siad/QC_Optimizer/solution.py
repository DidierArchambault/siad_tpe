import sys

class Solution:
    def __init__(self):
            pass

    def evaluate(self) -> float:
        # TODO Ajouter le code pour calculer la valeur de la fonction objectif # dans les classes dérivées
        # Nous supposons que la valeur de l'objectif doit être minimisée.
        # Par défaut, nous retournons donc la plus grande valeur possible pour # un nombre à virgule flottante.
        return sys.float_info.max

    def validate(self) -> bool:
        # TODO Ajouter le code pour vérifier si une solution est réalisable # dans les classes dérivées
        # Pour l'instant, nous avons une solution vide que nous considérons # toujours non réalisable.
        return False