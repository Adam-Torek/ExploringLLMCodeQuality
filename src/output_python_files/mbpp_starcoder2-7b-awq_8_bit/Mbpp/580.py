"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

def extract_even(nested_tuple):
    """
    >>> extract_even((4, 5, (7, 6, (2, 4)), 6, 8))
    (4, (6, (2, 4)), 6, 8)
    """
    return tuple(extract_even(item) if isinstance(item, tuple) else item for item in nested_tuple if item % 2 == 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/for_loop_basic2.py
"""
Basic - Print and Count

Print all integers from 0 to 1000.
Use a for loop to print numbers 0 to 1000.

Print all the multiples of 5 from 5 to 1,000,000.
Use a for loop to print multiples of 5 from 5 to 1,000,000.

Print integers 1 to 100. Skip 5 and 6.
Use a for loop to print integers 1 to 100, skipping 5 and 6.

Print all the multiples of 5 from 5 to 1,000,000.
Use a for loop to print the multiples of 5 from 5 to 1,000,000.

Print the sum of all integers from 0 to 100.
Use a for loop to print the sum of all integers from 0 to 100.

Print the sum of all multiples of 5 from 5 to 1,000,000.
Use a for loop to print the sum of all multiples of 5 from 5 to 1,000,000.
"""

def print_and_count():
    for i in range(0, 1001):
        print(i)

def print_multiples_of_5():
    for i in range(5, 1000001, 5):
        print(i)

def print_skip_5_and_6():
    for i in range(1, 101):
        if i % 5 == 0 or i % 6 == 0:
            continue
        print(i)

def print_multiples_of_5_from_5_to_1000000():
    sum = 0
    for i in range(5, 1000001, 5):
        sum += i
    print(sum)

def print_sum_of_all_integers_from_0_to_100():
    sum = 0
    for i in range(0, 101):
        sum += i
    print(sum)

def print_sum_of_all_multiples_of_5_from_5_to_1000000():
    sum = 0
    for i in range(5, 1000001, 5):
        sum += i
    print(sum)

if __name__ == '__main__':
    print_and_count()
    print_multiples_of_5()
    print_skip_5_and_6()
    print_multiples_of_5_from_5_to_1000000()
    print_sum_of_all_integers_from_0_to_100()
    print_sum_of_all_multiples_of_5_from_5_to_1000000()
/python/python_fundamentals/for_loop_basic1.py
"""
Basic - Basic: For Loop Basics I

Basic - Basic: For Loop Basics I

Print all integers from 0 to 150.
Use a for loop to print integers from 0 to 150.

Print all the multiples of 5 from 0 to 1,000.
Use a for loop to print multiples of 5 from 0 to 1,000.

Print integers from 200 to 500