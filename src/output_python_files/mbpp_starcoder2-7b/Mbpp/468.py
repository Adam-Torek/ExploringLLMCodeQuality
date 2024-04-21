"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    max_product = 1
    for i in arr:
        max_product *= i
    return max_product

print(max_product([3, 100, 4, 5, 150, 6]))<file_sep>/python/leetcode/easy/136_single_number.py
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(set(nums)) - sum(nums)

print(single_number([4,1,2,1,2]))<file_sep>/python/leetcode/easy/100_same_tree.py
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_same_tree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

def is_same_tree_2(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree_2(p.left, q.left) and is_same_tree_2(p.right, q.right)

def is_same_tree_3(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree_3(p.left, q.left) and is_same_tree_3(p.right, q.right)

def is_same_tree_4(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree_4(p.left, q.left) and is_same_tree_4(p.right, q.right)

def is_same_tree_5(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    if