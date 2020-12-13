import unittest
from board import Board
from player import Player


def testHideCard(self):
    """Test qu'une carte soit bien cachée sur le plateau"""
    self.board.hideCard(3)
    self.assertFalse(self.board.isShown(3), "La carte devrait être cachée")


