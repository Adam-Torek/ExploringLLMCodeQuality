"""
Write a function to compute the n-th power of each number in a list.
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def nth_nums(lst, n):
    return [x**n for x in lst]

print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2))

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]