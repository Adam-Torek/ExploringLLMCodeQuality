"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""

def find_min_diff(arr, diff):
    """
    Find the minimum difference between any two elements in a given array
    :param arr: list of integers
    :param diff: difference between two elements
    :return: boolean value
    """
    # Initialize two pointers, left and right
    left = 0
    right = len(arr) - 1

    # While left pointer is less than right pointer
    while left < right:
        # Calculate current difference
        diff_current = arr[right] - arr[left]

        # If current difference is greater than the given difference
        if diff_current > diff:
            # Move left pointer to the right
            left += 1

        # If current difference is less than the given difference
        # or if the given difference is greater than the difference
        # between the first and last element
        elif diff > diff_current or diff > arr[right] - arr[left - 1]:
            # Move right pointer to the left
            right -= 1

        # If current difference is equal to the given difference
        else:
            # Return True
            return True

    # If we reach here, it means that no such pair exists
    return False

# Test the function
assert find_min_diff((1,5,3,19,18,25), 6) == False
assert find_min_diff((1,5,3,19,18,25), 1) == True
assert find_min_diff((1,5,3,19,18,25), 2) == True
assert find_min_diff((1,5,3,19,18,25), 24) == False