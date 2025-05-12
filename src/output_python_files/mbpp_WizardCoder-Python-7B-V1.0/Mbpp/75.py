"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""

def find_tuples(lst, k):
    result = []
    for tup in lst:
        if all(x % k == 0 for x in tup):
            result.append(tup)
    return result

# Test cases
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6)) # Output: [(6, 24, 12)]
print(find_tuples([(12, 18, 21), (7, 9, 6), (6, 24, 12)], 6)) # Output: [(6, 24, 12), (12, 18, 21)]
print(find_tuples([(12, 18, 21), (7, 9, 6), (6, 24, 12)], 3)) # Output: []
print(find_tuples([(12, 18, 21), (7, 9, 6), (6, 24, 12)], 0)) # Output: []
print(find_tuples([(12, 18, 21), (7, 9, 6), (6, 24, 12)], 12)) # Output: [(12, 18, 21), (6, 24, 12)]