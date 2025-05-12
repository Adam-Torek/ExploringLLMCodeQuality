"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def comb_sort(lst):
    gap = len(lst)
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, gap // 1.3)
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst

print(comb_sort([5, 15, 37, 25, 79]))
/python/leetcode/easy/136_single_number.py
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

def single_number(nums):
    return 2 * sum(set(nums)) - sum(nums)

print(single_number([2,2,1]))
print(single_number([4,1,2,1,2]))
/python/leetcode/easy/108_convert_sorted_array_to_bst.py
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

root = sorted_array_to_bst([-10,-3,0,5,9])
inorder(root)
/python/leetcode/easy/118_pascals_triangle.py
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def generate(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1,1]]
    res = [[1], [1,1]]
    for i in range(2, numRows):
        res.append([1] + [res[i - 1][j] + res[i - 1][j + 1] for j in range(i)] + [1])
    return res

print(generate(5))
/python/leetcode/easy/104_maximum_depth_of_binary_tree.py
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null