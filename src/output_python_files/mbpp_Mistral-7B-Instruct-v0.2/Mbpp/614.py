"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""
def cummulative_sum(tuples):
    total = 0
    for i in tuples:
        if isinstance(i, tuple):
            total += sum(i)
        else:
            total += i
    return total

assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
assert cummulative_sum([1, 2, 3, 4, 5]) == 15
assert cummulative_sum([1, 2, 3]) == 6
assert cummulative_sum([1, 2]) == 3
assert cummulative_sum([1]) == 1
assert cummulative_sum([]) == 0