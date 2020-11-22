from board import Board
from player import Player


class Game:
    board = Board()
    players = [Player(), Player()]
    chosenCards = []

    def play(self):
        isPlaying = True
        currPlayer = 0

        print("Début de la partie")
        self.board.draw()
        while isPlaying:
            while self.players[0].getScore() + self.players[1].getScore() < self.board.getPairCount():
                score = self.players[currPlayer].getScore()
                print(f'Tour du joueur {currPlayer + 1} (Nombre de paire : {score})')
                i = self.processInput()
                print("Vous n'avez pas trouvé de paire...")
        self.chosenCards.clear()
        self.board.draw()
        print("Fin de la partie")

    def processInput(self):
        hasValidInput = False
        hasEnteredInput = False
        while not hasValidInput:
            if hasEnteredInput:
                print("Vous ne pouvez pas choisir cette carte!")
            print("Choisissez une carte")
            i = int(input()) - 1
            hasEnteredInput = True
            if self.board.isOnBoard(i) and not self.board.isShown(i):
                hasValidInput = True
        return i
