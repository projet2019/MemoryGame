class Player:
  """Représente le joueur."""

  def __init__(self):
    self.cards = set()
  
  def gainCard(self, card):
    """Ajoute une paire de carte."""
    self.cards.add(card)
    
  def getScore(self):
    """Calcule le nombre de paire."""
    return len(self.cards)
