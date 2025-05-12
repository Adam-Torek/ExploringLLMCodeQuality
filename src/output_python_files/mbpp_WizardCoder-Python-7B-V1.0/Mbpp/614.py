"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""

def cummulative_sum(tup_list):
    result = 0
    for tup in tup_list:
        result += sum(tup)
    return result

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 18
print(cummulative_sum([(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]) # Output: 55