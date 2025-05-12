"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""

def bell_number(n):
    """
    >>> bell_number(2)
    2
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number(n-1) + sum([bell_number(i)*bell_number(n-1-i) for i in range(n)])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/README.md
# python-algorithms

This is a collection of algorithms implemented in Python.

## Algorithms

### Sorting

- [Bubble Sort](https://github.com/joshua-chen/python-algorithms/blob/master/sorting/bubble_sort.py)
- [Insertion Sort](https://github.com/joshua-chen/python-algorithms/blob/master/sorting/insertion_sort.py)
- [Merge Sort](https://github.com/joshua-chen/python-algorithms/blob/master/sorting/merge_sort.py)
- [Quick Sort](https://github.com/joshua-chen/python-algorithms/blob/master/sorting/quick_sort.py)
- [Selection Sort](https://github.com/joshua-chen/python-algorithms/blob/master/sorting/selection_sort.py)

### Searching

- [Binary Search](https://github.com/joshua-chen/python-algorithms/blob/master/searching/binary_search.py)
- [Linear Search](https://github.com/joshua-chen/python-algorithms/blob/master/searching/linear_search.py)

### Graphs

- [Breadth First Search](https://github.com/joshua-chen/python-algorithms/blob/master/graphs/breadth_first_search.py)
- [Depth First Search](https://github.com/joshua-chen/python-algorithms/blob/master/graphs/depth_first_search.py)
- [Dijkstra's Algorithm](https://github.com/joshua-chen/python-algorithms/blob/master/graphs/dijkstra.py)
- [Prim's Algorithm](https://github.com/joshua-chen/python-algorithms/blob/master/graphs/prim.py)
- [Kruskal's Algorithm](https://github.com/joshua-chen/python-algorithms/blob/master/graphs/kruskal.py)

### Dynamic Programming

- [Fibonacci](https://github.com/joshua-chen/python-algorithms/blob/master/dynamic_programming/fibonacci.py)
- [Longest Common Subsequence](https://github.com/joshua-chen/python-algorithms/blob/master/dynamic_programming/longest_common_subsequence.py)
- [Longest Increasing Subsequence](https://github.com/joshua-chen/python-algorithms/blob/master/dynamic_programming/longest_increasing_subsequence.py)
- [Longest Palindromic Subsequence](https://github.com/joshua-chen/python-algorithms/blob/master/dynamic_programming/longest_palindromic_subsequence.py)
- [Longest Palindromic Substring](https://github.com/joshua-chen/python-algorithms/blob/master/dynamic_programming/longest_palindromic_substring.py)
- [Longest Substring Without Repeating Characters](https://github.com/joshua-chen/python-algorithms/blob/master/dynamic_programming/longest_substring_without_repeating_characters.py)
- [Longest Substring with Same Letters After Replacement](https://github.com/joshua-chen/python-algorithms/blob/master/dynamic_programming/longest_substring_with_same_letters_after_replacement.py)
- [Longest Substring with Same Letters After Replacement](https://github.com/joshua-chen/python-algorithms/blob/master/dynamic_programming/longest_substring_with_same_letters_after_replacement.py)
- [Longest Substring with Same Letters After Replacement](https://github.com/