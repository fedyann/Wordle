from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from scripts.game import Game
from scripts.profile import Profile
from scripts.rules import Rules
from scripts.settings import Settings


class Home(QMainWindow):
    def __init__(self, username, password, language='rus', length='5'):
        super().__init__()
        self.language = language
        self.length = length
        self.username = username
        self.password = password
        uic.loadUi(Path(__file__).parent.parent /'design/home.ui', self)
        self.game.clicked.connect(self.new_game)
        self.settings.clicked.connect(self.to_settings)
        self.account.clicked.connect(self.to_profile)
        self.help.clicked.connect(self.to_rules)

    def new_game(self):
        self.game = Game(self.username, self.password, self.language, self.length)
        self.game.show()
        self.game.move(600, 20)
        self.close()

    def to_settings(self):
        self.setting = Settings(self.username, self.password)
        self.setting.show()
        self.close()

    def to_profile(self):
        self.profile = Profile(self.username, self.password, self.language, self.length)
        self.profile.show()
        self.close()

    def to_rules(self):
        self.rules = Rules(self.username, self.password, self.language, self.length)
        self.rules.show()
        self.rules.move(600, 20)
        self.close()

