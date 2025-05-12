"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""


def replace_blank(string, character):
    return string.replace(" ", character)


print(replace_blank("hello people", '@'))