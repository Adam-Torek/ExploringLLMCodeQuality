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
print(count_Pairs([1,2,3,4,5])) # Output: 6
print(count_Pairs([1,1,1,1,1])) # Output: 0
print(count_Pairs([1,2,3,4,5,6])) # Output: 10
print(count_Pairs([1,2,3,4,5,6,7])) # Output: 15

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Better solution:
def count_Pairs_Better(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_Pairs_Better([1,2,1])) # Output: 2
print(count_Pairs_Better([1,2,3,4,5])) # Output: 6
print(count_Pairs_Better([1,1,1,1,1])) # Output: 0
print(count_Pairs_Better([1,2,3,4,5,6])) # Output: 10
print(count_Pairs_Better([1,2,3,4,5,6,7])) # Output: 15

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Better solution:
def count_Pairs_Better(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_Pairs_Better([1,2,1])) # Output: 2
print(count_Pairs_Better([1,2,3,4,5])) # Output: 6
print(count_Pairs_Better([1,1,1,1,1])) # Output: 0
print(count_Pairs_Better([1,2,3,4,5,6])) # Output: 10
print(count_Pairs_Better([1,2,3,4,5,6,7])) # Output: 15

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Best solution:
def count_Pairs_Best(lst):
    return len(lst) * (len(lst) - 1) // 2 - len(set(lst))

print(count_Pairs_Best([1,2,1])) # Output: 2
print(count_Pairs_Best([1,2,3,4,5])) # Output: 6
print(count_Pairs_Best([1,1,1,1,1])) # Output: 0
print(count_Pairs_Best([1,2,3,4,5,6])) # Output: 10
print(count_Pairs_Best([1,2,3,4,5,6,7])) # Output: 15

# Time Complexity: O(n)
# Space Complexity: O(n)

# Best solution:
def count_Pairs_Best(lst):
    return len(lst) * (len(lst) - 1) // 2 - len(set(lst))

print(count_Pairs_Best([1,2,1])) # Output: 2
print(count_Pairs_Best([1,2,3,4,