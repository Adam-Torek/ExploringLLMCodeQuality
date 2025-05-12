"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    max_product = arr[0]
    for i in range(1, len(arr)):
        max_product = max(max_product, arr[i], arr[i] * max_product)
    return max_product

print(max_product([3, 100, 4, 5, 150, 6]))
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

def is_same_tree_iterative(p, q):
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

def is_same_tree_recursive(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree_recursive(p.left, q.left) and is_same_tree_recursive(p.right, q.right)

def is_same_tree_recursive_iterative(p, q):
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

def is_same_tree_recursive_iterative_2(p, q):
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

def is_same_tree_recursive_iterative_3(p, q):
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
        if p.val!= q.