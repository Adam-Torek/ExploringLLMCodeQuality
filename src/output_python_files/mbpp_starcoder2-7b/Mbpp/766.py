"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""

def pair_wise(lst):
    return [(lst[i],lst[i+1]) for i in range(len(lst)-1)]

print(pair_wise([1,1,2,3,3,4,4,5]))
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
    if n < 10:
        return n
    else:
        return digital_root(sum([int(i) for i in str(n)]))

print(digital_root(132189))
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
    return sum([i for i in range(1,n*2,2)])

print(row_sum_odd_numbers(1))
<file_sep>/python/codewars/7kyu/sum_of_positive.py
"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    return sum([i for i in arr if i > 0])

print(positive_sum([1,-4,7,12]))
<file_sep>/python/codewars/7kyu/sum_of_odd_cubed_numbers.py
"""
Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/null if any of the values aren't numbers.

Note: there are no arrays of null/None/undefined.

Example
sum_of_cubed_odds([2, 4, 6, 8]) # should return 78 (2 + 3 + 4 + 5)
sum_of_cubed_odds([1, 2, 10]) # should return 1099
"""

def sum_of_cubed_odds(lst):
    return sum([i**3 for i in lst if i % 2!= 0])

print(sum_of_cubed_odds([2, 4, 6, 8]))
<file_sep>/python/codewars/7kyu/sum_of_digits