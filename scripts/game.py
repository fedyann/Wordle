import random
from pathlib import Path

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel

from scripts.all_words import ALL_WORDS
from scripts.wordle import Wordle


class Game(QMainWindow):
    def __init__(self, username, password, language='rus', length='5'):
        super().__init__()
        self.username = username
        self.password = password
        self.language = language
        self.length = length
        self.word = ''
        self.words = f'{self.language}_words{self.length}'
        self.wordle = Wordle(ALL_WORDS[self.words])
        self.answer = self.wordle.get_answer()
        self.coordinates = {'eng_4': 200, 'eng_5': 160, 'eng_6': 120,
                            'rus_4': 270, 'rus_5': 230, 'rus_6': 190}
        name = Path(__file__).parent.parent /f'design/game_{self.language}.ui'
        uic.loadUi(name, self)
        self.move(600, 20)
        self.build_labels()

        for i in self.alphabet.buttons():
            i.clicked.connect(self.game)
        self.enter.clicked.connect(self.get_result)
        self.delete_2.clicked.connect(self.delete)
        self.home.clicked.connect(self.go_home)
        self.quastion.clicked.connect(self.help)

    def build_labels(self):
        x = self.coordinates[f'{self.language}_{self.length}']
        y = 120
        self.all_labels = []
        labels = []
        for i in range(6):
            for j in range(int(self.length)):
                self.label = QLabel(self)
                self.label.resize(78, 78)
                self.label.setStyleSheet(
                    'border: 5px solid rgb(52, 52, 52);'
                    'background-color: white;'
                    'border-radius: 10px;'
                    'font: 81 20pt "Montserrat ExtraBold";')
                self.label.setAlignment(Qt.AlignCenter)
                self.label.move(x, y)
                x += 90
                labels.append(self.label)
            x = self.coordinates[f'{self.language}_{self.length}']
            y += 90
            self.all_labels.append(labels)
            labels = []
            self.count_word = 0
            self.count_letter = 0

    def help(self):
        word = random.choice(ALL_WORDS[self.words])
        self.error.setText('Попробуйте ввести слово ' + word)

    def go_home(self):
        from scripts.home import Home
        self.home = Home(self.username, self.password, self.language, self.length)
        self.home.show()
        self.home.move(600, 20)
        self.close()

    def game(self):
        if len(self.word) < int(self.length):
            self.error.setText('')
            self.word += self.sender().text()
            self.all_labels[self.count_word][self.count_letter].setText(self.sender().text())
            if self.count_letter <= int(self.length) - 1:
                self.count_letter += 1

    def get_result(self):
        if self.count_letter == int(self.length):
            colors = self.wordle.guess(self.word.lower())
            if colors:
                self.count_word += 1
                self.count_letter = 0
                buttons_colors = {}
                for label in self.all_labels[self.count_word - 1]:
                    color = colors[self.all_labels[self.count_word - 1].index(label)]
                    label.setStyleSheet(
                        f'background-color: {color}; border: 5px solid rgb(52, 52, 52);'
                        f'border-radius: 10px;font: 81 20pt "Montserrat ExtraBold";')
                    for btn in self.alphabet.buttons():
                        if btn.text() == label.text():
                            if btn.text() in buttons_colors:
                                if color == '#aaff7f':
                                    buttons_colors[btn.text()] = color
                                elif color == '#ffff7f' and buttons_colors[btn.text()] != '#aaff7f':
                                    buttons_colors[btn.text()] = color
                            else:
                                buttons_colors[btn.text()] = color
                for btn in buttons_colors:
                    for b in self.alphabet.buttons():
                        if b.text() == btn:
                            color = buttons_colors[btn]
                            b.setStyleSheet(
                                f'background-color: {color}; border: 4px solid rgb(52, 52, 52); border-radius: 10px;')
                            if color == '#9a9cca':
                                b.setEnabled(False)
            else:
                self.error.setText('В словаре игры нет такого слова')
            self.word = ''
            if colors == ['#aaff7f' for i in range(int(self.length))]:
                self.result('You win!')
            elif self.count_word == 6:
                self.result('You lose!')
        else:
            self.error.setText('Введите слово')

    def result(self, text):
        if text == 'You win!':
            result = True
        else:
            result = False
        from scripts.statistic import Statistic
        Statistic(self.username, self.password).add_data(self.language, self.length, self.count_word, result)
        from scripts.result import Result
        self.result = Result(self.answer, text, self.username, self.password, self.language, self.length)
        self.result.show()
        self.close()

    def delete(self):
        if self.count_letter > 0:
            self.count_letter -= 1
            self.word = self.word[:-1]
            self.error.setText('')
        self.all_labels[self.count_word][self.count_letter].setText('')
