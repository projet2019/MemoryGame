from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from board import Board
from player import Player


class MemoryGame(BoxLayout):
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
        card = self.board.getCard(i)
        button = self.cardButtons[i]
        button.text = card
        self.chosenCards.append((i, card))
        if len(self.chosenCards) == 2:
            if self.chosenCards[0][1] == self.chosenCards[1][1]:
                self.players[self.currPlayer].gainCard(card)
            else:
                button = self.cardButtons[self.chosenCards[0][0]]
                button.text = '?'
                button = self.cardButtons[self.chosenCards[1][0]]
                button.text = '?'
                self.currPlayer ^= 1  # change 0 en 1 et 1 en 0
            self.chosenCards.clear()
        self.scoreLabel.text = f'Nombre de paire: Joueur 1 ({self.players[0].getScore()}) - Joueur 2 ({self.players[1].getScore()})'
        self.currPlayerLabel.text = f'Tour du joueur {self.currPlayer + 1}'


class MemoryApp(App):
    def build(self):
        return MemoryGame(orientation='vertical')


if __name__ == '__main__':
    MemoryApp().run()
