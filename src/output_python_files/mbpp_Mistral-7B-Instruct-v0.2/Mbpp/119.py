"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""
def search(arr):
    """
    :param arr: sorted array
    :return: the element that appears only once in the array
    """
    if len(arr) == 1:
        return arr[0]

    start, end = 0, len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] != arr[mid + 1]:
            return arr[mid]

        if arr[mid] == arr[mid + 1]:
            if arr[mid] == arr[start]:
                start += 1
            else:
                end = mid

    return arr[start]

if __name__ == "__main__":
    import pytest

    @pytest.mark.parametrize(
        "arr, expected",
        [
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
        ],
    )
    def test_search(arr, expected):
        assert search(arr) == expected

    test_search([], None)
    test_search([1], 1)
    test_search([1, 1], None)
    test_search([1, 1, 1], None)
    test_search([1, 1, 1, 1], None)
    test_search([1, 1, 2, 2, 3], 3)
    test_search([1, 1, 2, 3, 3], 2)
    test_search([1, 1, 2, 3, 4], 4)
    test_search([1, 1, 2, 3, 4, 4], 3)
    test_search([1, 1, 2, 3, 4, 4, 5], 5)
    test_search([1, 1, 2, 3, 4, 4, 5, 5], 3)