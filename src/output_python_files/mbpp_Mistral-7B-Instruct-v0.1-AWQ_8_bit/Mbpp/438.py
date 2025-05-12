"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""

def count_bidirectional(lst):
    """
    Count the number of bidirectional pairs in a list of tuples.
    """
    bidirectional_pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][0] > lst[j][0] and lst[i][1] < lst[j][1]:
                bidirectional_pairs.append(lst[i])
                bidirectional_pairs.append(lst[j])
    return len(bidirectional_pairs)

# assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == 3
print(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]))