"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""

def intersection_array(a,b):
    return [x for x in a if x in b]

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]))/python/python_fundamentals/for_loop_basic2.py
"""
1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
"""

def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

print(biggie_size([-1, 3, 5, -5]))

"""
2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
Example: count_positives([-1, 1, 1, 1]) changes the original list to [-1, 1, 1, 3] and returns it
Example: count_positives([1, 6, -4, -2, -7, -2]) changes the list to [1, 6, -4, -2, -7, 2] and returns it
"""

def count_positives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr

print(count_positives([1, 6, -4, -2, -7, -2]))

"""
3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7
"""

def sum_total(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

"""
4. Average - Create a function that takes a list and returns the average of all the values.
Example: average([1,2,3,4]) should return 2.5
"""

def average(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum/len(arr)

print(average([1,2,3,4]))

"""
5. Length - Create a function that takes a list and returns the length of the list.
Example: length([37,2,1,-9]) should return 4
"""

def length(arr):
    return len(arr)

print(length([37,2,1,-9]))

"""
6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
Example: minimum([37,2,1,-9]) should return -9
Example: minimum([]) should return False
"""

def minimum(arr):
    if len(arr) == 0:
        return False
    else:
        min = arr[0]
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
        return min

print(minimum([37,2,1,-9]))
print(minimum([]))

"""
7. Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
Example: maximum([37,2,1,-9]) should return 37
Example: maximum([]) should return False
"""

def maximum