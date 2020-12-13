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



