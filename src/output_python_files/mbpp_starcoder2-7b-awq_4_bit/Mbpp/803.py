"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""

def is_perfect_square(num):
    if num < 0:
        return False
    root = int(num ** 0.5)
    return root * root == num

assert not is_perfect_square(10)
assert is_perfect_square(9)
assert is_perfect_square(16)
assert not is_perfect_square(17)
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

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
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
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if i < len(arr):
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1
        if i < len(arr):
            if arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1
    return root

def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)

def test_is_same_tree():
    s = Solution()
    assert s.isSameTree(build_tree([1,2,3]), build_tree([1,2,3]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree([1,2,None]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree([1,None,2]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree([1,None,3]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree([1,3,2]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree([1,3,None]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree([1,None,None]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree([1,None,None]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree([1,None,None]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree([1,None,None]))
    assert not s.isSameTree(build_tree([1,2,3]), build_tree