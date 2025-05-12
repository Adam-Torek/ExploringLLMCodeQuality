"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""
def first_non_repeating_character(string):
    """
    :param string: string to find the first non-repeated character
    :return: first non-repeated character or None if all characters are repeated
    """
    if len(string) == 0:
        return None

    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string:
        if char_count[char] == 1:
            return char

    return None