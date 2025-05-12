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

This repository contains some of the algorithms I have implemented in Python.

## Algorithms

### Sorting

- [Bubble Sort](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Sorting/bubble_sort.py)
- [Insertion Sort](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Sorting/insertion_sort.py)
- [Merge Sort](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Sorting/merge_sort.py)
- [Quick Sort](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Sorting/quick_sort.py)
- [Selection Sort](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Sorting/selection_sort.py)
- [Shell Sort](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Sorting/shell_sort.py)
- [Pancake Sort](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Sorting/pancake_sort.py)

### Searching

- [Binary Search](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Searching/binary_search.py)
- [Linear Search](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Searching/linear_search.py)

### Graphs

- [Breadth First Search](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Graphs/breadth_first_search.py)
- [Depth First Search](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Graphs/depth_first_search.py)
- [Dijkstra's Algorithm](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Graphs/dijkstra.py)
- [Prim's Algorithm](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Graphs/prim.py)
- [Kruskal's Algorithm](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Graphs/kruskal.py)

### Dynamic Programming

- [Fibonacci](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Dynamic%20Programming/fibonacci.py)
- [Knapsack](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Dynamic%20Programming/knapsack.py)
- [Longest Common Subsequence](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Dynamic%20Programming/longest_common_subsequence.py)
- [Longest Increasing Subsequence](https://github.com/siddharth-k-jain/Python-Algorithms/blob/master/Dynamic%20Programming/longest_increasing_subsequence.py)
- [Longest Palindromic Subsequence](https://github.com/siddharth-k-jain/Python-Algorithms/blob