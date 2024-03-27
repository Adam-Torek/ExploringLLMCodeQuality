"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""

def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_Number(n-1) + (n-1)*bell_Number(n-1)

print(bell_Number(2))
<file_sep>/recursion/sum_of_digits.py
"""
Write a python function to find sum of digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)

print(sum_of_digits(123))
<file_sep>/recursion/sum_of_digits_2.py
"""
Write a python function to find sum of digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)

def sum_of_digits_2(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_2(n//10)

print(sum_of_digits_2(123))
<file_sep>/recursion/sum_of_digits_3.py
"""
Write a python function to find sum of digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)

def sum_of_digits_3(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_3(n//10)

def sum_of_digits_4(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_4(n//10)

print(sum_of_digits_4(123))
<file_sep>/recursion/sum_of_digits_4.py
"""
Write a python function to find sum of digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)

def sum_of_digits_2(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_2(n//10)

def sum_of_digits_3(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_3(n//10)

def sum_of_digits_4(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_4(n//10)

def sum_of_digits_5(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_5(n//10)

print(sum_of_digits_5(123))
<file_sep>/recursion/sum_of_digits_5.py
"""
Write a python function to find sum of digits of a number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)

def sum_of_digits_2(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_2(n//10)

def sum_of_digits_3(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits_3