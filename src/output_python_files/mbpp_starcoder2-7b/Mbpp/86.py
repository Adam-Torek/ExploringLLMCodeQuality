"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""

def centered_hexagonal_number(n):
    """
    >>> centered_hexagonal_number(10)
    271
    """
    return (n**2 + n + 2) * 6 - 6

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/leetcode/0001-0100/0031-next-permutation.py
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i + 1)

    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    s.nextPermutation(nums)
    print(nums)
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print(nums)
    nums = [1, 1, 5]
    s.nextPermutation(nums)
    print(nums)
/python/leetcode/0001-0100/0054-spiral-matrix.py
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        while m > 0 and n > 0:
            if m == 1:
                res += matrix[0][:n]
                break
            if n == 1:
                for i in range(m):
                    res.append(matrix[i][0])
                break
            res += matrix[0][:n]
            for i in range(1, m - 1):
                res.append(matrix[i][n - 1])
            res += matrix[m - 1][n - 1::-1]
            for i in range(m - 2, 0, -1):
                res.append(matrix[i][0])
            res += matrix[0][1:n]
            matrix = matrix[1:m - 1]
            m, n