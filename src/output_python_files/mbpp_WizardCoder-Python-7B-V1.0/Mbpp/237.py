"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""

def check_occurences(lst):
    d = {}
    for tup in lst:
        if tup in d:
            d[tup] += 1
        else:
            d[tup] = 1
    return d

# Test the function with the example given in the prompt
print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)])) # Output: {(1, 3): 2, (2, 5): 2, (3, 6): 1}