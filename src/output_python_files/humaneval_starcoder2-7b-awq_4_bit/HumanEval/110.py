def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

def main():
    """Main function."""
    lst1 = [1, 2, 3, 4]
    lst2 = [1, 2, 3, 4]
    print(exchange(lst1, lst2))

if __name__ == '__main__':
    main()
/python/leetcode/easy/100_same_tree.py
#!/usr/bin/env python3
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

from typing import Optional

class TreeNode:
    """Tree node."""

    def __init__(self, val=0, left=None, right=None):
        """Constructor."""
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Check if two trees are the same."""
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

def main():
    """Main function."""
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(is_same_tree(p, q))

if __name__ == '__main__':
    main()
/python/leetcode/easy/107_binary_tree_level_order_traversal_ii.py
#!/usr/bin/env python3
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

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

from typing import List, Optional

class TreeNode:
    """Tree node."""

    def __init__(self, val=0, left=None, right=None):
        """Constructor."""
        self.val = val
        self.left = left
        self