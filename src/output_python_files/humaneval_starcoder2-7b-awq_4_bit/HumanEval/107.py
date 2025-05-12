def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
/leetcode/1001-1100/1001-1010/1009.complement-of-base-10-integer/complement-of-base-10-integer.py
# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return N ^ (1 << (N.bit_length() + 1) - 1)
/leetcode/1001-1100/1001-1010/1005.maximize-sum-of-array-after-k-negations/maximize-sum-of-array-after-k-negations.py
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        for i in xrange(K):
            if A[i] < 0:
                A[i] = -A[i]
            else:
                break
        A.sort()
        return sum(A) - 2*sum(A[:K]) if K else sum(A)
/leetcode/1001-1100/1001-1010/1007.minimum-domino-rotations-for-equal-row/minimum-domino-rotations-for-equal-row.py
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A:
            return 0
        if not B:
            return 0
        if len(A)!= len(B):
            return -1
        if len(set(A)) == 1:
            return 0
        if len(set(B)) == 1:
            return 0
        return min(self.minDominoRotationsHelper(A, B, A[0]), self.minDominoRotationsHelper(A, B, B[0]))

    def minDominoRotationsHelper(self, A, B, target):
        countA, countB = 0, 0
        for i in xrange(len(A)):
            if A[i]!= target and B[i]!= target:
                return -1
            if A[i]!= target:
                countA += 1
            if B[i]!= target:
                countB += 1
        return min(countA, countB)
/leetcode/1001-1100/1001-1010/1008.construct-binary-search-tree-from-preorder-traversal/construct-binary-search-tree-from-preorder-traversal.py
# Time:  O(n)
# Space: O(h)

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]