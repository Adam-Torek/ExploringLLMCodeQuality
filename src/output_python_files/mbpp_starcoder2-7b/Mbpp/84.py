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

print(sequence(10))
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

print(fibonacci(10))
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

print(factorial(5))
/python/recursion/sum_of_digits.py
"""
Write a function to find the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))
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

print(reverse_string("hello"))
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

print(palindrome("racecar"))
/python/recursion/sum_of_numbers.py
"""
Write a function to find the sum of the numbers in a list.
assert sum_of_numbers([1, 2, 3]) == 6
"""

def sum_of_numbers(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + sum_of_numbers(l[1:])

print(sum_of_numbers([1, 2, 3]))
/python/recursion/sum_of_squares.py
"""
Write a function to find the sum of the squares of the numbers in a list.
assert sum_of_squares([1, 2, 3]) == 14
"""

def sum_of_squares(l):
    if len(l) == 1:
        return l[0] ** 2
    else:
        return l[0] ** 2 + sum_of_squares(l[1:])

print(sum_of_squares([1, 2, 3]))
/python/recursion/sum_of_odds.py
"""
Write a function to find the sum of the odd numbers in a list.
assert sum_of_odds([1, 2, 3]) == 4
"""

def sum_of_odds(l):
    if len(l) == 1:
        return l[0] if l[0] % 2 == 1 else 0
    else:
        return l[0] if l[0] % 2 == 1 else 0 + sum_of_odds(l[1:])

print(sum_of_odds([1, 2, 3]))
/python/recursion/sum_of_evens.py
"""
Write a function to find the sum of the even numbers in a list.
assert sum_of