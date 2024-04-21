"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""

def find_tuples(lst, k):
    return [t for t in lst if all(x % k == 0 for x in t)]

# Test cases
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6)) # [(6, 24, 12)]<|endoftext|>