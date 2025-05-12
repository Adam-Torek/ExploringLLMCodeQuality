"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i.
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""

def max_sum_increasing_subseq(arr, k, i, j):
    if i == j:
        return arr[i]
    if k == j:
        return arr[k]
    if k > j:
        return arr[i]
    if k < i:
        return arr[j]
    return max(max_sum_increasing_subseq(arr, k, i, j-1), max_sum_increasing_subseq(arr, k, i+1, j), arr[k])

print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6))
/leetcode/1302.py
"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.ans
/leetcode/1304.py
"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1, n)) + list(range(-n+1, 0))
/leetcode/1305.py
"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            ans.append([node.val for node in q])
            q = [child for node in q for child in (node.left, node.right) if child]
        return ans
/leetcode/1306.py
"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.
"""

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n):
            if arr[i]!= arr[i+n//4]:
                continue
            if arr[i]!= arr[i+n//2]:
                continue
            if arr[i]!= arr[i+3*n//4]:
                continue
            return arr[i]
/leetcode/1307.py
"""
Given two strings word1 and word2, return true if the two strings are anagrams. Otherwise, return false.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, word1: str, word2: str) ->