"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""

def get_Inv_Count(arr):
    if len(arr) == 1:
        return 0
    mid = len(arr)//2
    left = get_Inv_Count(arr[:mid])
    right = get_Inv_Count(arr[mid:])
    return left + right

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def get_Inv_Count(arr):
    return merge_sort(arr)

print(get_Inv_Count([1,20,6,4,5]))
/leetcode/100/100.py
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
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
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
/leetcode/101/101.py
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
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
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val!= right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
/leetcode/102/102.py
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = [root