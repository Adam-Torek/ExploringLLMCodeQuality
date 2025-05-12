from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
<file_sep>/src/python/data_structures/linked_list/linked_list.py
from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data: Any) -> None:
        """ Append a new node containing the data to the end of the list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data: Any) -> None:
        """ Prepend a new node containing the data to the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data: Any) -> None:
        """ Delete the first node containing the data.
        """
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def find(self, data: Any) -> Optional[Node]:
        """ Return the first node containing the data.
        """
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def find_last(self, data: Any) -> Optional[Node]:
        """ Return the last node containing the data.
        """
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def delete_at_index(self, index: int) -> None:
        """ Delete the node at the given index.
        """
        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next

    def get_at_index(self, index: int) -> Optional[Node]:
        """ Return the node at the given index.
        """
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def insert_at_index(self, index: int, data: Any) -> None:
        """ Insert a new node containing the data at the given index.
        """
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def reverse(self) -> None:
        """ Reverse the list in-place.
        """
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def print(self) -> None:
        """ Print the list.
        """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
<file_sep>/src/python/data_structures/linked_list