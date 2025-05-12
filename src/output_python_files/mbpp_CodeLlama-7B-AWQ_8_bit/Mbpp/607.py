"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""


def find_literals(string, pattern):
    """
    Search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
    """
    start = 0
    end = 0
    for i in range(len(string)):
        if string[i] == pattern[0]:
            if string[i:i + len(pattern)] == pattern:
                start = i
                end = i + len(pattern)
                return pattern, start, end
    return None, None, None


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
    print(find_literals('The quick brown fox jumps over the