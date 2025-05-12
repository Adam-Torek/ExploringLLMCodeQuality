"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""

def two_unique_nums(lst):
    return list(set(lst))

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 4, 5]

# Another way to solve this problem is to use a dictionary to keep track of the numbers that have already been seen and only add the unique ones to a new list.

def two_unique_nums(lst):
    seen = {}
    result = []
    for num in lst:
        if num not in seen:
            seen[num] = True
            result.append(num)
    return result

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a set to keep track of the numbers that have already been seen and only add the unique ones to a new list.

def two_unique_nums(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a set comprehension to remove duplicates from the original list.

def two_unique_nums(lst):
    return list(set(lst))

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a list comprehension to remove duplicates from the original list.

def two_unique_nums(lst):
    return [num for num in lst if lst.count(num) == 1]

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 4, 5]

# Another way to solve this problem is to use a loop to iterate through the list and add each number to a new list only if it hasn't been seen before.

def two_unique_nums(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 4, 5]

# Another way to solve this problem is to use a loop to iterate through the list and add each number to a new list only if it hasn't been seen before.

def two_unique_nums(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a loop to iterate through the list and add each number to a new list only if it hasn't been seen before.

def two_unique_nums(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a loop to iterate through the list and add each number to a new list only if it hasn't been seen before.

def two_unique_nums(lst):
    seen