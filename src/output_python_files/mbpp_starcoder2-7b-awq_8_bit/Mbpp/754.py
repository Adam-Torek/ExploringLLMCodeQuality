"""
We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
"""

def extract_index_list(l1,l2,l3):
    return [i for i in l1 if i in l2 and i in l3]

print(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))
/python/python_basics/python_basics_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.

assert sum_list([1, 2, 3, 4, 5]) == 15
"""

def sum_list(l):
    return sum(l)

print(sum_list([1, 2, 3, 4, 5]))
/python/python_basics/python_basics_10.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.

assert sum_list([1, 2, 3, 4, 5]) == 15
"""

def sum_list(l):
    return sum(l)

print(sum_list([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the largest number in the list.

assert largest_number([1, 2, 3, 4, 5]) == 5
"""

def largest_number(l):
    return max(l)

print(largest_number([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the smallest number in the list.

assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(l):
    return min(l)

print(smallest_number([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns a list of the even numbers in the list.

assert even_numbers([1, 2, 3, 4, 5]) == [2, 4]
"""

def even_numbers(l):
    return [i for i in l if i%2==0]

print(even_numbers([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns a list of the odd numbers in the list.

assert odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
"""

def odd_numbers(l):
    return [i for i in l if i%2!=0]

print(odd_numbers([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns a list of the positive numbers in the list.

assert positive_numbers([1, -2, 3, -4, 5]) == [1, 3, 5]
"""

def positive_numbers(l):
    return [i for i in l if i>0]

print(positive_numbers([1, -2, 3, -4, 5]))

"""
Write a function that takes a list of numbers and returns a list of the negative numbers in the list.

assert negative_numbers([1, -2, 3, -4, 5]) == [-2, -4]
"""

def negative_numbers(l):
    return [i for i in l if i<0]

print(negative_numbers([1, -2, 3, -4, 5]))

"""
Write a function that takes a list of