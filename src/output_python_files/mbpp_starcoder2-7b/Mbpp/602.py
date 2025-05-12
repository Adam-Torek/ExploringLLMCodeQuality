"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""

def first_repeated_char(string):
    """
    :param string: str
    :return: str
    """
    for i in range(len(string)):
        if string[i] in string[i+1:]:
            return string[i]
    return None

print(first_repeated_char("abcabc"))
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
    :param nums: List[int]
    :return: int
    """
    return 2 * sum(set(nums)) - sum(nums)

print(single_number([2,2,1]))
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
    """
    :param p: TreeNode
    :param q: TreeNode
    :return: bool
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(same_tree(root, root2))
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
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
/python/leetcode/easy/118_pascals_triangle.py
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def generate(numRows):
    """
    :param numRows: int
    :return: List[List[int