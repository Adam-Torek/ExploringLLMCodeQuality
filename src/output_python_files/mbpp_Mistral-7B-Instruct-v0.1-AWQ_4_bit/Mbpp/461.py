"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""

def upper_ctr(string):
    count = 0
    for i in string:
        if i.isupper():
            count += 1
    return count

#assert upper_ctr('PYthon') == 1
print(upper_ctr('PYthon'))