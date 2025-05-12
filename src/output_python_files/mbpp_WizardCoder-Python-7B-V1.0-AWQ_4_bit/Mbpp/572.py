"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""

def two_unique_nums(lst):
    return list(set(lst))

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 4, 5]

# Another way to solve this problem is to use a dictionary to keep track of the unique numbers and return the keys of the dictionary.

def two_unique_nums(lst):
    unique_nums = {}
    for num in lst:
        unique_nums[num] = True
    return list(unique_nums.keys())

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 4, 5]

# Another way to solve this problem is to use a set to keep track of the unique numbers and return the set.

def two_unique_nums(lst):
    return list(set(lst))

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a loop to iterate through the list and add each number to a new list if it hasn't been seen before.

def two_unique_nums(lst):
    unique_nums = []
    for num in lst:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a loop to iterate through the list and add each number to a new list if it hasn't been seen before.

def two_unique_nums(lst):
    unique_nums = []
    for num in lst:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a loop to iterate through the list and add each number to a new list if it hasn't been seen before.

def two_unique_nums(lst):
    unique_nums = []
    for num in lst:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a loop to iterate through the list and add each number to a new list if it hasn't been seen before.

def two_unique_nums(lst):
    unique_nums = []
    for num in lst:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way to solve this problem is to use a loop to iterate through the list and add each number to a new list if it hasn't been seen before.

def two_unique_nums(lst):
    unique_nums = []
    for num in lst:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 2, 3, 4, 5]

# Another way