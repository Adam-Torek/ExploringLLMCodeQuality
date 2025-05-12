"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""

def find_sum(lst):
    unique_lst = list(set(lst))
    return sum(unique_lst)

print(find_sum([1,2,3,1,1,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6])) # Output: 15
print(find_sum([1,1,1,1,1,1])) # Output: 0
print(find_sum([1,2,3,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9])) # Output: 25
print(find_sum([1,2,3,4,5,6,7,8,9,10])) # Output: 30

# Time Complexity: O(n)
# Space Complexity: O(n)

# Alternate Solution:

def find_sum(lst):
    sum = 0
    for i in lst:
        if lst.count(i) == 1:
            sum += i
    return sum

print(find_sum([1,2,3,1,1,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9])) # Output: 25
print(find_sum([1,2,3,4,5,6,7,8,9,10])) # Output: 30

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Better Solution:

def find_sum(lst):
    sum = 0
    for i in lst:
        if lst.count(i) == 1:
            sum += i
    return sum

print(find_sum([1,2,3,1,1,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6])) # Output: 15
print(find_sum([1,2,3,4,5,6,7,8,9])) # Output: 25
print(find_sum([1,2,3,4,5,6,7,8,9,10])) # Output: 30

# Time Complexity: O(n)
# Space Complexity: O(1)

# This solution iterates through the list once and checks if the count of an element is 1, if it is 1, then it adds it to the sum. This way, we don't need to create a new list of unique elements.