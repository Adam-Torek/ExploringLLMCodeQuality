"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""
def search(arr):
    """
    This function finds the element that appears only once in a sorted array.
    :param arr: A sorted list of integers
    :return: The integer that appears only once in the list
    """
    if len(arr) == 1:
        return arr[0]

    slow, fast = 0, len(arr) // 2
    while slow <= fast:
        mid = (slow + fast) // 2
        if mid > 0 and arr[mid] == arr[mid - 1]:
            fast = mid - 1
        elif mid < len(arr) - 1 and arr[mid] == arr[mid + 1]:
            slow = mid + 1
        else:
            return arr[mid]

if __name__ == "__main__":
    import pytest
    @pytest.mark.parametrize("arr, expected", [
        ([1, 1, 2, 2, 3], 3),
        ([1, 1, 2, 3, 3], 2),
        ([1, 1, 2, 3, 4], 4),
        ([1, 1, 2, 3, 4, 4], 3),
        ([1, 1, 2, 3, 4, 4, 5], 5),
        ([1, 1, 2, 3, 4, 4, 5, 5], 3),
        ([], None),
        ([1], 1),
        ([1, 1], None),
        ([1, 1, 1], None),
        ([1, 1, 1, 1], None),
        ([1, 1, 1, 1, 1], None),
        ([1, 1, 1, 1, 1, 1], None),
        ([1, 1, 1, 1, 1, 1, 1], None),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1], None),
    ])
    def test_search(arr, expected):
        assert search(arr) == expected

    test_search([], None)
    test_search([1], 1)
    test_search([1, 1], None)
    test_search([1, 1, 1], None)
    test_search([1, 1, 1, 1], None)
    test_search([1, 1, 1, 1, 1], None)
    test_search([1, 1, 1, 1, 1, 1], None)
    test_search([1, 1, 1, 1, 1, 1, 1], None)
    test_search([1, 1, 1, 1, 1, 1, 1, 1, 1], None)
    test_search([1, 1, 2, 2, 3], 3)
    test_search([1, 1, 2, 3, 3], 2)
    test_search([1, 1, 2, 3, 4], 4)
    test_search([1, 1, 2, 3, 4, 4], 3)
    test_search([1, 1, 2, 3, 4, 4, 5], 5)
    test_search([1, 1, 2, 3, 4, 4, 5, 5], 3)