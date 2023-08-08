import re


string = input()
words = re.findall(r"s\w+", string)
print(words)