"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
def first_repeated_char(string):
    """
    :param string: string to find the first repeated character
    :return: the first character that is repeated in the string
    """
    # Create a dictionary to store the count of each character in the string
    char_count = {}
    for char in string:
        # If the character is already in the dictionary, return it
        if char in char_count:
            return char
        # Otherwise, add it to the dictionary with a count of 1
        char_count[char] = 1
    # If no character is repeated, return None
    return None