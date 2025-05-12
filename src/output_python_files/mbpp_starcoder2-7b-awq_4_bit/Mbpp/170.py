"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""

def sum_range_list(lst, start, end):
    """
    :param lst: list of numbers
    :param start: start index
    :param end: end index
    :return: sum of numbers in range
    """
    return sum(lst[start:end+1])

assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
/python/list_comprehension.py
"""
List comprehension is a way to create lists in a single line.
"""

# Example 1
# Create a list of numbers from 1 to 10
numbers = [i for i in range(1, 11)]
print(numbers)

# Example 2
# Create a list of squares of numbers from 1 to 10
squares = [i**2 for i in range(1, 11)]
print(squares)

# Example 3
# Create a list of even numbers from 1 to 10
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

# Example 4
# Create a list of odd numbers from 1 to 10
odd_numbers = [i for i in range(1, 11) if i % 2!= 0]
print(odd_numbers)

# Example 5
# Create a list of numbers from 1 to 100 which are divisible by 3
divisible_by_3 = [i for i in range(1, 101) if i % 3 == 0]
print(divisible_by_3)

# Example 6
# Create a list of numbers from 1 to 100 which are divisible by 3 and 5
divisible_by_3_and_5 = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(divisible_by_3_and_5)

# Example 7
# Create a list of numbers from 1 to 100 which are divisible by 3 or 5
divisible_by_3_or_5 = [i for i in range(1, 101) if i % 3 == 0 or i % 5 == 0]
print(divisible_by_3_or_5)

# Example 8
# Create a list of numbers from 1 to 100 which are divisible by 3 and not 5
divisible_by_3_not_5 = [i for i in range(1, 101) if i % 3 == 0 and i % 5!= 0]
print(divisible_by_3_not_5)

# Example 9
# Create a list of numbers from 1 to 100 which are divisible by 3 or not 5
divisible_by_3_or_not_5 = [i for i in range(1, 101) if i % 3 == 0 or i % 5!= 0]
print(divisible_by_3_or_not_5)

# Example 10
# Create a list of numbers from 1 to 100 which are divisible by 3 and 5 or 7
divisible_by_3_5_or_7 = [i for i in range(1, 101) if i % 3 == 0 and (i % 5 == 0 or i % 7 == 0)]
print(divisible_by_3_5_or_7)

# Example 11
# Create a list of numbers from 1 to 100 which are divisible by 3 and 5 and not 7
divisible_by_3_5_not_7 = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0 and i % 7!=