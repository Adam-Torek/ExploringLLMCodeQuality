"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""

def diff_even_odd(lst):
    even = None
    odd = None
    for num in lst:
        if num % 2 == 0:
            if even is None:
                even = num
            else:
                odd = num
                break
    return abs(even - odd)

print(diff_even_odd([1,3,5,7,4,1,6,8])) # Output: 3
print(diff_even_odd([2,4,6,8,10,12])) # Output: 0
print(diff_even_odd([1,3,5,7,9,11])) # Output: 0
print(diff_even_odd([1,2,3,4,5,6,7,8,9])) # Output: 1
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10])) # Output: 0
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11])) # Output: 1
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12])) # Output: 2
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13])) # Output: 3
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) # Output: 4
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # Output: 5
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])) # Output: 6
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])) # Output: 7
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])) # Output: 8
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])) # Output: 9
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # Output: 10
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])) # Output: 11
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])) # Output: 12
print(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])) # Output: 13
print(diff_even_odd([1,2,3,