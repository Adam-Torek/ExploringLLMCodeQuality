"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""

def freq_count(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))
/python/python_fundamentals/fundamentals/fundamentals_1.py
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
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7
"""

def sum_total(lst):
    total = 0
    for i in lst:
        total += i
    return total

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

"""
4. Average - Create a function that takes a list and returns the average of all the values.x
Example: average([1,2,3,4]) should return 2.5
"""

def average(lst):
    total = 0
    for i in lst:
        total += i
    return total/len(lst)

print(average([1,2,3,4]))

"""
5. Length - Create a function that takes a list and returns the length of the list.
Example: length([37,2,1,-9]) should return 4
Example: length([]) should return 0
"""

def length(lst):
    return len(lst)

print(length([37,2,1,-9]))
print(length([]))

"""
6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
Example: minimum([37,2,1,-9]) should return -9
Example: minimum([]) should return False
"""

def minimum(lst):
    if len(lst) == 0:
        return False
    else:
        min = lst[0]
        for i in lst:
            if i < min:
                min = i
        return min

print(minimum([37,2,1,-9]))