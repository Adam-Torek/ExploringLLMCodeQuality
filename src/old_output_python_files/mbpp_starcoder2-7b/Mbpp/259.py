"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""

def maximize_elements(tuple1, tuple2):
    """
    :param tuple1: tuple of tuples
    :param tuple2: tuple of tuples
    :return: tuple of tuples
    """
    return tuple(max(x, y) for x, y in zip(tuple1, tuple2))


if __name__ == '__main__':
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))))
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
    """
    :param n: int
    :return: int
    """
    return n if n < 10 else digital_root(sum(map(int, str(n))))


if __name__ == '__main__':
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))
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
    :param n: int
    :return: int
    """
    return sum(range(1, n * 2, 2))


if __name__ == '__main__':
    print(row_sum_odd_numbers(1))
    print(row_sum_odd_numbers(2))
    print(row_sum_odd_numbers(3))
    print(row_sum_odd_numbers(4))
    print(row_sum_odd_numbers(5))
<file_sep>/python/codewars/7kyu/sum_of_positive.py
"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    """
    :param arr: list of int
    :return: int
    """
    return sum(filter(lambda x: x > 0, arr))


if __name__ == '__main__':
    print(positive_sum([1, -4