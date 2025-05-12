"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""


def lps(s):
    """
    :param s: string
    :return: length of the longest palindromic subsequence in the given string
    """
    if not s:
        return 0
    if len(s) == 1:
        return 1

    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1

    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            dp[i][i + 2] = 1

    for i in range(len(s) - 3):
        if s[i] == s[i + 3]:
            dp[i][i + 3] = 1

    for i in range(len(s) - 4):
        if s[i] == s[i + 4]:
            dp[i][i + 4] = 1

    for i in range(len(s) - 5):
        if s[i] == s[i + 5]:
            dp[i][i + 5] = 1

    for i in range(len(s) - 6):
        if s[i] == s[i + 6]:
            dp[i][i + 6] = 1

    for i in range(len(s) - 7):
        if s[i] == s[i + 7]:
            dp[i][i + 7] = 1

    for i in range(len(s) - 8):
        if s[i] == s[i + 8]:
            dp[i][i + 8] = 1

    for i in range(len(s) - 9):
        if s[i] == s[i + 9]:
            dp[i][i + 9] = 1

    for i in range(len(s) - 10):
        if s[i] == s[i + 10]:
            dp[i][i + 10] = 1

    for i in range(len(s) - 11):
        if s[i] == s[i + 11]:
            dp[i][i + 11] = 1

    for i in range(len(s) - 12):
        if s[i] == s[i + 12]:
            dp[i][i + 12] = 1

    for i in range(len(s) - 13):
        if s[i] == s[i + 13]:
            dp[i][i + 13] = 1

    for i in range(len(s) - 14):
        if s[i] == s[i + 14]:
            dp[i][i + 14] = 1

    for i in range(len(s) - 15):
        if s[i] == s[i + 15]:
            dp[i][i + 15] = 1

    for i in range(len(s) - 16):
        if s[i] == s[i + 16]:
            dp[i][i + 16] = 1

    for i in range(len(s) - 17):
        if s[i] == s[i + 17]:
            dp[i][i + 17] = 1

    for i in range(len(s) - 18):
        if