"""
Write a function to remove all elements from a given list present in another list.
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
"""

def remove_elements(list1, list2):
    return [x for x in list1 if x not in list2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])) # [1, 3, 5, 7, 9, 10]

# or

def remove_elements(list1, list2):
    return list(set(list1) - set(list2))

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])) # [1, 3, 5, 7, 9, 10]

# or

def remove_elements(list1, list2):
    return [x for x in list1 if x not in list2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])) # [1, 3, 5, 7, 9, 10]

# or

def remove_elements(list1, list2):
    return list(filter(lambda x: x not in list2, list1))

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])) # [1, 3, 5, 7, 9, 10]

# or

def remove_elements(list1, list2):
    return [x for x in list1 if x not in list2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])) # [1, 3, 5, 7, 9, 10]

# or

def remove_elements(list1, list2):
    return [x for x in list1 if x not in list2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])) # [1, 3, 5, 7, 9, 10]

# or

def remove_elements(list1, list2):
    return list(set(list1) - set(list2))

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])) # [1, 3, 5, 7, 9, 10]

# or

def remove_elements(list1, list2):
    return list(filter(lambda x: x not in list2, list1)

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])) # [1, 3, 5, 7, 9, 10]

# or

def remove_elements(list1, list2):
    return list(set(list1) - set(list2))

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) # [1, 3, 5, 7, 9, 10]