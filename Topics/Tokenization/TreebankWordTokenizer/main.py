from nltk.tokenize import TreebankWordTokenizer
sentence = input()

tbw = TreebankWordTokenizer()
print(tbw.tokenize(sentence))
