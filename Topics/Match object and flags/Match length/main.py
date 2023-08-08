import re

string = input()
template = r'are you ready??.?.?'

match_result = re.search(template, string)
if match_result:
    matching_substring = match_result.group(0)
    matching_length = len(matching_substring)
    print(matching_length)
else:
    print(0)