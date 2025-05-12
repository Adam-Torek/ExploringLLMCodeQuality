"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""

def max_length(lst):
    max_len = 0
    max_list = []
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
            max_list = i
    return max_len, max_list

print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
/python/python_fundamentals/for_loop_basic2.py
"""
1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
"""

def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst

print(biggie_size([-1, 3, 5, -5]))

"""
2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
Example: count_positives([-1, 1, 1, 1]) changes the original list to [-1, 1, 1, 3] and returns it
Example: count_positives([1, 6, -4, -2, -7, -2]) changes the list to [1, 6, -4, -2, -7, 2] and returns it
"""

def count_positives(lst):
    count = 0
    for i in lst:
        if i > 0:
            count += 1
    lst[len(lst)-1] = count
    return lst

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

"""
3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
Example: sum_total([1, 2, 3, 4]) should return 10
Example: sum_total([6, 3, -2]) should return 7
"""

def sum_total(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))

"""
4. Average - Create a function that takes a list and returns the average of all the values.
Example: average([1, 2, 3, 4]) should return 2.5
"""

def average(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum/len(lst)

print(average([1, 2, 3, 4]))

"""
5. Length - Create a function that takes a list and returns the length of the list.
Example: length([37, 2, 1, -9]) should return 4
Example: length([]) should return 0
"""

def length(lst):
    return len(lst)

print(length([37, 2, 1, -9]))
print(length([]))

"""
6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
Example: minimum([37, 2, 1, -9]) should return -9
Example: minimum([]) should return False
"""

def minimum(lst):
    if len(lst) == 0:
        return False
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min

print(minimum([37, 2, 1, -9]))
print(minimum([]))

"""