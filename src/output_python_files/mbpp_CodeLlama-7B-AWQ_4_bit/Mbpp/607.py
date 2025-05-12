"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""


def find_literals(string, pattern):
    """
    Finds the first occurrence of a pattern in a string and returns the matching substring, a start index and an end index.
    :param string: The string to search.
    :param pattern: The pattern to search for.
    :return: The matching substring, a start index and an end index.
    """
    start_index = string.find(pattern)
    end_index = start_index + len(pattern)
    return pattern, start_index, end_index


if __name__ == '__main__':
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'dog'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The'))
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
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.'))
    print(find_literals('The quick brown