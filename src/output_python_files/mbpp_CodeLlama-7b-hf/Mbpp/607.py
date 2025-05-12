"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""

import re


def find_literals(text, pattern):
    """
    Finds the first occurrence of a pattern in a string.
    :param text: The string to search.
    :param pattern: The pattern to search for.
    :return: The matching substring, a start index and an end index.
    """
    match = re.search(pattern, text)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None, None, None


if __name__ == '__main__':
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'dog'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'brown'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'lazy'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))