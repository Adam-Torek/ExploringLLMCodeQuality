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

# Time Complexity: O(n^3)
# Space Complexity: O(1)

# Optimized Solution
def count_Substrings_Optimized(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if sum(int(d) for d in s[i:j+1]) == j-i+1:
                count += 1
    return count

print(count_Substrings_Optimized('112112'))

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Optimized Solution using Hashing
def count_Substrings_Hashing(s):
    count = 0
    n = len(s)
    hash_map = {}
    for i in range(n):
        if s[i] in hash_map:
            hash_map[s[i]] += 1
        else:
            hash_map[s[i]] = 1
    for i in range(n):
        if hash_map[s[i]] > 0:
            hash_map[s[i]] -= 1
            count += hash_map[s[i]]
    return count

print(count_Substrings_Hashing('112112'))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimized Solution using Hashing and Cumulative Sum
def count_Substrings_Cumulative_Sum(s):
    count = 0
    cum_sum = 0
    n = len(s)
    hash_map = {}
    for i in range(n):
        cum_sum += int(s[i])
        if cum_sum in hash_map:
            count += hash_map[cum_sum]
        if cum_sum in hash_map:
            hash_map[cum_sum] += 1
        else:
            hash_map[cum_sum] = 1
    return count

print(count_Substrings_Cumulative_Sum('112112'))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimized Solution using Hashing and Cumulative Sum with Precomputed Cumulative Sum
def count_Substrings_Cumulative_Sum_Precomputed(s):
    count = 0
    cum_sum = 0
    n = len(s)
    cum_sum_arr = [0] * n
    cum_sum_arr[0] = int(s[0])
    for i in range(1, n):
        cum_sum_arr[i] = cum_sum_arr[i-1] + int(s[i])
    hash_map = {0: 1}
    for i in range(1, n):
        count += hash_map.get(cum_sum_arr[i]-i, 0)
        if cum_sum_arr[i] in hash_map:
            hash_map[cum_sum_arr[i]] += 1
        else:
            hash_map[cum_sum_arr[i]] = 1
    return count

print(count_Substrings_Cumulative_Sum_Precomputed('112112'))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimized Solution using Hashing and Cumulative Sum with Precomputed Cumulative Sum and Binary Search
def count_Substrings_Cumulative_Sum_Binary_Search(s):
    count = 0
    cum_sum = 0
    n