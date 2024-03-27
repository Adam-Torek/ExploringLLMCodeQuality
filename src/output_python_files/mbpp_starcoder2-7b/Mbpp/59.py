"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""

def is_octagonal(n):
    return (8*n**2 - 24*n + 17) ** 0.5 == int((8*n**2 - 24*n + 17) ** 0.5)

def nth_octagonal(n):
    i = 1
    while True:
        if is_octagonal(i):
            n -= 1
            if n == 0:
                return i
        i += 1

print(nth_octagonal(1000))
<file_sep>/python/project_euler/001-050/004.py
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome():
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i*j) and i*j > largest:
                largest = i*j
    return largest

print(largest_palindrome())
<file_sep>/python/project_euler/001-050/001.py
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples(n):
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

print(sum_multiples(1000))
<file_sep>/python/project_euler/001-050/010.py
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def sum_primes(n):
    return sum([i for i in range(n) if is_prime(i)])

print(sum_primes(2000000))
<file_sep>/python/project_euler/001-050/005.py
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def is_divisible(n):
    for i in range(1, 21):
        if n % i!= 0:
            return False
    return True

def smallest_divisible():
    i = 20
    while True:
        if is_divisible(i):
            return i
        i += 20

print(smallest_divisible())
<file_sep>/python/project_euler/001-050/003.py
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n):
    largest =