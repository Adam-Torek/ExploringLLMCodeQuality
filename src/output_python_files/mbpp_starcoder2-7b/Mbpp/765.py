"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""

def is_polite(n):
    """
    >>> is_polite(7)
    11
    """
    return n * (n + 1) // 2

def nth_polite(n):
    """
    >>> nth_polite(7)
    11
    """
    return is_polite(n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
<file_sep>/python/leetcode/1000-1099/1000.py
"""
1000. Minimum Cost to Merge Stones

There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""

from typing import List

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        """
        >>> Solution().mergeStones([3,2,4,1], 2)
        20
        >>> Solution().mergeStones([3,2,4,1], 3)
        -1
        >>> Solution().mergeStones([3,5,1,2,6], 3)
        25
        """
        if len(stones) < K:
            return -1
        if len(stones) == K:
            return sum(stones)
        if K == 1:
            return sum(stones) - len(stones)
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = stones[i]
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                if (j - i + 1) % (K - 1) == 0:
                    dp[i][j] += sum(stones[i:j + 1])
        return dp[0][n - 1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
<file_sep>/python/leetcode/100-199/12