import unittest
from board import Board

from player import Player


def testHideCard(self):
    """Test qu'une carte soit bien cachée sur le plateau"""
    self.board.hideCard(3)
    self.assertFalse(self.board.isShown(3), "La carte devrait être cachée")


def test5IsOnBoard(self):
    """Test qu'un nombre est bien dans les limites du plateau"""
    self.assertTrue(self.board.isOnBoard(5), "5 devrait faire partie du plateau de jeu")


def test18IsNotOnBoard(self):
    """Test qu'un nombre est bien en dehors des limites du plateau"""
    self.assertFalse(self.board.isOnBoard(18), "18 ne devrait pas faire partie du plateau de jeu")


class TestPlayer(unittest.TestCase):
    """Test que le joueur soit correctement implémenté"""

    player = Player()


def testScore(self):
    """Test que le score soit correctement calculé"""
    self.player.gainCard('S')
    self.player.gainCard('A')
    self.player.gainCard('C')
    self.assertEqual(self.player.getScore(), 3, "Le joueur doit avoir 3 paires")



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
