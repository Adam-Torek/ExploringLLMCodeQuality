"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731,...
assert jacobsthal_num(5) == 11
"""

def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return jacobsthal_num(n-1) + (2 * jacobsthal_num(n-2))

print(jacobsthal_num(5))
/python/recursion/fibonacci.py
"""
Write a function to find the nth fibonacci number. https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,...
assert fibonacci(5) == 5
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
/python/recursion/factorial.py
"""
Write a function to find the factorial of a number. https://www.geeksforgeeks.org/program-for-factorial-of-a-number/ 0!, 1!, 2!, 3!, 4!, 5!, 6!, 7!, 8!, 9!, 10!,...
assert factorial(5) == 120
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
/python/recursion/sum_of_digits.py
"""
Write a function to find the sum of the digits of a number. https://www.geeksforgeeks.org/sum-digits-number-using-recursion/ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,...
assert sum_of_digits(5) == 5
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(5))
/python/recursion/sum_of_digits_2.py
"""
Write a function to find the sum of the digits of a number. https://www.geeksforgeeks.org/sum-digits-number-using-recursion/ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,...
assert sum_of_digits(5) == 5
"""

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(n // 10) + n % 10

print(sum_of_digits(5))
/python/recursion/sum_of_digits_3.py
"""
Write a function to find the sum of the digits of a number. https://www.geeksforgeeks.org/sum-digits-number-using-recursion/ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1