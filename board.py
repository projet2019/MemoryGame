import string
import random
from card import Card


class Board:
    size = 4

    def __init__(self):
        pairCount = int(self.size * self.size / 2)
        values = list(string.ascii_uppercase[0:pairCount])
        values += values  # double les valeurs
        random.shuffle(values)
        self.cards = [Card(value) for value in values]
    def getCard(self, i):
        return self.cards[i].value

    def showCard(self, i):
        self.cards[i].isShown = True

    def hideCard(self, i):
        self.cards[i].isShown = False

    def isOnBoard(self, i):
        return i >= 0 and i < self.size * self.size

    def isShown(self, i):
        return self.cards[i].isShown
    def draw(self):
        display = ""
        for i, card in enumerate(self.cards):
            if card.isShown:
                display += " {} ".format(card.value)
            else:
                display += " X "
            if i % self.size == self.size - 1 and i != self.size * self.size - 1:
                display += "\n"
        print(display)

