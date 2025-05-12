"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""

def substract_elements(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i] - t2[i])
    return result

assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)<|endoftext|>