"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""

def first_non_repeating_character(string):
    """
    :param string: string
    :return: first non-repeated character
    """
    # create a dictionary to store the frequency of each character
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # iterate over the string
    for char in string:
        # if the frequency of the character is 1, return it
        if char_freq[char] == 1:
            return char

    # if no non-repeated character is found, return None
    return None