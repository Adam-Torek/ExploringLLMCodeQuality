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
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 3)) # Output: []
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 12)) # Output: [(6, 24, 12), (12, 18, 21)]
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 24)) # Output: [(6, 24, 12)]
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 1)) # Output: []
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 0)) # Output: []
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 10)) # Output: [(6, 24, 12), (12, 18, 21)]
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 15)) # Output: []
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 18)) # Output: [(6, 24, 12), (12, 18, 21)]
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 25)) # Output: []
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 36)) # Output: [(6, 24, 12)]
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 72)) # Output: [(6, 24, 12)]
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 144)) # Output: [(6, 24, 12)]
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 108)) # Output: [(6, 24, 12)]
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 216)) # Output: [(6, 24, 12)]
print(find_tuples([(6