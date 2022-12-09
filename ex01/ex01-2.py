from nltk.book import *

four_letter_words = []

for w in text5:
    if len(w) == 4:
        four_letter_words.append(w)

FreqDist(four_letter_words).plot(len(four_letter_words))
