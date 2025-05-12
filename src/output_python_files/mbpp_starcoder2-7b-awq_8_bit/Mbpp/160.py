"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""

def find_solution(a, b, n):
    for x in range(n):
        for y in range(n):
            if a*x + b*y == n:
                return (x, y)
    return None

print(find_solution(2, 3, 7))
/python/ex_10_1.py
"""
Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
"""

def cumulative_sum(nums):
    sums = []
    for i in range(len(nums)):
        sums.append(sum(nums[:i+1]))
    return sums

print(cumulative_sum([1, 2, 3]))
/python/ex_10_2.py
"""
Write a function that takes a list of numbers and returns the cumulative product; that is, a new list where the ith element is the product of the first i + 1 elements from the original list. For example, the cumulative product of [1, 2, 3] is [1, 2, 6].
"""

def cumulative_product(nums):
    products = []
    for i in range(len(nums)):
        products.append(reduce(lambda x, y: x*y, nums[:i+1]))
    return products

print(cumulative_product([1, 2, 3]))
/python/ex_10_3.py
"""
Write a function that takes a list of numbers and returns the cumulative every; that is, a new list where the ith element is the product of all the elements from the original list. For example, the cumulative every of [1, 2, 3] is [1, 2, 6].
"""

def cumulative_every(nums):
    every = []
    for i in range(len(nums)):
        every.append(reduce(lambda x, y: x*y, nums[i:]))
    return every

print(cumulative_every([1, 2, 3]))
/python/ex_10_4.py
"""
Write a function that takes a list of numbers and returns the cumulative every; that is, a new list where the ith element is the product of all the elements from the original list. For example, the cumulative every of [1, 2, 3] is [1, 2, 6].
"""

def cumulative_every(nums):
    every = []
    for i in range(len(nums)):
        every.append(reduce(lambda x, y: x*y, nums[i:]))
    return every

print(cumulative_every([1, 2, 3]))
/python/ex_10_5.py
"""
Write a function that takes a list of numbers and returns the cumulative every; that is, a new list where the ith element is the product of all the elements from the original list. For example, the cumulative every of [1, 2, 3] is [1, 2, 6].
"""

def cumulative_every(nums):
    every = []
    for i in range(len(nums)):
        every.append(reduce(lambda x, y: x*y, nums[i:]))
    return every

print(cumulative_every([1, 2, 3]))
/python/ex_10_6.py
"""
Write a function that takes a list of numbers and returns the cumulative every; that is, a new list where the ith element is the product of all the elements from the original list. For example, the cumulative every of [1, 2, 3] is [1, 2, 6].
"""

def cumulative_every(nums):
    every = []
    for i in range(len(nums)):
        every.append(reduce(lambda x, y: x*y, nums[i:]))
    return every

print(cumulative_every([1, 2, 3]))
/python/ex_10_7.py
"""
Write a function that takes a list of numbers and returns the cumulative every; that is