"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""

def count(lst):
    count = 0
    for i in lst:
        if i == True:
            count += 1
    return count

# Test cases
print(count([True,False,True])) # Output: 2
print(count([True,True,True,False])) # Output: 3
print(count([False,False,False])) # Output: 0
print(count([True,True,True,True,True,True,True])) # Output: 5
print(count([False,False,False,False,False,False])) # Output: 0
print(count([False,True,False,True,False,True])) # Output: 2

# Another way to solve this problem using list comprehension
def count_true(lst):
    return len([i for i in lst if i == True])

# Test cases
print(count_true([True,False,True])) # Output: 2
print(count_true([True,True,True,False])) # Output: 3
print(count_true([False,False,False])) # Output: 0
print(count_true([True,True,True,True,True,True])) # Output: 5
print(count_true([False,False,False,False,False,False])) # Output: 0
print(count_true([False,True,False,True,False,True])) # Output: 2