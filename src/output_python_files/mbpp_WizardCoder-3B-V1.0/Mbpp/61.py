"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""

def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if sum(int(digit) for digit in s[i:j]) == j-i:
                count += 1
    return count

# Test the function
assert count_Substrings('112112') == 6<|endoftext|>