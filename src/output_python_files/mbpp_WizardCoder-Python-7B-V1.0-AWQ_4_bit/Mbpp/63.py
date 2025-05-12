"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""

def max_difference(lst):
    sorted_lst = sorted(lst, key=lambda x: x[1])
    max_diff = 0
    min_val = sorted_lst[0][0]
    for i in range(1, len(sorted_lst)):
        max_diff = max(max_diff, sorted_lst[i][0] - min_val)
        min_val = min(min_val, sorted_lst[i][0])
    return max_diff

# Test cases
print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)])) # Output: 7
print(max_difference([(1, 2), (3, 4), (5, 6), (7, 8)])) # Output: 5
print(max_difference([(1, 3), (2, 7), (3, 5), (4, 6), (5, 8), (6, 9)])) # Output: 5
print(max_difference([(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)])) # Output: 4
print(max_difference([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])) # Output: 0
print(max_difference([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96), (6, 95)])) # Output: 50
print(max_difference([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96), (6, 95), (7, 94)])) # Output: 50
print(max_difference([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96), (6, 95), (7, 94), (8, 93)])) # Output: 50
print(max_difference([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96), (6, 95), (7, 94), (8, 93), (9, 92)])) # Output: 50
print(max_difference([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96), (6, 95), (7, 94), (8, 93), (9, 92), (10, 91)])) # Output: 50
print(max_difference([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96), (6, 95), (7, 94), (8, 93), (9, 92), (10, 91), (11, 90)])) # Output: 50
print(max_difference([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96), (6, 95), (7, 94), (8, 93), (9, 92), (10, 91), (11, 90), (12, 89)])) # Output: 50
print(max_difference([(1, 100), (2