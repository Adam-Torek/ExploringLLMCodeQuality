"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""

def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            count += 1
    return count

print(number_of_substrings("abc")) # Output: 6
print(number_of_substrings("")) # Output: 0
print(number_of_substrings("a")) # Output: 1
print(number_of_substrings("aaa")) # Output: 3
print(number_of_substrings("abcd")) # Output: 10
print(number_of_substrings("abcde")) # Output: 15
print(number_of_substrings("abcdefg")) # Output: 21

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Optimized Solution
def number_of_substrings(s):
    return len(s) * (len(s) + 1) // 2

print(number_of_substrings("abc")) # Output: 6
print(number_of_substrings("")) # Output: 0
print(number_of_substrings("a")) # Output: 1
print(number_of_substrings("aaa")) # Output: 3
print(number_of_substrings("abcd")) # Output: 10
print(number_of_substrings("abcdefg")) # Output: 21

# Time Complexity: O(1)
# Space Complexity: O(1)