"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""

def snake_to_camel(s):
    return s.title().replace('_','')

print(snake_to_camel('python_program'))
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
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

def create_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in arr[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def print_list(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    head = create_list([1,2,3,4,5])
    head.next.next.next.next.next = head.next
    print_list(head)
    print(Solution().hasCycle(head))
/python/leetcode/easy/100_same_tree.py
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

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
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!= q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def create_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if arr[i]!= None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if arr[i]!= None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

def print_tree(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.val)
            queue.append(node.left)
            queue.append(node.right)

if __name__ == '__main__':
    p = create_tree([1,2,3])
    q = create_tree([1,2,3])
    print(Solution().isSameTree(p, q))
/python/leetcode/easy/107_binary_tree_level_order_traversal_ii.py
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object