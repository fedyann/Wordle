import sqlite3
from pathlib import Path


class Statistic:
    def __init__(self, username, password):
        self.con = sqlite3.connect(Path(__file__).parent.parent /"data_bases/wordle.db")
        self.cur = self.con.cursor()
        self.username = username
        self.password = password
        self.account = self.cur.execute(f"SELECT id from accounts where name = '{self.username}' "
                                        f"and password = '{self.password}'").fetchall()[0][0]

    def add_data(self, language, length, guesses_count, result):
        self.language = language
        self.length = length
        self.guesses_count = guesses_count
        self.result = result
        add = f"INSERT INTO statistic(account_id, language, word_length, guesses_count, is_won)" \
              f"VALUES({self.account}, '{self.language}', {self.length}, {self.guesses_count}, {self.result})"
        self.cur.execute(add).fetchall()
        self.con.commit()
        self.con.close()

    def games_count(self, language, length):
        if language == 'Все' and length == 'Все':
            select = f"SELECT COUNT(*) from statistic where account_id = {self.account}"
        elif language == 'Все':
            select = f"SELECT COUNT(*) from statistic where account_id = {self.account} and word_length = {int(length)}"
        elif length == 'Все':
            select = f"SELECT COUNT(*) from statistic where account_id = {self.account} and language = '{language}'"
        else:
            select = f"SELECT COUNT(*) from statistic where account_id = {self.account}" \
                     f" and language = '{language}' and word_length = {int(length)}"
        result = self.cur.execute(select).fetchall()[0][0]
        if not result:
            result = 0
        return str(result)

    def min_guesses_count(self, language, length):
        if language == 'Все' and length == 'Все':
            select = f"SELECT MIN(guesses_count) from statistic where account_id = {self.account}"
        elif language == 'Все':
            select = f"SELECT MIN(guesses_count) from statistic where account_id = {self.account} " \
                     f"and word_length = {int(length)}"
        elif length == 'Все':
            select = f"SELECT MIN(guesses_count) from statistic where account_id = {self.account} " \
                     f"and language = '{language}'"
        else:
            select = f"SELECT MIN(guesses_count) from statistic where account_id = {self.account}" \
                     f" and word_length = {int(length)} and language = '{language}'"
        result = self.cur.execute(select).fetchall()[0][0]
        if not result:
            result = 0
        return str(result)

    def average_guesses_count(self, language, length):
        if int(self.games_count(language, length)) > 0:
            if language == 'Все' and length == 'Все':
                select = f"SELECT avg(guesses_count) from statistic where account_id = {self.account}"
            elif language == 'Все':
                select = f"SELECT avg(guesses_count) from statistic where account_id = {self.account} " \
                         f"and word_length = {int(length)}"
            elif length == 'Все':
                select = f"SELECT avg(guesses_count) from statistic where account_id = {self.account} " \
                         f"and language = '{language}'"
            else:
                select = f"SELECT avg(guesses_count) from statistic where account_id = {self.account}" \
                         f" and word_length = {int(length)} and language = '{language}'"
            result = int(self.cur.execute(select).fetchall()[0][0])
        else:
            result = 0
        return str(result)

    def get_all_win(self, language, length):
        if language == 'Все' and length == 'Все':
            select = f"SELECT COUNT(*) from statistic where account_id = {self.account} and is_won = True"
        elif language == 'Все':
            select = f"SELECT COUNT(*) from statistic where account_id = {self.account} " \
                     f"and is_won = True and word_length = {int(length)}"
        elif length == 'Все':
            select = f"SELECT COUNT(*) from statistic where account_id = {self.account} " \
                     f"and is_won = True and language = '{language}'"
        else:
            select = f"SELECT COUNT(*) from statistic where account_id = {self.account} and is_won = True" \
                     f" and word_length = {int(length)} and language = '{language}'"
        result = self.cur.execute(select).fetchall()[0][0]
        if not result:
            result = 0
        return str(result)
