class Card:
    """Représente une carte de jeu."""

    isShown: bool = False

    def __init__(self, value: str):
        self.value: str = value
