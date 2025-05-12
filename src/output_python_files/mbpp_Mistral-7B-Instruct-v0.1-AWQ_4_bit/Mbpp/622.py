"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""

def get_median(list1, list2, size):
    """
    This function takes two sorted lists of same size and returns the median.
    """
    if size % 2 == 0:
        return (list1[size//2] + list2[size//2])/2
    else:
        return list1[size//2]

assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0