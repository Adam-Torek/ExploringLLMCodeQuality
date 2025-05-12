"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""

def tuple_intersection(tuple_list):
    """
    :param tuple_list: list of tuples
    :return: set of tuples
    """
    return set.intersection(*tuple_list)

if __name__ == '__main__':
    print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)]))
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
    :param nums: list of integers
    :return: integer
    """
    return 2 * sum(set(nums)) - sum(nums)

if __name__ == '__main__':
    print(single_number([2,2,1]))
    print(single_number([4,1,2,1,2]))
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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_same_tree(p, q):
    """
    :param p: TreeNode
    :param q: TreeNode
    :return: boolean
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == '__main__':
    print(is_same_tree(TreeNode(1), TreeNode(1)))
    print(is_same_tree(TreeNode(1), TreeNode(2)))
    print(is_same_tree(TreeNode(1), TreeNode(1)))
    print(is_same_tree(TreeNode(1), TreeNode(1)))
/python/leetcode/easy/104_max_depth_of_binary_tree.py
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root):
    """
    :param root: TreeNode
    :return: integer
    """
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

if __name