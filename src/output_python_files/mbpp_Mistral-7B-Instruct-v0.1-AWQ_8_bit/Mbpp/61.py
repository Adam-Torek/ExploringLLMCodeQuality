"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""

def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if int(s[i:j+1]) == len(s[i:j+1]):
                count += 1
    return count


# assert count_Substrings('112112') == 6
print(count_Substrings('112112'))