"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""

def lps(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

            for k in range(i+1, j):
                if s[i:k+1] == s[k+1:j+1]:
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])

    return dp[0][n-1]

# Test cases
print(lps("TENS FOR TENS")) # Output: 5
print(lps("BBABCDBA")) # Output: 7
print(lps("ABCD")) # Output: 1
print(lps("AAAA")) # Output: 4
print(lps("BBBB")) # Output: 2
print(lps("")) # Output: 0
print(lps("A")) # Output: 1
print(lps("ABAB")) # Output: 2
print(lps("ABCDCBA")) # Output: 7
print(lps("ABBDCBA")) # Output: 7
print(lps("ABCDCB")) # Output: 5
print(lps("ABCDCACB")) # Output: 7
print(lps("ABCDCACBA")) # Output: 8
print(lps("ABCDCACBAB")) # Output: 9
print(lps("ABCDCACBABD")) # Output: 10
print(lps("ABCDCACBABDAC")) # Output: 11
print(lps("ABCDCACBABDACB")) # Output: 12
print(lps("ABCDCACBABDACBAB")) # Output: 13
print(lps("ABCDCACBABDACBABD")) # Output: 14
print(lps("ABCDCACBABDACBABDA")) # Output: 15
print(lps("ABCDCACBABDACBABDAE")) # Output: 15
print(lps("ABCDCACBABDACBABDAEF")) # Output: 16
print(lps("ABCDCACBABDACBABDAEFF")) # Output: 17
print(lps("ABCDCACBABDACBABDAEFFF")) # Output: 18
print(lps("ABCDCACBABDACBABDAEFFFF")) # Output: 19
print(lps("ABCDCACBABDACBABDAEFFFFF")) # Output: 20
print(lps("ABCDCACBABDACBABDAEFFFFFF")) # Output: 21
print(lps("ABCDCACBABDACBABDAEFFFFFFF")) # Output: 22
print(lps("ABCDCACBABDACBABDAEFFFFFFFG")) # Output: 22
print(lps("ABCDCACBABDACBABDAEFFFFFFFGH")) # Output: 22
print(lps("ABCDCACBABDACBABDAEFFFFFFFGHH")) # Output: 23
print(lps("ABCDCACBABDACBABDAEFFFFFFFGHHH")) # Output: 24
print(lps("ABCDCACBABDACBABDAEFFFFFFFGHHHH")) # Output: 25