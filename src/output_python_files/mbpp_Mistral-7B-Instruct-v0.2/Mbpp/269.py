"""
Write a function to find the ascii value of a character.
assert ascii_value('A')==65
"""
def ascii_value(char):
    """
    :param char: a single character
    :return: the ascii value of the character
    """
    return ord(char)

if __name__ == "__main__":
    assert ascii_value('A') == 65
    assert ascii_value('a') == 97
    assert ascii_value('0') == 48
    assert ascii_value('!') == 33
    assert ascii_value(' ') == 32
    assert ascii_value('_') == 95
    print("All tests passed.")</s>