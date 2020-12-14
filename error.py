class MemoryGameError(Exception):
    """Classe de base pour les erreurs du jeu"""
    pass


class InvalidInputError(MemoryGameError):
    """Exception indiquant que la commande entrée est invalide"""
    pass


class InvalidCardError(MemoryGameError):
    """Exception indiquant que la carte selectionnée a déjà été choisi ou est en dehors du plateau de jeu"""
    pass
