"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""

def find_combinations(tuples):
    """
    Find the combinations of sums with tuples in the given tuple list.
    """
    # Create a set of tuples
    set_tuples = set(tuples)

    # Create a set of tuples with their sums
    set_tuples_sums = set()
    for tuple in set_tuples:
        set_tuples_sums.add(tuple[0] + tuple[1])

    # Find the combinations of sums with tuples
    combinations = []
    for sum in set_tuples_sums:
        for tuple in set_tuples:
            if sum == tuple[0] + tuple[1]:
                combinations.append(tuple)

    return combinations