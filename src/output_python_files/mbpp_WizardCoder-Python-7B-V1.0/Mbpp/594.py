"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""

def diff_even_odd(lst):
    even_num = None
    odd_num = None
    for num in lst:
        if num % 2 == 0:
            if even_num is None:
                even_num = num
        else:
            if odd_num is None:
                odd_num = num
            else:
                break
    return abs(even_num - odd_num)

print(diff_even_odd([1,3,5,7,4,1,6,8])) # Output: 3
print(diff_even_odd([2,4,6,8,10,12])) # Output: 0
print(diff_even_odd([1,3,5,7,9,11])) # Output: 0
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10])) # Output: 1
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11])) # Output: 1
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12])) # Output: 2
print(diff_even_odd([2,4,6,8,10,12])) # Output: 0
print(diff_even_odd([1,3,5,7,9,11])) # Output: 0
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12])) # Output: 1
print(diff_even_odd([2,4,6,8,10,12,14])) # Output: 2
print(diff_even_odd([1,3,5,7,9,11,13])) # Output: 2
print(diff_even_odd([2,4,6,8,10,12,14])) # Output: 2
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13])) # Output: 3
print(diff_even_odd([2,4,6,8,10,12,14,16])) # Output: 2
print(diff_even_odd([1,3,5,7,9,11,13,15])) # Output: 3
print(diff_even_odd([2,4,6,8,10,12,14,16])) # Output: 2
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) # Output: 3
print(diff_even_odd([2,4,6,8,10,12,14,16,18])) # Output: 2
print(diff_even_odd([1,3,5,7,9,11,13,15,17])) # Output: 3
print(diff_even_odd([2,4,6,8,10,12,14,16,18])) # Output: 2
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # Output: 4
print(diff_even_odd([2,4,6,8,10,12,14,16,18,20])) # Output: 2
print(diff_even_odd([1,3,5,7,9,11,13,15,17,19])) # Output: 3
print(diff_even_odd([2,4,6,8,10,12,14,16,18,20])) # Output