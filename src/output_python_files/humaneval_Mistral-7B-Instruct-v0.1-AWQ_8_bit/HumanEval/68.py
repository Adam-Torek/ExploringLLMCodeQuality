def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    if not nodes:
        return []
    min_even = nodes[0][0]
    min_even_index = 0
    for i in range(1, len(nodes)):
        if nodes[i][0] % 2 == 0 and nodes[i][0] < min_even:
            min_even = nodes[i][0]
            min_even_index = i
    return [min_even, min_even_index]


# Test code

def main():
    # Test with different inputs
    # to test with empty array
    test1 = []
    # to test with array containing only odd numbers
    test2 = [1, 2, 3]
    # to test with array containing only even numbers
    test3 = [2, 4, 6]
    # to test with array containing mixed numbers
    test4 = [4, 2, 3, 0, 5, 2]
    # to test with array containing only zeros
    test5 = [0, 0, 0, 0, 0, 0]
    # Test with array containing only positive numbers
    test6 = [1, 2, 3, 4, 5, 6]
    # Test with array containing only negative numbers
    test7 = [-1, -2, -3, -4, -5, -6]
    # Test with array containing only even numbers
    test8 = [2, 4, 6, 8, 10, 12]
    # Test with array containing only odd numbers
    test9 = [1, 3, 5, 7, 9, 11]
    # Test with array containing mixed numbers
    test10 = [4, 2, 3, 0, 5, 2, 1, 3, 0, 4]
    # Test with array containing only zeros
    test11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Test with array containing only positive numbers
    test12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Test with array containing only negative numbers
    test13 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    # Test with array containing only even numbers
    test14 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    # Test with array containing only odd numbers
    test15 = [1, 3, 5, 7, 9, 11, 13,