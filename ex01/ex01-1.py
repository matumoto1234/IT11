from nltk.book import *

print(sorted(set(w.lower() for w in text5)))
print(sorted(w.lower() for w in set(text5)))
