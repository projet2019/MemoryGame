class Card:
    isShown = False

    def __init__(self, value):
        self.value = value

    def show(self):
        self.isShown = True
