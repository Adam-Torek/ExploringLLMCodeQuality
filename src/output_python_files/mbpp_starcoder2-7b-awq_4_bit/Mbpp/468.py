"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    max_product_so_far = 0
    max_product_ending_here = 0
    for i in range(len(arr)):
        max_product_ending_here = max(max_product_ending_here * arr[i], arr[i])
        max_product_so_far = max(max_product_so_far, max_product_ending_here)
    return max_product_so_far

print(max_product([3, 100, 4, 5, 150, 6]))
/python/leetcode/easy/136_single_number.py
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(set(nums)) - sum(nums)

print(single_number([1, 2, 1, 3, 2, 5]))
/python/leetcode/easy/104_maximum_depth_of_binary_tree.py
"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(max_depth(root))
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

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_order_bottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        result.append([node.val for node in queue])
        queue = [child for node in queue for child in (node.left, node.right) if child]
    return result[::-1]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(level_order_bottom(root))
/python/leetcode/