import string
import random
from card import Card
from typing import List


class Board:
    """Crée et gère les cartes du jeu."""
    size = 4

    def __init__(self):
        pairCount = int(self.getPairCount())
        values = list(string.ascii_uppercase[0:pairCount])
        pairCount: int = int(self.getPairCount())
        values: List[str] = list(string.ascii_uppercase[0:pairCount])
        values += values  # double les valeurs
        random.shuffle(values)
        self.cards = [Card(value) for value in values]
        self.cards: List[Card] = [Card(value) for value in values]

    def getCard(self, i) -> str:  # i(int): Numéro de la carte
        """Renvoie la value d'une carte à une position donnée . 
            PRE: i (int) d'une valeur >= 0 et < self.size*self.size
            POST: Renvoie str valeur de la carte choisie
            RAISES: -
        """

        return self.cards[i].value

    def showCard(self, i: int):  # i(int): Numéro de la carte
        """
        Indique qu'une carte à une position donnée doit être affichée.
         PRE:i: int d'une valeur >= 0 et < self.size*self.size
         POST: attribut isShown de la carte choisie est True
         RAISES: -
        """
        self.cards[i].isShown = True

    def hideCard(self, i: int):
        """
        Indique qu'une carte à une position donnée doit être cachée.
        PRE: i: int d'une valeur >= 0 et < self.size*self.size
        POST: attribut isShown de la carte choisie est False
        RAISES: -
        """
        self.cards[i].isShown = False

    def isOnBoard(self, i: int) -> bool:
        """
        Indique si la position donnée se trouve bien sur le plateau de jeu.
        PRE: i (int): Numéro de la carte
        POST:  Renvoie bool True si la carte est dans les limites. False sinon
        RAISES:-
        """
        return 0 <= i < self.size * self.size

    def getPairCount(self) -> int:
        """
        Renvoie le nombre de paire.
        PRE: -
        POST: Renvoie int le nombre de paire
        RAISES:-
        """
        return self.size * self.size / 2

    def isShown(self, i: int) -> bool:
        """
        Indique si une carte à une position donnée est affichée ou cachée.
        PRE: i (int): Numéro de la carte
        POST:  bool: True si la carte est affichée et False sinon
        RAISES:-
        """
        return self.cards[i].isShown

    def draw(self):
        """Affiche le plateau de jeu dans la console.
            PRE: -
            POST: Si une carte est cachée, affiche X dans le terminal.
                  Sinon, affiche la valeur de la carte.
            RAISES: -
        """

        display: str = ""
        for i, card in enumerate(self.cards):
            if card.isShown:
                display += " {} ".format(card.value)
            else:
                display += " X "
            if i % self.size == self.size - 1 and i != self.size * self.size - 1:
                display += "\n"
        print(display)
