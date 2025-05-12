"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""

def count_X(tup, x):
    count = 0
    for i in tup:
        if i == x:
            count += 1
    return count

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4)) # should return 0
print(count_X((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 10) # should return 2
print(count_X((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 1) # should return 1
print(count_X((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 8) # should return 3
print(count_X((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 5) # should return 1
print(count_X((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 9) # should return 1
print(count_X((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 0) # should return 0