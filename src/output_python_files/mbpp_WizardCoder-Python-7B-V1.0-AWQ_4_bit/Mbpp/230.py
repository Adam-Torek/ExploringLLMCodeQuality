"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
def replace_blank(string, character):
    return string.replace(" ", character)

print(replace_blank("hello people",'@'))

#Alternative solution:
def replace_blank(string, character):
    return string.replace(" ", character)

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([character if char == " " else char for char in string])

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string])

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char for char in string if char != " "] + [character])

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char for i, char in enumerate(string) if i != string.index(" ")] + [character])

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for i, char in enumerate(string)]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#Another alternative solution:
def replace_blank(string, character):
    return "".join([char if char != " " else character for char in string]

print(replace_blank("hello people",'@'))

#An