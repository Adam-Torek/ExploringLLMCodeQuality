"""
Write a function to find then'th star number.
assert find_star_num(3) == 37
"""

def find_star_num(n):
    """
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    else:
        return find_star_num(n-1) + 2*(n-1) + 1

print find_star_num(3)
/python/leetcode/100_same_tree.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == '__main__':
    s = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print s.isSameTree(p, q)
/python/leetcode/101_symmetric_tree.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            return left.val == right.val and self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print s.isSymmetric(root)
/python/leetcode/102_binary_tree_level_order_traversal.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        else:
            return self.levelOrderHelper(root, 0)

    def levelOrderHelper(self, root, level):
        if root is None:
            return []
        else:
            if len(self.levelOrderHelper(root, level+1)) == 0:
                return [[root.val]]
            else:
                return [self.levelOrderHelper(root, level+1)[0]] + self.levelOrderHelper(root, level+1)[1:]

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print s.levelOrder(root)
/python/leetcode/103_binary_tree_zigzag_level_order_traversal.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):