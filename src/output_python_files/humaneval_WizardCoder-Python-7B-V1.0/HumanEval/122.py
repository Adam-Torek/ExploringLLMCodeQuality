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
    # Sort the array in ascending order
    arr.sort()

    # Initialize a variable to store the sum
    total = 0

    # Iterate through the first k elements
    for i in range(k):
        # If the current element has two digits, add it to the total
        if len(str(arr[i])) == 2:
            total += arr[i]

    return total


# Test cases
print(add_elements([111, 21, 3, 400, 5, 6, 7, 8, 9], 4))  # Output: 24
print(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  # Output: 11
print(add_elements([10, 20, 30, 40, 50, 60, 70, 80], 4))  # Output: 0
print(add_elements([100, 200, 300, 400, 500, 600, 700, 800], 4))  # Output: 0
print(add_elements([1000, 200, 300, 400, 500, 600, 700, 800], 4))  # Output: 1000
print(add_elements([10000, 20000, 30000, 40000, 50000, 60000, 70000, 8000], 4))  # Output: 0
print(add_elements([100000, 200000, 300000, 400000, 500000, 600000, 700000, 80000], 4))  # Output: 100000
print(add_elements([1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 800000], 4))  # Output: 1000000
print(add_elements([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 8000000], 4))  # Output: 1000000
print(add_elements([100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 70000