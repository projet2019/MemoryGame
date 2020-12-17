from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from board import Board
from player import Player


class MemoryGame(BoxLayout):
    """Gère le déroulement du jeu et les widgets de la fenêtre"""

    board = Board()
    players = [Player(), Player()]
    chosenCards = []
    cardButtons = []
    currPlayer = 0

    def __init__(self, **kwargs):
        super(MemoryGame, self).__init__(**kwargs)
        self.scoreLabel = Label(
            text=f'Nombre de paire: Joueur 1 ({self.players[0].getScore()}) - Joueur 2 ({self.players[1].getScore()})',
            size_hint=(1, None), height=30)
        self.currPlayerLabel = Label(text=f'Tour du joueur {self.currPlayer + 1}', size_hint=(1, None), height=30)
        self.boardWidget = GridLayout(cols=4, rows=4, padding=10, spacing=10)
        for i, card in enumerate(self.board.cards):
            button = Button(text='?', on_press=lambda event, arg=i: self.update(arg))
            self.cardButtons.append(button)
            self.boardWidget.add_widget(button)
        self.add_widget(self.scoreLabel)
        self.add_widget(self.currPlayerLabel)
        self.add_widget(self.boardWidget)

    def update(self, i):
        """Met à jour l'interface lorsqu'une carte est sélectionnée"""
        card = self.board.getCard(i)
        button = self.cardButtons[i]
        button.text = card
        button.background_color = (0, 0, 1, 1)
        self.chosenCards.append((i, card))
        if len(self.chosenCards) == 2:
            if self.chosenCards[0][1] == self.chosenCards[1][1]:
                self.players[self.currPlayer].gainCard(card)
            Clock.schedule_once(self.resetChosenCard, 1)  # attend 1s avant de cacher la carte

        if self.board.isOnBoard(i) and not self.board.isShown(i) and len(self.chosenCards) < 2:
            self.board.showCard(i)
            card = self.board.getCard(i)
            button = self.cardButtons[i]
            button.text = card
            button.background_color = (0, 0, 1, 1)
            self.chosenCards.append((i, card))
            if len(self.chosenCards) == 2:
                if self.chosenCards[0][1] == self.chosenCards[1][1]:
                    self.players[self.currPlayer].gainCard(card)
                Clock.schedule_once(self.resetChosenCard, 1)  # attend 1s avant de cacher la carte

    def resetChosenCard(self, dt):
        """Supprime les cartes sélectionnées et met à jour l'affichage du score"""
        for chosenCard in self.chosenCards:

            self.board.hideCard(chosenCard[0])
            button = self.cardButtons[chosenCard[0]]
            if self.chosenCards[0][1] != self.chosenCards[1][1]:
                button.text = '?'
        if self.chosenCards[0][1] != self.chosenCards[1][1]:
            self.currPlayer ^= 1  # change 0 en 1 et 1 en 0
        self.chosenCards.clear()

        self.scoreLabel.text = f'Nombre de paire: Joueur 1 ({self.players[0].getScore()}) - Joueur 2 ({self.players[1].getScore()})'
        self.currPlayerLabel.text = f'Tour du joueur {self.currPlayer + 1}'
        if self.players[0].getScore() + self.players[1].getScore() < self.board.getPairCount():
            self.currPlayerLabel.text = f'Tour du joueur {self.currPlayer + 1}'
        else:
            self.currPlayerLabel.text = 'Fin de la partie'


class MemoryApp(App):
    def build(self):
        return MemoryGame(orientation='vertical')


if __name__ == '__main__':
    MemoryApp().run()
