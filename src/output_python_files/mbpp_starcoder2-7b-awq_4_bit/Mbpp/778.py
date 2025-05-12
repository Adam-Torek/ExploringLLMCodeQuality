"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""

def pack_consecutive_duplicates(lst):
    """
    >>> pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
    [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    """
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    if len(lst) == 2:
        if lst[0] == lst[1]:
            return [[lst[0], lst[1]]]
        else:
            return [lst]
    if len(lst) == 3:
        if lst[0] == lst[1] and lst[1] == lst[2]:
            return [[lst[0], lst[1], lst[2]]]
        elif lst[0] == lst[1]:
            return [[lst[0], lst[1]], lst[2]]
        elif lst[1] == lst[2]:
            return [lst[0], [lst[1], lst[2]]]
        else:
            return [lst]
    if len(lst) > 3:
        if lst[0] == lst[1]:
            return [[lst[0], lst[1]]] + pack_consecutive_duplicates(lst[2:])
        elif lst[1] == lst[2]:
            return [lst[:2]] + pack_consecutive_duplicates(lst[3:])
        else:
            return [lst[:3]] + pack_consecutive_duplicates(lst[3:])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/leetcode/easy/108_convert_sorted_array_to_bst.py
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],