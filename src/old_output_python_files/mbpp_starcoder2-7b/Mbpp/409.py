"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""

def min_product_tuple(lst):
    return min(lst, key=lambda x: x[0] * x[1])[0] * min(lst, key=lambda x: x[0] * x[1])[1]

assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
<file_sep>/python/codewars/7kyu/sum_of_digits_digital_root.py
"""
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works (Ruby example given):

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29...
=> 2 + 9
=> 11...
=> 1 + 1
=> 2
"""

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))

assert digital_root(16) == 7
assert digital_root(942) == 6
assert digital_root(132189) == 6
assert digital_root(493193) == 2
<file_sep>/python/codewars/7kyu/sum_of_odd_cubed_numbers.py
"""
Given a positive integer n, return the sum of all odd cubed numbers up to n, inclusive.

Example:

sum_of_cubed_odd_numbers(243) # -> 506036
"""

def sum_of_cubed_odd_numbers(n):
    return sum(i ** 3 for i in range(1, n + 1) if i % 2!= 0)

assert sum_of_cubed_odd_numbers(243) == 506036
<file_sep>/python/codewars/7kyu/sum_of_odd_numbers.py
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""

def row_sum_odd_numbers(n):
    return sum(i for i in range(1, n * 2, 2))

assert row_sum_odd_numbers(1) == 1
assert row_sum_odd_numbers(2) == 8
<file_sep>/python/codewars/7kyu/sum_of_odd_numbers_2.py
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the number of odd numbers that are below the given row index.

E.g.

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3
"""

def row_sum_odd_numbers(n):
    return n * n

assert row_sum_