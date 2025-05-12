"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""
def count_char_position(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for char in string:
        if char in alphabet:
            index = alphabet.index(char)
            count += 1
    return count

assert count_char_position("xbcefg") == 2