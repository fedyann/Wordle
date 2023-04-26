from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from scripts.statistic import Statistic


class Profile(QMainWindow):
    def __init__(self, username, password, language='rus', length=5):
        super().__init__()
        self.username = username
        self.password = password
        self.language_text = language
        self.length_text = length
        uic.loadUi(Path(__file__).parent.parent /'design/account.ui', self)
        self.name.setText(f'Привет, {self.username}!')
        self.statistic = Statistic(self.username, self.password)

        self.done.clicked.connect(self.set_data)
        self.home.clicked.connect(self.go_home)

    def set_data(self):
        self.chosen_language = self.language.currentText()
        self.chosen_length = self.length.currentText()
        if self.chosen_language == 'Английский':
            self.chosen_language = 'eng'
        elif self.chosen_language == 'Русский':
            self.chosen_language = 'rus'
        self.all_games.setText(self.statistic.games_count(self.chosen_language, self.chosen_length))
        self.all_wins.setText(self.statistic.get_all_win(self.chosen_language, self.chosen_length))
        self.min_guesses.setText(self.statistic.min_guesses_count(self.chosen_language, self.chosen_length))
        self.average_guesses.setText(self.statistic.average_guesses_count(self.chosen_language, self.chosen_length))

    def go_home(self):
        self.statistic.con.close()
        from scripts.home import Home
        self.home = Home(self.username, self.password, self.language_text, self.length_text)
        self.home.show()
        self.home.move(600, 20)
        self.close()

