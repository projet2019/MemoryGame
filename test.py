import unittest
from board import Board


class TestBoard(unittest.TestCase):
    """Test que le plateau de jeu est correctement généré"""

    board = Board()

    def testCardNumber(self):
        """Test qu'il y ait le bon nombre de carte sur le plateau"""
        self.assertEqual(len(self.board.cards), 16, "Il faut 16 cartes")
