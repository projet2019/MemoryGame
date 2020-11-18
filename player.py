class Player:

    score = 0;

    def __init__(self):
        self.cards = set()

    def gainCard(self, card):
        self.cards.add(card)

    def getScore(self):
        return len(self.cards)

