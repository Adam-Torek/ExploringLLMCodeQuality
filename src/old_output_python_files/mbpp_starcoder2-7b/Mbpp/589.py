"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

def perfect_squares(start, end):
    return [x for x in range(start, end+1) if x**0.5 == int(x**0.5)]

print(perfect_squares(1,30))
<file_sep>/python/0001-1000/0043-sum-of-digits-of-a-number.py
"""
Given a number, find the sum of its digits.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    return sum([int(x) for x in str(n)])

print(sum_of_digits(123))
<file_sep>/python/0001-1000/0012-find-the-largest-palindrome-product-of-two-3-digit-numbers.py
"""
Find the largest palindrome made from the product of two 3-digit numbers.
assert largest_palindrome_product(3)==906609
"""

def largest_palindrome_product(n):
    return max([x*y for x in range(10**(n-1), 10**n) for y in range(10**(n-1), 10**n) if str(x*y) == str(x*y)[::-1]])

print(largest_palindrome_product(3))
<file_sep>/python/0001-1000/0020-sum-of-digits-of-factorial.py
"""
Find the sum of digits of the number 100!
assert sum_of_digits_of_factorial(100)==648
"""

def sum_of_digits_of_factorial(n):
    return sum([int(x) for x in str(reduce(lambda x, y: x*y, range(1, n+1)))])

print(sum_of_digits_of_factorial(100))
<file_sep>/python/0001-1000/0036-palindrome-number.py
"""
Determine whether an integer is a palindrome.
assert is_palindrome(121)==True
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(121))
<file_sep>/python/0001-1000/0027-sum-square-difference.py
"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
assert sum_square_difference(100)==25164150
"""

def sum_square_difference(n):
    return sum([x**2 for x in range(1, n+1)]) - sum(range(1, n+1))**2

print(sum_square_difference(100))
<file_sep>/python/0001-1000/0033-digit-cancelling-fractions.py
"""
Find the product of the numerator and denominator of the lowest fraction among all fractions that are cancellable, i.e. the numerator and denominator share a common digit.
assert digit_cancelling_fractions()==100
"""

def digit_cancelling_fractions():
    return reduce(lambda x, y: x*y, [x for x in range(10, 100) for y in range(x+1, 100) if str(x)[1] == str(y)[0] and float(x)/y == float(str(x)[0])/float(str(y)[1])])

print(digit_cancelling_fractions())
<file_sep>/python/0001-1000/0015-lattice-paths.py
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
assert lattice_paths(20)==137846528820
"""