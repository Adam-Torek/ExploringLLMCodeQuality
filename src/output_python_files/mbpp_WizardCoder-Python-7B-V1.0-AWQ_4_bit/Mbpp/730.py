"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""

def consecutive_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            result.append(lst[i])
        else:
            continue
    return result

# Testing the function
print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

# Another way to solve the problem using set() and list()
def remove_consecutive_duplicates(lst):
    return list(set(lst))

# Testing the function
print(remove_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Another way to solve the problem using list comprehension
def remove_consecutive_duplicates_list_comprehension(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]

# Testing the function
print(remove_consecutive_duplicates_list_comprehension([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

# Another way to solve the problem using itertools.groupby()
from itertools import groupby
def remove_consecutive_duplicates_groupby(lst):
    return [key for key, _ in groupby(lst)]

# Testing the function
print(remove_consecutive_duplicates_groupby([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

# Another way to solve the problem using itertools.groupby() and list comprehension
from itertools import groupby
def remove_consecutive_duplicates_groupby_list_comprehension(lst):
    return [key for key, _ in groupby(lst)]

# Testing the function
print(remove_consecutive_duplicates_groupby_list_comprehension([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

# Another way to solve the problem using itertools.groupby() and filter()
from itertools import groupby
def remove_consecutive_duplicates_groupby_filter(lst):
    return list(filter(lambda x: x[0], groupby(lst)))

# Testing the function
print(remove_consecutive_duplicates_groupby_filter([0, 0, 1, 2, 3, 4, 4, 5, 6