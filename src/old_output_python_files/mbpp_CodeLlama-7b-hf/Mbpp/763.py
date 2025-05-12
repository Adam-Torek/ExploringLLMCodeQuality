"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""


def find_min_diff(arr, n):
    """
    :param arr: array of integers
    :param n: length of array
    :return: minimum difference between any two elements in the array
    """
    arr.sort()
    min_diff = float('inf')
    for i in range(n-1):
        min_diff = min(min_diff, arr[i+1]-arr[i])
    return min_diff


if __name__ == '__main__':
    print(find_min_diff((1, 5, 3, 19, 18, 25), 6))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 7))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 8))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 9))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 10))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 11))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 12))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 13))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 14))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 15))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 16))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 17))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 18))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 19))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 20))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 21))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 22))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 23))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 24))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 25))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 26))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 27))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 28))
    print(find_min_diff((1, 5, 3, 19, 18, 25), 29))
    print(find_min_diff((1, 5, 3,