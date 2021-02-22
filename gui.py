from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from board import Board
from player import Player
from datetime import datetime
from card import Card
from typing import List, Tuple, TextIO
from game import Game

class MemoryGame(BoxLayout):
    """Gère le déroulement du jeu et les widgets de la fenêtre"""

    game: Game = Game()
    cardButtons: List[Button] = []
    chosenCardButtons: List[Tuple[Button, str]] = []

    def __init__(self, **kwargs):
        super(MemoryGame, self).__init__(**kwargs)
        self.scoreLabel: Label = Label(
            text=f'Nombre de paire: Joueur 1 ({self.game.players[0].getScore()}) - Joueur 2 ({self.game.players[1].getScore()})',
            size_hint=(1, None), height=30)
        self.currPlayerLabel: Label = Label(text=f'Tour du joueur {self.game.currPlayer + 1}', size_hint=(1, None), height=30)
        self.boardWidget: GridLayout = GridLayout(cols=4, rows=4, padding=10, spacing=10)
        for i, card in enumerate(self.game.board.cards):
            button: Button = Button(text='?', on_press=lambda event, arg=i: self.update(arg))
            self.cardButtons.append(button)
            self.boardWidget.add_widget(button)
        self.add_widget(self.scoreLabel)
        self.add_widget(self.currPlayerLabel)
        self.add_widget(self.boardWidget)
        print(f'Tour du joueur {self.currPlayer + 1} (Nombre de paire : {self.players[self.currPlayer].getScore()})')
        self.board.draw()
        self.game.showStartGame()
    def update(self, i: int):
        """Met à jour l'interface lorsqu'une carte est sélectionnée
        PRE: i: int d'une valeur >= 0 et < board.size*board.size
        POST: Affiche le tour du joueur et son nombre de paire dans l'interface
              Affiche les cartes selectionnées dans l'interface
        RAISES: -
        """
        if self.game.isInputValid(i) and len(self.game.chosenCards) < 2:
            self.game.showPlayerTurn()
            turnEnded: bool = self.game.update(i)
            card: str = self.game.board.getCard(i)
            button: Button = self.cardButtons[i]
            button.text = card
            button.background_color = (0, 0, 1, 1)
            self.chosenCards.append((i, card))
            self.chosenCardButtons.append((button, card))
            if len(self.chosenCardButtons) == 2:
                Clock.schedule_once(self.resetChosenCard, 1)  # attend 1s avant de cacher la carte

    def resetChosenCard(self, dt: float):
        """Supprime les cartes sélectionnées et met à jour l'affichage du score
        PRE: dt: float d'une valeur > 0
        POST: Met à jour le tour du joueur dans l'interface
              Met à jour les cartes selectionnées
        RAISES: -
"""
        for button in self.chosenCardButtons:
            if self.chosenCardButtons[0][1] != self.chosenCardButtons[1][1]:
                button[0].text = '?'
            button[0].background_color = (1, 1, 1, 1)
        self.chosenCardButtons.clear()
        self.scoreLabel.text = f'Nombre de paire: Joueur 1 ({self.game.players[0].getScore()}) - Joueur 2 ({self.game.players[1].getScore()})'
        if self.game.players[0].getScore() + self.game.players[1].getScore() < self.game.board.getPairCount():
            self.currPlayerLabel.text = f'Tour du joueur {self.game.currPlayer + 1}'

        else:
            self.currPlayerLabel.text = 'Fin de la partie'
            print("Fin de la partie")
            f = open("games.log", "a")
            dateTime = datetime.now()
            if self.players[0].getScore() > self.players[1].getScore():
                print("Le joueur 1 a gagné!")
                f.write(f'{dateTime.day}/{dateTime.month}/{dateTime.year} {dateTime.hour}:{dateTime.minute} Le joueur 1 a gagné!\n')
            elif self.players[0].getScore() < self.players[1].getScore():
                print("Le joueur 2 a gagné!")
                f.write(f'{dateTime.day}/{dateTime.month}/{dateTime.year} {dateTime.hour}:{dateTime.minute} Le joueur 2 a gagné!\n')
            else:
                print("Egalité!")
                f.write(f'{dateTime.day}/{dateTime.month}/{dateTime.year} {dateTime.hour}:{dateTime.minute} Egalité!\n')
            f.close()
            self.game.showEndGame()

class MemoryApp(App):
    def build(self):
        return MemoryGame(orientation='vertical')


if __name__ == '__main__':
    MemoryApp().run()
