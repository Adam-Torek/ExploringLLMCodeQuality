"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""

def heap_queue_largest(lst, n):
    heapq.heapify(lst)
    return [heapq.heappop(lst) for _ in range(n)]

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3))
/python/leetcode/100_same_tree.py
"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val!= q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Test
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(1)

root4 = TreeNode(1)
root4.left = TreeNode(1)
root4.right = TreeNode(1)

root5 = TreeNode(1)
root5.left = TreeNode(2)

root6 = TreeNode(1)
root6.right = TreeNode(2)

root7 = TreeNode(1)
root7.left = TreeNode(2)
root7.right = TreeNode(2)

root8 = TreeNode(1)
root8.left = TreeNode(2)
root8.right = TreeNode(2)
root8.left.left = TreeNode(3)
root8.right.right = TreeNode(3)

root9 = TreeNode(1)
root9.left = TreeNode(2)
root9.right = TreeNode(2)
root9.left.left = TreeNode(1)
root9.right.right = TreeNode(1)

root10 = TreeNode(1)
root10.left = TreeNode(2)
root10.right = TreeNode(2)
root10.left.left = TreeNode(1)
root10.right.right = TreeNode(1)
root10.left.left.left = TreeNode(3)
root10.right.right.right = TreeNode(3)

root11 = TreeNode(1)
root11.left = TreeNode(2)
root11.right = TreeNode(2)
root11.left.left = TreeNode(1)
root11.right.right = TreeNode(1)
root11.left.left.left = TreeNode(3)
root11.right.right.right = TreeNode(3)
root11.left.left.left.left = TreeNode(4)
root11.right.right.right.right = TreeNode(4)

root12 = TreeNode(1)
root12.left = TreeNode(2)
root12.right = TreeNode(2)
root12.left.left = TreeNode(1)
root12.right.right = TreeNode(1)
root12.left.left.left = TreeNode(3)
root12.right.right.right = TreeNode(3)
root12.left.left.left.left = TreeNode(4)
root12.right.right.right.right = TreeNode(4)
root12.left.left.left.left.left = TreeNode(5)
root12.right.right.right.right.