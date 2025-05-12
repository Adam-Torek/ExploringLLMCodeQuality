"""
Write a function to sort the given array by using shell sort.
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""

def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array

print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))
/01_Data_Structures/02_Linked_Lists/01_Singly_Linked_List/01_Singly_Linked_List.py
"""
Singly Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.insert_at_beginning(data_to_insert)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert)
                node.next = itr.next
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_before_value(self, data_before, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_before:
            self.insert_at_beginning(data_to_insert)
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data_before:
                node = Node(data_to_insert)
                node.next = itr.next
                itr.next = node
                break
            itr = itr.next

    def print_list(self):
        if