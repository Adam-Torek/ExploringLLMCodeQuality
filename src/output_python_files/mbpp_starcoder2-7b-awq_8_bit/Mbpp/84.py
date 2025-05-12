"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""

def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence(n-1) + sequence(n-2)

print sequence(10)
/python/recursion/fibonacci.py
"""
Write a function to find the nth number in the fibonacci sequence.
assert fibonacci(10) == 55
"""

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(10)
/python/recursion/factorial.py
"""
Write a function to find the factorial of a number.
assert factorial(5) == 120
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(5)
/python/recursion/sum_of_digits.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(n/10) + n%10

print sum_of_digits(123)
/python/recursion/reverse_string.py
"""
Write a function to reverse a string.
assert reverse_string("hello") == "olleh"
"""

def reverse_string(s):
    if len(s) == 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print reverse_string("hello")
/python/recursion/palindrome.py
"""
Write a function to check if a string is a palindrome.
assert palindrome("racecar") == True
"""

def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

print palindrome("racecar")
/python/recursion/sum_of_squares.py
"""
Write a function to find the sum of the squares of the first n natural numbers.
assert sum_of_squares(5) == 55
"""

def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_of_squares(n-1)

print sum_of_squares(5)
/python/recursion/sum_of_integers.py
"""
Write a function to find the sum of the first n natural numbers.
assert sum_of_integers(5) == 15
"""

def sum_of_integers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_integers(n-1)

print sum_of_integers(5)
/python/recursion/sum_of_cubes.py
"""
Write a function to find the sum of the cubes of the first n natural numbers.
assert sum_of_cubes(5) == 225
"""

def sum_of_cubes(n):
    if n == 1:
        return 1
    else:
        return n**3 + sum_of_cubes(n-1)

print sum_of_cubes(5)
/python/recursion/sum_of_digits_2.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(n/10) + n%10

print sum_of_digits(123)
/python/recursion/sum_of_squares_2.py
"""
Write a function to find the sum of the squares of the first n natural numbers.
assert sum_of_squares(5) == 55
"""