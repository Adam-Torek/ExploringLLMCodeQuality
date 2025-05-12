"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""


def is_majority(arr, n, element):
    """
    :param arr: sorted array
    :param n: length of array
    :param element: element to check
    :return: True if element is majority element, False otherwise
    """
    # Write your code here.
    if n == 0:
        return False
    if arr[0] == element:
        return True
    if arr[n - 1] == element:
        return True
    if arr[n // 2] == element:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 10) == True
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 1) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 2) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 4) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 5) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 6) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 7) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 8) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 9) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 10) == True
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 11) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 12) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 13) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 14) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 15) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 16) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 17) == False
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 18) == False
    assert is_majority([