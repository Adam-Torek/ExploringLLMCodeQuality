"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""

def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        sum = 0
        for j in range(i, len(s)):
            sum += int(s[j])
            if sum == len(s):
                count += 1
    return count


# Test
assert count_Substrings('112112') == 6