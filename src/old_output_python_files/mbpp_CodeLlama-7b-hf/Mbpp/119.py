"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""


def search(arr):
    """
    :param arr: sorted array
    :return: element that appears only once
    """
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] != arr[1] else None
    else:
        mid = len(arr) // 2
        if arr[mid] == arr[mid - 1]:
            return search(arr[:mid])
        elif arr[mid] == arr[mid + 1]:
            return search(arr[mid + 1:])
        else:
            return arr[mid]


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
    print(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,