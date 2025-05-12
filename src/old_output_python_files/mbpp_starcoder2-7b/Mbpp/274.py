"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""

def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(0, n+1, 2):
        sum += binomial_Coeff(n, i)
    return sum

print(even_binomial_Coeff_Sum(4))
<file_sep>/python/recursion/factorial.py
"""
Write a python function that takes in a positive integer n and returns the factorial of n.
assert factorial(4) == 24
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))
<file_sep>/python/recursion/fibonacci.py
"""
Write a python function that takes in a positive integer n and returns the nth fibonacci number.
assert fibonacci(4) == 3
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))
<file_sep>/python/recursion/sum_of_digits.py
"""
Write a python function that takes in a positive integer n and returns the sum of the digits of n.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))
<file_sep>/python/recursion/sum_of_digits_2.py
"""
Write a python function that takes in a positive integer n and returns the sum of the digits of n.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))

def sum_of_digits_2(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits_2(n // 10)

print(sum_of_digits_2(123))
<file_sep>/python/recursion/sum_of_digits_3.py
"""
Write a python function that takes in a positive integer n and returns the sum of the digits of n.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))

def sum_of_digits_2(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits_2(n // 10)

print(sum_of_digits_2(123))

def sum_of_digits_3(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits_3(n // 10)

print(sum_of_digits_3(123))
<file_sep>/python/recursion/sum_of_digits_4.py
"""
Write a python function that takes in a positive integer n and returns the sum of the digits of n.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))

def sum_of_digits_2(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits_2(n // 10)

print(sum_of_digits_2(123))

def sum