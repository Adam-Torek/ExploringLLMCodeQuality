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
/python/recursion/fibonacci.py
"""
Write a function that takes in a number and returns the nth number of the fibonacci sequence.
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13
assert fibonacci(8) == 21
assert fibonacci(9) == 34
assert fibonacci(10) == 55
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
/python/recursion/factorial.py
"""
Write a function that takes in a number and returns the factorial of that number.
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720
assert factorial(7) == 5040
assert factorial(8) == 40320
assert factorial(9) == 362880
assert factorial(10) == 3628800
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(10))
/python/recursion/reverse_string.py
"""
Write a function that takes in a string and returns the reversed string.
assert reverse_string("abc") == "cba"
assert reverse_string("hello") == "olleh"
assert reverse_string("hello world") == "dlrow olleh"
"""

def reverse_string(string):
    if len(string) == 1:
        return string
    return reverse_string(string[1:]) + string[0]

print(reverse_string("hello world"))
/python/recursion/power.py
"""
Write a function that takes in a base and exponent and returns the power of the base to the exponent.
assert power(2, 1) == 2
assert power(2, 2) == 4
assert power(2, 3) == 8
assert power(2, 4) == 16
assert power(2, 5) == 32
assert power(2, 6) == 64
assert power(2, 7) == 128
assert power(2, 8) == 256
assert power(2, 9) == 512
assert power(2, 10) == 1024
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

print(power(2, 10))
/python/recursion/reverse_array.py
"""
Write a function that takes in an array and returns the reversed array.
assert reverse_array([1,2,3]) == [3,2,1]
assert reverse_array([1,2,3,4]) == [4,3,2,1]
assert reverse_array([1,2,3,4,5]) == [5,4,3,2,1]
"""

def reverse_array(arr):
    if len(arr) == 1