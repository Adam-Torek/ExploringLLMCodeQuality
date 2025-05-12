"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""

def index_multiplication(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i] * t2[i])
    return tuple(result)

print(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))) ) # Output: ((6, 21), (12, 45), (2, 9), (7, 30))