import nltk

with open('austen-persuasion.txt', 'r') as f:
    text = f.read()
    morpheme_list = nltk.word_tokenize(text)
    print('length of morpheme list:', len(morpheme_list))
    print('length of unique morpheme list:', len(set(morpheme_list)))
