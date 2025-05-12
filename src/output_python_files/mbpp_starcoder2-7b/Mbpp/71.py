"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def comb_sort(lst):
    gap = len(lst)
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.25))
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst

print(comb_sort([5, 15, 37, 25, 79]))
/python/data_structures/linked_list/linked_list.py
"""
Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in list")
            return
        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node

    def delete_node(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        node = self.head
        while node.next:
            if node.next.data == key:
                node.next = node.next.next
                return
            node = node.next

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_after_node(ll.head.next, 6)
    ll.print_list()
    ll.delete_node(3)
    ll.print_list()
/python/data_structures/stack/stack.py
"""
Stack
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size())
/python/data_structures/queue/queue.py
"""
Queue
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue