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
                dp[i][j] = dp[i+1][j-1] + 2
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
print(lps("abcdefgfedcbaa")) # Output: 8
print(lps("abcdefgfedcbab")) # Output: 7
print(lps("abcdefgfedcbabc")) # Output: 8
print(lps("abcdefgfedcbabcd")) # Output: 8
print(lps("abcdefgfedcbabcdc")) # Output: 9
print(lps("abcdefgfedcbabcde")) # Output: 10
print(lps("abcdefgfedcbabcdee")) # Output: 11
print(lps("abcdefgfedcbabcdef")) # Output: 11
print(lps("abcdefgfedcbabcdefg")) # Output: 12
print(lps("abcdefgfedcbabcdefgh")) # Output: 13
print(lps("abcdefgfedcbabcdefghi")) # Output: 14
print(lps("abcdefgfedcbabcdefghij")) # Output: 15
print(lps("abcdefgfedcbabcdefghijk")) # Output: 16
print(lps("abcdefgfedcbabcdefghijkl")) # Output: 17
print(lps("abcdefgfedcbabcdefghijklm")) # Output: 18
print(lps("abcdefgfedcbabcdefghijklmn")) # Output: 19
print(lps("abcdefgfedcbabcdefghijklmno")) # Output: 20
print(lps("abcdefgfedcbabcdefghijklmnop")) # Output: 21
print(lps("abcdefgfedcbabcdefghijklmnopq")) # Output: 22
print(lps("abcdefgfedcbabcdefghijklmnopqr")) # Output: 23
print(lps("abcdefgfedcbabcdefghijklmnopqrs")) # Output: 24
print(lps("abcdefgfedcbabcdefghijklmnopqrst")) # Output: 25
print(lps("abcdefgfedcbabcdefghijklmnopqrstu")) # Output: 26
print(lps("abcdefgfedcbabcdefghijklmnopqrstuv")) # Output: 27