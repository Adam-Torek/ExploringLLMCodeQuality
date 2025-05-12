"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""

def intersection_array(arr1, arr2):
    """
    This function takes two arrays as input and returns the intersection of the two arrays.
    """
    # Create a set of elements in arr1
    set1 = set(arr1)
    # Create a set of elements in arr2
    set2 = set(arr2)
    # Find the intersection of the two sets
    intersection = set1.intersection(set2)
    # Convert the intersection set back to a list
    intersection_list = list(intersection)
    return intersection_list

# Test the function with the given example
print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])) # Output: [1, 2, 8, 9]<|endoftext|>