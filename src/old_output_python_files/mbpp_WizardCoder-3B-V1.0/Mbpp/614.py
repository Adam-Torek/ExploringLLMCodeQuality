"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""

def cummulative_sum(lst):
    cum_sum = 0
    for tup in lst:
        cum_sum += sum(tup)
    return cum_sum

# Test case
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30<|endoftext|>