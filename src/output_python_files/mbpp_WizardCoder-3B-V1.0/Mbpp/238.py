"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""

def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            count += 1
    return count

# Test the function
assert number_of_substrings("abc") == 6<|endoftext|>