"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""

def change_date_format(date):
    return date[8:] + "-" + date[5:7] + "-" + date[:4]

print(change_date_format("2026-01-02"))
<file_sep>/python/0001_python_basics/0001_python_basics.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert find_largest([1, 2, 3, 4, 5]) == 5
"""

def find_largest(numbers):
    return max(numbers)

print(find_largest([1, 2, 3, 4, 5]))
<file_sep>/python/0002_python_basics/0002_python_basics.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert find_smallest([1, 2, 3, 4, 5]) == 1
"""

def find_smallest(numbers):
    return min(numbers)

print(find_smallest([1, 2, 3, 4, 5]))
<file_sep>/python/0003_python_basics/0003_python_basics.py
"""
Write a function that takes a list of numbers and returns the sum of all the numbers in the list.
assert sum_numbers([1, 2, 3, 4, 5]) == 15
"""

def sum_numbers(numbers):
    return sum(numbers)

print(sum_numbers([1, 2, 3, 4, 5]))
<file_sep>/python/0004_python_basics/0004_python_basics.py
"""
Write a function that takes a list of numbers and returns the average (mean) of all the numbers in the list.
assert average([1, 2, 3, 4, 5]) == 3
"""

def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))
<file_sep>/python/0005_python_basics/0005_python_basics.py
"""
Write a function that takes a list of numbers and returns the median of all the numbers in the list.
assert median([1, 2, 3, 4, 5]) == 3
"""

def median(numbers):
    numbers.sort()
    return numbers[len(numbers) // 2]

print(median([1, 2, 3, 4, 5]))
<file_sep>/python/0006_python_basics/0006_python_basics.py
"""
Write a function that takes a list of numbers and returns the mode of all the numbers in the list.
assert mode([1, 2, 3, 4, 5]) == 1
"""

def mode(numbers):
    return max(set(numbers), key=numbers.count)

print(mode([1, 2, 3, 4, 5]))
<file_sep>/python/0007_python_basics/0007_python_basics.py
"""
Write a function that takes a list of numbers and returns the range of all the numbers in the list.
assert range([1, 2, 3, 4, 5]) == 4
"""

def range(numbers):
    return max(numbers) - min(numbers)

print(range([1, 2, 3, 4, 5]))
<file_sep>/python/0008_python_basics/0008_python_basics.py
"""
Write a function that takes a list of numbers and returns the variance of all the numbers in the list.
assert variance([1, 2, 3, 4, 5]) == 2
"""

def variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

print(variance([1, 2, 3, 4, 5]))
<file_sep>/python