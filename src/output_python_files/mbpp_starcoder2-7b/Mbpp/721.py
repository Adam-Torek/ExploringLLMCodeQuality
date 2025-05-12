"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""

def maxAverageOfPath(matrix):
    # Write your code here
    if not matrix:
        return 0
    n = len(matrix)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = matrix[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + matrix[0][i]
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[n-1][n-1] / (n*n)

if __name__ == "__main__":
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))/leetcode/1004.py
"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.

assert longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
"""

def longestOnes(A, K):
    # Write your code here
    if not A:
        return 0
    n = len(A)
    left = 0
    right = 0
    max_len = 0
    while right < n:
        if A[right] == 0:
            K -= 1
        if K < 0:
            if A[left] == 0:
                K += 1
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len

if __name__ == "__main__":
    print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))/leetcode/1003.py
"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

assert removeDuplicates("abbaca") == "ca"
"""

def removeDuplicates(S):
    # Write your code here
    if not S:
        return ""
    stack = []
    for c in S:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

if __name__ == "__main__":
    print(removeDuplicates("abbaca"))/leetcode/1002.py
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
"""

def minWindow(S, T):
    # Write your code here
    if not S or not T:
        return ""
    n = len(S)
    m = len(T)
    if n < m:
        return ""
    left = 0
    right = 0
    min_len = float("inf")
    min_str = ""
    count = 0
    while right < n:
        if S[right] in T:
            count += 1
        if count == m:
            while S[left] not in T:
                left += 1
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_str = S