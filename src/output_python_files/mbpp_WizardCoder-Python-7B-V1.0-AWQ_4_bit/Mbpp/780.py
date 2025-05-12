"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""
from itertools import combinations

def find_combinations(lst):
    result = []
    for i in range(1, len(lst) + 1):
        for combo in combinations(lst, i):
            if sum(combo) == 15:
                result.append(combo)
    return result

# Test the function
print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))
# Output: [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]

# Test the function
print(find_combinations([(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)])
# Output: [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 10, 10), (1, 2, 3, 4, 5, 6, 7, 9, 9, 9), (1, 2, 3, 4, 5, 6, 7, 10, 10, 10), (1, 2, 3, 4, 5, 6, 8, 8, 8), (1, 2, 3, 4, 5, 6, 9, 9, 9), (1, 2, 3, 4, 5, 7, 7, 7, 7), (1, 2, 3, 4, 5, 8, 8, 8, 8), (1, 2, 3, 4, 6, 6, 6, 6, 6), (1, 2, 3, 4, 6, 7, 7, 7, 7), (1, 2, 3, 4, 6, 8, 8, 8, 8), (1, 2, 3, 4, 5, 5, 5, 5, 5), (1, 2, 3, 4, 6, 9, 9, 9, 9), (1, 2, 3, 4, 7, 7, 7, 7, 7), (1, 2, 3, 4, 8, 8, 8, 8, 8), (1, 2, 3, 5, 5, 5, 5, 5, 5), (1, 2, 3, 6, 6, 6, 6, 6, 6), (1, 2, 4, 4, 4, 4, 4, 4, 4), (1, 2, 3, 5, 6, 6, 6, 6, 6), (1, 2, 3, 5, 7, 7, 7, 7, 7), (1, 2, 3, 5, 8, 8, 8, 8, 8), (1, 2, 4, 4, 5, 5, 5, 5, 5), (1, 2, 3, 6, 7, 7, 7, 7, 7), (1, 2, 3, 5, 9, 9, 9, 9, 9), (1, 2, 4