"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""

def neg_nos(lst):
    return [num for num in lst if num < 0]

print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]
print(neg_nos([1,2,3,4,5,6])) # Output: []
print(neg_nos([-5,-3,-2,-4,-1])) # Output: [-5, -3, -2, -4, -1]

# Another way to solve the problem using list comprehension
def neg_nos(lst):
    return [num for num in lst if num < 0]

print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]
print(neg_nos([1,2,3,4,5,6])) # Output: []
print(neg_nos([-5,-3,-2,-4,-1])) # Output: [-5, -3, -2, -4, -1]

# Another way to solve the problem using filter() and lambda function
def neg_nos(lst):
    return list(filter(lambda x: x < 0, lst))

print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]
print(neg_nos([1,2,3,4,5,6])) # Output: []
print(neg_nos([-5,-3,-2,-4,-1])) # Output: [-5, -3, -2, -4, -1]

# Another way to solve the problem using map() and lambda function
def neg_nos(lst):
    return list(map(lambda x: x, filter(lambda x: x < 0, lst))

print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]
print(neg_nos([1,2,3,4,5,6])) # Output: []
print(neg_nos([-5,-3,-2,-4,-1])) # Output: [-5, -3, -2, -4, -1]

# Another way to solve the problem using set()
def neg_nos(lst):
    return list(set([num for num in lst if num < 0])

print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]
print(neg_nos([1,2,3,4,5,6])) # Output: []
print(neg_nos([-5,-3,-2,-4,-1])) # Output: [-5, -3, -2, -4, -1]

# Another way to solve the problem using set() and lambda function
def neg_nos(lst):
    return list(set(filter(lambda x: x < 0, lst))

print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]
print(neg_nos([1,2,3,4,5,6])) # Output: []
print(neg_nos([-5,-3,-2,-4,-1])) # Output: [-5, -3, -2, -4, -1]

# Another way to solve the problem using set() and list comprehension
def neg_nos(lst):
    return list(set([num for num in lst if num < 0])

print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]
print(neg_nos([1,2,3,4,5,6])) # Output: []
print(neg_nos([-5,-3,-2,-4,-1])) # Output: [-5, -3, -2, -4, -1]

# Another way to solve the problem using set() and lambda function
def neg_nos(lst):
    return list(set(filter(lambda x: x < 0, lst))

print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]
print(neg_nos([1,2,3,4,5,6])) # Output: []
print(neg_nos([-5,-3,-2,-4,-1]))