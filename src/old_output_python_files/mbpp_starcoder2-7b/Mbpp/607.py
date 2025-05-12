"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""

def find_literals(string, pattern):
    """
    >>> find_literals('The quick brown fox jumps over the lazy dog.', 'fox')
    ('fox', 16, 19)
    """
    return re.search(pattern, string).group(), re.search(pattern, string).start(), re.search(pattern, string).end()

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE DOING GREAT!\n"
<file_sep>/week_01/day_02/02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02_02