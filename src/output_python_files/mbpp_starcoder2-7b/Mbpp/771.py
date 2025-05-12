"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""

def check_expression(expression):
    pass
/python/data_structures/linked_list/linked_list.py
"""
Implement a linked list.

You should be able to:

- Add a node to the start and end of the list
- Remove a node from the start and the end of the list
- Get the size of the list
- Traverse the list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_start(self, data):
        pass

    def add_to_end(self, data):
        pass

    def remove_from_start(self):
        pass

    def remove_from_end(self):
        pass

    def get_size(self):
        pass

    def traverse(self):
        pass
/python/data_structures/queue/queue.py
"""
Implement a queue.

You should be able to:

- Enqueue an element
- Dequeue an element
- Get the size of the queue
"""

class Queue:
    def __init__(self):
        pass

    def enqueue(self, data):
        pass

    def dequeue(self):
        pass

    def get_size(self):
        pass
/python/data_structures/stack/stack.py
"""
Implement a stack.

You should be able to:

- Push an element
- Pop an element
- Get the size of the stack
"""

class Stack:
    def __init__(self):
        pass

    def push(self, data):
        pass

    def pop(self):
        pass

    def get_size(self):
        pass
/python/data_structures/binary_tree/binary_tree.py
"""
Implement a binary tree.

You should be able to:

- Add a node
- Remove a node
- Get the size of the tree
- Traverse the tree
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add_node(self, data):
        pass

    def remove_node(self, data):
        pass

    def get_size(self):
        pass

    def traverse(self):
        pass
/python/data_structures/binary_search_tree/binary_search_tree.py
"""
Implement a binary search tree.

You should be able to:

- Add a node
- Remove a node
- Get the size of the tree
- Traverse the tree
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add_node(self, data):
        pass

    def remove_node(self, data):
        pass

    def get_size(self):
        pass

    def traverse(self):
        pass
/python/data_structures/hash_table/hash_table.py
"""
Implement a hash table.

You should be able to:

- Add a key/value pair
- Remove a key/value pair
- Get the value of a key
"""

class HashTable:
    def __init__(self):
        pass

    def add(self, key, value):
        pass

    def remove(self, key):
        pass

    def get(self, key):
        pass
/python/data_structures/heap/heap.py
"""
Implement a heap.

You should be able to:

- Add an element
- Remove an element
- Get the size of the heap
"""

class Heap:
    def __init__(self):
        pass

    def add(self, data):
        pass

    def remove(self):
        pass

    def get_size(self):
        pass
/python/data_structures/graph/graph.py
"""