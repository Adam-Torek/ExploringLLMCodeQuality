"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""


def search(arr):
    """
    :param arr: sorted array
    :return: element that appears only once
    """
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0] != arr[1] else None
    if arr[0] != arr[1]:
        return arr[0]
    for i in range(2, len(arr)):
        if arr[i] != arr[i - 1]:
            return arr[i]
    return None


if __name__ == '__main__':
    print(search([1, 1, 2, 2, 3]))
    print(search([1, 1, 2, 2, 3, 3]))
    print(search([1, 1, 2, 2, 3, 3, 4]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11]))
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6,