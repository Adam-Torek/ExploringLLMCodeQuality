"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""

def max_sum_list(lst):
    max_sum = 0
    max_lst = []
    for l in lst:
        if sum(l) > max_sum:
            max_sum = sum(l)
            max_lst = l
    return max_lst

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])) # Output: [10, 11, 12]
print(max_sum_list([[1,2,3,4], [4,5,6,7], [10,11,12,13], [7,8,9,10]])) # Output: [10, 11, 12, 13]
print(max_sum_list([[1,2,3,4,5], [4,5,6,7,8], [10,11,12,13,14], [7,8,9,10,11]])) # Output: [10, 11, 12, 13, 14]

# Alternative solution using lambda function and map()
def max_sum_list(lst):
    return max(lst, key=lambda x: sum(x))

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])) # Output: [10, 11, 12]
print(max_sum_list([[1,2,3,4], [4,5,6,7], [10,11,12,13], [7,8,9,10]])) # Output: [10, 11, 12, 13]
print(max_sum_list([[1,2,3,4,5], [4,5,6,7,8], [10,11,12,13,14], [7,8,9,10,11]])) # Output: [10, 11, 12, 13, 14]

# Alternative solution using list comprehension
def max_sum_list(lst):
    return max(lst, key=lambda x: sum(x))

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])) # Output: [10, 11, 12]
print(max_sum_list([[1,2,3,4], [4,5,6,7], [10,11,12,13], [7,8,9,10]])) # Output: [10, 11, 12, 13]
print(max_sum_list([[1,2,3,4,5], [4,5,6,7,8], [10,11,12,13,14], [7,8,9,10,11]])) # Output: [10, 11, 12, 13, 14]

# Alternative solution using list comprehension and lambda function
def max_sum_list(lst):
    return max(lst, key=lambda x: sum(x))

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])) # Output: [10, 11, 12]
print(max_sum_list([[1,2,3,4], [4,5,6,7], [10,11,12,13], [7,8,9,10]])) # Output: [10, 11, 12, 13]
print(max_