"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
from math import sqrt

def newman_prime(n):
    if n < 1:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n == 4:
        return 7

    def is_prime(num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    def newman_shanks(n):
        if n == 1:
            return 2
        if n == 2:
            return 3
        if n == 3:
            return 5
        if n == 4:
            return 7
        if n % 2 == 0:
            n -= 1
        if n % 3 == 0:
            n -= 1
        if n % 5 == 0:
            n -= 1
        if n % 7 == 0:
            n -= 1
        if n % 11 == 0:
            n -= 1
        if n % 13 == 0:
            n -= 1
        if n % 17 == 0:
            n -= 1
        if n % 19 == 0:
            n -= 1
        if n % 23 == 0:
            n -= 1
        if n % 29 == 0:
            n -= 1
        if n % 31 == 0:
            n -= 1
        if n % 37 == 0:
            n -= 1
        if n % 41 == 0:
            n -= 1
        if n % 43 == 0:
            n -= 1
        if n % 47 == 0:
            n -= 1
        if n % 53 == 0:
            n -= 1
        if n % 59 == 0:
            n -= 1
        if n % 61 == 0:
            n -= 1
        if n % 67 == 0:
            n -= 1
        if n % 71 == 0:
            n -= 1
        if n % 73 == 0:
            n -= 1
        if n % 79 == 0:
            n -= 1
        if n % 83 == 0:
            n -= 1
        if n % 89 == 0:
            n -= 1
        if n % 97 == 0:
            n -= 1
        if n % 101 == 0:
            n -= 1
        if n % 103 == 0:
            n -= 1
        if n % 107 == 0:
            n -= 1
        if n % 109 == 0:
            n -= 1
        if n % 113 == 0:
            n -= 1
        if n % 127 == 0:
            n -= 1
        if n % 131 == 0:
            n -= 1
        if n % 137 == 0:
            n -= 1
        if n % 139 == 0:
            n -= 1
        if n % 149 == 0:
            n -= 1
        if n % 157 == 0:
            n -= 1
        if n % 163 == 0:
            n -= 1
        if n % 173 == 0