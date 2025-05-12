"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""

def union_elements(tuple1, tuple2):
    return sorted(set(tuple1 + tuple2))

print(union_elements((3, 4, 5, 6),(5, 7, 4, 10) ))
/python_basics/python_basics_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1, 2, 3, 4, 5]) == 15
"""

def sum_numbers(list_of_numbers):
    return sum(list_of_numbers)

print(sum_numbers([1, 2, 3, 4, 5]))
/python_basics/python_basics_10.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1, 2, 3, 4, 5]) == 5
"""

def largest_number(list_of_numbers):
    return max(list_of_numbers)

print(largest_number([1, 2, 3, 4, 5]))
/python_basics/python_basics_11.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(list_of_numbers):
    return min(list_of_numbers)

print(smallest_number([1, 2, 3, 4, 5]))
/python_basics/python_basics_12.py
"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.
assert average([1, 2, 3, 4, 5]) == 3
"""

def average(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)

print(average([1, 2, 3, 4, 5]))
/python_basics/python_basics_13.py
"""
Write a function that takes a list of numbers and returns the median of the numbers.
assert median([1, 2, 3, 4, 5]) == 3
"""

def median(list_of_numbers):
    list_of_numbers.sort()
    if len(list_of_numbers) % 2 == 0:
        return (list_of_numbers[len(list_of_numbers) // 2] + list_of_numbers[len(list_of_numbers) // 2 - 1]) / 2
    else:
        return list_of_numbers[len(list_of_numbers) // 2]

print(median([1, 2, 3, 4, 5]))
/python_basics/python_basics_14.py
"""
Write a function that takes a list of numbers and returns the mode of the numbers.
assert mode([1, 2, 3, 4, 5]) == 1
"""

def mode(list_of_numbers):
    return max(set(list_of_numbers), key = list_of_numbers.count)

print(mode([1, 2, 3, 4, 5]))
/python_basics/python_basics_15.py
"""
Write a function that takes a list of numbers and returns the variance of the numbers.
assert variance([1, 2, 3, 4, 5]) == 2.5
"""

def variance(list_of_numbers):
    return sum((x - sum(list_of_numbers) / len(list_of_numbers)) ** 2 for x in list_of_numbers) / len(list_of_numbers)

print(variance([1, 2, 3, 4, 5]))
/python_basics/python_basics_16.py
"""
Write a function that takes a list of numbers and returns the standard deviation of