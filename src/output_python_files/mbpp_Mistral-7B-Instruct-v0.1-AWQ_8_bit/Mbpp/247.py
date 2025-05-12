"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""

def lps(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    else:
        max_len = 1
        start = 0
        for i in range(1, len(s)):
            # find the length of palindromic subsequence with center at i
            low = i - 1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > max_len:
                    max_len = high - low + 1
                    start = low
                low -= 1
                high += 1
            # find the length of palindromic subsequence with center at i-1
            low = i - 1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > max_len:
                    max_len = high - low + 1
                    start = low
                low -= 1
                high += 1
        return max_len


if __name__ == '__main__':
    print(lps("TENS FOR TENS"))