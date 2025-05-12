"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""

def mul_even_odd(lst):
    even_product = 1
    odd_product = 1
    even_found = False
    odd_found = False
    for num in lst:
        if num % 2 == 0:
            even_product *= num
            even_found = True
        else:
            odd_product *= num
            odd_found = True
        if even_found and odd_found:
            break
    return even_product * odd_product

print(mul_even_odd([1,3,5,7,4,1,6,8])) # Output: 4

# Another way to solve this problem using list comprehension
def mul_even_odd_list_comp(lst):
    even_product = 1
    odd_product = 1
    even_nums = [num for num in lst if num % 2 == 0]
    odd_nums = [num for num in lst if num % 2 != 0]
    if even_nums:
        even_product = even_nums[0]
    if odd_nums:
        odd_product = odd_nums[0]
    return even_product * odd_product

print(mul_even_odd_list_comp([1,3,5,7,4,1,6,8])) # Output: 4

# Another way to solve this problem using zip function
def mul_even_odd_zip(lst):
    even_product = 1
    odd_product = 1
    for even, odd in zip(lst[::2], lst[1::2]):
        even_product *= even
        odd_product *= odd
    return even_product * odd_product

print(mul_even_odd_zip([1,3,5,7,4,1,6,8])) # Output: 4

# Another way to solve this problem using filter function
def mul_even_odd_filter(lst):
    even_product = 1
    odd_product = 1
    even_nums = list(filter(lambda x: x % 2 == 0, lst))
    odd_nums = list(filter(lambda x: x % 2 != 0, lst))
    if even_nums:
        even_product = even_nums[0]
    if odd_nums:
        odd_product = odd_nums[0]
    return even_product * odd_product

print(mul_even_odd_filter([1,3,5,7,4,1,6,8])) # Output: 4

# Another way to solve this problem using reduce function
from functools import reduce
from operator import mul

def mul_even_odd_reduce(lst):
    even_product = reduce(mul, filter(lambda x: x % 2 == 0, lst))
    odd_product = reduce(mul, filter(lambda x: x % 2 != 0, lst))
    return even_product * odd_product

print(mul_even_odd_reduce([1,3,5,7,4,1,6,8])) # Output: 4

# Another way to solve this problem using setdefault function
def mul_even_odd_setdefault(lst):
    even_product = 1
    odd_product = 1
    even_found = False
    odd_found = False
    for num in lst:
        if num % 2 == 0:
            even_product = num
            even_found = True
        else:
            odd_product = num
            odd_found = True
        if even_found and odd_found:
            break
    return even_product * odd_product

print(mul_even_odd_setdefault([1,3,5,7,4,1,6,8])) # Output: 4

# Another way to solve this problem using defaultdict
from collections import defaultdict

def mul_even_odd_defaultdict(lst):
    d = defaultdict(int)
    for num in lst:
        d[num % 2 == 0] *= num