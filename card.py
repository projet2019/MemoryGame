class Card:
    """Représente une carte de jeu."""

    def __init__(self, value: str):
        self.value: str = value
        self.isShown: bool = False
