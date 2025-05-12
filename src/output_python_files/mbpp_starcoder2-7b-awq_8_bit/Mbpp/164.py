"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""

def are_equivalent(a, b):
    """
    >>> are_equivalent(36, 57)
    False
    >>> are_equivalent(36, 36)
    True
    """
    return sum_divisors(a) == sum_divisors(b)

def sum_divisors(n):
    """
    >>> sum_divisors(36)
    57
    >>> sum_divisors(57)
    36
    """
    return sum(divisors(n))

def divisors(n):
    """
    >>> divisors(36)
    [1, 2, 3, 4, 6, 9, 12, 18, 36]
    >>> divisors(57)
    [1, 3, 9, 13, 39, 57]
    """
    return [i for i in range(1, n+1) if n % i == 0]

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
    if n < 10:
        return n
    else:
        return digital_root(sum([int(i) for i in str(n)]))

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
    return sum([i for i in range(1, n*2, 2)])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/codewars/7kyu/find_the_odd_int.py
"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) ==