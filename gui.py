from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
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

        for i, card in enumerate(self.game.board.cards):
            button: Button = Button(text='?', on_press=lambda event, arg=i: self.update(arg))
            self.cardButtons.append(button)
            self.boardWidget.add_widget(button)
            self.add_widget(self.scoreLabel)
            self.add_widget(self.currPlayerLabel)
        self.add_widget(self.boardWidget)

        if self.game.isInputValid(i) and len(self.game.chosenCards) < 2:
            self.game.showPlayerTurn()
            turnEnded: bool = self.game.update(i)
            card: str = self.game.board.getCard(i)
            button: Button = self.cardButtons[i]
            button.text = card
            button.background_color = (0, 0, 1, 1)


class MemoryApp(App):
    def build(self):
        return MemoryGame(orientation='vertical')


if __name__ == '__main__':
    MemoryApp().run()
