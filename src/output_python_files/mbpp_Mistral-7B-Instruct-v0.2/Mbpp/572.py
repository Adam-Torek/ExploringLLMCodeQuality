"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""
def two_unique_nums(lists):
    # Flatten all lists and convert to set to remove duplicates
    unique_nums = set([num for list in lists for num in list])
    # Convert set back to list
    return list(unique_nums)

# Test case
assert two_unique_nums([[1,2,3,2,3,4,5], [6,7,8,9,1,2,3], [1,1,1,1,1,1,1]]) == [1, 4, 5, 6, 7, 8, 9]</s>