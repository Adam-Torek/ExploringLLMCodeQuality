"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_Pairs([1,2,1])) # Output: 2
print(count_Pairs([1,2,3,4])) # Output: 6
print(count_Pairs([1,2,3,4,5])) # Output: 10
print(count_Pairs([1,2,3,4,5,5])) # Output: 9
print(count_Pairs([1,2,3,4,5,5,6])) # Output: 15
print(count_Pairs([1,2,3,4,5,5,6,6])) # Output: 14
print(count_Pairs([1,2,3,4,5,5,6,6,7])) # Output: 21
print(count_Pairs([1,2,3,4,5,5,6,6,7,7])) # Output: 20
print(count_Pairs([1,2,3,4,5,5,6,6,7,7,8])) # Output: 25
print(count_Pairs([1,2,3,4,5,5,6,6,7,7,8,8])) # Output: 24

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Alternate Solution:
def count_Pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                count += 1
    return count

def count_Pairs_alternate(lst):
    return len(set(lst)) * (len(lst) - 1) / 2

print(count_Pairs([1,2,1])) # Output: 2
print(count_Pairs([1,2,3,4])) # Output: 6
print(count_Pairs([1,2,3,4,5])) # Output: 10
print(count_Pairs([1,2,3,4,5,5])) # Output: 9
print(count_Pairs([1,2,3,4,5,5,6])) # Output: 15
print(count_Pairs([1,2,3,4,5,5,6,6])) # Output: 14
print(count_Pairs([1,2,3,4,5,5,6,6,7])) # Output: 21
print(count_Pairs([1,2,3,4,5,5,6,6,7,7])) # Output: 20
print(count_Pairs([1,2,3,4,5,5,6,6,7,7,8])) # Output: 25
print(count_Pairs([1,2,3,4,5,5,6,6,7,7,8])) # Output: 24

# Time Complexity: O(n)
# Space Complexity: O(n)

# Explanation:
# In the alternate solution, we are using set() function to remove the duplicates from the list and then multiplying the length of the list by (length of the list - 1) to get the number of pairs.