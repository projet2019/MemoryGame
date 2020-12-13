import unittest
from board import Board


class TestBoard(unittest.TestCase):
    """Test que le plateau de jeu est correctement généré"""

    board = Board()

    def testCardNumber(self):
        """Test qu'il y ait le bon nombre de carte sur le plateau"""
        self.assertEqual(len(self.board.cards), 16, "Il faut 16 cartes")

    def testPairCount(self):
        """Test qu'il y ait le bon nombre de paire de carte sur le plateau"""
        cards = [card.value for card in self.board.cards]
        pairs = set([card for card in cards if cards.count(card) == 2])
        self.assertEqual(len(pairs), 8, "Il faut 8 paires")

    def testShowCard(self):
        """Test qu'une carte soit bien affichée sur le plateau"""
        self.board.showCard(3)
        self.assertTrue(self.board.isShown(3), "La carte devrait être affichée")


if __name__ == "__main__":
    unittest.main()
