"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""


def check_Consecutive(arr):
    if len(arr) < 2:
        return False
    for i in range(len(arr) - 1):
        if arr[i] + 1 != arr[i + 1]:
            return False
    return True


if __name__ == '__main__':
    print(check_Consecutive([1, 2, 3, 4, 5]))
    print(check_Consecutive([1, 2, 3, 5, 6]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17