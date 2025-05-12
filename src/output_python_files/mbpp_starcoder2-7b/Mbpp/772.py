"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""

def remove_length(string, k):
    words = string.split()
    result = []
    for word in words:
        if len(word)!= k:
            result.append(word)
    return''.join(result)

print(remove_length('The person is most value tet', 3))
/python/00001-00500/00100-00150/00130-00139/00138.py
"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
/python/00001-00500/00100-00150/00120-00129/00122.py
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit
/python/00001-00500/00100-00150/00110-00119/00118.py
"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j]
            result.append(row)
        return result
/python/00001-00500/00100-00150/00110-00119/00111.py
"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class