"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(lst):
    """
    >>> max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])
    36
    """
    return max([a*b for a,b in lst])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
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
    """
    >>> digital_root(16)
    7
    >>> digital_root(942)
    6
    >>> digital_root(132189)
    6
    >>> digital_root(493193)
    2
    """
    return n if n < 10 else digital_root(sum([int(i) for i in str(n)]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
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
    """
    >>> row_sum_odd_numbers(1)
    1
    >>> row_sum_odd_numbers(2)
    8
    >>> row_sum_odd_numbers(3)
    21
    >>> row_sum_odd_numbers(4)
    45
    """
    return sum([i for i in range(1, 2*n, 2)])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/codewars/7kyu/find_the_odd_int.py
"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
"""

def find_it(seq):
    """
    >>> find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    5
    """
    return [i for i in seq if seq.count(i) % 2!= 0][0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/codewars/7kyu/find_the_odd_int.py
"""
Given an array, find the int that appears an odd number of times.

There will always