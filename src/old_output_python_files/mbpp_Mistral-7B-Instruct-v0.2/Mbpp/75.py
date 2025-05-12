"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""
def find_tuples(tuples_list, k):
    result = []
    for tuple in tuples_list:
        if all(x % k == 0 for x in tuple):
            result.append(tuple)
    return result

# Test case
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
assert find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 2) == []
assert find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9), (12, 12, 12)], 3) == [(12, 12, 12)]
assert find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9), (12, 12, 12)], 4) == [(4, 5, 6), (12, 12, 12)]
assert find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9), (12, 12, 12)], 5) == [(12, 12, 12)]
assert find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9), (12, 12, 12)], 7) == []
assert find_tuples([], 3) == []
assert find_tuples([], 5) == []
assert find_tuples([], 7) == []
assert find_tuples([], 1) == []
assert find_tuples([], 2) == []
assert find_tuples([], 4) == []
assert find_tuples([], 6) == []
assert find_tuples([], 8) == []
assert find_tuples([], 9) == []
assert find_tuples([], 10) == []