"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""

def pancake_sort(lst):
    """
    Sorts a list of elements using pancake sort.
    """
    for i in range(len(lst)):
        max_index = lst.index(max(lst[i:]))
        if max_index!= i:
            lst[i], lst[max_index] = lst[max_index], lst[i]
            lst[i+1:] = lst[i+1:][::-1]
    return lst

print(pancake_sort([15, 79, 25, 38, 69]))
/README.md
# Python-Algorithms

This repository contains my solutions to various algorithms in Python.

## Algorithms

### Sorting

- [Bubble Sort](https://github.com/james-willett/Python-Algorithms/blob/master/sorting/bubble_sort.py)
- [Insertion Sort](https://github.com/james-willett/Python-Algorithms/blob/master/sorting/insertion_sort.py)
- [Merge Sort](https://github.com/james-willett/Python-Algorithms/blob/master/sorting/merge_sort.py)
- [Quick Sort](https://github.com/james-willett/Python-Algorithms/blob/master/sorting/quick_sort.py)
- [Selection Sort](https://github.com/james-willett/Python-Algorithms/blob/master/sorting/selection_sort.py)
- [Pancake Sort](https://github.com/james-willett/Python-Algorithms/blob/master/sorting/pancake_sort.py)

### Searching

- [Binary Search](https://github.com/james-willett/Python-Algorithms/blob/master/searching/binary_search.py)
- [Linear Search](https://github.com/james-willett/Python-Algorithms/blob/master/searching/linear_search.py)

### Graphs

- [Breadth First Search](https://github.com/james-willett/Python-Algorithms/blob/master/graphs/breadth_first_search.py)
- [Depth First Search](https://github.com/james-willett/Python-Algorithms/blob/master/graphs/depth_first_search.py)
- [Dijkstra's Algorithm](https://github.com/james-willett/Python-Algorithms/blob/master/graphs/dijkstra.py)
- [Prim's Algorithm](https://github.com/james-willett/Python-Algorithms/blob/master/graphs/prim.py)
- [Kruskal's Algorithm](https://github.com/james-willett/Python-Algorithms/blob/master/graphs/kruskal.py)

### Other

- [Binary Search Tree](https://github.com/james-willett/Python-Algorithms/blob/master/other/binary_search_tree.py)
- [Linked List](https://github.com/james-willett/Python-Algorithms/blob/master/other/linked_list.py)
- [Stack](https://github.com/james-willett/Python-Algorithms/blob/master/other/stack.py)
- [Queue](https://github.com/james-willett/Python-Algorithms/blob/master/other/queue.py)
- [Doubly Linked List](https://github.com/james-willett/Python-Algorithms/blob/master/other/doubly_linked_list.py)
- [Circular Linked List](https://github.com/james-willett/Python-Algorithms/blob/master/other/circular_linked_list.py)
- [Hash Table](https://github.com/james-willett/Python-Algorithms/blob/master/other/hash_table.py)
- [Trie](https://github.com/james-willett/Python-Algorithms/blob/master/other/trie.py)
- [Heap](https://github.com/james-willett/Python-Algorithms/blob/master/other/heap.py)
- [AVL Tree](https