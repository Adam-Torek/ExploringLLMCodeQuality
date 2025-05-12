"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""

def extract_freq(lst):
    freq = {}
    for tup in lst:
        if tup in freq:
            freq[tup] += 1
        else:
            freq[tup] = 1
    return len(freq)

# Test cases
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3<|endoftext|>