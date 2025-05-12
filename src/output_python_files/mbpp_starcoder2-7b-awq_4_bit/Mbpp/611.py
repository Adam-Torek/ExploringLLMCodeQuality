"""
Write a function which given a matrix represented as a list of lists returns the max of then'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""

def max_of_nth(matrix, n):
    return max(matrix[i][n] for i in range(len(matrix)))

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))
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
        return digital_root(sum(int(i) for i in str(n)))

print(digital_root(493193))
/python/codewars/7kyu/sum_of_odd_numbers.py
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
31    33    35    37    39
...
Calculate the row sums of this triangle from the row index (starting at index 1).

Example:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""

def row_sum_odd_numbers(n):
    return sum(range(1, 2 * n + 1, 2))

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
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
        return digital_root(sum(int(i) for i in str(n)))

print(digital_root(493193