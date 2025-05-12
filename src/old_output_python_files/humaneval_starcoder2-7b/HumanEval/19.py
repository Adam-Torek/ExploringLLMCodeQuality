from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

#     numbers = numbers.split()
#     numbers.sort()
#     return''.join(numbers)

    return''.join(sorted(numbers.split()))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE DOING GREAT!\n")
<file_sep>/python/codewars/7kyu/sum_of_digits_digital_root.py
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
    return digital_root(sum(int(i) for i in str(n)))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE DOING GREAT!\n")
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
    """
    >>> row_sum_odd_numbers(1)
    1
    >>> row_sum_odd_numbers(2)
    8
    >>> row_sum_odd_numbers(3)
    27
    >>> row_sum_odd_numbers(4)
    64
    """
    return sum(i for i in range(1, n * 2, 2))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE DOING GREAT!\n")
<file_sep>/python/codewars/7kyu/sum_of_positive.py
"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""


def positive_sum(arr):
    """
    >>> positive_sum([1, 2, 3, 4, 5])
    15
    >>> positive_sum([1, -2, 3, 4, 5])
    1