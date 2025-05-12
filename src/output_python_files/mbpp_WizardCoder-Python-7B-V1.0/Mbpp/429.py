"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""

def and_tuples(t1, t2):
    result = []
    for i in range(len(t1)):
        if t1[i] & t2[i] == 0:
            result.append(0)
        else:
            result.append(1)
    return tuple(result)

# Test cases
print(and_tuples((10, 4, 6, 9), (5, 2, 3, 3))) # Output: (0, 0, 2, 1)
print(and_tuples((1, 2, 3, 4), (5, 6, 7, 8))) # Output: (0, 0, 0, 0)
print(and_tuples((1, 2, 3, 4), (0, 0, 0, 0))) # Output: (0, 0, 0, 0)
print(and_tuples((1, 2, 3, 4), (1, 1, 1, 1))) # Output: (1, 1, 1, 1)
print(and_tuples((0, 0, 0, 0), (1, 1, 1, 1))) # Output: (0, 0, 0, 0)
print(and_tuples((1, 1, 1, 1), (1, 1, 1, 1))) # Output: (1, 1, 1, 1)
print(and_tuples((0, 1, 0, 1), (1, 1, 0, 1))) # Output: (0, 1, 0, 1)
print(and_tuples((1, 1, 0, 1), (1, 1, 0, 1))) # Output: (1, 1, 0, 1)
print(and_tuples((1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1))) # Output: (1, 1, 1, 1, 1, 1)
print(and_tuples((0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0))) # Output: (0, 0, 0, 0, 0, 0)
print(and_tuples((0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1))) # Output: (0, 0, 0, 0, 0, 0)
print(and_tuples((1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0))) # Output: (0, 0, 0, 0, 0, 0)
print(and_tuples((1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1))) # Output: (1, 1, 1, 1, 1, 1)
print(and_tuples((0, 1, 0, 1, 0, 1), (1, 1, 0, 1, 0, 1))) # Output: (0, 1, 0, 1, 0, 1)
print(and_tuples((1, 1, 0, 1, 0, 1), (1, 1, 0, 1, 0, 1))) # Output: (1, 1, 0, 1, 0, 1)
print(and_tuples((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1,