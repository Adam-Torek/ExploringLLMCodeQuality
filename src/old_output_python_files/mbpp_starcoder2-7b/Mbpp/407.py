"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""

def rearrange_bigger(num):
    num_list = list(str(num))
    for i in range(len(num_list)-1,0,-1):
        if num_list[i] > num_list[i-1]:
            num_list[i], num_list[i-1] = num_list[i-1], num_list[i]
            return int(''.join(num_list))
    return -1

print(rearrange_bigger(12))
print(rearrange_bigger(1234567890))
print(rearrange_bigger(123456789))
print(rearrange_bigger(12345678))
print(rearrange_bigger(1234567))
print(rearrange_bigger(123456))
print(rearrange_bigger(12345))
print(rearrange_bigger(1234))
print(rearrange_bigger(123))
print(rearrange_bigger(12))
print(rearrange_bigger(1))
print(rearrange_bigger(0))
print(rearrange_bigger(-1))
<file_sep>/python/leetcode/100_same_tree.py
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

def main():
    s = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(s.isSameTree(root1, root2))
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(1)
    root2 = TreeNode(1)
    root2.left = TreeNode(1)
    root2.right = TreeNode(2)
    print(s.isSameTree(root1, root2))

if __name__ == '__main__':
    main()
<file_sep>/python/leetcode/101_symmetric_tree.py
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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def is