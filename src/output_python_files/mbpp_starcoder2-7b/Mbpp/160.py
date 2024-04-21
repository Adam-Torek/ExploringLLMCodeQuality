"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""

def find_solution(a, b, n):
    """
    >>> find_solution(2, 3, 7)
    (2, 1)
    >>> find_solution(2, 3, 11)
    None
    """
    for x in range(n):
        for y in range(n):
            if a * x + b * y == n:
                return (x, y)
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
<file_sep>/week02/day02/03_list_comprehension.py
"""
List comprehension
"""

# List comprehension

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j', 't', 'l', 'd']

# Create a list of the first letters of every word in the following sentence:

sentence = "the quick brown fox jumps over the lazy dog"

# Expected output: ['t', 'q', 'b', 'f', 'j