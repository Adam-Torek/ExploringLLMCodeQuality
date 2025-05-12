"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""

def difference(n):
    return sum([i**3 for i in range(1,n+1)]) - sum([i for i in range(1,n+1)])**2

print(difference(3))/python/codewars/7kyu/sum_of_digits_digital_root.py
"""
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

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
    if n < 10:
        return n
    else:
        return digital_root(sum([int(i) for i in str(n)]))

print(digital_root(132189))/python/codewars/7kyu/sum_of_odd_numbers.py
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
    return sum([i for i in range(1,n*2,2)])

print(row_sum_odd_numbers(1))/python/codewars/7kyu/find_the_odd_int.py
"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2!= 0:
            return i

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))/python/codewars/7kyu/find_the_unique_number.py
"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
"""

def find_uniq(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))/python/codewars/7kyu/find_the_odd_int.py
"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

def find_it(seq):
    return [i for i in seq if seq.count(i) % 2!= 0][0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,