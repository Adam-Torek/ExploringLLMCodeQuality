"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""

def even_position(lst):
    for i in range(0,len(lst),2):
        if lst[i]%2!= 0:
            return False
    return True

print(even_position([3,2,1]))
print(even_position([2,4,6,8]))
print(even_position([2,4,6,7]))
/python_basics/python_basics_1.py
"""
Write a python function to check whether a given number is prime or not.
assert is_prime(7) == True
assert is_prime(10) == False
"""

def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
/python_basics/python_basics_3.py
"""
Write a python function to check whether a given number is palindrome or not.
assert is_palindrome(121) == True
assert is_palindrome(123) == False
"""

def is_palindrome(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i]!= num_str[-i-1]:
            return False
    return True

print(is_palindrome(121))
print(is_palindrome(123))
/python_basics/python_basics_2.py
"""
Write a python function to check whether a given number is armstrong number or not.
assert is_armstrong(153) == True
assert is_armstrong(123) == False
"""

def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for i in range(num_len):
        sum += int(num_str[i])**num_len
    if sum == num:
        return True
    return False

print(is_armstrong(153))
print(is_armstrong(123))