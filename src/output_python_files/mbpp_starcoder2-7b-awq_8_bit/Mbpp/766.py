"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""

def pair_wise(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]

print(pair_wise([1,1,2,3,3,4,4,5]))
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
    if n < 10:
        return n
    else:
        return digital_root(sum([int(i) for i in str(n)]))

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
    return sum([i for i in range(1, n*2, 2)])

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
/python/codewars/7kyu/find_the_odd_int.py
"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
"""

def find_it(seq):
    return [i for i in seq if seq.count(i) % 2!= 0][0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
/python/codewars/7kyu/find_the_odd_int.py
"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
"""

def find_it(seq):
    return [i for i in seq if seq.count(i) % 2!= 0][0]

print(find_it([20