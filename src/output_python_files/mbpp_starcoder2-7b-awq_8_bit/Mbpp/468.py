"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    max_product_so_far = arr[0]
    max_product_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_product_ending_here = max(max_product_ending_here * arr[i], arr[i])
        max_product_so_far = max(max_product_so_far, max_product_ending_here)
    return max_product_so_far

print(max_product([3, 100, 4, 5, 150, 6]))
/leetcode/python/100_same_tree.py
"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val!= root2.val:
        return False
    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(is_same_tree(root1, root2))
/leetcode/python/101_symmetric_tree.py
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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
/leetcode/python/102_binary_tree_level_order_traversal.py
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while len(queue) > 0:
        level_size = len(queue)
        level = []
        for i in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(level)
    return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(