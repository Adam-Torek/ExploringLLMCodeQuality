"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""

def eulerian_num(n, m):
    """
    :param n: int
    :param m: int
    :return: int
    """
    if n == 0:
        return 1
    if m == 0:
        return 0
    return eulerian_num(n - 1, m) + m * eulerian_num(n - 1, m - 1)

def test_eulerian_num():
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(3, 2) == 12
    assert eulerian_num(3, 3) == 36
    assert eulerian_num(4, 1) == 10
    assert eulerian_num(4, 2) == 60
    assert eulerian_num(4, 3) == 240
    assert eulerian_num(4, 4) == 960
    assert eulerian_num(5, 1) == 20
    assert eulerian_num(5, 2) == 180
    assert eulerian_num(5, 3) == 1080
    assert eulerian_num(5, 4) == 5040
    assert eulerian_num(5, 5) == 20160

if __name__ == '__main__':
    test_eulerian_num()
/leetcode/1000-1099/1038.py
"""
1038. Binary Search Tree to Greater Sum Tree
Medium

Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
Example 3:

Input: root = [1,0,2]
Output: [3,3,2]
Example 4:

Input: root = [3,2,4,1]
Output: [7,9,4,10]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-104 <= Node.val <= 104
All the values in the tree are unique.
root is guaranteed to be a valid binary search tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if node is None:
                return 0
            right = dfs(node.right)
            node.val += right
            left = dfs(node.left)
            return node.val + left
        dfs(root)
        return root
/leetcode/100-199/142.py
"""
142. Linked List Cycle II
Medium

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuous