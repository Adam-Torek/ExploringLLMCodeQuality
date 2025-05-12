"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""

def find_Index(n):
    # TODO: Write your code here
    pass

if __name__ == '__main__':
    print(find_Index(2))
/python/leetcode/1001-1100/1001-1010/1008.py
"""
1008. Construct Binary Search Tree from Preorder Traversal
Medium

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Constraints:
1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""

from typing import List

from leetcode import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        def helper(left, right):
            if left > right:
                return None
            root = TreeNode(preorder[left])
            i = left + 1
            while i <= right and preorder[i] < preorder[left]:
                i += 1
            root.left = helper(left + 1, i - 1)
            root.right = helper(i, right)
            return root

        return helper(0, len(preorder) - 1)


if __name__ == '__main__':
    print(Solution().bstFromPreorder([8, 5, 1, 7, 10, 12]))  # [8,5,10,1,7,null,12]
/python/leetcode/1001-1100/1001-1010/1002.py
"""
1002. Find Common Characters
Easy

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]

Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """
        Time complexity: O(n * m)
        Space complexity: O(n)
        """
        res = []
        for i in range(26):
            count = 101
            for j in range(len(A)):
                count = min(count, A[j].count(chr(i + ord('a'))))
            for _ in range(count):
                res.append(chr(i + ord('a')))
        return res


if __name__ == '__main__':
    print(Solution().commonChars(["bella", "label", "roller"]))  # ["e", "l", "l"]
    print(Solution().commonChars(["cool", "lock", "cook"]))  # ["c", "o"]
/