import re

string = input()
# your code here
expenses = re.findall(r"(?<=\$)\d+", string)
total = 0
for e in expenses:
    total += int(e)

print(f"This week you have spent: {total} dollars")
