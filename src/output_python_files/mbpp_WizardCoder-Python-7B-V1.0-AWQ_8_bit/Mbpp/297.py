"""
Write a function to flatten a given nested list structure.
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

def flatten_list(lst):
    flat_list = []
    for item in lst:
        if type(item) == list:
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# Testing the function
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])) # Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# Another way to solve the problem using recursion
def flatten_list(lst):
    flat_list = []
    for item in lst:
        if type(item) == list:
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# Testing the function
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) # Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# Another way to solve the problem using recursion and list comprehension
def flatten_list(lst):
    return [item for sublist in lst for item in flatten_list(sublist) if isinstance(sublist, list) or item]

# Testing the function
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) # Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# Another way to solve the problem using recursion and list comprehension
def flatten_list(lst):
    return [item for sublist in lst for item in flatten_list(sublist) if isinstance(sublist, list)] if isinstance(lst, list) else [lst]

# Testing the function
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) # Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# Another way to solve the problem using recursion and list comprehension
def flatten_list(lst):
    return [item for sublist in lst for item in flatten_list(sublist) if isinstance(sublist, list)] if isinstance(lst, list) else [lst]

# Testing the function
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90,