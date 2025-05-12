"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""


def max_Abs_Diff(arr):
    """
    :param arr: array of integers
    :return: maximum difference between any two elements in the array
    """
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) > max_diff:
                max_diff = abs(arr[i] - arr[j])
    return max_diff


if __name__ == '__main__':
    print(max_Abs_Diff((2, 1, 5, 3)))
    print(max_Abs_Diff((-2, 1, 5, 3)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000, 10000)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000, 10000, 100000)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000, 10000, 100000, 1000000)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000, 10000, 100000, 1000000, 10000000)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000)))
    print(max_Abs_Diff((2, 1, 5, 3, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000