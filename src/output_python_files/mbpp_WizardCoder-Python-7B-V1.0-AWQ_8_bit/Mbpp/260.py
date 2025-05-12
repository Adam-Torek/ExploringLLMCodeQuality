"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def newman_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

print(newman_prime(3))

# def newman_prime(n):
#     count = 0
#     num = 1
#     while count < n:
#         num += 1
#         if is_prime(num):
#             count += 1
#     return num
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# print(newman_prime(3))