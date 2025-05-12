"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""

def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])

# Test cases
print(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10)) # Output: 29
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 5)) # Output: 18
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 3)) # Output: 14
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9)) # Output: 55
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 1)) # Output: 2
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 0)) # Output: 1
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9, 9)) # Output: 10
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 10)) # Output: 55
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 0)) # Output: 1
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 10)) # Output: 55
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10)) # Output: 55
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 100)) # Output: 55
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1, 100)) # Output: 55
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 0)) # Output: 0
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10)) # Output: 0
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11)) # Output: 0
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1, 11)) # Output: 0
print(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11)) #