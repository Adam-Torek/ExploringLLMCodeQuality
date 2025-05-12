"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""

def count_first_elements(tuple):
    count = 0
    for i in tuple:
        if type(i) == tuple:
            count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10)))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1, 2, 3]) == 6
"""

def sum_numbers(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_numbers([1, 2, 3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a function that takes a list of numbers and returns the largest number.
assert largest_number([1, 2, 3]) == 3
"""

def largest_number(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

print(largest_number([1, 2, 3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a function that takes a list of numbers and returns the smallest number.
assert smallest_number([1, 2, 3]) == 1
"""

def smallest_number(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_number([1, 2, 3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.
assert average([1, 2, 3]) == 2
"""

def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

print(average([1, 2, 3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a function that takes a list of numbers and returns the median of the numbers.
assert median([1, 2, 3]) == 2
"""

def median(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[int(len(list) / 2)] + list[int(len(list) / 2) - 1]) / 2
    else:
        return list[int(len(list) / 2)]

print(median([1, 2, 3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a function that takes a list of numbers and returns the mode of the numbers.
assert mode([1, 2, 3]) == 1
"""

def mode(list):
    count = 0
    for i in list:
        if list.count(i) > count:
            count = list.count(i)
            mode = i
    return mode

print(mode([1, 2, 3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a function that takes a list of numbers and returns the range of the numbers.
assert range([1, 2, 3]) == 2
"""

def range(list):
    list.sort()
    return list[len(list) - 1] - list[0]

print(range([1, 2, 3]))
/Python/Python_Basics/Python_Basics_1/Python