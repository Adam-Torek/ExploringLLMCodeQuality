"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""

def is_woodall(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_woodall(383))
/01_python_basics/01_python_basics_01.py
"""
Write a function to check if the given number is even or not.
assert is_even(383) == False
"""

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(383))
/01_python_basics/01_python_basics_02.py
"""
Write a function to check if the given number is odd or not.
assert is_odd(383) == True
"""

def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

print(is_odd(383))
/01_python_basics/01_python_basics_03.py
"""
Write a function to check if the given number is prime or not.
assert is_prime(383) == False
"""

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print(is_prime(383))
/01_python_basics/01_python_basics_04.py
"""
Write a function to check if the given number is perfect or not.
assert is_perfect(6) == True
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
/01_python_basics/01_python_basics_05.py
"""
Write a function to check if the given number is amstrong or not.
assert is_amstrong(153) == True
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
/01_python_basics/01_python_basics_06.py
"""
Write a function to check if the given number is armstrong or not.
assert is_armstrong(153) == True
"""

def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(num))
        temp //= 10
    if sum == num:
        return True
    else:
        return False

print(is_armstrong(153))
/01_python_basics/01_python_basics_07.py
"""
Write a function to check if the given number is palindrome or not.
assert is_palindrome(121) == True
"""

def is_palindrome(num):
    temp = num
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    if rev == num:
        return True
    else:
        return False

print(is_palindrome(121))
/01_python_basics/01_python_basics_08.py
"""
Write a function to check if the given number is fibonacci or not.
assert is_fibonacci(144) == True
"""

def is_fibonacci(num):
    a = 0
    b = 1
    while b < num:
        temp = a
        a = b
        b = temp + b
        if b == num:
            return True
    return False

print(is_fibonacci(144))
/01_