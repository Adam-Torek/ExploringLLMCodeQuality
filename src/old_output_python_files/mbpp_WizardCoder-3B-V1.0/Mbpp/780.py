"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""

def find_combinations(lst):
    lst.sort()
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i+1, n):
            if lst[i][0] + lst[j][0] == lst[n-1][0]:
                result.append((lst[i][0], lst[j][0]))
    return result

assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]<|endoftext|>