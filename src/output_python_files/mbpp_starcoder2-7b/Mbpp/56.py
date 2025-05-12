"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""

def check(num):
    return num == int(str(num)[::-1]) - 1

print(check(70))
/python/codewars/7kyu/sum_of_digits_digital_root.py
"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples

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

print(digital_root(132189))
/python/codewars/7kyu/sum_of_odd_numbers.py
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
    return sum(range(1, n * 2 + 1, 2))

print(row_sum_odd_numbers(1))
/python/codewars/7kyu/sum_of_positive.py
"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    return sum(filter(lambda x: x > 0, arr))

print(positive_sum([1,-4,7,12]))
/python/codewars/7kyu/sum_of_two_lowest_positive_integers.py
"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
/python/codewars/7kyu/sum_of_odd_cubed_numbers.py
"""
Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.

Note: there are no arrays of strings that can be passed into this method, so you may have to use a try/catch block to filter out if there are any strings.
"""

def cube_odd(arr):
    return sum(map(lambda