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
    if len(arr) == 0:
        return 0

    # Initialize
    sum_of_elements = 0

    # Iterate through the array
    for i in range(k):
        # If the element is less than 10, add it to the sum
        if arr[i] < 10:
            sum_of_elements += arr[i]
        # If the element is greater than 10, add the first digit to the sum
        else:
            sum_of_elements += arr[i] // 10

    return sum_of_elements


def test_function(test_case):
    arr = test_case[0]
    k = test_case[1]
    solution = test_case[2]
    output = add_elements(arr, k)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 4, 24])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 5, 36])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 6, 45])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 7, 54])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 8, 63])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 9, 72])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 10, 81])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 11, 90])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 12, 99])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 13, 108])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 14, 117])
test_function([[111, 21, 3, 4000, 5, 6, 7, 8, 9], 15, 126])
test_function([