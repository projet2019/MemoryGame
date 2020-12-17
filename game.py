from board import Board
from player import Player
from error import InvalidInputError, InvalidCardError
from datetime import datetime


class Game:
    """Gère le déroulement du jeu"""

    board = Board()
    players = [Player(), Player()]
    chosenCards = []

    def play(self):
        """Démarre une partie."""
        currPlayer = 0

        print("Début de la partie")
        self.board.draw()
        while self.players[0].getScore() + self.players[1].getScore() < self.board.getPairCount():
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
        print("Fin de la partie")
        for i in range(2):
            print(f'Le joueur {i + 1} a trouvé {self.players[i].getScore()} paire')
            f = open("games.log", "a")
            dateTime = datetime.now()
        if self.players[0].getScore() > self.players[1].getScore():
            print("Le joueur 1 a gagné!")
            f.write(
                f'{dateTime.day}/{dateTime.month}/{dateTime.year} {dateTime.hour}:{dateTime.minute} Le joueur 1 a gagné!\n')
        elif self.players[0].getScore() < self.players[1].getScore():
            print("Le joueur 2 a gagné!")
            f.write(
                f'{dateTime.day}/{dateTime.month}/{dateTime.year} {dateTime.hour}:{dateTime.minute} Le joueur 2 a gagné!\n')
        else:
            print("Egalité!")
            f.write(f'{dateTime.day}/{dateTime.month}/{dateTime.year} {dateTime.hour}:{dateTime.minute} Egalité!\n')
            f.close()

    def processInput(self):
        """Récupère une commande valide de la part de l'utilisateur."""
        hasValidInput = False

        while not hasValidInput:
            try:
                inputString = input("Choisissez une carte : ")
                if not inputString.isnumeric():
                    raise InvalidInputError
                i = int(inputString) - 1
                if self.board.isOnBoard(i) and not self.board.isShown(i):
                    hasValidInput = True
                else:
                    raise InvalidCardError
            except InvalidInputError:
                print("Commande non valide!")
                continue
            except InvalidCardError:
                print("Vous ne pouvez pas choisir cette carte!")
                continue

        return i
