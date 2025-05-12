"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""

def get_pairs_count(numbers, sum):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                count += 1
    return count

print(get_pairs_count([1,1,1,1],2))
/python/leetcode/easy/141_linked_list_cycle.py
"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow!= fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

def print_linked_list(head):
    cur = head
    while cur is not None:
        print(cur.val)
        cur = cur.next

head = create_linked_list([1,2,3,4,5])
head.next.next.next.next.next = head.next
print_linked_list(head)
print(Solution().hasCycle(head))
/python/leetcode/easy/104_maximum_depth_of_binary_tree.py
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

def create_tree(arr):
    if len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    q = [root]
    i = 1
    while i < len(arr):
        node = q.pop(0)
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root

def print_tree(root):
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        if node is None:
            print(None)
        else:
            print(node.val)
            q.append(node.left)
            q.append(node.right)

root = create_tree([1,2,3,None,5,None,4])
print_tree(root)
print(Solution().maxDepth(root))
/python/leetcode/easy/108_convert_sorted_array_to_binary_search_tree.py
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :