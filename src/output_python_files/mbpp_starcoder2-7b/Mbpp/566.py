"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""

def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

print(sum_digits(345))
/02_data_structures/02_lists/02_list_comprehensions.py
"""
List comprehensions are a way to create lists in a concise way.
"""

# Create a list of the first 10 square numbers
squares = [x**2 for x in range(10)]
print(squares)

# Create a list of the first 10 square numbers that are divisible by 3
squares_div_3 = [x**2 for x in range(10) if x**2 % 3 == 0]
print(squares_div_3)

# Create a list of the first 10 square numbers that are divisible by 3
# and are even
squares_div_3_even = [x**2 for x in range(10) if x**2 % 3 == 0 and x**2 % 2 == 0]
print(squares_div_3_even)

# Create a list of the first 10 square numbers that are divisible by 3
# and are even
# and are odd
squares_div_3_even_odd = [x**2 for x in range(10) if x**2 % 3 == 0 and x**2 % 2 == 0 and x**2 % 2 == 1]
print(squares_div_3_even_odd)
/02_data_structures/02_lists/01_list_basics.py
"""
Lists are a data structure that can hold multiple values.
"""

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Create a list of strings
strings = ["hello", "world"]
print(strings)

# Create a list of mixed types
mixed = [1, "hello", 2, "world"]
print(mixed)

# Create a list of lists
lists = [[1, 2, 3], [4, 5, 6]]
print(lists)

# Create a list of lists of lists
lists_of_lists = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
print(lists_of_lists)

# Create a list of lists of lists of lists
lists_of_lists_of_lists = [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], [[[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]]]
print(lists_of_lists_of_lists)

# Create a list of lists of lists of lists of lists
lists_of_lists_of_lists_of_lists = [[[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], [[[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]]], [[[[25, 26, 27], [28, 29, 30]], [[31, 32, 33], [34, 35, 36]]], [[[37, 38, 39], [40, 41, 42]], [[43, 44, 45], [46, 47, 48]]]]]
print(lists_of_lists_of_lists_of_lists)

# Create a list of lists of lists of lists of lists of lists
lists