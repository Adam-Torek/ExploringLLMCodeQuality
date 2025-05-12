"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""

def reverse_words(string):
    return " ".join(string.split()[::-1])

print(reverse_words("python program"))
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)

def same_tree_iterative(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    stack = [(p, q)]
    while stack:
        p, q = stack.pop()
        if p is None and q is None:
            continue
        if p is None or q is None:
            return False
        if p.val!= q.val:
            return False
        stack.append((p.left, q.left))
        stack.append((p.right, q.right))
    return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(same_tree(root, root2))
print(same_tree_iterative(root, root2))
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_order_bottom(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left