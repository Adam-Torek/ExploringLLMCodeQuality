"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""

def left_rotate(num, d):
    return (num << d) | (num >> (32 - d))

print left_rotate(16,2)
/python/leetcode/110_balanced_binary_tree.py
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isBalancedHelper(root)

    def isBalancedHelper(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left:
            return self.isBalancedHelper(root.right)
        if not root.right:
            return self.isBalancedHelper(root.left)
        return self.isBalancedHelper(root.left) and self.isBalancedHelper(root.right) and abs(self.height(root.left) - self.height(root.right)) <= 1

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
/python/leetcode/104_maximum_depth_of_binary_tree.py
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
/python/leetcode/101_symmetric_tree.py
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
/python/leetcode/100_same_tree.py
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#