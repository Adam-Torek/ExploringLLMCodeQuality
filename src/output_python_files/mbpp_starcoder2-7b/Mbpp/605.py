"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""
def prime_num(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, num, 2):
            if num % i == 0:
                return False
        return True

print(prime_num(13))
<file_sep>/python/0001-1000/0002_even_fibonacci_numbers.py
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def even_fibonacci_numbers(num):
    a, b = 1, 2
    sum = 0
    while b < num:
        if b % 2 == 0:
            sum += b
        a, b = b, a + b
    return sum

print(even_fibonacci_numbers(4000000))
<file_sep>/python/0001-1000/0001_multiples_of_3_and_5.py
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples_of_3_and_5(num):
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples_of_3_and_5(1000))
<file_sep>/python/0001-1000/0003_largest_prime_factor.py
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def largest_prime_factor(num):
    i = 2
    while i * i < num:
        while num % i == 0:
            num = num / i
        i += 1
    return num

print(largest_prime_factor(600851475143))
<file_sep>/python/0001-1000/0004_largest_palindrome_product.py
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largest_palindrome_product(num):
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1] and product > max:
                max = product
    return max

print(largest_palindrome_product(1000))
<file_sep>/python/0001-1000/0005_smallest_multiple.py
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallest_multiple(num):
    i = 1
    while True:
        for j in range(1, num + 1):
            if i % j!= 0:
                break
        else:
            return i
        i += 1

print(smallest_multiple(20))
<file_sep>/python/0001-1000/0006_sum_square_difference.py
"""
The sum of