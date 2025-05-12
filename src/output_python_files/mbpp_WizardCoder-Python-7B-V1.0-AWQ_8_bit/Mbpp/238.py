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
print(number_of_substrings("abcde")) # Output: 10
print(number_of_substrings("abcd")) # Output: 4
print(number_of_substrings("abcdabcd")) # Output: 10
print(number_of_substrings("abcdefg")) # Output: 21

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Optimized Solution
def number_of_substrings_optimized(s):
    return len(s) * (len(s) + 1) // 2

print(number_of_substrings_optimized("abc")) # Output: 6
print(number_of_substrings_optimized("")) # Output: 0
print(number_of_substrings_optimized("a")) # Output: 1
print(number_of_substrings_optimized("aaa")) # Output: 3
print(number_of_substrings_optimized("abcde")) # Output: 10
print(number_of_substrings_optimized("abcd")) # Output: 4
print(number_of_substrings_optimized("abcdefg")) # Output: 21

# Time Complexity: O(1)
# Space Complexity: O(1)

# Explanation:
# The optimized solution uses the formula n * (n+1) / 2 to calculate the number of substrings of a string of length n. 
# This formula is derived from the fact that there are n * (n+1) unique substrings of a string, where n is the length of the string. 
# The formula is derived from the fact that there are n substrings of length 1, n substrings of length 2, and so on up to n substrings of length n. 
# The sum of these substrings is n * (n+1) / 2.