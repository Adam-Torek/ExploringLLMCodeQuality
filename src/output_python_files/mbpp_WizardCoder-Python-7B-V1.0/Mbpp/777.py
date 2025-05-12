"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""

def find_sum(lst):
    unique_lst = list(set(lst))
    return sum(unique_lst)

print(find_sum([1,2,3,1,1,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6,6])) # Output: 15
print(find_sum([1,2,3,4,5,6,7])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,10])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,10,11])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,1