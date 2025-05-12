"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
"""

def tuple_modulo(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i] % t2[i])
    return tuple(result)

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5))) # Output: (0, 4, 5, 1)