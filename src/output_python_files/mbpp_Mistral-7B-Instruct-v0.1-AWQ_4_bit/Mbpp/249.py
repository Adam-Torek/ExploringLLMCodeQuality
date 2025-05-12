"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""

def intersection_array(arr1, arr2):
    intersection = []
    for i in arr1:
        if i in arr2:
            intersection.append(i)
    return intersection


# Test the function
arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr2 = [1, 2, 4, 8, 9]

assert intersection_array(arr1, arr2) == [1, 2, 8, 9]