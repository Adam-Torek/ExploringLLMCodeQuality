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
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
/python/recursion/factorial.py
"""
Write a function that takes in a number and returns the factorial of that number.
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
/python/recursion/reverse_string.py
"""
Write a function that takes in a string and returns the reversed string.
assert reverse_string("hello") == "olleh"
assert reverse_string("hello world") == "dlrow olleh"
"""

def reverse_string(string):
    if len(string) == 1:
        return string
    return reverse_string(string[1:]) + string[0]

print(reverse_string("hello"))
print(reverse_string("hello world"))
/python/recursion/power.py
"""
Write a function that takes in a number and a power and returns the number raised to the power.
assert power(2, 2) == 4
assert power(2, 3) == 8
assert power(2, 4) == 16
assert power(2, 5) == 32
assert power(2, 6) == 64
"""

def power(num, power):
    if power == 0:
        return 1
    return num * power(num, power-1)

print(power(2, 2))
print(power(2, 3))
print(power(2, 4))
print(power(2, 5))
print(power(2, 6))
/python/recursion/reverse_array.py
"""
Write a function that takes in an array and returns the reversed array.
assert reverse_array([1,2,3,4]) == [4,3,2,1]
assert reverse_array([1,2,3,4,5]) == [5,4,3,2,1]
"""

def reverse_array(arr):
    if len(arr) == 1:
        return arr
    return [arr[-1]] + reverse_array(arr[:-1])

print(reverse_array([1,2,3,4]))
print(reverse_array([1,2,3,4,5]))
/python/recursion/sum_