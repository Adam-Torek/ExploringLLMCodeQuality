"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""

def get_median(list1, list2, size):
    """
    This function takes two sorted lists of same size and returns the median of the two lists.
    """
    # Merge the two lists
    merged_list = list1 + list2

    # Sort the merged list
    sorted_list = sorted(merged_list)

    # Find the median
    if size % 2 == 0:
        median = (sorted_list[size//2 - 1] + sorted_list[size//2]) / 2
    else:
        median = sorted_list[size//2]

    return median

# Test the function
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0<|endoftext|>