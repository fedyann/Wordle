from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from scripts.accounts import Accounts
from scripts.home import Home


class Welcome(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(Path(__file__).parent.parent /'design/welcome.ui', self)
        self.accounts = Accounts()
        self.new_acc.clicked.connect(self.new_account)
        self.log.clicked.connect(self.log_in)

    def new_account(self):
        if self.accounts.account(self.login.text(), self.password.text()) == 'ok':
            self.go_home()
        else:
            self.error.setText(self.accounts.account(self.login.text(), self.password.text()))

    def log_in(self):
        if self.accounts.log_in(self.login.text(), self.password.text()) == 'ok':
            self.go_home()
        else:
            self.error.setText(self.accounts.log_in(self.login.text(), self.password.text()))

    def go_home(self):
        self.accounts.con.close()
        self.home = Home(self.login.text(), self.password.text())
        self.home.show()
        self.home.move(600, 20)
        self.close()
