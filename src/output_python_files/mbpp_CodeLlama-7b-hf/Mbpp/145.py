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
    print(max_Abs_Diff((1, 2, 3, 4, 5)))
    print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
    print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)))
    print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)))
    print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)))
    print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3