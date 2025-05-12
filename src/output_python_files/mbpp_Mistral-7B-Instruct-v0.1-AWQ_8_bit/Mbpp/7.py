"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""

def find_char_long(string):
    """
    Find all words which are at least 4 characters long in a string.
    """
    # split the string into a list of words
    words = string.split()
    # create an empty set to store the words
    result = set()
    # iterate over the words
    for word in words:
        # check if the word is at least 4 characters long
        if len(word) >= 4:
            # add the word to the set
            result.add(word)
    # return the set of words
    return result