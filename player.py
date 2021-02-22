from typing import Set


class Player:
    """Représente le joueur."""

    def __init__(self):
        self.cards: Set[str] = set()

    def gainCard(self, card: str):
        """Ajoute une paire de carte.
    ARGS:
        card: Valeur de la carte
       PRE:
        card: char
       POST: Ajoute la valeur de la carte aux paires du joueur
       RAISES: -
    """
        self.cards.add(card)

    def getScore(self) -> int:
        """Calcule le nombre de paire.
    PRE: -
       POST: Renvoie int nombre de paire trouvé
       RAISES: -
    """
        return len(self.cards)
