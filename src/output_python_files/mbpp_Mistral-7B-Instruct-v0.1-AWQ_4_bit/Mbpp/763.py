"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""

def find_min_diff(arr, diff):
    """
    :param arr: array of integers
    :param diff: difference between two elements
    :return: minimum difference between any two elements in the array
    """
    n = len(arr)
    min_diff = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            diff_temp = arr[i] - arr[j]
            if diff_temp < min_diff:
                min_diff = diff_temp
    return min_diff


if __name__ == '__main__':
    arr = (1,5,3,19,18,25)
    print(find_min_diff(arr,6))