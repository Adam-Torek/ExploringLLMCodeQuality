"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""

def remove_odd(lst):
    return [num for num in lst if num % 2 == 0]

print(remove_odd([1,2,3])) # Output: [2]
print(remove_odd([1,3,5,4,6,8,9,7])) # Output: [4, 6, 8]
print(remove_odd([2,4,6,8])) # Output: [2, 4, 6, 8]
print(remove_odd([])) # Output: []

# Another way to solve this problem using list comprehension
def remove_odd_list_comp(lst):
    return [num for num in lst if num % 2 != 0]

print(remove_odd_list_comp([1,2,3])) # Output: []
print(remove_odd_list_comp([1,3,5,4,6,8,9,7])) # Output: [4, 6, 8]
print(remove_odd_list_comp([2,4,6,8])) # Output: [2, 4, 6, 8]
print(remove_odd_list_comp([])) # Output: []

# Another way to solve this problem using filter() function
def remove_odd_filter(lst):
    return list(filter(lambda num: num % 2 == 0, lst))

print(remove_odd_filter([1,2,3])) # Output: [2]
print(remove_odd_filter([1,3,5,4,6,8,9,7])) # Output: [4, 6, 8]
print(remove_odd_filter([2,4,6,8])) # Output: [2, 4, 6, 8]
print(remove_odd_filter([])) # Output: []

# Another way to solve this problem using lambda function
def remove_odd_lambda(lst):
    return list(filter(lambda num: num % 2 == 0, lst))

print(remove_odd_lambda([1,2,3])) # Output: [2]
print(remove_odd_lambda([1,3,5,4,6,8,9,7])) # Output: [4, 6, 8]
print(remove_odd_lambda([2,4,6,8])) # Output: [2, 4, 6, 8]
print(remove_odd_lambda([])) # Output: []

# Another way to solve this problem using set() function
def remove_odd_set(lst):
    return list(set(lst) - set([num for num in lst if num % 2 != 0])

print(remove_odd_set([1,2,3])) # Output: [2]
print(remove_odd_set([1,3,5,4,6,8,9,7])) # Output: [4, 6, 8]
print(remove_odd_set([2,4,6,8])) # Output: [2, 4, 6, 8]
print(remove_odd_set([])) # Output: []

# Another way to solve this problem using set() function and lambda function
def remove_odd_set_lambda(lst):
    return list(set(lst) - set(filter(lambda num: num % 2 != 0, lst))

print(remove_odd_set_lambda([1,2,3])) # Output: [2]
print(remove_odd_set_lambda([1,3,5,4,6,8,9,7])) # Output: [4, 6, 8]
print(remove_odd_set_lambda([2,4,6,8])) # Output: [2, 4, 6, 8]
print(remove_odd_set_lambda([])) # Output