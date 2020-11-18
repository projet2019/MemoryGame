from board import Board

from player import Player


class Game:
    board = Board()
    players = [Player(), Player()]
    chosenCards = []

    def play(self):
        self.board.draw()

        isPlaying = True
        currPlayer = 0

        self.board.draw()
        while isPlaying:
            score = self.players[currPlayer].getScore()
            print(f'Tour du joueur {currPlayer + 1} (Nombre de paire : {score})')
            i = self.processInput()

            self.board.showCard(i)
            self.board.draw()

            card = self.board.getCard(i)
            self.chosenCards.append((i, card))
            if len(self.chosenCards) == 2:
                if self.chosenCards[0][1] == self.chosenCards[1][1]:
                    self.players[currPlayer].gainCard(card)
                    print("Vous avez trouvé une paire!")
                else:
                    self.board.hideCard(self.chosenCards[0][0])
                    self.board.hideCard(self.chosenCards[1][0])
                    currPlayer ^= 1  # change 0 en 1 et 1 en 0
                    print("Vous n'avez pas trouvé de paire...")
                self.chosenCards.clear()
                self.board.draw()

    def processInput(self):
        hasValidInput = False
        hasEnteredInput = False
        while not hasValidInput:
            if hasEnteredInput:
                print("Vous ne pouvez pas choisir cette carte!")
            print("Choisissez une carte")
            i = int(input()) - 1
            hasEnteredInput = True
            if self.board.isOnBoard(i):
                hasValidInput = True
        return i

