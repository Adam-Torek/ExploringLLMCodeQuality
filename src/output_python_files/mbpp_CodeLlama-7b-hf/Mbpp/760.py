"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""


def unique_Element(arr):
    if len(arr) == 1:
        return True
    else:
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    return False
        return True


if __name__ == '__main__':
    print(unique_Element([1, 1, 1]))
    print(unique_Element([1, 1, 2]))
    print(unique_Element([1, 2, 3]))
    print(unique_Element([1, 2, 3, 4]))
    print(unique_Element([1, 2, 3, 4, 5]))
    print(unique_Element([1, 2, 3, 4, 5, 6]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(unique_Element([1, 2, 3,