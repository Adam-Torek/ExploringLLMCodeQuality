"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(s):
    return tuple(map(int, s[1:-1].split(', ')))

def test_tuple_str_int():
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
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
    return 2 * sum(set(nums)) - sum(nums)

def test_single_number():
    assert single_number([2,2,1]) == 1
    assert single_number([4,1,2,1,2]) == 4
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

def same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)

def test_same_tree():
    assert same_tree(None, None)
    assert same_tree(TreeNode(1), TreeNode(1))
    assert not same_tree(TreeNode(1), TreeNode(2))
    assert not same_tree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(1), TreeNode(2)))
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
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        res.append([node.val for node in queue])
        queue = [child for node in queue for child in (node.left, node.right) if child]
    return res[::-1]

def test_level_order_bottom():
    assert level_order_bottom(None) == []
    assert level_order_bottom(TreeNode(3)) == [[3]]
    assert level_order_bottom(TreeNode(3, TreeNode(9), TreeNode(20))) == [[9, 20], [3]]
    assert level_order_bottom(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [[15, 7], [9, 20], [3]]
/python/leetcode/easy/118_pascals_triangle.py
"""
Given a non-negative integer numRows, generate the first numRows