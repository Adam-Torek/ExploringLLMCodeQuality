"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""

def Find_Max(lst):
    max_length = 0
    max_element = []
    for i in lst:
        if len(i) > max_length:
            max_length = len(i)
            max_element = i
    return max_element

print(Find_Max([['A'],['A','B'],['A','B','C']]))

# Output: ['A','B','C']

# Time Complexity: O(n)
# Space Complexity: O(1)

# We can also use the max() function to find the maximum length element in the list and return it.

def Find_Max(lst):
    return max(lst, key=len)

print(Find_Max([['A'],['A','B'],['A','B','C']]))

# Output: ['A','B','C']

# Time Complexity: O(n)
# Space Complexity: O(1)

# We can also use a loop to iterate through the list and find the maximum length element.

def Find_Max(lst):
    max_length = 0
    max_element = []
    for i in lst:
        if len(i) > max_length:
            max_length = len(i)
            max_element = i
    return max_element

print(Find_Max([['A'],['A','B'],['A','B','C']])

# Output: ['A','B','C']

# Time Complexity: O(n)
# Space Complexity: O(1)

# We can also use a list comprehension to find the maximum length element in the list.

def Find_Max(lst):
    return [i for i in lst if len(i) == max([len(j) for j in lst])][0]

print(Find_Max([['A'],['A','B'],['A','B','C']])

# Output: ['A','B','C']

# Time Complexity: O(n)
# Space Complexity: O(n)

# All the above methods will return the maximum length element in the list.