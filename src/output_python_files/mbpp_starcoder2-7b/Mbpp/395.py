"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""

def first_non_repeating_character(string):
    # TODO: Write your code here
    pass
/python/data_structures/linked_list/linked_list.py
"""
Implement a linked list.

The linked list should have the following methods:

insert(value) - insert a new node with the given value at the beginning of the list
remove(value) - remove the first node with the given value
search(value) - search for a node with the given value and return the node
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        # TODO: Write your code here
        pass

    def remove(self, value):
        # TODO: Write your code here
        pass

    def search(self, value):
        # TODO: Write your code here
        pass
/python/data_structures/queue/queue.py
"""
Implement a queue.

The queue should have the following methods:

enqueue(value) - insert a new value at the end of the queue
dequeue() - remove the first value from the queue
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        # TODO: Write your code here
        pass

    def dequeue(self):
        # TODO: Write your code here
        pass
/python/data_structures/stack/stack.py
"""
Implement a stack.

The stack should have the following methods:

push(value) - insert a new value at the top of the stack
pop() - remove the top value from the stack
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        # TODO: Write your code here
        pass

    def pop(self):
        # TODO: Write your code here
        pass
/python/data_structures/binary_tree/binary_tree.py
"""
Implement a binary tree.

The binary tree should have the following methods:

insert(value) - insert a new node with the given value at the appropriate location in the tree
search(value) - search for a node with the given value and return the node
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # TODO: Write your code here
        pass

    def search(self, value):
        # TODO: Write your code here
        pass
/python/data_structures/hash_table/hash_table.py
"""
Implement a hash table.

The hash table should have the following methods:

insert(key, value) - insert a new key-value pair at the appropriate location in the hash table
remove(key) - remove the key-value pair with the given key from the hash table
search(key) - search for a key-value pair with the given key and return the value
"""

class HashTable:
    def __init__(self):
        self.table = []

    def insert(self, key, value):
        # TODO: Write your code here
        pass

    def remove(self, key):
        # TODO: Write your code here
        pass

    def search(self, key):
        # TODO: Write your code here
        pass
/python/data_structures/binary_search_tree/binary_search_tree.py
"""
Implement a binary search tree.

The binary search tree should have the following methods:

insert(value) - insert a new node with the given value at the appropriate location in the tree
search(value) - search for a node with the given value