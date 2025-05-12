"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""

def magic_square_test(matrix):
    # Your code here
    return False

# Test
print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
/02-data-structures/02-stacks-queues/01-stack.py
"""
Implement a Stack class using a list.
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# Test
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.size())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
/02-data-structures/01-linked-lists/02-linked-list.py
"""
Implement a Linked List class using a Node class.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def to_list(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        return nodes

    def insert(self, index, value):
        if index >= self.size():
            self.append(value)
            return

        if index == 0:
            node = Node(value)
            node.next = self.head
            self.head = node
            return

        node = self.head
        new_node = Node(value)
        while index > 1:
            node = node.next
            index -= 1

        new_node.next = node.next
        node.next = new_node

    def remove(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

# Test
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print(linked_list.to_list())
linked_list.insert(0, 4)
print(linked_list.to_list())
linked_list.insert(1, 5)
print(linked_list.to_list())
linked_list.insert(2, 6)
print(linked_list.to_list())
linked_list.remove(1)
print(linked_list.to_list())
linked_list.remove(4)
print(linked_list.to_list())
linked_list.remove(3)
print(linked_list.to_list())
/01-algorithms/01-searching/01-linear-search.py
"""
Write a function that takes in a list and the item to search for.
Return the index of the item if found, -1 otherwise.
"""

def linear_search(array, item):