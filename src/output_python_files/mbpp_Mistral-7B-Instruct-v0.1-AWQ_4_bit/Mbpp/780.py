"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""

def find_combinations(tuples):
    """
    :type tuples: List[Tuple[int, int]]
    :rtype: List[Tuple[int, int]]
    """
    result = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            result.append(tuple(sorted(sum(tuples[i:j]) + tuples[j])))
    return result