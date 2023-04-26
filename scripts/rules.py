from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class Rules(QMainWindow):
    def __init__(self, username, password, language='rus', length='5'):
        super().__init__()
        self.language = language
        self.length = length
        self.username = username
        self.password = password
        uic.loadUi(Path(__file__).parent.parent /'design/rules.ui', self)
        self.home.clicked.connect(self.go_home)

    def go_home(self):
        from scripts.home import Home
        self.home = Home(self.username, self.password, self.language, self.length)
        self.home.show()
        self.home.move(600, 20)
        self.close()