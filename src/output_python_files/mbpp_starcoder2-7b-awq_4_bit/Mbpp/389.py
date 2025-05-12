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

print find_lucas(9)
/recursion/fibonacci.py
"""
Write a function to find the nth fibonacci number.
assert find_fibonacci(9) == 34
"""

def find_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return find_fibonacci(n-1) + find_fibonacci(n-2)

print find_fibonacci(9)
/recursion/factorial.py
"""
Write a function to find the factorial of a number.
assert find_factorial(5) == 120
"""

def find_factorial(n):
    if n == 0:
        return 1
    else:
        return n * find_factorial(n-1)

print find_factorial(5)
/recursion/sum_of_digits.py
"""
Write a function that finds the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n/10)

print sum_of_digits(123)
/recursion/sum_of_squares.py
"""
Write a function that finds the sum of the squares of the digits of a number.
assert sum_of_squares(123) == 14
"""

def sum_of_squares(n):
    if n == 0:
        return 0
    else:
        return (n % 10) ** 2 + sum_of_squares(n/10)

print sum_of_squares(123)
/recursion/sum_of_digits_2.py
"""
Write a function that finds the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n/10)

print sum_of_digits(123)

def sum_of_digits_2(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits_2(n/10)

print sum_of_digits_2(123)
/recursion/sum_of_squares_2.py
"""
Write a function that finds the sum of the squares of the digits of a number.
assert sum_of_squares(123) == 14
"""

def sum_of_squares(n):
    if n == 0:
        return 0
    else:
        return (n % 10) ** 2 + sum_of_squares(n/10)

print sum_of_squares(123)

def sum_of_squares_2(n):
    if n == 0:
        return 0
    else:
        return (n % 10) ** 2 + sum_of_squares_2(n/10)

print sum_of_squares_2(123)
/recursion/sum_of_digits_3.py
"""
Write a function that finds the sum of the digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n/10)

print sum_of_digits(123)

def sum_of_digits_2(n):
    if n == 0:
        return 0
    else:
        return n % 10 +