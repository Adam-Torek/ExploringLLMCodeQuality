"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""
def first_non_repeating_character(string):
    """
    :param string: string
    :return: first non-repeated character or None
    """
    if len(string) == 0:
        return None

    # create a dictionary to store the count of each character
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # find the first character with count 1
    for char in string:
        if char_count[char] == 1:
            return char

    # if no character is found with count 1, return None
    return None</s>