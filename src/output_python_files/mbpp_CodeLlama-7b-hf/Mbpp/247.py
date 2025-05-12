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
            dp[i][i + 1] = 2
    for i in range(len(s) - 2, -1, -1):
        for j in range(i + 2, len(s)):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]


if __name__ == '__main__':
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print(lps("TENS FOR TENS"))
    print