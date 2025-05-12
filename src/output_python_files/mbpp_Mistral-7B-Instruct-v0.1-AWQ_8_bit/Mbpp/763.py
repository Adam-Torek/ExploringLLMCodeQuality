"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""

def find_min_diff(arr, diff):
    """
    :param arr: array
    :param diff: difference
    :return: minimum difference
    """
    n = len(arr)
    min_diff = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            diff_val = abs(arr[i] - arr[j])
            if diff_val < min_diff:
                min_diff = diff_val
    return min_diff


if __name__ == '__main__':
    arr = (1,5,3,19,18,25)
    print(find_min_diff(arr,6))