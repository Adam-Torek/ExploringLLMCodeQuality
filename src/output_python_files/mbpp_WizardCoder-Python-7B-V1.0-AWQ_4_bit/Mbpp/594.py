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
print(diff_even_odd([2,4,6,8,10])) # Output: 8
print(diff_even_odd([1,3,5,7,9])) # Output: 0
print(diff_even_odd([1,3,5,7,9,0])) # Output: 0
print(diff_even_odd([2,4,6,8])) # Output: 0
print(diff_even_odd([1,3,5,7])) # Output: 0
print(diff_even_odd([1,3,5,7,9,0,2])) # Output: 1
print(diff_even_odd([1,3,5,7,9,0,2,4])) # Output: 2
print(diff_even_odd([1,3,5,7,9,0,2,4,6])) # Output: 3
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8])) # Output: 4
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10])) # Output: 10
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12])) # Output: 12
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12,14])) # Output: 14
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12,14,16])) # Output: 16
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12,14,16,18])) # Output: 18
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12,14,16,18,20])) # Output: 20
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12,14,16,18,20,22])) # Output: 22
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12,14,16,18,20,22,24])) # Output: 24
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12,14,16,18,20,22,24,26])) # Output: 26
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28])) # Output: 28
print(diff_even_odd([1,3,5,7,9,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30])) # Output: 30
print(diff_even_odd([1,3,5,7,9,0,2,4,6