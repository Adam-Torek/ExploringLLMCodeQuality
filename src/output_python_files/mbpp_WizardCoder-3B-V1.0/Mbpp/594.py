"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
def diff_even_odd(lst):
    even_lst = [num for num in lst if num % 2 == 0]
    odd_lst = [num for num in lst if num % 2!= 0]
    return abs(even_lst[0] - odd_lst[0])

# Test the function
print(diff_even_odd([1,3,5,7,4,1,6,8])) # Output: 3<|endoftext|>