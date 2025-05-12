"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def max_sub_array_sum_repeated(arr, k, n):
    if k == 1:
        return max(arr)
    if k > n:
        return max(arr) * n
    max_sum = 0
    for i in range(n):
        sum = 0
        for j in range(k):
            sum += arr[i]
        max_sum = max(max_sum, sum)
    return max_sum

print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))
/leetcode/100_same_tree.py
"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(is_same_tree(root1, root2))
/leetcode/101_symmetric_tree.py
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if root is None:
        return True
    return is_symmetric_helper(root.left, root.right)

def is_symmetric_helper(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val!= right.val:
        return False
    return is_symmetric_helper(left.left, right.right) and is_symmetric_helper(left.right, right.left)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(is_symmetric(root))
/leetcode/102_binary_tree_level_order_traversal.py
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(level_order(root))
/leetcode/103_binary_tree_zigzag_level_order_traversal.py
"""