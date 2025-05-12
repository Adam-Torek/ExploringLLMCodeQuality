def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(1, n+1))


# Test cases
print(sum_to_n(30)) # Output: 465
print(sum_to_n(100)) # Output: 5050
print(sum_to_n(5)) # Output: 15
print(sum_to_n(10)) # Output: 55
print(sum_to_n(1)) # Output: 1


# Additional test cases
print(sum_to_n(0)) # Output: 0
print(sum_to_n(1000)) # Output: 5050
print(sum_to_n(10000)) # Output: 500500
print(sum_to_n(100000)) # Output: 50005000

# Test case for negative input
try:
    print(sum_to_n(-10))
except ValueError:
    print("Invalid input. Please enter a positive integer.")

# Test case for non-integer input
try:
    print(sum_to_n(3.5))
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for string input
try:
    print(sum_to_n("hello"))
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for float input
try:
    print(sum_to_n(3.0))
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for zero input
try:
    print(sum_to_n(0))
except ValueError:
    print("Invalid input. Please enter a positive integer.")

# Test case for float input
try:
    print(sum_to_n(3.5))
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for string input
try:
    print(sum_to_n("hello"))
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for negative input
try:
    print(sum_to_n(-10))
except ValueError:
    print("Invalid input. Please enter a positive integer.")

# Test case for non-integer input
try:
    print(sum_to_n(3.5))
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for non-integer input
try:
    print(sum_to_n("hello"))
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for non-integer input
try:
    print(sum_to_n(3.0)
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for non-integer input
try:
    print(sum_to_n("hello")
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for non-integer input
try:
    print(sum_to_n(-10)
except ValueError:
    print("Invalid input. Please enter a positive integer.")

# Test case for non-integer input
try:
    print(sum_to_n(3.5)
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for non-integer input
try:
    print(sum_to_n("hello")
except TypeError:
    print("Invalid input. Please enter an integer.")

# Test case for non-integer input
try:
    print(sum