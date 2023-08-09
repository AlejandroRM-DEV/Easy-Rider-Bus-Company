import nltk
from nltk import word_tokenize

sentence = str(input())  # input sentence
tokenized = word_tokenize(sentence)
pos = nltk.pos_tag(tokenized)
verbs_nouns = [w[0] for w in pos if w[1] in ["VB","VBG","VBD","VBN","VBP","VBZ"]]
print(verbs_nouns)
