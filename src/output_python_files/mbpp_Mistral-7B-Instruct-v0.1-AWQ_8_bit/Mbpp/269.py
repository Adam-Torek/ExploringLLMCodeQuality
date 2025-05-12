"""
Write a function to find the ascii value of a character.
assert ascii_value('A')==65
"""

def ascii_value(character: str) -> int:
    """
    This function takes a character as an input and returns its ASCII value.
    """
    return ord(character)