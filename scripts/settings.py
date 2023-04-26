from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Settings(QWidget):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        uic.loadUi(Path(__file__).parent.parent /'design/settings.ui', self)
        self.home.clicked.connect(self.go_home)

    def go_home(self):
        from scripts.home import Home
        self.chosen_language = self.language.currentText()
        self.chosen_length = self.length.currentText()
        if self.chosen_language == 'Русский':
            self.chosen_language = 'rus'
        else:
            self.chosen_language = 'eng'
        self.home = Home(self.username, self.password, self.chosen_language, self.chosen_length)
        self.home.show()
        self.home.move(600, 20)
        self.close()
