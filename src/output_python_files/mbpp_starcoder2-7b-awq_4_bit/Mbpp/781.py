"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""

def count_divisors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count

def is_even(num):
    return count_divisors(num) % 2 == 0

assert is_even(10) == True
assert is_even(11) == False
/python/basic/python-basic-1-exercise-12.py
"""
Write a python function to check whether the given number is even or odd. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-12.php
assert is_even(10)
"""

def is_even(num):
    return num % 2 == 0

assert is_even(10) == True
assert is_even(11) == False
/python/basic/python-basic-1-exercise-11.py
"""
Write a python function to check whether the given number is prime or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-11.php
assert is_prime(10)
"""

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

assert is_prime(10) == False
assert is_prime(11) == True
/python/basic/python-basic-1-exercise-13.py
"""
Write a python function to check whether the given number is perfect or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-13.php
assert is_perfect(6)
"""

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

assert is_perfect(6) == True
assert is_perfect(10) == False
/python/basic/python-basic-1-exercise-10.py
"""
Write a python function to check whether the given number is palindrome or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-10.php
assert is_palindrome(10)
"""

def is_palindrome(num):
    return str(num) == str(num)[::-1]

assert is_palindrome(10) == False
assert is_palindrome(11) == True
/python/basic/python-basic-1-exercise-14.py
"""
Write a python function to check whether the given number is strong number or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-14.php
assert is_strong(145)
"""

def is_strong(num):
    sum = 0
    for i in str(num):
        sum += factorial(int(i))
    return sum == num

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

assert is_strong(145) == True
assert is_strong(11) == False
/python/basic/python-basic-1-exercise-15.py
"""
Write a python function to check whether the given number is automorphic number or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-15.php
assert is_automorphic(16)
"""

def is_automorphic(num):
    return str(num ** 2) == str(num)

assert is_automorphic(16) == True
assert is