"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""

def count_X(tup, x):
    """
    tup: a tuple
    x: a value
    returns: the number of times x appears in tup
    """
    count = 0
    for i in tup:
        if i == x:
            count += 1
    return count

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),2))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),15))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),1))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),100))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),1000))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10000))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),100000))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),1000000))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10000000))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),100000000))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),1000000000))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10000000000))
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),100000000000))
print(count_X((10, 8, 5, 2, 10, 15, 10,