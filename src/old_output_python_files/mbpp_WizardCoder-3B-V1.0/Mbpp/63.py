"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""

def max_difference(lst):
    lst.sort()
    max_diff = 0
    for i in range(len(lst)-1):
        diff = lst[i+1] - lst[i]
        if diff > max_diff:
            max_diff = diff
    return max_diff

# Test cases
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(1, 2), (3, 4), (5, 6), (7, 8)]) == 8
assert max_difference([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]) == 10<|endoftext|>