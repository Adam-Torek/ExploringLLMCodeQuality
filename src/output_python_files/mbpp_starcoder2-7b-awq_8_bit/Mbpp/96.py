"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""

def divisor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

print(divisor(15))
/python/0002_fibonacci.py
"""
Write a python function to find the nth fibonacci number.
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
/python/0001_factorial.py
"""
Write a python function to find the factorial of a given integer.
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
/python/0003_palindrome.py
"""
Write a python function to check if a given string is a palindrome.
assert palindrome("racecar") == True
assert palindrome("hello") == False
"""

def palindrome(s):
    return s == s[::-1]

print(palindrome("racecar"))
print(palindrome("hello"))