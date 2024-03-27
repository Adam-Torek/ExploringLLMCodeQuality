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
assert count_char_position("abcdefghijklmnopqrstuvwxyz") == 26
assert count_char_position("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
assert count_char_position("1234567890") == 0
assert count_char_position("") == 0
assert count_char_position("a") == 1
assert count_char_position("z") == 1
assert count_char_position("xz") == 2
assert count_char_position("xzx") == 3
assert count_char_position("xzxz") == 4
assert count_char_position("xzxzx") == 5
assert count_char_position("xzxzxz") == 6
assert count_char_position("xzxzxzx") == 7
assert count_char_position("xzxzxzxx") == 8
assert count_char_position("xzxzxzxxx") == 9
assert count_char_position("xzxzxzxxxx") == 10
assert count_char_position("xzxzxzxxxxx") == 11
assert count_char_position("xzxzxzxxxxxx") == 12
assert count_char_position("xzxzxzxxxxxxx") == 13
assert count_char_position("xzxzxzxxxxxxxx") == 14
assert count_char_position("xzxzxzxxxxxxxxx") == 15
assert count_char_position("xzxzxzxxxxxxxxxx") == 16
assert count_char_position("xzxzxzxxxxxxxxxxx") == 17
assert count_char_position("xzxzxzxxxxxxxxxxxx") == 18
assert count_char_position("xzxzxzxxxxxxxxxxxxx") == 19
assert count_char_position("xzxzxzxxxxxxxxxxxxxx") == 20
assert count_char_position("xzxzxzxxxxxxxxxxxxxxx") == 21
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxx") == 22
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxx") == 23
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxx") == 24
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxxx") == 25
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxxxx") == 26
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxxxxx") == 27
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxxxxxx") == 28
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxxxxxxx") == 29
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxxxxxxxx") == 30
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxxxxxxxxx") == 31
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxxxxxxxxxx") == 32
assert count_char_position("xzxzxzxxxxxxxxxxxxxxxxxxxxxxxxxxx