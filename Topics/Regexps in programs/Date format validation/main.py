import re

string = input()
# your code here
if re.match("[0-3][0-9]/[0-1][1-2]/[1-3][0-9][0-9][0-9]", string):
    print(True)
else:
    print(False)