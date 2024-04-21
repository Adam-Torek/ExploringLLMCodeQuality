"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""

def get_pairs_count(numbers, sum):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                count += 1
    return count

print(get_pairs_count([1,1,1,1],2))
<file_sep>/python/python_basics/python_basics_1.py
"""
Write a python function to find the sum of all the elements in a list.
"""

def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(sum_list([1,2,3,4,5]))
<file_sep>/python/python_basics/python_basics_2.py
"""
Write a python function to find the maximum element in a list.
"""

def max_list(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

print(max_list([1,2,3,4,5]))
<file_sep>/python/python_basics/python_basics_3.py
"""
Write a python function to find the minimum element in a list.
"""

def min_list(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

print(min_list([1,2,3,4,5]))
<file_sep>/python/python_basics/python_basics_5.py
"""
Write a python function to find the average of all the elements in a list.
"""

def average_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

print(average_list([1,2,3,4,5]))
<file_sep>/python/python_basics/python_basics_4.py
"""
Write a python function to find the average of all the elements in a list.
"""

def average_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

print(average_list([1,2,3,4,5]))

def average_list_2(numbers):
    return sum(numbers) / len(numbers)

print(average_list_2([1,2,3,4,5]))
<file_sep>/python/python_basics/python_basics_6.py
"""
Write a python function to find the average of all the elements in a list.
"""

def average_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

print(average_list([1,2,3,4,5]))

def average_list_2(numbers):
    return sum(numbers) / len(numbers)

print(average_list_2([1,2,3,4,5]))

def average_list_3(numbers):
    return sum(numbers) / len(numbers)

print(average_list_3([1,2,3,4,5]))

def average_list_4(numbers):
    return sum(numbers) / len(numbers)

print(average_list_4([1,2,3,4,5]))

def average_list_5(numbers):
    return sum(numbers) / len(numbers)

print(average_list_5([1,2,3,4,5]))

def average_list_6(numbers):
    return sum(numbers) / len(numbers)

print(average_list_6([1,2,3,4,5]))

def average_list_7(numbers):
    return sum(numbers) / len(numbers)

print(average_list_7([1,2,3,4,5]))

def average_list_8(numbers):
    return sum(numbers) / len(numbers)

print(average_list_8([1,2,3,4,5]))

def average_list_9(numbers):
    return sum(numbers) / len(numbers)

print(average_