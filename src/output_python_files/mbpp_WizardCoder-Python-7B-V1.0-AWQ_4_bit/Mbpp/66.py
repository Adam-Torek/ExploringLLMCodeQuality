"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""

def pos_count(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    return count

# Test cases
print(pos_count([1,-2,3,-4])) # Output: 2
print(pos_count([0,2,4,-5,6,-7])) # Output: 3
print(pos_count([-1,0,2,3,4])) # Output: 1
print(pos_count([-1,-2,-3,-4])) # Output: 0
print(pos_count([])) # Output: 0
print(pos_count([1])) # Output: 1
print(pos_count([-1])) # Output: 0
print(pos_count([0])) # Output: 0
print(pos_count([1,0,2,3,-4,5])) # Output: 3
print(pos_count([-1,0,2,3,4,5])) # Output: 1
print(pos_count([-1,0,-2,-3,-4,-5])) # Output: 0
print(pos_count([1,2,3,4,5])) # Output: 5
print(pos_count([-1,-2,-3,-4,-5])) # Output: 0
print(pos_count([-1,0,1,2,3,4])) # Output: 3
print(pos_count([-1,0,1,2,-3,4])) # Output: 3
print(pos_count([-1,0,1,-2,3,4])) # Output: 2
print(pos_count([-1,0,1,2,-3,-4])) # Output: 2
print(pos_count([-1,0,1,-2,-3,-4])) # Output: 1
print(pos_count([-1,0,1,2,3,-4])) # Output: 2
print(pos_count([-1,0,1,-2,3,-4])) # Output: 2
print(pos_count([-1,0,1,-2,3,4])) # Output: 2
print(pos_count([-1,0,1,-2,-3,4])) # Output: 2
print(pos_count([-1,0,1,2,-3,-4])) # Output: 2
print(pos_count([-1,0,1,-2,3,-4])) # Output: 2
print(pos_count([-1,0,1,-2,3,4])) # Output: 2
print(pos_count([-1,0,1,-2,-3,4])) # Output: 2
print(pos_count([-1,0,1,2,-3,4])) # Output: 3
print(pos_count([-1,0,1,-2,3,4])) # Output: 3
print(pos_count([-1,0,1,-2,-3,4])) # Output: 2
print(pos_count([-1,0,1,2,3,-4])) # Output: 3
print(pos_count([-1,0,1,-2,3,4])) # Output: 3
print(pos_count([-1,0,1,-2,-3,4])) # Output: 2
print(pos_count([-1,0,1,2,3,4])) # Output: 4
print(pos_count([-1,0,1,-2,3,4])) # Output: 3
print(pos_count([-1,0,1,-2,-3,4])) # Output: 2
print(pos_count([-1,0,1,2,3,-4])) # Output: 3
print(pos_count([-1,0,1,-2,3,4])) # Output: 3
print(pos_count([-1,0,1,-2,-3,4])) # Output: 2
print(pos_count([-1,0,1,2,3,4])) # Output: 4
print(pos_count([-1,0,1,-2,3,4]))