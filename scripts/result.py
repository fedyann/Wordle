from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Result(QWidget):
    def __init__(self, answer, text, username, password, language, length):
        super().__init__()
        self.answer = answer
        self.text = text
        self.username = username
        self.password = password
        self.language = language
        self.length = length
        if self.text == 'You win!':
            uic.loadUi(Path(__file__).parent.parent /'design/result_win.ui', self)
        else:
            uic.loadUi(Path(__file__).parent.parent /'design/result_lose.ui', self)
        self.word.setText(self.answer.capitalize())
        self.home.clicked.connect(self.go_home)
        self.game.clicked.connect(self.new_game)

    def go_home(self):
        from scripts.home import Home
        self.home = Home(self.username, self.password, self.language, self.length)
        self.home.show()
        self.home.move(600, 20)
        self.close()

    def new_game(self):
        from scripts.game import Game
        self.game = Game(self.username, self.password, self.language, self.length)
        self.game.show()
        self.game.move(600, 20)
        self.close()
