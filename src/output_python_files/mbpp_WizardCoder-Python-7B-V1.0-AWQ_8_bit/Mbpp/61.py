"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""

def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(len(s)-i+1):
            if sum(int(d) for d in s[i:i+j]) == j:
                count += 1
    return count

print(count_Substrings('112112'))

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Optimized Solution

def count_Substrings_Optimized(s):
    count = 0
    for i in range(len(s)):
        total = 0
        for j in range(i, len(s)):
            total += int(s[j])
            if total == j-i+1:
                count += 1
    return count

print(count_Substrings_Optimized('112112'))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Better Solution

def count_Substrings_Better(s):
    count = 0
    total = 0
    for i in range(len(s)):
        total += int(s[i])
        if total == i:
            count += 1
        if total < i:
            count += 1
    return count

print(count_Substrings_Better('112112'))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Better Solution 2

def count_Substrings_Better2(s):
    count = 0
    total = 0
    for i in range(len(s)):
        total += int(s[i])
        if total == i:
            count += 1
        if total < i:
            count += 1
    return count

print(count_Substrings_Better2('112112'))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Better Solution 3

def count_Substrings_Better3(s):
    count = 0
    total = 0
    for i in range(len(s)):
        total += int(s[i])
        if total == i:
            count += 1
        if total < i:
            count += 1
    return count

print(count_Substrings_Better3('112112'))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Better Solution 4

def count_Substrings_Better4(s):
    count = 0
    total = 0
    for i in range(len(s)):
        total += int(s[i])
        if total == i:
            count += 1
        if total < i:
            count += 1
    return count

print(count_Substrings_Better4('112112'))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Better Solution 5

def count_Substrings_Better5(s):
    count = 0
    total = 0
    for i in range(len(s)):
        total += int(s[i])
        if total == i:
            count += 1
        if total < i:
            count += 1
    return count

print(count_Substrings_Better5('112112'))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Better Solution 6

def count_Substrings_Better6(s):
    count = 0
    total = 0
    for i in range(len(s)):
        total += int(s[i])
        if total == i:
            count += 1
        if total < i:
            count += 1
    return count

print(count_Substrings_Better6('112112'))

# Time Complexity: O(n)