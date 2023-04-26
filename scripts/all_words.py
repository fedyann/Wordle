import csv
from pathlib import Path

import nltk

nltk.download('averaged_perceptron_tagger')
with open(Path(__file__).parent.parent /'data_bases/eng_words.csv', encoding="utf8") as csvfile:
    reader = list(csv.reader(csvfile, delimiter=','))
    words4 = [i[0] for i in reader if len(i[0]) == 4]
    words4 = nltk.pos_tag(words4)
    words4 = [w for w, n in words4 if n == 'NN']
    ENG_WORDS_4 = words4[:10000]

with open(Path(__file__).parent.parent /'data_bases/eng_words.csv', encoding="utf8") as csvfile:
    reader = list(csv.reader(csvfile, delimiter=','))
    words5 = [i[0] for i in reader if len(i[0]) == 5]
    words5 = nltk.pos_tag(words5)
    words5 = [w for w, n in words5 if n == 'NN']
    ENG_WORDS_5 = words5[:10000]

with open(Path(__file__).parent.parent /'data_bases/eng_words.csv', encoding="utf8") as csvfile:
    reader = list(csv.reader(csvfile, delimiter=','))
    words6 = [i[0] for i in reader if len(i[0]) == 6]
    words6 = nltk.pos_tag(words6)
    words6 = [w for w, n in words6 if n == 'NN']
    ENG_WORDS_6 = words6[:10000]

with open(Path(__file__).parent.parent /'data_bases/rus_words.txt', mode='r') as file:
    reader = file.readlines()
    words4 = [i.split()[2] for i in reader if len(i.split()[2]) == 4 and i.split()[3] == 'noun']
    RUS_WORDS_4 = words4[:10000]

with open(Path(__file__).parent.parent /'data_bases/rus_words.txt', mode='r') as file:
    reader = file.readlines()
    words5 = [i.split()[2] for i in reader if len(i.split()[2]) == 5 and i.split()[3] == 'noun']
    RUS_WORDS_5 = words5[:10000]

with open(Path(__file__).parent.parent /'data_bases/rus_words.txt', mode='r') as file:
    reader = file.readlines()
    words6 = [i.split()[2] for i in reader if len(i.split()[2]) == 6 and i.split()[3] == 'noun']
    RUS_WORDS_6 = words6[:10000]

ALL_WORDS = {"rus_words4": RUS_WORDS_4, "rus_words5": RUS_WORDS_5, "rus_words6": RUS_WORDS_6,
             "eng_words4": ENG_WORDS_4, "eng_words5": ENG_WORDS_5, "eng_words6": ENG_WORDS_6}
