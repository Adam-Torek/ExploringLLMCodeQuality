"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""

def kth_element(arr, k):
    return arr[k-1]

print(kth_element([12,3,5,7,19], 2))/python/recursion/fibonacci.py
"""
Write a function that returns the nth fibonacci number.
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
"""

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))/python/recursion/reverse_string.py
"""
Write a function that returns a string in reverse.
assert reverse_string("hello") == "olleh"
"""

def reverse_string(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))/python/recursion/factorial.py
"""
Write a function that returns the factorial of a number.
assert factorial(5) == 120
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))/python/recursion/sum_of_digits.py
"""
Write a function that returns the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))/python/recursion/sum_of_digits_2.py
"""
Write a function that returns the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(n // 10) + n % 10

print(sum_of_digits(123))/python/recursion/sum_of_digits_3.py
"""
Write a function that returns the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(n // 10) + n % 10

print(sum_of_digits(123))/python/recursion/sum_of_digits_4.py
"""
Write a function that returns the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(n // 10) + n % 10

print(sum_of_digits(123))/python/recursion/sum_of_digits_5.py
"""
Write a function that returns the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(n // 10) + n % 10

print(sum_of_digits(123))/python/recursion/sum_of_digits_6.py
"""
Write a function that returns the sum of the digits of a number.
assert sum_of