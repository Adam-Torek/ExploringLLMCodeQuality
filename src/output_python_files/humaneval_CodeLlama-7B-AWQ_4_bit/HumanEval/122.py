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

    # Initialize variables
    sum_of_elements = 0
    max_digits = 0

    # Iterate through the array
    for i in range(k):
        # Get the number of digits of the current element
        digits = len(str(arr[i]))

        # If the number of digits is greater than the max, update the max
        if digits > max_digits:
            max_digits = digits

        # Add the current element to the sum
        sum_of_elements += arr[i]

    # Return the sum of the elements with at most two digits
    return sum_of_elements if max_digits <= 2 else 0


def test_function(test_case):
    print(
        f"add_elements({test_case[0]}, {test_case[1]}) returned "
        f"{add_elements(test_case[0], test_case[1])}, "
        f"expected {test_case[2]}"
    )


test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 4, 24])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 5, 0])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 6, 0])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 7, 0])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 8, 0])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 9, 0])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 10, 0])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 11, 0])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 12, 0])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 13, 0])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 14, 0])
test_function([[111, 21, 3, 4000, 5, 6