from board import Board
from player import Player
from error import InvalidInputError, InvalidCardError
from datetime import datetime
from typing import List, Tuple, TextIO


class Game:
    """Gère le déroulement du jeu"""

    board: Board = Board()
    players: List[Player] = [Player(), Player()]
    chosenCards: List[Tuple[int, str]] = []
    currPlayer: int = 0


def play(self):
    """Démarre une partie.
           PRE: -
           POST:
            Affiche les message de début de jeu et démarre la partie
            Quand la partie est finie, affiche les messages de fin de jeu
           RAISES: -"""
    self.showStartGame()
    while self.players[0].getScore() + self.players[1].getScore() < self.board.getPairCount():
        self.showPlayerTurn()
        i: int = self.processInput()
        self.update(i)

    self.showEndGame()


def update(self, i: int):
    """Met à jour le jeu selon la carte choisie par le joueur
       ARGS:
        i: Numéro de la carte
       PRE:
        i: int d'une valeur >= 0 et < board.size*board.size
       POST:
        Affiche le nouveau plateau de jeu dans le terminal
        Affiche si le joueur a trouvé une paire ou non
       RAISES: -
       :param i:
       :param self:
    """
    self.board.showCard(i)
    self.board.draw()

    card: str = self.board.getCard(i)
    self.chosenCards.append((i, card))
    if len(self.chosenCards) == 2:
        if self.chosenCards[0][1] == self.chosenCards[1][1]:
            self.players[self.currPlayer].gainCard(card)
            print("Vous avez trouvé une paire!")
        else:
            self.board.hideCard(self.chosenCards[0][0])
            self.board.hideCard(self.chosenCards[1][0])
            self.currPlayer ^= 1  # change 0 en 1 et 1 en 0
            print("Vous n'avez pas trouvé de paire...")
        self.chosenCards.clear()
        self.board.draw()


def showPlayerTurn(self):
    """Affiche les messages relatifs au joueur actuel
               PRE: -
               POST:
                Affiche le joueur actuel et son nombre de paire
               RAISES: -
            """
    score: int = self.players[self.currPlayer].getScore()
    print(f'Tour du joueur {self.currPlayer + 1} (Nombre de paire : {score})')


def showStartGame(self):
    """Affiche les messages de début de la partie.
               PRE: -
               POST:
                Affiche un message d'accueil et le plateau de jeu
               RAISES: -
            """
    print("Début de la partie")
    self.board.draw()


def showEndGame(self):
    """Affiche les messages de fin de la partie.
               PRE: -
               POST:
                Affiche le score de chaque jour et le joueur gagnant dans le terminal
                Ecrit le résultat de la partie dans le fichier games.log
               RAISES: -
            """
    print("Fin de la partie")
    for i in range(2):
        print(f'Le joueur {i + 1} a trouvé {self.players[i].getScore()} paire')
    f: TextIO = open("games.log", "a")
    dateTime: datetime = datetime.now()
    if self.players[0].getScore() > self.players[1].getScore():
        print("Le joueur 1 a gagné!")
        f.write(
            f'{dateTime.day}/{dateTime.month}/{dateTime.year} {dateTime.hour}:{dateTime.minute} Le joueur 1 a gagné!\n')
    elif self.players[0].getScore() < self.players[1].getScore(): \
            print("Le joueur 2 a gagné!")
    f.write(f'{dateTime.day}/{dateTime.month}/{dateTime.year} {dateTime.hour}:{dateTime.minute} Le joueur 2 a gagné!\n')

    print("Egalité!")
    f.write(f'{dateTime.day}/{dateTime.month}/{dateTime.year} {dateTime.hour}:{dateTime.minute} Egalité!\n')
    f.close()


def processInput(self) -> int:
    """Récupère une commande valide de la part de l'utilisateur.
       PRE: -
       POST:
        Renvoie int index de la carte quand une commande valide est entrée.
        Affiche un message d'erreur sinon
       RAISES: -
    """
    hasValidInput: bool = False
    i: int

    while not hasValidInput:
        try:
            hasValidInput, i = self.getInput()
        except InvalidInputError:
            print("Commande non valide!")
            continue
        except InvalidCardError:
            print("Vous ne pouvez pas choisir cette carte!")
            continue
        return i


def isInputValid(self, i: int) -> bool:
    """Vérifie la validité d'une commande.
       ARGS:
        i: Numéro de la carte
       PRE:
        i: int
       POST: Renvoie bool True si la carte est dans les limites et n'est pas affichée
       RAISES: -
       :param i:
       :param self:
    """
    return self.board.isOnBoard(i) and not self.board.isShown(i)


def getInput(self) -> Tuple[bool, int]:
    """Récupère la commande de l'utilisateur.
       PRE: -
       POST: Renvoie Tuple contenant True et l'index de la carte
       RAISES:
        InvalidInputError si la valeur entrée par l'utilisateur n'est pas numérique
        InvalidCardError si l'index de la carte est >= board.size*board.size
          ou si la carte est déjà affichée
    """
    inputString: str = input("Choisissez une carte : ")
    if not inputString.isnumeric():
        raise InvalidInputError
    i: int = int(inputString) - 1
    if self.isInputValid(i):
        return True, i
    else:
        raise InvalidCardError
