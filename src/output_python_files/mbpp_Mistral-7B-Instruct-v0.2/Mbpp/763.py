"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""

def find_min_diff(arr, diff):
    """
    Find the minimum difference between any two elements in a given array
    :param arr: list of integers
    :param diff: difference between two elements
    :return: boolean value indicating if such pair exists
    """
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] > diff:
            right -= 1
        elif arr[left] + arr[right] < diff:
            left += 1
        else:
            return True
    return False

if __name__ == "__main__":
    assert find_min_diff((1,5,3,19,18,25), 6) == True
    assert find_min_diff((1,5,3,19,18,25), 10) == False
    assert find_min_diff((1,5,3,19,18,25), 1) == True
    assert find_min_diff((1,5,3,19,18,25), 26) == False