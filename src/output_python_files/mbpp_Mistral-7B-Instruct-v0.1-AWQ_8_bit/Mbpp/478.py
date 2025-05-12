"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""

def remove_lowercase(string):
    """
    This function removes all lowercase substrings from a given string.
    """
    # split the string into a list of words
    words = string.split()
    # iterate over the list of words
    for i in range(len(words)):
        # check if the current word is lowercase
        if words[i].islower():
            # remove the current word from the list of words
            del words[i]
    # join the list of words back into a string
    return ''.join(words)