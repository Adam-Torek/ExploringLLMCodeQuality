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
<file_sep>/python/recursion/factorial.py
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
<file_sep>/python/recursion/fibonacci.py
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
<file_sep>/python/recursion/sum.py
"""
Write a function to find the sum of all numbers from 1 to n.
assert sum(10) == 55
"""

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

print(sum(10))
<file_sep>/python/recursion/palindrome.py
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
<file_sep>/python/recursion/reverse.py
"""
Write a function to reverse a string.
assert reverse("racecar") == "racecar"
"""

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

print(reverse("racecar"))
<|endoftext|>