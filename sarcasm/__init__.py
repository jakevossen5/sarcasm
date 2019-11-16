#!/usr/local/bin/python3
import string
import random
str = input('Input your string: ')
str = str.lower()
result = ""
weighted_array = [True, False]
for c in str:
    if c in string.ascii_letters:
        if random.choice(weighted_array):
            result += c
            weighted_array.append(False)
            weighted_array.remove(True)
        else:
            result += c.upper()
            weighted_array.append(True)
            weighted_array.remove(False)

    else:
        result += c
print(result)
