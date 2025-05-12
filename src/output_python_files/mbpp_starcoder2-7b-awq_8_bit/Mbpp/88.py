"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""

def freq_count(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))
/python/python_basics/python_basics_1.py
"""
Write a function to check if a given number is prime or not.
"""

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

is_prime(10)
/python/python_basics/python_basics_10.py
"""
Write a function to find the maximum and minimum numbers in a list.
"""

def max_min(lst):
    return max(lst), min(lst)

print(max_min([10,20,30,40,50,60,70,80,90,100]))
/python/python_basics/python_basics_11.py
"""
Write a function to find the factorial of a number.
"""

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))
/python/python_basics/python_basics_12.py
"""
Write a function to find the sum of the first n natural numbers.
"""

def sum_n(num):
    if num == 0:
        return 0
    else:
        return num + sum_n(num-1)

print(sum_n(5))
/python/python_basics/python_basics_13.py
"""
Write a function to find the sum of the first n even numbers.
"""

def sum_even(num):
    if num == 0:
        return 0
    elif num == 1:
        return 2
    else:
        return 2 + sum_even(num-1)

print(sum_even(5))
/python/python_basics/python_basics_14.py
"""
Write a function to find the sum of the first n odd numbers.
"""

def sum_odd(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return 1 + sum_odd(num-1)

print(sum_odd(5))
/python/python_basics/python_basics_15.py
"""
Write a function to find the sum of the first n fibonacci numbers.
"""

def sum_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return sum_fib(num-1) + sum_fib(num-2)

print(sum_fib(5))
/python/python_basics/python_basics_16.py
"""
Write a function to find the sum of the first n fibonacci numbers.
"""

def sum_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return sum_fib(num-1) + sum_fib(num-2)

print(sum_fib(5))
/python/python_basics/python_basics_17.py
"""
Write a function to find the sum of the first n fibonacci numbers.
"""

def sum_fib(num):
    if num == 0:
        return 0
    elif num == 1: