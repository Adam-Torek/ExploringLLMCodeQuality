"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""

def count_bidirectional(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][1] == lst[j][0] and lst[j][1] == lst[i][0]:
                count += 1
    return count

# Test
print(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)])) # Output: 3