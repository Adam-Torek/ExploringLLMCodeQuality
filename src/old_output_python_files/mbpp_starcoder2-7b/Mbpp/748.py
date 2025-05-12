"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""

def capital_words_spaces(string):
    return string

print(capital_words_spaces("Python"))
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
    return n

print(digital_root(16))
<file_sep>/python/codewars/7kyu/sum_of_odd_cubed_numbers.py
"""
Find the sum of the odd numbers within an array, after cubing the initial integers.
For example, the array [1, 2, 3, 4] becomes 1^3 + 3^3 + 5^3 + 7^3 = 27.
"""

def cube_odd(arr):
    return sum(i**3 for i in arr if i % 2!= 0)

print(cube_odd([1, 2, 3, 4]))
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
    return sum(i for i in range(1, n*2, 2))

print(row_sum_odd_numbers(1))
<file_sep>/python/codewars/7kyu/sum_of_a_sequence.py
"""
Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, function should returns 0

Examples

sequence_sum(2,2,2) === 2
sequence_sum(2,6,2) === 12 // 2 + 4 + 6
sequence_sum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
sequence_sum(1,5,3) === 5 // 1 + 4
"""

def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))

print(sequence_sum(2, 6, 2))
<file_sep>/python/codewars/7kyu/sum_of_positive.py
"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    return sum(i for i in arr if i > 0)