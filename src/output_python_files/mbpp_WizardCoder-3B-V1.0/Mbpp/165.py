"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""

def count_char_position(s):
    count = 0
    for i in range(26):
        count += s.lower().count(chr(i+97))
    return count

# Test cases
assert count_char_position("xbcefg") == 2<|endoftext|>