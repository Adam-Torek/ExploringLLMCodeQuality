"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""

def lps(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    max_len = 1
    start = 0

    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    start = i
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return max_len

# Test cases
assert lps("TENS FOR TENS") == 5
assert lps("ABCDABCDABCD") == 10
assert lps("ABCDABCDABCDABCD") == 18<|endoftext|>