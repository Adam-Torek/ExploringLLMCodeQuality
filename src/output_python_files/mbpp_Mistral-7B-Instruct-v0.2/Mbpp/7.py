"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
def find_char_long(string):
    """
    :param string: string to find words in
    :return: set of words which are at least 4 characters long
    """
    words = string.split()
    result = set(word for word in words if len(word) >= 4)
    return result