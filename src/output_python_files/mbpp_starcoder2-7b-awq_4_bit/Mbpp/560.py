"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""

def union_elements(tup1, tup2):
    return sorted(set(tup1 + tup2))

print(union_elements((3, 4, 5, 6),(5, 7, 4, 10) ))
/python_basics/python_basics_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1, 2, 3, 4, 5]) == 15
"""

def sum_numbers(numbers):
    return sum(numbers)

print(sum_numbers([1, 2, 3, 4, 5]))
/python_basics/python_basics_10.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1, 2, 3, 4, 5]) == 5
"""

def largest_number(numbers):
    return max(numbers)

print(largest_number([1, 2, 3, 4, 5]))
/python_basics/python_basics_12.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(numbers):
    return min(numbers)

print(smallest_number([1, 2, 3, 4, 5]))
/python_basics/python_basics_11.py
"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.
assert average([1, 2, 3, 4, 5]) == 3
"""

def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))
/python_basics/python_basics_13.py
"""
Write a function that takes a list of numbers and returns the median of the numbers.
assert median([1, 2, 3, 4, 5]) == 3
"""

def median(numbers):
    numbers.sort()
    return numbers[len(numbers) // 2]

print(median([1, 2, 3, 4, 5]))
/python_basics/python_basics_14.py
"""
Write a function that takes a list of numbers and returns the mode of the numbers.
assert mode([1, 2, 3, 4, 5]) == 5
"""

def mode(numbers):
    return max(set(numbers), key=numbers.count)

print(mode([1, 2, 3, 4, 5]))
/python_basics/python_basics_15.py
"""
Write a function that takes a list of numbers and returns the range of the numbers.
assert range([1, 2, 3, 4, 5]) == 4
"""

def range(numbers):
    return max(numbers) - min(numbers)

print(range([1, 2, 3, 4, 5]))
/python_basics/python_basics_16.py
"""
Write a function that takes a list of numbers and returns the variance of the numbers.
assert variance([1, 2, 3, 4, 5]) == 2.5
"""

def variance(numbers):
    return sum((x - sum(numbers) / len(numbers)) ** 2 for x in numbers) / len(numbers)

print(variance([1, 2, 3, 4, 5]))
/python_basics/python_basics_17.py
"""
Write a function that takes a list of numbers and returns the standard deviation of the numbers.
assert standard_deviation([1, 2, 3, 4, 5]) == 1.5811388300841898
"""

def standard_deviation(