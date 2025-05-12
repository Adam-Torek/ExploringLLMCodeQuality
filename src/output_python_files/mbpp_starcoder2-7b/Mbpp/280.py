"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""

def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))
/python/recursion/factorial.py
"""
Write a function that takes in a number and returns the factorial of that number.
assert factorial(5) == 120
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
/python/recursion/fibonacci.py
"""
Write a function that takes in a number and returns the nth number of the fibonacci sequence.
assert fibonacci(5) == 5
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
/python/recursion/reverse_string.py
"""
Write a function that takes in a string and returns a new string with the characters in reverse order.
assert reverse_string("hello") == "olleh"
"""

def reverse_string(string):
    if len(string) == 1:
        return string
    return reverse_string(string[1:]) + string[0]

print(reverse_string("hello"))
/python/recursion/power.py
"""
Write a function that takes in a base and an exponent and returns the power of the base to the exponent.
assert power(2,3) == 8
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

print(power(2,3))
/python/recursion/palindrome.py
"""
Write a function that takes in a string and returns a boolean indicating whether or not the input string is a palindrome.
assert palindrome("racecar") == True
"""

def palindrome(string):
    if len(string) == 1:
        return True
    if string[0]!= string[-1]:
        return False
    return palindrome(string[1:-1])

print(palindrome("racecar"))
/python/recursion/sum_array.py
"""
Write a function that takes in an array of numbers and returns the sum of all the numbers in the array.
assert sum_array([1,2,3,4]) == 10
"""

def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_array(arr[1:])

print(sum_array([1,2,3,4]))
/python/recursion/sum_digits.py
"""
Write a function that takes in a number and returns the sum of all the digits in the number.
assert sum_digits(123) == 6
"""

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(sum_digits(123))
/python/recursion/product_array.py
"""
Write a function that takes in an array of numbers and returns the product of all the numbers in the array.
assert product_array([1,2,3,4]) == 24
"""

def product_array(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] * product_array(arr[1:])

print(product_array([1,2,3,4]))
/python/recursion/reverse_array.py
"""
Write a function that takes in an array of numbers and returns a new array where the elements are in reverse order.
assert reverse_array([1