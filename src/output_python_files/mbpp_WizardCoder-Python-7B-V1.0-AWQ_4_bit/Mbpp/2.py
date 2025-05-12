"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    return set(list1) & set(list2)

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve this problem is to use a loop to iterate through each element in the first list and check if it exists in the second list. If it does, add it to a new list. Then return the new list.

def similar_elements(list1, list2):
    shared_elements = []
    for element in list1:
        if element in list2:
            shared_elements.append(element)
    return set(shared_elements)

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: {4, 5}

# Another way to solve this problem is to use a loop to iterate through each element in the first list and check if it exists in the second list using the 'in' keyword. If it does, add it to a new list. Then return the new list.

def similar_elements(list1, list2):
    shared_elements = []
    for element in list1:
        if element in list2:
            shared_elements.append(element)
    return shared_elements

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: [4, 5]

# This will return a list of the shared elements, but we can convert it to a set using the set() function to get the same output as the first solution.