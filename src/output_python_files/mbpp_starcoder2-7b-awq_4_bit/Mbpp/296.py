"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""

def get_Inv_Count(arr):
    if len(arr) == 1:
        return 0
    mid = len(arr) // 2
    left = get_Inv_Count(arr[:mid])
    right = get_Inv_Count(arr[mid:])
    return left + right

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def get_Inv_Count(arr):
    return merge_sort(arr)

print(get_Inv_Count([1,20,6,4,5]))
/leetcode/100/100.py
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
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    if not root:
        return True
    return isMirror(root.left, root.right)

def isMirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))
/leetcode/101/101.py
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
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    if not root:
        return True
    return isMirror(root.left, root.right)

def isMirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root