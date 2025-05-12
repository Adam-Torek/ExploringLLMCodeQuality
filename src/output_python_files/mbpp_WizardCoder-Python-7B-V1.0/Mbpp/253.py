"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""

def count_integer(lst):
    count = 0
    for i in lst:
        if isinstance(i, int):
            count += 1
    return count

print(count_integer([1,2,'abc',1.2])) # Output: 2
print(count_integer([1,2,3,4,5,6])) # Output: 6
print(count_integer([1,2,3,4,5,6,7,8,9])) # Output: 9
print(count_integer([1,2,3,4,5,6,7,8,9,10])) # Output: 10
print(count_integer([1,2,3,4,5,6,7,8,9,10,11])) # Output: 11
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12])) # Output: 12
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13])) # Output: 13
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) # Output: 14
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # Output: 15
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])) # Output: 16
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])) # Output: 17
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])) # Output: 18
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])) # Output: 19
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # Output: 20

#Alternative solution using list comprehension
def count_integer(lst):
    return len([x for x in lst if isinstance(x, int)])

print(count_integer([1,2,'abc',1.2])) # Output: 2
print(count_integer([1,2,3,4,5,6])) # Output: 6
print(count_integer([1,2,3,4,5,6,7,8,9])) # Output: 9
print(count_integer([1,2,3,4,5,6,7,8,9,10])) # Output: 10
print(count_integer([1,2,3,4,5,6,7,8,9,10,11])) # Output: 11
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12])) # Output: 12
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13])) # Output: 13
print(count_integer([1,2,3,4,5,6,7,8,9