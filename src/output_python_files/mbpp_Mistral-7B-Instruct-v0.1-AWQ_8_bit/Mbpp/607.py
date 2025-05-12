"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""

import re

def find_literals(text, pattern):
    """
    Find a regex pattern in a string and return the matching substring, start and end index.
    """
    match = re.search(pattern, text)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None, None, None


if __name__ == '__main__':
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'dog') == ('dog', 25, 29)
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'cat') == None