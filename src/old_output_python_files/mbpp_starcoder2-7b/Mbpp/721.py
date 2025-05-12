"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""

def maxAverageOfPath(matrix):
    # Write your code here
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = matrix[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[m-1][n-1] / (m+n-1)

print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))
<file_sep>/leetcode/1000-1099/1000.py
"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.
assert evenOddSort([1, 3, 5]) == [1, 3, 5]
assert evenOddSort([2, 4, 6, 8]) == [2, 4, 6, 8]
assert evenOddSort([1, 2, 3, 4]) == [2, 4, 1, 3]
assert evenOddSort([1, 1, 1, 1]) == [1, 1, 1, 1]
"""

def evenOddSort(A):
    # Write your code here
    even = []
    odd = []
    for num in A:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd

print(evenOddSort([1, 3, 5]))
print(evenOddSort([2, 4, 6, 8]))
print(evenOddSort([1, 2, 3, 4]))
print(evenOddSort([1, 1, 1, 1]))
<file_sep>/leetcode/100-199/100.py
"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
assert isSameTree(None, None) == True
assert isSameTree(None, TreeNode(1)) == False
assert isSameTree(TreeNode(1), TreeNode(1)) == True
assert isSameTree(TreeNode(1), TreeNode(2)) == False
assert isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))) == True
assert isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))) == False
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    # Write your code here
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val!= q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

print(isSameTree(None, None))
print(isSameTree(None, TreeNode(1)))
print