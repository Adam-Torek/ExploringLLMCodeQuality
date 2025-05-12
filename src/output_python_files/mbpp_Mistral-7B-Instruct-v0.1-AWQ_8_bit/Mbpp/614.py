"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""

def cummulative_sum(lst):
    """
    This function takes a list of tuples as an argument and returns the cumulative sum of all the values present in the list.
    """
    sum = 0
    for i in lst:
        sum += sum(i)
    return sum

assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30