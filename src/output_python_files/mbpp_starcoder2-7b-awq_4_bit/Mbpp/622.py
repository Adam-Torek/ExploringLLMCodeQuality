"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""

def get_median(list1, list2, n):
    if n == 0:
        return 0
    if n == 1:
        return (list1[0] + list2[0]) / 2
    if n == 2:
        return (max(list1[0], list2[0]) + min(list1[1], list2[1])) / 2

    m1 = median(list1, n)
    m2 = median(list2, n)

    if m1 == m2:
        return m1
    elif m1 < m2:
        return get_median(list1[n//2:], list2, n - n//2)
    else:
        return get_median(list1, list2[n//2:], n - n//2)

def median(list, n):
    if n % 2 == 0:
        return (list[n//2] + list[n//2 - 1]) / 2
    else:
        return list[n//2]

print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5))
/leetcode/100/100.py
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, min_val, max_val):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)
/leetcode/101/101.py
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

Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val