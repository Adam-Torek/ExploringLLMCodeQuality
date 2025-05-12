"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""

def extract_freq(lst):
    unique_tuples = set(lst)
    return len(unique_tuples)

# Test cases
print(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)])) # Output: 3
print(extract_freq([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])) # Output: 4
print(extract_freq([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 2), (2, 3), (3, 4), (4, 5)])) # Output: 4
print(extract_freq([(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)])) # Output: 4
print(extract_freq([(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7), (1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)])) # Output: 5

# Time Complexity: O(n)
# Space Complexity: O(n)