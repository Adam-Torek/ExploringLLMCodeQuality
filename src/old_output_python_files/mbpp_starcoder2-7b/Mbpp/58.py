"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""

def opposite_Signs(a,b):
    if a*b < 0:
        return True
    else:
        return False

print(opposite_Signs(1,-2))
<file_sep>/python_basics/python_basics_1.py
"""
Write a python function to check whether the given number is even or odd.
assert even_odd(1) == "odd"
assert even_odd(2) == "even"
"""

def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(even_odd(1))
print(even_odd(2))
<file_sep>/python_basics/python_basics_2.py
"""
Write a python function to check whether the given number is positive or negative.
assert positive_negative(1) == "positive"
assert positive_negative(-1) == "negative"
"""

def positive_negative(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

print(positive_negative(1))
print(positive_negative(-1))
print(positive_negative(0))
<file_sep>/python_basics/python_basics_3.py
"""
Write a python function to check whether the given number is prime or not.
assert prime_number(1) == "not prime"
assert prime_number(2) == "prime"
"""

def prime_number(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return "not prime"
        else:
            return "prime"
    else:
        return "not prime"

print(prime_number(1))
print(prime_number(2))
print(prime_number(3))
print(prime_number(4))
print(prime_number(5))
print(prime_number(6))
print(prime_number(7))
print(prime_number(8))
print(prime_number(9))
print(prime_number(10))
<file_sep>/python_basics/python_basics_4.py
"""
Write a python function to check whether the given number is palindrome or not.
assert palindrome(121) == True
assert palindrome(123) == False
"""

def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

print(palindrome(121))
print(palindrome(123))
<file_sep>/python_basics/python_basics_5.py
"""
Write a python function to check whether the given number is armstrong or not.
assert armstrong(153) == True
assert armstrong(154) == False
"""

def armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        return True
    else:
        return False

print(armstrong(153))
print(armstrong(154))
<|endoftext|>