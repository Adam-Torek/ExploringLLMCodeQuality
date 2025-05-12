"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""

def max_Abs_Diff(arr):
    """
    This function takes an array as input and returns the maximum absolute difference between any two elements in the array.
    """
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

# Test the function
arr = (2,1,5,3)
print(max_Abs_Diff(arr))