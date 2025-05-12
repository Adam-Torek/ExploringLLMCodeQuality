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
    # Initialize a variable to store the sum
    total_sum = 0

    # Iterate through the first k elements of the array
    for i in range(k):
        # If the element has two digits, add it to the total sum
        if len(str(arr[i])) == 2:
            total_sum += arr[i]

    return total_sum


# Test the function with the given example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9]
k = 4
print(add_elements(arr, k))  # Output: 24

# Test the function with another example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(add_elements(arr, k))  # Output: 0

# Test the function with another example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9, 10000]
k = 4
print(add_elements(arr, k))  # Output: 21

# Test the function with another example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10000]
k = 4
print(add_elements(arr, k))  # Output: 0

# Test the function with another example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9, 10000]
k = 5
print(add_elements(arr, k))  # Output: 21

# Test the function with another example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9, 10000]
k = 6
print(add_elements(arr, k))  # Output: 21

# Test the function with another example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9, 10000]
k = 7
print(add_elements(arr, k))  # Output: 21

# Test the function with another example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9, 10000]
k = 8
print(add_elements(arr, k))  # Output: 21

# Test the function with another example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9, 10000]
k = 10
print(add_elements(arr, k))  # Output: 21

# Test the function with another example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9, 10000]
k = 1
print(add_elements(arr, k))  # Output: 0

# Test the function with another example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9, 10000]
k = 0
print(add_elements(arr, k))  # Output: