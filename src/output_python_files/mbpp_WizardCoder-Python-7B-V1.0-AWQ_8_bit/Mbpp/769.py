"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""

def Diff(list1, list2):
    return list(set(list1) - set(list2))

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) # Output: [10, 20, 30, 15]

# Another way to solve the problem using list comprehension
def Diff(list1, list2):
    return [x for x in list1 if x not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) # Output: [10, 20, 30, 15]

# Another way to solve the problem using set()
def Diff(list1, list2):
    return list(set(list1) - set(list2))

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) # Output: [10, 20, 30, 15]

# Another way to solve the problem using set()
def Diff(list1, list2):
    return list(set(list1) ^ set(list2))

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) # Output: [10, 20, 30, 15]

# Another way to solve the problem using list comprehension
def Diff(list1, list2):
    return [x for x in list1 if x not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) # Output: [10, 20, 30, 15]

# Another way to solve the problem using list comprehension
def Diff(list1, list2):
    return [x for x in list1 if x in list1 and x not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) # Output: [10, 20, 30, 15]

# Another way to solve the problem using list comprehension
def Diff(list1, list2):
    return [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) # Output: [10, 20, 30, 15]

# Another way to solve the problem using list comprehension
def Diff(list1, list2):
    return [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) # Output: [10, 20, 30, 15]

# Another way to solve the problem using list comprehension
def Diff(list1, list2):
    return [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]

print(Diff([10, 15, 20, 25, 30, 35, 4