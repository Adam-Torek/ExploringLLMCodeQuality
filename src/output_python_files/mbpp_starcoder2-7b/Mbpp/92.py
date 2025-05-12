"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""

def is_undulating(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            return False
    return True

print(is_undulating(1212121))
/python/001-100/002_sum_of_digits.py
"""
Write a function that takes a number and returns the sum of its digits.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(sum_of_digits(123))
/python/001-100/007_is_prime.py
"""
Write a function that takes a number and returns True if it's prime.
assert is_prime(7) == True
"""

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
/python/001-100/008_is_palindrome.py
"""
Write a function that takes a number and returns True if it's palindrome.
assert is_palindrome(12321) == True
"""

def is_palindrome(num):
    num = str(num)
    for i in range(len(num)//2):
        if num[i]!= num[-i-1]:
            return False
    return True

print(is_palindrome(12321))
/python/001-100/003_is_even.py
"""
Write a function that takes a number and returns True if it's even.
assert is_even(123) == False
"""

def is_even(num):
    return num % 2 == 0

print(is_even(123))
/python/001-100/006_is_armstrong.py
"""
Write a function that takes a number and returns True if it's armstrong.
assert is_armstrong(153) == True
"""

def is_armstrong(num):
    sum = 0
    for i in str(num):
        sum += int(i)**len(str(num))
    return sum == num

print(is_armstrong(153))
/python/001-100/004_is_odd.py
"""
Write a function that takes a number and returns True if it's odd.
assert is_odd(123) == True
"""

def is_odd(num):
    return num % 2!= 0

print(is_odd(123))
/python/001-100/005_is_divisible.py
"""
Write a function that takes two numbers and returns True if the first number is divisible by the second one.
assert is_divisible(12, 3) == True
"""

def is_divisible(num1, num2):
    return num1 % num2 == 0

print(is_divisible(12, 3))
/python/001-100/009_is_perfect.py
"""
Write a function that takes a number and returns True if it's perfect.
assert is_perfect(6) == True
"""

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

print(is_perfect(6))
/python/001-100/010_is_abundant.py
"""
Write a function that takes a number and returns True if it's abundant.
assert is_abundant(12) == True
"""

def is_abundant(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum > num