"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""

def remove_length(string, k):
    words = string.split()
    result = []
    for word in words:
        if len(word)!= k:
            result.append(word)
    return''.join(result)

print(remove_length('The person is most value tet', 3))
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
    result = 0
    for num in nums:
        result ^= num
    return result

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
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

def is_same_tree_2(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree_2(p.left, q.left) and is_same_tree_2(p.right, q.right)

def is_same_tree_3(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree_3(p.left, q.left) and is_same_tree_3(p.right, q.right)

def is_same_tree_4(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree_4(p.left, q.left) and is_same_tree_4(p.right, q.right)

def is_same_tree_5(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree_5(p.left, q.left) and is_same_tree_5(p.right, q.right)

def is_same_tree_6(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False