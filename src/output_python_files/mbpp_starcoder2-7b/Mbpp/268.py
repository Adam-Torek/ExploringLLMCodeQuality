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
        return find_star_num(n-1) * 10 + 37

print(find_star_num(3))
/python/leetcode/1001-1100/1008.py
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
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
            res.append(level)
        return res
/python/leetcode/1001-1100/1003.py
"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        count = collections.Counter(S)
        max_count = max(count.values())
        if max_count > (len(S) + 1) // 2:
            return ""
        res = []
        for c in count:
            res.extend([c] * count[c])
        res = res[::-1]
        res = "".join(res)
        return res
/python/leetcode/1-100/10.py
"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1
/python/leetcode/1-100/10.py
"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int