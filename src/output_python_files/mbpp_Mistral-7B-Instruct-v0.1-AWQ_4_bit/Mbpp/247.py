"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""

def lps(s):
    n = len(s)
    max_len = 0
    start = 0
    for i in range(n):
        low = i
        high = i
        while low < n and high >= 0 and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low += 1
            high -= 1
        if max_len < i - low + 1:
            start = i
            max_len = i - low + 1
    return max_len


assert lps("TENS FOR TENS") == 5