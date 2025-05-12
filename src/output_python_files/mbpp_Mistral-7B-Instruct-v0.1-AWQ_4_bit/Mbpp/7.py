"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""

def find_char_long(string):
    """
    Find all words which are at least 4 characters long in a string.
    """
    words = string.split()
    result = []
    for word in words:
        if len(word) >= 4:
            result.append(word)
    return result


if __name__ == '__main__':
    assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])