"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""

def max_difference(lst):
    max_diff = 0
    for i in range(len(lst)-1):
        diff = lst[i][1] - lst[i+1][0]
        if diff > max_diff:
            max_diff = diff
    return max_diff

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7