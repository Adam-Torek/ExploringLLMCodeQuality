"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""

def pack_consecutive_duplicates(lst):
    """
    :param lst: list
    :return: list
    """
    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append([lst[i]])
        elif lst[i] == lst[i-1]:
            result[-1].append(lst[i])
        else:
            result.append([lst[i]])
    return result

print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
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
    :param nums: list
    :return: int
    """
    return 2 * sum(set(nums)) - sum(nums)

print(single_number([2,2,1]))
print(single_number([4,1,2,1,2]))
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

def is_palindrome(s):
    """
    :param s: str
    :return: bool
    """
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
/python/leetcode/easy/104_max_depth_binary_tree.py
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root):
    """
    :param root: TreeNode
    :return: int
    """
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(max_depth(root))
/python/leetcode/easy/110_balanced_binary_tree.py
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node