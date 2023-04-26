import sqlite3
from pathlib import Path


class Accounts:
    def __init__(self):
        self.con = sqlite3.connect(Path(__file__).parent.parent /"data_bases/wordle.db")
        self.cur = self.con.cursor()

    def account(self, accaunt, password):
        if accaunt and password:
            s = "SELECT * FROM accounts WHERE name = " + f'"{accaunt}" and password = "{password}"'
            res = self.cur.execute(s).fetchall()
            if res:
                return 'Такой аккаунт уже существует'
            else:
                stroke = "INSERT INTO accounts(name, password) VALUES" + f'("{accaunt}", "{password}")'
                self.cur.execute(stroke).fetchall()
                self.con.commit()
                return 'ok'
        else:
            return 'Введите логин и пароль'

    def log_in(self, accaunt, passw):
        if accaunt and passw:
            stroke = "SELECT * FROM accounts WHERE name = " + f'"{accaunt}" and password = "{passw}"'
            result = self.cur.execute(stroke).fetchall()
            if result:
                return 'ok'
            else:
                return 'Неправильный логин или пароль'
        else:
            return 'Введите логин и пароль'
