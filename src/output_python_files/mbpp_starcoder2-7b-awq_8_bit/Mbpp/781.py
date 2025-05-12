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

print(count_divisors(10))
/python_basics/python_basics_1_exercise_18.py
"""
Write a python function to check whether the given number is prime or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-18.php
assert is_prime(11)
"""

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

print(is_prime(11))
/python_basics/python_basics_1_exercise_13.py
"""
Write a python function to check whether the given number is even or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-13.php
assert is_even(10)
"""

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
/python_basics/python_basics_1_exercise_12.py
"""
Write a python function to check whether the given number is odd or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-12.php
assert is_odd(10)
"""

def is_odd(num):
    if num % 2!= 0:
        return True
    else:
        return False

print(is_odd(10))
/python_basics/python_basics_1_exercise_16.py
"""
Write a python function to check whether the given number is perfect or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-16.php
assert is_perfect(6)
"""

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False

print(is_perfect(6))
/python_basics/python_basics_1_exercise_17.py
"""
Write a python function to check whether the given number is amstrong or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-17.php
assert is_amstrong(153)
"""

def is_amstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == num:
        return True
    else:
        return False

print(is_amstrong(153))
/python_basics/python_basics_1_exercise_19.py
"""
Write a python function to check whether the given number is armstrong or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-19.php
assert is_armstrong(153)
"""

def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == num:
        return True
    else:
        return False

print(is_armstrong(153))
/python_basics/python_basics_1_exercise_14.py
"""
Write a python function to check whether the given number is palindrome or not. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-14.php
assert is_palindrome(121)
"""

def is_palindrome(num):
    temp = num
    reverse =