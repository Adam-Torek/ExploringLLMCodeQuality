"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""

def count_bidirectional(tuples):
    count = 0
    seen = set()
    for t in tuples:
        if (t[1], t[0]) in seen:
            count += 1
        else:
            seen.add(t)
    return count

# Test cases
print(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)])) # Output: 3
print(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 1), (5, 6), (6, 5)])) # Output: 2
print(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 1)])) # Output: 3
print(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 1)])) # Output: 4
print(count_bidirectional([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1)])) # Output: 5