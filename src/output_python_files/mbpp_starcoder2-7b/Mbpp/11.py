"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""

def remove_Occ(string,char):
    return string.replace(char,'',1)

print(remove_Occ("hello","l"))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a python function to check whether a given number is even or odd.
"""

def check_even_odd(number):
    if number%2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a python function to check whether a given number is prime or not.
"""

def check_prime(number):
    if number > 1:
        for i in range(2,number):
            if number%i == 0:
                return "Not Prime"
        else:
            return "Prime"
    else:
        return "Not Prime"

print(check_prime(10))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a python function to check whether a given number is perfect or not.
"""

def check_perfect(number):
    sum = 0
    for i in range(1,number):
        if number%i == 0:
            sum += i
    if sum == number:
        return "Perfect"
    else:
        return "Not Perfect"

print(check_perfect(6))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a python function to check whether a given number is strong or not.
"""

def check_strong(number):
    sum = 0
    temp = number
    while number > 0:
        digit = number%10
        sum += factorial(digit)
        number = number//10
    if sum == temp:
        return "Strong"
    else:
        return "Not Strong"

def factorial(number):
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)

print(check_strong(145))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a python function to check whether a given number is armstrong or not.
"""

def check_armstrong(number):
    sum = 0
    temp = number
    while number > 0:
        digit = number%10
        sum += digit**3
        number = number//10
    if sum == temp:
        return "Armstrong"
    else:
        return "Not Armstrong"

print(check_armstrong(153))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a python function to check whether a given number is palindrome or not.
"""

def check_palindrome(number):
    sum = 0
    temp = number
    while number > 0:
        digit = number%10
        sum = sum*10 + digit
        number = number//10
    if sum == temp:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(check_palindrome(121))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a python function to check whether a given number is fibonacci or not.
"""

def check_fibonacci(number):
    a = 0
    b = 1
    while b < number:
        c = a + b
        a = b
        b = c
    if b == number:
        return "Fibonacci"
    else:
        return "Not Fibonacci"

print(check_fibonacci(144))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a python function to check whether a given number is armstrong or not.
"""

def check_armstrong(number):
    sum