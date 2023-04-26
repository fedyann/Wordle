import random


class Wordle:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.answer = random.choice(self.dictionary)

    def get_answer(self):
        return self.answer

    def guess(self, word):
        if word not in self.dictionary:
            return None
        else:
            return self.colors(word)

    def colors(self, word):
        colors = []
        answer = self.answer
        for i in range(len(word)):
            letter = word[i]
            if letter in answer:
                if word[i] == answer[i]:
                    answer = answer[:i] + ' ' + answer[i + 1:]
                    colors.append('#aaff7f')
                else:
                    if word.count(letter) > 1:
                        if answer.count(letter) > 1:
                            word = word[:i] + ' ' + word[i + 1:]
                            colors.append('#ffff7f')
                        else:
                            word = word[:i] + ' ' + word[i + 1:]
                            colors.append('#9a9cca')
                    else:
                        colors.append('#ffff7f')
            else:
                colors.append('#9a9cca')
        return colors
