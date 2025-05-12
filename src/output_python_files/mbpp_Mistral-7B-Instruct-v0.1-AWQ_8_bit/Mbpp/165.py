"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""

def count_char_position(string):
    """
    Count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i in range(len(string)):
        if string[i] == alphabet[i]:
            count += 1
    return count

# Test the function
assert count_char_position("xbcefg") == 2