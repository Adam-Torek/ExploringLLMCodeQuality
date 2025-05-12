"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""

def move_num(s):
    """
    :param s: input string
    :return: string with all numbers moved to the end
    """
    return ''.join(sorted(s, key=lambda x: x.isdigit()))

if __name__ == '__main__':
    print(move_num('I1love143you55three3000thousand'))
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
    :param nums: input list
    :return: single number
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

def is_same_tree(p, q):
    """
    :param p: input tree
    :param q: input tree
    :return: True if trees are the same, False otherwise
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == '__main__':
    print(is_same_tree(None, None))
    print(is_same_tree(None, [1]))
    print(is_same_tree([1], None))
    print(is_same_tree([1], [1]))
    print(is_same_tree([1,2,3], [1,2,3]))
    print(is_same_tree([1,2], [1,None,2]))
    print(is_same_tree([1,2,1], [1,1,2]))
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
    """
    :param root: input tree
    :return: bottom-up level order traversal of its nodes' values
    """
    if root is None:
        return []
    res = []
    queue = [root]
    while queue:
        res.append([node.val for node in queue])
        queue = [child for node in queue for child in (node.