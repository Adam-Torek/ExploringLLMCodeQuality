"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""

def area_tetrahedron(a):
    return (a**2*sqrt(3))/4

print(area_tetrahedron(3))
/0001_python_basics/0001_python_basics.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.

assert sum_list([1, 2, 3, 4, 5]) == 15
"""

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list([1, 2, 3, 4, 5]))
/0003_python_basics/0003_python_basics.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.

assert largest_number([1, 2, 3, 4, 5]) == 5
"""

def largest_number(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

print(largest_number([1, 2, 3, 4, 5]))
/0002_python_basics/0002_python_basics.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.

assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_number([1, 2, 3, 4, 5]))
/0004_python_basics/0004_python_basics.py
"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.

assert average([1, 2, 3, 4, 5]) == 3
"""

def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

print(average([1, 2, 3, 4, 5]))
/0005_python_basics/0005_python_basics.py
"""
Write a function that takes a list of numbers and returns the median number.

assert median([1, 2, 3, 4, 5]) == 3
"""

def median(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[int(len(list)/2)] + list[int(len(list)/2) - 1])/2
    else:
        return list[int(len(list)/2)]

print(median([1, 2, 3, 4, 5]))
/0006_python_basics/0006_python_basics.py
"""
Write a function that takes a list of numbers and returns a list of the min and max numbers.

assert min_max([1, 2, 3, 4, 5]) == [1, 5]
"""

def min_max(list):
    list.sort()
    return [list[0], list[-1]]

print(min_max([1, 2, 3, 4, 5]))
/0007_python_basics/0007_python_basics.py
"""
Write a function that takes a list of numbers and returns a list of the min, max and mean numbers.

assert min_max_mean([1, 2, 3, 4, 5]) == [1, 5, 3]
"""

def min_max_mean(list):
    list.sort()
    return [list[0], list[-1], sum