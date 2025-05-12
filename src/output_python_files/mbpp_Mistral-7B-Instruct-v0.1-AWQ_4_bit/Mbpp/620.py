"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""

def largest_subset(lst):
    """
    Returns the size of the largest subset of a list of numbers so that every pair is divisible.
    """
    if not lst:
        return 0
    else:
        max_size = 1
        for i in range(1,len(lst)):
            for j in range(i):
                if lst[i] % lst[j] == 0:
                    subset = lst[:i+1]
                    if len(subset) > max_size:
                        max_size = len(subset)
        return max_size

# Test the function
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4