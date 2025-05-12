"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""

def add_dict_to_tuple(tup, dict):
    return tup + (dict,)

print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ))
/python_basics/python_basics_001.py
"""
Write a function to check if a number is even or odd.
assert is_even(10) == True
assert is_even(11) == False
"""

def is_even(num):
    return num % 2 == 0

print(is_even(10))
print(is_even(11))
/python_basics/python_basics_003.py
"""
Write a function to check if a number is prime or not.
assert is_prime(10) == False
assert is_prime(11) == True
"""

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(10))
print(is_prime(11))
/python_basics/python_basics_005.py
"""
Write a function to check if a number is perfect or not.
assert is_perfect(6) == True
assert is_perfect(10) == False
"""

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

print(is_perfect(6))
print(is_perfect(10))
/python_basics/python_basics_004.py
"""
Write a function to check if a number is armstrong or not.
assert is_armstrong(153) == True
assert is_armstrong(154) == False
"""

def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum == num

print(is_armstrong(153))
print(is_armstrong(154))
/python_basics/python_basics_006.py
"""
Write a function to check if a number is strong or not.
assert is_strong(145) == True
assert is_strong(146) == False
"""

def is_strong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += factorial(digit)
        temp //= 10
    return sum == num

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

print(is_strong(145))
print(is_strong(146))
/python_basics/python_basics_007.py
"""
Write a function to check if a number is deficient or not.
assert is_deficient(10) == True
assert is_deficient(12) == False
"""

def is_deficient(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum < num

print(is_deficient(10))
print(is_deficient(12))
/python_basics/python_basics_008.py
"""
Write a function to check if a number is perfect or not.
assert is_perfect(6) == True
assert is_perfect(10) == False
"""

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

print(is_perfect(6))
print(is_perfect