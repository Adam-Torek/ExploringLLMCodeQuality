def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # Edge case
    if k == 0:
        return 0

    # Sort the array
    arr.sort()

    # Initialize the sum
    sum = 0

    # Iterate over the first k elements
    for i in range(k):
        # Get the first two digits of the current element
        first_two_digits = arr[i] // 10
        second_digit = arr[i] % 10

        # Add the sum of the first two digits
        sum += first_two_digits

        # Add the second digit if it is less than 2
        if second_digit < 2:
            sum += second_digit

    return sum


def test_add_elements():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 5) == 33
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 6) == 42
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 7) == 51
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 8) == 60
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 9) == 69
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 10) == 78
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 11) == 87
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 12) == 96
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 13) == 105
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 14) == 114
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 15) == 123
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 16) == 132
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 17) == 141
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 18)