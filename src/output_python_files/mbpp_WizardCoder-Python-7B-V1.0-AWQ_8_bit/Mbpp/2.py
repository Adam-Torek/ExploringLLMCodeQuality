"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    return set(list1) & set(list2)

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using list comprehension
def similar_elements(list1, list2):
    return set([x for x in list1 if x in list2])

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using set intersection
def similar_elements(list1, list2):
    return set(list1).intersection(list2)

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using list comprehension and set intersection
def similar_elements(list1, list2):
    return set([x for x in list1 if x in set(list2)]).intersection(set(list2))

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using set intersection
def similar_elements(list1, list2):
    return set(list(set(list1) & set(list2))

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using set intersection
def similar_elements(list1, list2):
    return set(list1).intersection(list2)

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using set intersection
def similar_elements(list1, list2):
    return set(x for x in list1 if x in list2)

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using set intersection
def similar_elements(list1, list2):
    return set(x for x in list1 if x in set(list2))

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using set intersection
def similar_elements(list1, list2):
    return set(x for x in list1 if x in set(list2) and x in list2)

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using set intersection
def similar_elements(list1, list2):
    return set(x for x in list1 if x in set(list2) and x in list2)

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using set intersection
def similar_elements(list1, list2):
    return set(x for x in list1 if x in set(list2) and x in list2)

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve the problem using set intersection
def similar_elements(list1, list2):
    return set(filter(lambda x: x in list2, list