"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""

def lps(s):
    n = len(s)
    table = [[0 for _ in range(n)] for _ in range(n)]
    max_len = 0
    for i in range(n):
        table[i][i] = 1
        max_len = 1

    start = 0
    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            if s[i] == s[j] and k == 1:
                table[i][j] = 1
                max_len = k
                start = i
            elif s[i] == s[j]:
                table[i][j] = table[i + 1][j - 1] + 1
                if table[i][j] > max_len:
                    max_len = table[i][j]
                    start = i
            else:
                table[i][j] = 0

    return max_len, start

if __name__ == "__main__":
    s = "TENS FOR TENS"
    print(lps(s))