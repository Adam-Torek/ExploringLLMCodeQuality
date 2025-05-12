"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""

def swap_List(list):
    list[0], list[-1] = list[-1], list[0]
    return list

print(swap_List([12, 35, 9, 56, 24]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a python function to find the maximum of three numbers.
assert max_of_three(10, 11, 5) == 11
"""

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_of_three(10, 11, 5))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a python function to find the sum of the first n natural numbers.
assert sum_of_n(10) == 55
"""

def sum_of_n(n):
    return n * (n + 1) / 2

print(sum_of_n(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a python function to find the factorial of a number.
assert factorial(5) == 120
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a python function to find the sum of the first n even numbers.
assert sum_of_even_n(10) == 30
"""

def sum_of_even_n(n):
    return n * (n + 1) / 2 * 2

print(sum_of_even_n(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a python function to find the sum of the first n odd numbers.
assert sum_of_odd_n(10) == 25
"""

def sum_of_odd_n(n):
    return n * (n + 1) / 2 * 2 - 1

print(sum_of_odd_n(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a python function to find the sum of the first n prime numbers.
assert sum_of_prime_n(10) == 17
"""

def sum_of_prime_n(n):
    sum = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            sum += i
    return sum

print(sum_of_prime_n(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a python function to find the sum of the first n fibonacci numbers.
assert sum_of_fibonacci_n(10) == 143
"""

def sum_of_fibonacci_n(n):
    sum = 0
    a = 0
    b = 1
    for i in range(n):
        sum += a
        a, b = b, a + b
    return sum

print(sum_of_fibonacci_n(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a python function to find the sum of the first n square numbers.
assert sum_of_square_n(10) == 385
"""

def sum_of_square_n(n):
    sum = 0
    for