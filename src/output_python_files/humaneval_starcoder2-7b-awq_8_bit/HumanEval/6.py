from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
/python/leetcode/easy/125_valid_palindrome.py
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

from typing import List


def is_palindrome(s: str) -> bool:
    """
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    """
    s = s.lower()
    s = ''.join(filter(lambda x: x.isalnum(), s))
    return s == s[::-1]
/python/leetcode/easy/104_maximum_depth_of_binary_tree.py
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

from typing import List


def max_depth(root: TreeNode) -> int:
    """
    >>> max_depth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    3
    """
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1
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

from typing import List


def level_order_bottom(root: TreeNode) -> List[List[int]]:
    """
    >>> level_order_bottom(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    [[15, 7], [9, 20], [3]]
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

from typing import List


def sorted_array_to_bst(nums: List[int]) -> TreeNode:
    """
    >>> sorted