"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""

def get_median(list1, list2, n):
    if n % 2 == 0:
        return (get_kth(list1, list2, n // 2) + get_kth(list1, list2, n // 2 + 1)) / 2
    else:
        return get_kth(list1, list2, n // 2 + 1)

def get_kth(list1, list2, k):
    if len(list1) == 0:
        return list2[k - 1]
    if len(list2) == 0:
        return list1[k - 1]
    if k == 1:
        return min(list1[0], list2[0])
    i = min(len(list1), k // 2)
    j = min(len(list2), k // 2)
    if list1[i - 1] > list2[j - 1]:
        return get_kth(list1, list2[j:], k - j)
    else:
        return get_kth(list1[i:], list2, k - i)

print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5))
/leetcode/100. Same Tree.py
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
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val!= q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
/leetcode/101. Symmetric Tree.py
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.