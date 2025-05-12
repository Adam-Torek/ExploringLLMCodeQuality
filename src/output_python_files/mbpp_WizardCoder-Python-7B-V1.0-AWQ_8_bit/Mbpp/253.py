"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""

def count_integer(lst):
    count = 0
    for i in lst:
        if type(i) == int:
            count += 1
    return count

print(count_integer([1,2,'abc',1.2])) # Output: 2
print(count_integer([1,2,3,4,5])) # Output: 5
print(count_integer([1,2,3,4,5,6,7,8,9])) # Output: 9
print(count_integer([1,2,3,4,5,6,7,8,9,10])) # Output: 10
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # Output: 15
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # Output: 20

# Another way to solve this problem using list comprehension
def count_integer(lst):
    return len([x for x in lst if type(x) == int])

print(count_integer([1,2,'abc',1.2])) # Output: 2
print(count_integer([1,2,3,4,5])) # Output: 5
print(count_integer([1,2,3,4,5,6,7,8,9])) # Output: 9
print(count_integer([1,2,3,4,5,6,7,8,9,10]) # Output: 10
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # Output: 15
print(count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) # Output: 20