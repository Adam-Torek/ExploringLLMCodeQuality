"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""

def filter_data(data, min_height, min_weight):
    return {k:v for k,v in data.items() if v[0] > min_height and v[1] > min_weight}

print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))/python_basics/python_basics_1/task_1_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
"""

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1,2,3,4,5]))/python_basics/python_basics_1/task_1_3.py
"""
Write a function that takes a list of numbers and returns the largest number.
"""

def max_list(numbers):
    return max(numbers)

print(max_list([1,2,3,4,5]))/python_basics/python_basics_1/task_1_2.py
"""
Write a function that takes a list of numbers and returns the smallest number.
"""

def min_list(numbers):
    return min(numbers)

print(min_list([1,2,3,4,5]))/python_basics/python_basics_1/task_1_4.py
"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.
"""

def average_list(numbers):
    return sum(numbers)/len(numbers)

print(average_list([1,2,3,4,5]))/python_basics/python_basics_1/task_1_5.py
"""
Write a function that takes a list of numbers and returns a list with the min, max, sum and average values.
"""

def min_max_sum_average(numbers):
    return [min(numbers), max(numbers), sum(numbers), sum(numbers)/len(numbers)]

print(min_max_sum_average([1,2,3,4,5]))/python_basics/python_basics_1/task_1_6.py
"""
Write a function that takes a list of numbers and returns a list of the min, max, sum and average values.
"""

def min_max_sum_average(numbers):
    return [min(numbers), max(numbers), sum(numbers), sum(numbers)/len(numbers)]

print(min_max_sum_average([1,2,3,4,5]))/python_basics/python_basics_1/task_1_7.py
"""
Write a function that takes a list of numbers and returns a list of the min, max, sum and average values.
"""

def min_max_sum_average(numbers):
    return [min(numbers), max(numbers), sum(numbers), sum(numbers)/len(numbers)]

print(min_max_sum_average([1,2,3,4,5]))/python_basics/python_basics_1/task_1_8.py
"""
Write a function that takes a list of numbers and returns a list of the min, max, sum and average values.
"""

def min_max_sum_average(numbers):
    return [min(numbers), max(numbers), sum(numbers), sum(numbers)/len(numbers)]

print(min_max_sum_average([1,2,3,4,5]))/python_basics/python_basics_1/task_1_9.py
"""