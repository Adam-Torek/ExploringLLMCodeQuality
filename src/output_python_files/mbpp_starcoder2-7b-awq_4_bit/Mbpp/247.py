"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""

def lps(s):
    """
    :param s: string
    :return: int
    """
    # TODO: Write - Your - Code
    pass
/python/leetcode/easy/136_single_number.py
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
    :param nums: List[int]
    :return: int
    """
    return 2 * sum(set(nums)) - sum(nums)
/python/leetcode/easy/100_same_tree.py
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


def is_same_tree(p, q):
    """
    :param p: TreeNode
    :param q: TreeNode
    :return: bool
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
/python/leetcode/easy/107_binary_tree_level_order_traversal_ii.py
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


def level_order_bottom(root):
    """
    :param root: TreeNode
    :return: List[List[int]]
    """
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        res.append([node.val for node in queue])
        queue = [child for node in queue for child in (node.left, node.right) if child]
    return res[::-1]
/python/leetcode/easy/108_convert_sorted_array_to_binary_search_tree.py
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


def sorted_array_to_bst(nums):
    """
    :param nums: List[int]
    :return: TreeNode
    """
    if not nums:
        return None
    mid = len