"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""


def remove_Occ(string, char):
    return string[1:-1].replace(char, "")


print(remove_Occ("hello", "l"))