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
<file_sep>/leetcode/0001-0100/0016.py
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

        Example:

            Input: nums = [-1,2,1,-4], target = 1
            Output: 2
            Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

        Constraints:

            3 <= nums.length <= 10^3
            -10^3 <= nums[i] <= 10^3
            -10^4 <= target <= 10^4
        """
        nums.sort()
        res = float('inf')
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return res
<file_sep>/leetcode/0001-0100/0040.py
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

        Each number in candidates may only be used once in the combination.

        Note:

            All numbers (including target) will be positive integers.
            The solution set must not contain duplicate combinations.

        Example 1:

            Input: candidates = [10,1,2,7,6,1,5], target = 8
            Output:
            [
            [1,1,6],
            [1,2,5],
            [1,7],
            [2,6]
            ]

        Example 2:

            Input: candidates = [2,5,2,1,2], target = 5
            Output:
            [
            [1,2,2],
            [5]
            ]

        Constraints:

            1 <= candidates.length <= 100
            1 <= candidates[i] <= 50
            1 <= target <= 30
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, start, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)
<file_sep>/leetcode/0001-0100/0039.py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.