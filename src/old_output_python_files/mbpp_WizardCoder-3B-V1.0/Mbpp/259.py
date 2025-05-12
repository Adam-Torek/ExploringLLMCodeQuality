"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""

def maximize_elements(a, b):
    max_a = max(a[0], a[1])
    max_b = max(b[0], b[1])
    return ((max_a, max_b), (min(a[0], a[1]), min(b[0], b[1])))

# Test cases
print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))))<|endoftext|>