"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""

def unique_Element(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False

print(unique_Element([1,1,1]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a python function to check whether a number is even or odd.
assert even_odd(2) == "Even"
assert even_odd(3) == "Odd"
"""

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(2))
print(even_odd(3))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a python function to check whether a number is prime or not.
assert prime_number(2) == True
assert prime_number(3) == True
assert prime_number(4) == False
"""

def prime_number(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

print(prime_number(2))
print(prime_number(3))
print(prime_number(4))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a python function to check whether a number is positive or negative.
assert positive_negative(2) == "Positive"
assert positive_negative(-2) == "Negative"
"""

def positive_negative(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(positive_negative(2))
print(positive_negative(-2))
/Python/Python_Basics/Python_Basics_2/Python_Basics_2_1.py
"""
Write a python function to check whether a number is divisible by 5 and 11 or not.
assert divisible_by_5_and_11(55) == True
assert divisible_by_5_and_11(56) == False
"""

def divisible_by_5_and_11(num):
    if num % 5 == 0 and num % 11 == 0:
        return True
    else:
        return False

print(divisible_by_5_and_11(55))
print(divisible_by_5_and_11(56))
/Python/Python_Basics/Python_Basics_2/Python_Basics_2_2.py
"""
Write a python function to check whether a number is divisible by 7 or not.
assert divisible_by_7(49) == True
assert divisible_by_7(48) == False
"""

def divisible_by_7(num):
    if num % 7 == 0:
        return True
    else:
        return False

print(divisible_by_7(49))
print(divisible_by_7(48))
/Python/Python_Basics/Python_Basics_2/Python_Basics_2_3.py
"""
Write a python function to check whether a number is divisible by 5 or 7 or not.
assert divisible_by_5_or_7(35) == True
assert divisible_by_5_or_7(36) == False
"""

def divisible_by_5_or_7(num):
    if num % 5 == 0 or num % 7 == 0:
        return True
    else:
        return False

print(divisible_by_5_or_7(35))
print(divisible_by_5_or_7(36))
/Python/Python_Basics/Python_Basics_2/Python_Basics_2_4.py
"""
Write a python function to check whether a number is divisible by 5 and 7 or