"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
def first_repeated_char(string):
    """
    This function takes a string as an input and returns the first repeated character in it.
    """
    # Creating an empty dictionary to store the characters and their count
    char_count = {}

    # Iterating over each character in the string
    for char in string:
        # If the character is already present in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_count[char] = 1

    # Iterating over the dictionary to find the first character with a count greater than 1
    for k, v in char_count.items():
        if v > 1:
            return k

    # If no repeated character is found, return None
    return None