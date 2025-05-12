"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

def perfect_squares(start, end):
    return [x**2 for x in range(start, end+1) if x**0.5 == int(x**0.5)]

print(perfect_squares(1,30))
/python/codewars/7kyu/sum_of_digits_digital_root.py
"""
Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

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
    while n > 9:
        n = sum([int(x) for x in str(n)])
    return n

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
/python/codewars/7kyu/sum_of_odd_numbers.py
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1).

Example:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""

def row_sum_odd_numbers(n):
    return sum([x for x in range(1, n*2, 2)])

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
/python/codewars/7kyu/sum_of_digits.py
"""
Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. For example:

sumDigits(10);  // Returns 1
sumDigits(99);  // Returns 18
sumDigits(-32); // Returns 5
Let's assume that all numbers in the input will be integer values.
"""

def sum_digits(number):
    return sum([int(x) for x in str(abs(number))])

print(sum_digits(10))
print(sum_digits(99))
print(sum_digits(-32))
/python/codewars/7kyu/sum_of_odd_numbers_2.py
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the number of odd values in row n of the above triangle.

Example:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""

def row_sum_odd_numbers(n):
    return sum([x for x in range(1, n*2, 2)])

print(row_sum_odd_numbers(1))