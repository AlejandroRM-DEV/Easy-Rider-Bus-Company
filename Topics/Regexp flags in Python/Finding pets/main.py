import re 

string = input()
# your code here
pets = re.findall(r"dog|cat|parrot|hamster", string, flags=re.IGNORECASE)
print(pets)