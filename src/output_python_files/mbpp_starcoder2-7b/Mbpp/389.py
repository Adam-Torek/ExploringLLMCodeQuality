"""
Write a function to find then'th lucas number.
assert find_lucas(9) == 76
"""

def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return find_lucas(n-1) + find_lucas(n-2)

print(find_lucas(9))
/python/recursion/sum_of_digits.py
"""
Write a function that takes in a non-negative integer and returns the sum of its digits.
assert sum_of_digits(123) == 6
assert sum_of_digits(0) == 0
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))
/python/recursion/reverse_string.py
"""
Write a function that takes in a string and returns a new string with the characters in reverse order.
assert reverse_string("abcd") == "dcba"
assert reverse_string("a") == "a"
assert reverse_string("") == ""
"""

def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])

print(reverse_string("abcd"))
/python/recursion/factorial.py
"""
Write a function that takes in a non-negative integer and returns the factorial of that number.
assert factorial(5) == 120
assert factorial(0) == 1
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
/python/recursion/product_of_array.py
"""
Write a function that takes in a non-empty array of numbers and returns the product of all the numbers in the array.
assert product_of_array([1, 2, 3]) == 6
assert product_of_array([1, 2, 3, 10]) == 60
"""

def product_of_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] * product_of_array(arr[1:])

print(product_of_array([1, 2, 3]))
/python/recursion/power.py
"""
Write a function that takes in a base and an exponent and returns the power of the base to the exponent.
assert power(2, 3) == 8
assert power(3, 2) == 9
assert power(2, 0) == 1
"""

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)

print(power(2, 3))
/python/recursion/fibonacci.py
"""
Write a function that takes in a number and returns the nth number of the fibonacci sequence.
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
/python/recursion/reverse_array.py
"""
Write a function that takes in an array of numbers and returns a new array where the elements are in reverse order.
assert reverse_array([1, 2, 3]) == [3, 2, 1]
assert reverse_array([1, 2, 3, 10]) == [10, 3, 2, 1]
"""

def reverse_array(arr):
    if len(arr) == 1: