import re

string = input()
# Write your code here
letters = ('A', 'C', 'G', 'T')
for letter in letters:
    total = len(re.findall(letter, string))
    if total > 0:
        print(f"{letter}: {total}")
