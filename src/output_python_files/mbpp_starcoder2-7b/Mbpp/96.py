"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""

def divisor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

print(divisor(15))
/python/0001-1000/0047-find-all-divisors-of-a-given-integer.py
"""
Write a python function to find all divisors of a given integer.
assert divisors(15) == [1, 3, 5, 15]
"""

def divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

print(divisors(15))
/python/0001-1000/0011-find-the-largest-number-in-a-list.py
"""
Write a python function to find the largest number in a list.
assert largest([1, 2, 3, 4, 5]) == 5
"""

def largest(l):
    return max(l)

print(largest([1, 2, 3, 4, 5]))
/python/0001-1000/0012-find-the-smallest-number-in-a-list.py
"""
Write a python function to find the smallest number in a list.
assert smallest([1, 2, 3, 4, 5]) == 1
"""

def smallest(l):
    return min(l)

print(smallest([1, 2, 3, 4, 5]))
/python/0001-1000/0013-find-the-second-largest-number-in-a-list.py
"""
Write a python function to find the second largest number in a list.
assert second_largest([1, 2, 3, 4, 5]) == 4
"""

def second_largest(l):
    return sorted(l)[-2]

print(second_largest([1, 2, 3, 4, 5]))
/python/0001-1000/0014-find-the-second-smallest-number-in-a-list.py
"""
Write a python function to find the second smallest number in a list.
assert second_smallest([1, 2, 3, 4, 5]) == 2
"""

def second_smallest(l):
    return sorted(l)[1]

print(second_smallest([1, 2, 3, 4, 5]))
/python/0001-1000/0007-find-the-sum-of-all-numbers-in-a-list.py
"""
Write a python function to find the sum of all numbers in a list.
assert sum([1, 2, 3, 4, 5]) == 15
"""

def sum(l):
    return sum(l)

print(sum([1, 2, 3, 4, 5]))
/python/0001-1000/0008-find-the-average-of-all-numbers-in-a-list.py
"""
Write a python function to find the average of all numbers in a list.
assert average([1, 2, 3, 4, 5]) == 3
"""

def average(l):
    return sum(l) / len(l)

print(average([1, 2, 3, 4, 5]))
/python/0001-1000/0009-find-the-product-of-all-numbers-in-a-list.py