"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""

def extract_nth_element(list_of_tuples, n):
    return [x[n] for x in list_of_tuples]

assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
/python/python_fundamentals/for_loop_basic2.py
"""
1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
"""

def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

print(biggie_size([-1, 3, 5, -5]))

"""
2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
Example: count_positives([-1, 1, 1, 1]) changes the original list to [-1, 1, 1, 3] and returns it
Example: count_positives([1, 6, -4, -2, -7, -2]) changes the list to [1, 6, -4, -2, -7, 2] and returns it
"""

def count_positives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count += 1
    list[len(list)-1] = count
    return list

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

"""
3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7
"""

def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

"""
4. Average - Create a function that takes a list and returns the average of all the values.
Example: average([1,2,3,4]) should return 2.5
"""

def average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)

print(average([1,2,3,4]))

"""
5. Length - Create a function that takes a list and returns the length of the list.
Example: length([37,2,1,-9]) should return 4
"""

def length(list):
    return len(list)

print(length([37,2,1,-9]))

"""
6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
Example: minimum([37,2,1,-9]) should return -9
Example: minimum([]) should return False
"""

def minimum(list):
    if len(list) == 0:
        return False
    else: