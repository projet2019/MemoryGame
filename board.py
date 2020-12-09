import string
import random
from card import Card


class Board:
    """Crée et gère les cartes du jeu."""
    size = 4

    def __init__(self):
        pairCount = int(self.getPairCount())
        values = list(string.ascii_uppercase[0:pairCount])
        values += values  # double les valeurs
        random.shuffle(values)
        self.cards = [Card(value) for value in values]

    def getPairCount(self):
        """Renvoie le nombre de paire."""
        return self.size * self.size / 2

    def getCard(self, i):
        """Renvoie la value d'une carte à une position donnée."""
        return self.cards[i].value

    def showCard(self, i):
        """Indique qu'une carte à une position donnée doit être affichée."""
        self.cards[i].isShown = True

    def hideCard(self, i):
        """Indique qu'une carte à une position donnée doit être cachée."""
        self.cards[i].isShown = False


    def isOnBoard(self, i):
        """Indique si la position donnée se trouve bien sur le plateau de jeu."""
        return 0 <= i < self.size * self.size

    def getPairCount(self):
        """Renvoie le nombre de paire."""
        return self.size * self.size / 2

    def isShown(self, i):
        """Indique si une carte à une position donnée est affichée ou cachée."""
        return self.cards[i].isShown

    def draw(self):
        """Affiche le plateau de jeu dans la console.

    Si une carte est cachée, affiche X.
    Sinon, affiche la valeur de la carte."""
          

        display = ""
        for i, card in enumerate(self.cards):
            if card.isShown:
                display += " {} ".format(card.value)
            else:
                display += " X "
            if i % self.size == self.size - 1 and i != self.size * self.size - 1:
                display += "\n"
        print(display)
