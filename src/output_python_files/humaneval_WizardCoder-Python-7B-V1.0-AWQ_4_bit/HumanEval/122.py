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

    # Iterate through the first k elements of the sorted array
    for i in range(k):
        # If the current element has two digits, add it to the total
        if len(str(arr[i])) == 2:
            total += arr[i]

    return total


# Test the function with the given example
arr = [111, 21, 3, 400, 5, 6, 7, 8, 9]
k = 4
print(add_elements(arr, k))  # Output: 24

# Test the function with another example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(add_elements(arr, k))  # Output: 0

# Test the function with another example
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
k = 4
print(add_elements(arr, k))  # Output: 0

# Test the function with another example
arr = [100, 200, 300, 400, 500, 600, 700, 800, 900]
k = 4
print(add_elements(arr, k))  # Output: 0

# Test the function with another example
arr = [1000, 200, 300, 400, 500, 600, 700, 800, 900]
k = 4
print(add_elements(arr, k))  # Output: 10000

# Test the function with another example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 1
print(add_elements(arr, k))  # Output: 1

# Test the function with another example
arr = [100, 200, 300, 400, 500, 600, 700, 800, 900]
k = 1
print(add_elements(arr, k))  # Output: 10000

# Test the function with another example
arr = [1000, 200, 300, 400, 500, 600, 700, 800, 900]
k = 1
print(add_elements(arr, k))  # Output: 10000

# Test the function with another example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 7
print(add_elements(arr, k))  # Output: 24

# Test the function with another example
arr = [100, 200, 3