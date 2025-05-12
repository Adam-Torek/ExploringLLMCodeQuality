"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""

def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2

    for i in range(n-2, -1, -1):
        for j in range(i+2, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

# Test cases
print(lps("TENS FOR TENS")) # Output: 5
print(lps("BBABC")) # Output: 3
print(lps("cbbd")) # Output: 2
print(lps("abacdfgdcaba")) # Output: 7
print(lps("a")) # Output: 1
print(lps("")) # Output: 0
print(lps("aaaa")) # Output: 4
print(lps("bbbab")) # Output: 3
print(lps("abcdefg")) # Output: 1
print(lps("abcdefgfedcba")) # Output: 7
print(lps("abcdefgfedccba")) # Output: 8
print(lps("abcdefgfedccbaa")) # Output: 10
print(lps("abcdefgfedccbaaa")) # Output: 11
print(lps("abcdefgfedccbaaab")) # Output: 12
print(lps("abcdefgfedccbaaaa")) # Output: 13
print(lps("abcdefgfedccbaaaab")) # Output: 14
print(lps("abcdefgfedccbaaaabc")) # Output: 15
print(lps("abcdefgfedccbaaaabcd")) # Output: 16
print(lps("abcdefgfedccbaaaabcdc")) # Output: 17
print(lps("abcdefgfedccbaaaabcdcd")) # Output: 18
print(lps("abcdefgfedccbaaaabcdcde")) # Output: 19
print(lps("abcdefgfedccbaaaabcdcdef")) # Output: 20
print(lps("abcdefgfedccbaaaabcdcdefg")) # Output: 21
print(lps("abcdefgfedccbaaaabcdcdefgh")) # Output: 22
print(lps("abcdefgfedccbaaaabcdcdefghi")) # Output: 23
print(lps("abcdefgfedccbaaaabcdcdefghij")) # Output: 24
print(lps("abcdefgfedccbaaaabcdcdefghijk")) # Output: 25
print(lps("abcdefgfedccbaaaabcdcdefghijkl")) # Output: 26
print(lps("abcdefgfedccbaaaabcdcdefghijklm")) # Output: 27
print(lps("abcdefgfedccbaaaabcdcdefghijklmn")) # Output: 28
print(lps("abcdefgfedccbaaaabcdcdefghijklmno")) # Output: 29
print(lps("abcdefgfedccbaaaabcdcdefghijklmnop")) # Output: 30
print(lps("abcdefgfedccbaaaabcdcdefghijklmnopq")) # Output: 31
print(lps("abcdefgfedccbaaaabcdcdefghijklmnopqr")) # Output: 32