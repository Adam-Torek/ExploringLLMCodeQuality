"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""

def pair_xor_Sum(lst, k):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            result += lst[i]^lst[j]
    return result

print(pair_xor_Sum([5,9,7,6],4)) # Output: 47

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Can we do better?

def pair_xor_Sum_efficient(lst, k):
    lst.sort()
    result = 0
    i, j = 0, len(lst)-1
    while i < j:
        result += lst[i]^lst[j]
        i += 1
        j -= 1
    return result

print(pair_xor_Sum_efficient([5,9,7,6],4)) # Output: 47

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Can we do better?

def pair_xor_Sum_efficient(lst, k):
    lst.sort()
    result = 0
    i, j = 0, len(lst)-1
    while i < j:
        result += lst[i]^lst[j]
        if lst[i]^lst[j] == k:
            i += 1
        else:
            j -= 1
    return result

print(pair_xor_Sum_efficient([5,9,7,6],4)) # Output: 47

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Can we do better?

def pair_xor_Sum_efficient(lst, k):
    lst.sort()
    result = 0
    i, j = 0, len(lst)-1
    while i < j:
        result += lst[i]^lst[j]
        if lst[i]^lst[j] == k:
            i += 1
        else:
            j -= 1
    return result

print(pair_xor_Sum_efficient([5,9,7,6],4)) # Output: 47

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Can we do better?

def pair_xor_Sum_efficient(lst, k):
    lst.sort()
    result = 0
    i, j = 0, len(lst)-1
    while i < j:
        result += lst[i]^lst[j]
        if lst[i]^lst[j] == k:
            i += 1
        else:
            j -= 1
    return result

print(pair_xor_Sum_efficient([5,9,7,6],4)) # Output: 47

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Can we do better?

def pair_xor_Sum_efficient(lst, k):
    lst.sort()
    result = 0
    i, j = 0, len(lst)-1
    while i < j:
        result += lst[i]^lst[j]
        if lst[i]^lst[j] == k:
            i += 1
        else:
            j -= 1
    return result

print(pair_xor_Sum_efficient([5,9,7,6],4)) # Output: 47

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Can we do better?

def pair_xor_Sum_efficient(lst, k):
    lst.sort()
    result = 0
    i, j = 0, len(lst)-1
    while i < j:
        result += lst[i